// MIT license
// Author: Egon Willighagen

@Grab(group='org.apache.any23', module='apache-any23-core', version='2.7')
@Grab(group='io.github.egonw.bacting', module='managers-rdf', version='0.0.45')

import org.apache.any23.Any23
import org.apache.any23.source.HTTPDocumentSource
import org.apache.any23.writer.NTriplesWriter

workspaceRoot = "../ws"
rdf = new net.bioclipse.managers.RDFManager(workspaceRoot);

url = "https://vhp4safety.github.io/glossary/glossary"

Any23 runner = new Any23();
runner.setHTTPUserAgent("test-user-agent");
httpClient = runner.getHTTPClient()
source = new HTTPDocumentSource(runner.getHTTPClient(), url)

out = new ByteArrayOutputStream();
handler = new NTriplesWriter(out);
try { runner.extract(source, handler);
} finally { handler.close(); }

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
