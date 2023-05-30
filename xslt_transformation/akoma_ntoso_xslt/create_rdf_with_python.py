import rdflib
import xml.etree.ElementTree as ET
from rdflib import Namespace, Literal, RDF, URIRef

# Create the RDF graph and define namespaces
g = rdflib.Graph()
greek_lp = Namespace("http://purl.org/greeklinkedpolitics/vocabulary/")
dcterms = Namespace("http://purl.org/dc/terms/")
xsd = Namespace("http://www.w3.org/2001/XMLSchema#")
greek_lp_debates = Namespace(
    "http://purl.org/linkedpolitics/vocabulary/gr/debates/")
xsd = Namespace("http://www.w3.org/2001/XMLSchema#")

# Find the debate section element with name="main_debate_section"
namespaces = {"akn": "http://docs.oasis-open.org/legaldocml/ns/akn/3.0"}


# Define the input text
text = "./0005521.doc.xml"
# Parse the XML from a file
tree = ET.parse(text)
# Get the root element of the XML tree
root = tree.getroot()
# Find the debate section element with name="main_debate_section"
debate_section = root.find(
    './/akn:debateSection[@name="main_debate_section"]', namespaces)
root.tag = root.tag.replace('{%xsd;}', '%xsd;')
# Find the FRBRWork element
frbr_work = root.find(".//akn:FRBRWork", namespaces)

# Get the value of FRBRuri attribute within FRBRWork
frbr_uri = frbr_work.attrib.get("value") if frbr_work is not None else None
print(frbr_uri[0] if frbr_uri else None)
# Check if the debate section exists
if debate_section is not None:
    # Extract information from the parsed XML
    speech_elems = root.findall('.//akn:speech', namespaces)
    for speech_elem in speech_elems:
        length_speech_elems = len(speech_elems)
        speech_by = speech_elem.attrib['by']
        eId = speech_elem.attrib['eId']
        date = eId.split('_')[1]  # Extract the date from the eId
        speech_part = eId.split('_')[2]  # Extract the date from the eId
        print(speech_part)

        # Create the Speech resource
        speech_resource = greek_lp_debates[f"Speech_{eId}"]
        g.add((speech_resource, dcterms.date, Literal(date, datatype=xsd.date)))
        g.add((speech_resource, dcterms.language, Literal("gr")))
        g.add((speech_resource, dcterms["isPartOf"], URIRef(
            f"{greek_lp_debates}{date}")))
        # Add properties to the speech node
        if int(speech_part)+1 < length_speech_elems:
            g.add((speech_resource, greek_lp["hasSubsequent"], URIRef(
                f"{greek_lp_debates}Speech_debate_{date}_{int(speech_part)+1}")))
        g.add(
            (speech_resource, greek_lp["speaker"], greek_lp["EUmember_1103"]))

        # Extract the spokenText from the XML and add it as a literal property to the Speech resource
        spoken_text_elems = speech_elem.findall('.//akn:p', namespaces)
        spoken_text = '\n'.join(
            [elem.text for elem in spoken_text_elems if elem.text is not None])
        g.add((speech_resource, greek_lp.spokenText,
              Literal(spoken_text, lang='el')))

    # Serialize the RDF graph to RDF/XML format
    rdf_xml = g.serialize(format='xml')

    # Print or save the RDF/XML output
    # print(rdf_xml)
    with open(f"{text}.rdf", "w", encoding='utf8') as file:
        file.write(rdf_xml)

else:
    print("!!!!Debate section with name='main_debate_section' not found in the XML.")
