import os
import rdflib
import xml.etree.ElementTree as ET
from rdflib import Namespace, Literal, RDF, URIRef
import json


def find_or_add_name(name):
    name = name.lower()
    name = name.translate(str.maketrans(
        'άέόώήίϊΐiύϋΰ', 'αεοωηιιιιυυυ'))  # remove accents
    json_file = './all_speakers_names.json'
    # Load existing data from JSON file
    with open(json_file, 'r', encoding='utf8') as file:
        data = json.load(file)
    # Check if the name exists in the JSON data
    if name in data:
        return data[name]  # Return the existing ID
    # Get the next available ID
    last_id = max(data.values()) if data else 0
    new_id = last_id + 1
    # Add the new name and ID to the JSON data
    data[name] = new_id
    # Save the updated JSON data to the file
    with open(json_file, 'w', encoding='utf8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    return new_id


# Create the RDF graph and define namespaces
g_speech = rdflib.Graph()
g_debate = rdflib.Graph()
greek_lp = Namespace("http://purl.org/greeklinkedpolitics/vocabulary/")
dcterms = Namespace("http://purl.org/dc/terms/")
xsd = Namespace("http://www.w3.org/2001/XMLSchema#")
greek_lp_debates = Namespace(
    "http://purl.org/linkedpolitics/vocabulary/gr/debates/")
xsd = Namespace("http://www.w3.org/2001/XMLSchema#")
foaf = Namespace("http://xmlns.com/foaf/0.1/")

akn_namespace = {"akn": "http://docs.oasis-open.org/legaldocml/ns/akn/3.0"}


# Define the input text
datapath = "./input_xml_files/"
filenames = sorted([f for f in os.listdir(datapath) if not f.startswith('.')])
print(filenames)
# text = "./input_xml_files/0005521.doc.xml"

for filename in filenames:
    # Parse the XML from a file
    tree = ET.parse(datapath+filename)
    # Get the root element of the XML tree
    root = tree.getroot()
    # Find the debate section element with name="main_debate_section"
    debate_section = root.find(
        './/akn:debateSection[@name="main_debate_section"]', akn_namespace)
    root.tag = root.tag.replace('{%xsd;}', '%xsd;')
    # Find the FRBRuri
    frbr_uri_path = root.find(".//akn:FRBRWork//akn:FRBRuri", akn_namespace)
    frbr_uri = frbr_uri_path.attrib.get(
        "value") if frbr_uri_path is not None else None
    debate_uri = "/".join(frbr_uri.split("/")[1:-1])
    # Check if the debate section exists
    if debate_section is not None:
        # Extract information from the parsed XML
        speech_elems = root.findall('.//akn:speech', akn_namespace)
        for speech_elem in speech_elems:
            length_speech_elems = len(speech_elems)
            speech_by = speech_elem.attrib['by']
            name_speaker = speech_elem.find('.//akn:from', akn_namespace).text
            id_speaker = find_or_add_name(name_speaker)
            eId = speech_elem.attrib['eId']
            date = eId.split('_')[1]  # Extract the date from the eId
            # Extract the speech_part from the eId
            speech_part = eId.split('_')[3]
            # Create the Speech resource
            speech_resource = greek_lp[eId]
            g_speech.add((speech_resource, dcterms.date,
                          Literal(date, datatype=xsd.date)))
            g_speech.add((speech_resource, dcterms.language, Literal("gr")))
            g_speech.add((speech_resource, dcterms["isPartOf"], URIRef(
                f"{greek_lp}{debate_uri}")))

            # Add properties to the speech node
            if int(speech_part)+1 < length_speech_elems:
                g_speech.add((speech_resource, greek_lp["hasSubsequent"], URIRef(
                    f"{greek_lp}speech_{date}_debate_{int(speech_part)+1}")))
            g_speech.add(
                (speech_resource, greek_lp["speaker"], greek_lp[f"GRmember_{id_speaker}"]))

            # Extract the spokenText from the XML and add it as a literal property to the Speech resource
            spoken_text_elems = speech_elem.findall('.//akn:p', akn_namespace)
            spoken_text = '\n'.join(
                [elem.text for elem in spoken_text_elems if elem.text is not None])
            g_speech.add((speech_resource, greek_lp.spokenText,
                          Literal(spoken_text, lang='el')))

            # Create rdf for each debate file
            debate_resource = greek_lp[debate_uri]
            g_debate.add((debate_resource, dcterms.date,
                          Literal(date, datatype=xsd.date)))
            g_debate.add((debate_resource, dcterms["hasPart"], URIRef(
                f"{greek_lp}{eId}")))
            g_debate.add((debate_resource, dcterms.language, Literal("gr")))

        # Serialize the RDF graph to RDF/XML format
        rdf_xml_speeches = g_speech.serialize(format='xml')
        rdf_xml_debate = g_debate.serialize(format='xml')
    else:
        print(
            "!!!!Debate section with name='main_debate_section' not found in the XML.", f" {filename}")
try:
    with open("text_speeches.rdf", "w", encoding='utf8') as file:
        file.write(rdf_xml_speeches)
    with open("text_debate.rdf", "w", encoding='utf8') as file:
        file.write(rdf_xml_debate)
except:
    print("BIG PROBLEM !!!!")
