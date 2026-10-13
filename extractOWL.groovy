// MIT license
// Author: Egon Willighagen

@Grab(group='org.apache.any23', module='apache-any23-core', version='2.7')
@Grab(group='io.github.egonw.bacting', module='managers-rdf', version='0.0.45')

import org.apache.any23.Any23
import org.apache.any23.source.StringDocumentSource
import org.apache.any23.writer.NTriplesWriter

workspaceRoot = "../ws"
rdf = new net.bioclipse.managers.RDFManager(workspaceRoot);

url = "https://vhp4safety.github.io/glossary/"

// extract from the HTML rendering of the local index.md
page = new File(args ? args[0] : "index.md").getText("UTF-8")
if (!page.toLowerCase().contains("<html")) page = "<!DOCTYPE html>\n<html lang=\"en-US\"><body>\n${page}\n</body></html>"

Any23 runner = new Any23("html-rdfa11")
source = new StringDocumentSource(page, url, "text/html")

out = new ByteArrayOutputStream();
handler = new NTriplesWriter(out);
try { runner.extract(source, handler);
} finally { handler.close(); }

if (out.size() == 0) {
  System.err.println("No triples extracted")
  System.exit(1)
}

n3Stream = new ByteArrayInputStream(out.toByteArray())

kb = rdf.createInMemoryStore()
rdf.addPrefix(kb, "wp", "http://vocabularies.wikipathways.org/wp#")
rdf.addPrefix(kb, "gpml", "http://vocabularies.wikipathways.org/gpml#")
rdf.addPrefix(kb, "biopax", "http://www.biopax.org/release/biopax-level3.owl#")
rdf.addPrefix(kb, "skos", "http://www.w3.org/2004/02/skos/core#")
rdf.addPrefix(kb, "dc", "http://purl.org/dc/elements/1.1/")
rdf.addPrefix(kb, "dct", "http://purl.org/dc/terms/")
rdf.addPrefix(kb, "ncit", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#")
rdf.addPrefix(kb, "og", "http://ogp.me/ns#")
rdf.importFromStream(kb, n3Stream, "N3")

println rdf.asRDFN3(kb)
