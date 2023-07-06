# Greek Parliament Debates to Open Linked Data

This repository contains the code and resources for the "Greek Parliament Debates to Open Linked Data" diploma thesis. The project aims to convert Greek Parliament debates from text files (in Word or TXT format) to XML files based on the Akoma Ntoso standard. These XML files are then transformed into RDF triples and uploaded to Apache Fuseki for further analysis and querying using SPARQL.

## Project Structure

The repository is structured as follows:

- [`antlr4_grammar/`](https://github.com/john-papani/diploma/tree/master/antlr4_grammar): This directory contains the ANTLR4 grammar file used for parsing the text files and generating the XML output.
- [`text_to_akn_xml/`](https://github.com/john-papani/diploma/tree/master/text_to_akn_xml): This directory contains the Python code for converting the text files to Akoma Ntoso XML format.
- [`xml_to_rdf/`](https://github.com/john-papani/diploma/tree/master/xml_to_rdf): This directory contains the code for transforming the XML files into RDF triples.
- [`sparql_queries.txt`](https://github.com/john-papani/diploma/blob/master/sparql_queries.txt): This file provides a collection of example SPARQL queries that can be executed against the RDF data in Apache Fuseki.
- [`requirements.txt`](https://github.com/john-papani/diploma/blob/master/requirements.txt): This file lists the Python dependencies required to run the project.
- [`bugs.txt`](https://github.com/john-papani/diploma/blob/master/bugs.txt): This file is used to track and document any known issues or bugs in the project.

## Requirements

To run the code in this repository, you will need the following dependencies:

- Python 3.10
- ANTLR4 Python Runtime
- Apache Jena Fuseki

Please make sure to install these dependencies before running the code. You can use the following command to install the required Python packages:

```
pip install -r requirements.txt
```

 <details><summary><h2>Getting Started</h2></summary>

To get started with the project, follow these steps:

1. Clone the repository to your local machine using the following command:

   ```
   git clone https://github.com/john-papani/diploma
   ```

2. Navigate to the project directory:

   ```
   cd diploma
   ```

3. Install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

4. Run the conversion script to convert the text files to XML:

   ```
   python text_to_akn_xml/convert_to_xml.py
   ```

   This script will process the text files and generate corresponding XML files based on the Akoma Ntoso standard.

5. Once you have the XML files, run the RDF conversion script to transform them into RDF triples:

   ```
   python xml_to_rdf/create_rdf_speech_debate.py
   ```

   _and_

   ```
   python xml_to_rdf/create_rdf_members_policalFunction.py
   ```

   This script will generate RDF files based on the XML files.

6. Upload the generated RDF files to Apache Fuseki.
7. With the RDF data in Fuseki, you can now execute SPARQL queries to analyze and retrieve information from the Greek Parliament debates.

</p>
</details>

## Acknowledgements

- The ANTLR4 library: [https://github.com/antlr/antlr4](https://github.com/antlr/antlr4)
- Apache Jena Fuseki: [https://jena.apache.org/documentation/fuseki2](https://jena.apache.org/documentation/fuseki2)
- OASIS LegalDocumentML (LegalDocML) TC: [https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=legaldocml](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=legaldocml)
