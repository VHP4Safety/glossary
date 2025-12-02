import os
import pandas as pd
import logging
import urllib.parse

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# RDF prefixes
prefixes = {
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "ncit": "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#",
    "dc": "http://purl.org/dc/elements/1.1/",
    "dcterms": "http://purl.org/dc/terms/",
    "vhp": "https://vhp4safety.github.io/glossary#",
}

# Define paths
template_file = ".github/index.md"
output_file = "index.md"
template_dir = "templates"

sections = {
    "toxicology": "toxicology.tsv",
    "risk_assessment": "risk_assessment.tsv",
    "adverse_outcome": "adverse_outcome.tsv",
    "server": "server.tsv",
    "tools": "tools.tsv",
    "projects": "projects.tsv",
    "organizations": "organizations.tsv",
    "chemicals": "chemicals.tsv",
    "process_flow_steps": "process_flow.tsv"
}

# Clickable svg
SVG_ICON = (
    '<svg xmlns="http://www.w3.org/2000/svg" height="12" width="15" viewBox="0 0 640 512">'
    '<path d="M579.8 267.7c56.5-56.5 56.5-148 0-204.5c-50-50-128.8-56.5-186.3-15.4l-1.6 1.1c-14.4 10.3-17.7 30.3-7.4 44.6s30.3 17.7 44.6 7.4l1.6-1.1c32.1-22.9 76-19.3 103.8 8.6c31.5 31.5 31.5 82.5 0 114L422.3 334.8c-31.5 31.5-82.5 31.5-114 0c-27.9-27.9-31.5-71.8-8.6-103.8l1.1-1.6c10.3-14.4 6.9-34.4-7.4-44.6s-34.4-6.9-44.6 7.4l-1.1 1.6C206.5 251.2 213 330 263 380c56.5 56.5 148 56.5 204.5 0L579.8 267.7zM60.2 244.3c-56.5 56.5-56.5 148 0 204.5c50 50 128.8 56.5 186.3 15.4l1.6-1.1c14.4 10.3 17.7-30.3 7.4-44.6s-30.3-17.7-44.6-7.4l-1.6 1.1c-32.1 22.9-76 19.3-103.8-8.6C74 372 74 321 105.5 289.5L217.7 177.2c31.5-31.5 82.5-31.5 114 0c27.9 27.9 31.5 71.8 8.6 103.9l-1.1 1.6c-10.3 14.4-6.9 34.4 7.4 44.6s34.4-6.9 44.6-7.4l1.1-1.6C433.5 260.8 427 182 377 132c-56.5-56.5-148-56.5-204.5 0L60.2 244.3z"/>'
    "</svg>"
)


