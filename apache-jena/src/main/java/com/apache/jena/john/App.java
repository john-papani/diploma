package com.apache.jena.john;

import org.apache.jena.datatypes.RDFDatatype;
import org.apache.jena.datatypes.xsd.XSDDatatype;
import org.apache.jena.rdf.model.Literal;
import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.ModelFactory;
import org.apache.jena.rdf.model.Property;
import org.apache.jena.rdf.model.Resource;
import org.apache.jena.rdf.model.ResourceFactory;
import org.apache.jena.rdf.model.impl.PropertyImpl;
import org.apache.jena.sparql.vocabulary.FOAF;
import org.apache.jena.vocabulary.RDF;
import org.apache.jena.vocabulary.VCARD;

public class App {
    public static String BASE = "http://example.org/";

    public static void main(String[] args) {
        // Create an empty Jena Model object
        Model model = ModelFactory.createDefaultModel();
        Model model2 = ModelFactory.createDefaultModel();

        // ------------example1 -------------

        // Load the RDF/XML file into the Jena Model object
        String rdfxml = "C:/Users/johnp/Desktop/rdfxml/httppurl.orglinkedpoliticsrdfvocabulary.ttl.rdf";

        model.read(rdfxml);

        // ------------example2 -------------
        // some definitions
        String personURI = "http://somewhere/johnpapp";
        String fullName = "John Papanikolaou";
        Resource johnpapp = model2.createResource(personURI).addProperty(VCARD.FN, fullName)
                .addProperty(new PropertyImpl("test"), "magkas");

        // -----example 3 ------------

        Model model3 = ModelFactory.createDefaultModel();

        Resource alice = ResourceFactory.createResource("http://example.org/alice");

        Resource bob = ResourceFactory.createResource("http://example.org/bob");
        model3.add(alice, RDF.type, FOAF.Person);
        model3.add(alice, FOAF.name, "Alice");
        model3.add(alice, FOAF.mbox, ResourceFactory.createResource("mailto:alice@example.org"));
        model3.add(alice, FOAF.knows, bob);

        Model model4 = ModelFactory.createDefaultModel();

        Resource subject = r("s");

        model4.addLiteral(subject, p("p1"), 10);
        model4.addLiteral(subject, p("p2"), 0.5);
        model4.addLiteral(subject, p("p3"), (float) 0.5);
        model4.addLiteral(subject, p("p4"), l(20));
        model4.addLiteral(subject, p("p5"), l(0.99));
        model4.addLiteral(subject, p("p6"), true);
        model4.add(subject, p("p7"), l("2012-03-11", XSDDatatype.XSDdate));
        model4.add(subject, p("p8"), l("P2Y", XSDDatatype.XSDduration));

        model4.setNsPrefix("example", BASE);
        model4.setNsPrefix("xsd", "http://www.w3.org/2001/XMLSchema#");

        model.write(System.out, "TURTLE");
        System.out.println("----------------");
        model2.write(System.out, "TURTLE");
        System.out.println("----------------");
        model3.write(System.out, "TURTLE");
        System.out.println("----------------");
        model4.write(System.out, "TURTLE");

        // https://jena.apache.org/documentation/io/rdf-output.html
    }

    private static Resource r(String localname) {
        return ResourceFactory.createResource(BASE + localname);
    }

    private static Property p(String localname) {
        return ResourceFactory.createProperty(BASE, localname);
    }

    private static Literal l(Object value) {
        return ResourceFactory.createTypedLiteral(value);
    }

    private static Literal l(String lexicalform, RDFDatatype datatype) {
        return ResourceFactory.createTypedLiteral(lexicalform, datatype);
    }

}