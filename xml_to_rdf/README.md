# XML to RDF Conversion

This directory contains the code for transforming XML files generated from the Greek Parliament debates into RDF triples.

## Folder Structure

- `create_rdf_members_politicalFunction.py` : This script is responsible for generating RDF triples related to the political functions and member details of the participants in the debates. It processes the XML files and extracts information about the members' political functions, gender, party affiliation, and other relevant details, creating corresponding RDF triples.

- `create_rdf_speech_debate.py` : This script handles the conversion of XML files into RDF triples related to the speeches and debates. It parses the XML files and extracts speech-related information, generating RDF triples based on the extracted data.

- `official_data_directory.json` : This JSON file contains a collection of all speakers' names involved in the debates, mapping with their unique IDs. The data in this file is obtained from the official Parliament files, specifically from the files of [Dritsa repository](https://github.com/john-papani/diploma/tree/master/xml_to_rdf/files_from_opa_dritsa).

- `all_speakers_names.json` : This JSON file contains a collection of all speakers' names involved in the debates, mapping with their unique IDs. It is generated as a result of running the _create_rdf_speech_debate.py_ script and is utilized by the conversion scripts to enhance the RDF generation process.

- `/files_from_opa_dritsa` : This directory contains additional files obtained from the GitHub repository [Greek_Parliament_Proceedings_Dataset](https://github.com/Dritsa-Konstantina/Greek_Parliament_Proceedings_Dataset) (Dritsa Kontantina - iMEdD Lab Greece), which may be used as supplemental data during the RDF conversion process.

## Usage

To convert the XML files into RDF triples, follow these steps:

- Run the `create_rdf_members_politicalFunction.py` script:

  ```
  python create_rdf_members_politicalFunction.py
  ```

- After the members' political functions and details RDF triples are generated, run the `create_rdf_speech_debate.py` script:
  ```
  python create_rdf_speech_debate.py
  ```

The scripts will process the XML files, extract relevant information, and generate RDF triples based on the extracted data.
