import rdflib

# Create an RDF graph
g = rdflib.Graph()

# Define your custom namespace with explicit prefix
my_ns = rdflib.Namespace("http://example.org/my_namespace/")

# Define your subject, predicate, and object
subject = rdflib.URIRef("http://example.org/subject")
predicate = my_ns["predicate"]
object_value = rdflib.URIRef(my_ns["testing"])

# Add the triple to the graph
g.add((subject, predicate, object_value))

# Serialize the graph to RDF/XML format with the custom namespace prefix
rdf_xml = g.serialize(format="xml", namespaces={"my_ns": my_ns})
rdf_xml_with_doctype = ("<?xml version='1.0' encoding='UTF-8'?>\n"
                        '<!DOCTYPE rdf:RDF [\n'
                        '<!ENTITY xsd "http://www.w3.org/2001/XMLSchema#">\n'
                        '<!ENTITY my_ns "http://example.org/my_namespace/">\n'
                        ']>\n'
                        + rdf_xml
                        )

# Print the RDF/XML serialization
print(rdf_xml_with_doctype)
