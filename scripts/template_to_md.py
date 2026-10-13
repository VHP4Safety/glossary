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
    "chebi": "http://purl.obolibrary.org/obo/chebi/",
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


# Term-linking TSV columns: (RDF predicate, note shown under the term, label links by abbreviation)
TERM_LINKS = {
    "synonyms": ("owl:equivalentClass", "synonyms", True),
    "see_also": ("rdfs:seeAlso", "see also", False),
}


def load_term_links(sections):
    """Map each term ID to its linked terms {column: {ID: label}}, in both directions and across all templates."""
    terms, pairs = {}, []
    for tsv_file in sections.values():
        tsv_path = os.path.join(template_dir, tsv_file)
        if not os.path.exists(tsv_path):
            continue
        df = pd.read_csv(tsv_path, sep="\t", dtype=str).fillna("")
        for _, row in df.iterrows():
            row_id = row["ID"].strip()
            terms[row_id] = (row["Term"].strip(), row.get("Abbreviation", "").strip())
            for column in TERM_LINKS:
                for linked_id in row.get(column, "").split(","):
                    linked_id = linked_id.strip().split("#")[-1]
                    if linked_id:
                        pairs += [(column, row_id, linked_id), (column, linked_id, row_id)]

    links = {}
    for column, term_id, linked_id in pairs:
        if term_id not in terms or linked_id not in terms:
            logging.warning(f"Unknown {column} link {term_id} - {linked_id}. Skipping.")
            continue
        term, abbreviation = terms[linked_id]
        label = abbreviation if TERM_LINKS[column][2] and abbreviation else term
        links.setdefault(term_id, {}).setdefault(column, {})[linked_id] = label
    return links


def create_rdfa_table(tsv_file_path, links):
    try:
        df = pd.read_csv(tsv_file_path, sep="\t")
        logging.info(f"Processing TSV: {tsv_file_path}")
    except Exception as e:
        logging.error(f"Failed to read {tsv_file_path}: {e}")
        return "", set()

    if "Term" not in df.columns or "ID" not in df.columns:
        logging.error(f"Required columns not found in {tsv_file_path}. Skipping.")
        return "", set()

    df["Definition"] = df.apply(
        lambda row: add_superscripts(row["Definition"], row.get("ref")), axis=1
    )
    if "ref" in df.columns:
        df.drop("ref", axis=1, inplace=True)

    df.drop(columns=[column for column in TERM_LINKS if column in df.columns], inplace=True)

    def encode_smiles(smiles):
        smiles = smiles.strip()
        encoded_smiles = urllib.parse.quote(smiles.encode('utf-8'))
        url = "https://cdkdepict.cloud.vhp4safety.nl/depict/bot/svg?w=-1&h=-1&abbr=off&hdisp=bridgehead&showtitle=false&zoom=1.6&annotate=cip&r=0&smi="
        image_html = f'<a href="{url + encoded_smiles}"><img src="{url + encoded_smiles}" alt="{smiles}"></a>'
        return image_html + f'<span property="chebi:smiles" datatype="xsd:string">{smiles}</span>'

    if "SMILES" in df.columns:
        df["SMILES"] = df.apply(
            lambda row: encode_smiles(row["SMILES"]) if isinstance(row["SMILES"], str) else "", axis=1
        )

    terms_set = set(df["Term"].str.strip().tolist())

    # Adjusted prefix formatting
    table_html = (
        f'<table prefix="{" ".join([f"{k}: {v}" for k, v in prefixes.items()])}">\n'
    )

    # Adjusted headers to use <td> with <b>
    headers = [header for header in df.columns if header != "ID"]
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
        for column, (predicate, note, _) in TERM_LINKS.items():
            if column in links.get(row_id, {}):
                term_cell_content += f"<br><small>{note}: " + ", ".join(
                    f'<a property="{predicate}" resource="https://vhp4safety.github.io/glossary#{linked_id}" href="#{linked_id}">{label}</a>'
                    for linked_id, label in links[row_id][column].items()
                ) + "</small>"
        table_html += f"    <td>{term_cell_content}</td>\n"

        for header in headers[1:]:
            cell_value = (
                row[header] if header in row and not pd.isna(row[header]) else ""
            )
            cell_value = str(cell_value).strip()

            if header.lower() == "abbreviation":
                # no property on empty cells, to avoid empty literals in the OWL
                table_html += f'    <td property="ncit:C42610">{cell_value}</td>\n' if cell_value else "    <td></td>\n"
            elif header.lower() == "definition":
                # the dc:description span is added by add_superscripts, outside the reference links
                table_html += f"    <td>{cell_value}</td>\n"
            elif header.lower() == "related_to":
                if cell_value:
                    # Extract VHP identifier from URL and convert to vhp4safety.github.io format
                    vhp_id = cell_value.split('#')[-1] if '#' in cell_value else ""
                    github_url = f"https://vhp4safety.github.io/glossary#{vhp_id}"
                    table_html += f'    <td property="dcterms:relation" resource="{github_url}"><a href="{github_url}">{SVG_ICON} {vhp_id}</a></td>\n'
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
        definition = str(definition).strip()
    if definition:
        definition = f'<span property="dc:description">{definition}</span>'

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

    links = load_term_links(sections)
    for table_type, tsv_file in sections.items():
        tsv_path = os.path.join(template_dir, tsv_file)
        if not os.path.exists(tsv_path):
            logging.warning(f"TSV file not found: {tsv_path}")
            continue

        table_html, _ = create_rdfa_table(tsv_path, links)
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