def create_rdfa_table(tsv_file_path):
    try:
        df = pd.read_csv(tsv_file_path, sep="\t")
        logging.info(f"Processing TSV: {tsv_file_path}")
    except Exception as e:
        logging.error(f"Failed to read {tsv_file_path}: {e}")
        return "", set()

    if "Term" not in df.columns or "ID" not in df.columns:
        logging.error(f"Required columns not found in {tsv_file_path}. Skipping.")
        return "", set()

    if "ref" in df.columns:
        df["Definition"] = df.apply(
            lambda row: add_superscripts(row["Definition"], row["ref"]), axis=1
        )
        df.drop("ref", axis=1, inplace=True)


    def encode_smiles(smiles):
        encoded_smiles = urllib.parse.quote(smiles.encode('utf-8'))
        url = "https://cdkdepict.cloud.vhp4safety.nl/depict/bot/svg?w=-1&h=-1&abbr=off&hdisp=bridgehead&showtitle=false&zoom=1.6&annotate=cip&r=0&smi="
        image_html = f'<a href="{url + encoded_smiles}"><img src="{url + encoded_smiles}" alt="{smiles}"></a>'
        return image_html

    # Preserve original SMILES values before encoding
    if "SMILES" in df.columns:
        df["SMILES_original"] = df["SMILES"]
        df["SMILES"] = df.apply(
            lambda row: encode_smiles(row["SMILES"]) if isinstance(row["SMILES"], str) else "", axis=1
        )

    terms_set = set(df["Term"].str.strip().tolist())

    # Adjusted prefix formatting
    table_html = (
        f'<table prefix="{" ".join([f"{k}: {v}" for k, v in prefixes.items()])}">\n'
    )

    # Adjusted headers to use <td> with <b>, excluding ID and SMILES_original
    headers = [header for header in df.columns if header not in ["ID", "SMILES_original"]]
    table_html += (
        "  <tr>\n"
        + "".join([f"    <td><b>{header}</b></td>\n" for header in headers])
        + "  </tr>\n"
    )

    for _, row in df.iterrows():
        term_value = str(row.get("Term", "")).strip()
        row_id = str(row.get("ID", "")).strip()

        if not term_value or not row_id:
            logging.warning("Skipping row with missing 'Term' or 'ID'.")
            continue

        tr_attributes = f'id="{row_id}" about="https://vhp4safety.github.io/glossary#{row_id}" typeof="owl:Class"'
        table_html += f"  <tr {tr_attributes}>\n"

        term_cell_content = (
            f'<span property="rdfs:label">{term_value}</span> '
            f'<a href="https://vhp4safety.github.io/glossary#{row_id}">{SVG_ICON}</a>'
        )
        table_html += f"    <td>{term_cell_content}</td>\n"

        for header in headers[1:]:
            cell_value = (
                row[header] if header in row and not pd.isna(row[header]) else ""
            )
            cell_value = str(cell_value).strip()

            if header.lower() == "abbreviation":
                table_html += f'    <td property="ncit:C42610">{cell_value}</td>\n'
            elif header.lower() == "definition":
                table_html += f'    <td property="dc:description">{cell_value}</td>\n'
            elif header.lower() == "related_to":
                if cell_value:
                    # Extract VHP identifier from URL and convert to vhp4safety.github.io format
                    vhp_id = cell_value.split('#')[-1] if '#' in cell_value else ""
                    github_url = f"https://vhp4safety.github.io/glossary#{vhp_id}"
                    table_html += f'    <td property="dcterms:relation" resource="{github_url}"><a href="{github_url}">{SVG_ICON} {vhp_id}</a></td>\n'
                else:
                    table_html += "    <td></td>\n"
            elif header.lower() == "smiles":
                # Add SMILES with RDFa property using original SMILES value
                if cell_value:
                    original_smiles = str(row.get("SMILES_original", "")).strip()
                    if original_smiles:
                        table_html += f'    <td><span property="http://purl.obolibrary.org/obo/chebi/smiles" content="{original_smiles}">{cell_value}</span></td>\n'
                    else:
                        table_html += f"    <td>{cell_value}</td>\n"
                else:
                    table_html += "    <td></td>\n"
            else:
                table_html += f"    <td>{cell_value}</td>\n"

        table_html += "  </tr>\n"

    table_html += "</table>\n"
    return table_html, terms_set


def add_superscripts(definition, refs):
    if pd.isna(definition):
        definition = ""
    else:
        definition = str(definition)

    if pd.isna(refs):
        return definition

    refs = refs.split(",")
    refs_html = ""
    for ref_counter, ref in enumerate(refs, start=1):
        ref = ref.strip()
        if ref:
            href = ref if ref.startswith(("http://", "https://")) else f"#{ref}"
            refs_html += f'<a href="{href}"><sup>ref{ref_counter}</sup></a> '

    return f"{definition} {refs_html.strip()}" if refs_html else definition


def update_markdown_file(template_file, output_file, sections):
    try:
        with open(template_file, "r", encoding="utf-8") as f:
            content = f.read()
        logging.info(f"Loaded content from {template_file}")
    except Exception as e:
        logging.error(f"Failed to read {template_file}: {e}")
        return

    for table_type, tsv_file in sections.items():
        tsv_path = os.path.join(template_dir, tsv_file)
        if not os.path.exists(tsv_path):
            logging.warning(f"TSV file not found: {tsv_path}")
            continue

        table_html, _ = create_rdfa_table(tsv_path)
        if not table_html:
            continue
        content = content.replace(f"${{{table_type}}}", table_html)
        logging.info(f"Replaced content for table_type: {table_type}")

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)
        logging.info(f"Updated content written to {output_file}")
    except Exception as e:
        logging.error(f"Failed to write to {output_file}: {e}")


update_markdown_file(template_file, output_file, sections)
