# Greek Parliament Debates to Open Linked Data

This repository contains the code and resources for the "Greek Parliament Debates to Open Linked Data" diploma thesis. The project aims to convert Greek Parliament debates from text files (in Word or TXT format) to XML files based on the LegalDocML standard. These XML files are then transformed into RDF triples and uploaded to Apache Fuseki for further analysis and querying using SPARQL.
Additionally, the LegalDocML XML files are converted to XML files based on the TEI schema provided by the [ParlaMint repository](https://github.com/clarin-eric/ParlaMint).


<p align="center">
  <img src="greek_parliament_picture.png" width="550" height="335" />
</p>

## Dataset
The dataset used in this project is available at [https://github.com/john-papani/diploma_dataset](https://github.com/john-papani/diploma_dataset). It contains the raw text files of Greek Parliament debates in either Word or TXT format, which serve as the source material for the conversion process.

## Project Structure

The repository is structured as follows:

- [`akn_to_tei/`](https://github.com/john-papani/diploma/tree/master/akn_to_tei): Directory containing the code and resources for converting LegalDocML XML to TEI XML.
- [`antlr4_grammar/`](https://github.com/john-papani/diploma/tree/master/antlr4_grammar): This directory contains the ANTLR4 grammar file used for parsing the text files and generating the XML output.
- [`check_system_stats/`](https://github.com/john-papani/diploma/tree/master/check_system_stats):This directory contains code for generating statistics about the database and files.
- [`lda_topic_modeling/`](https://github.com/john-papani/diploma/tree/master/lda_topic_modeling):This directory contains code related to Latent Dirichlet Allocation (LDA) - Topic modelling.
- [`text_to_akn_xml/`](https://github.com/john-papani/diploma/tree/master/text_to_akn_xml): This directory contains the Python code for converting the text files to LegalDocML XML format.
- [`xml_akn_files/`](https://github.com/john-papani/diploma/tree/master/xml_akn_files): Directory to store the generated LegalDocML XML files.
- [`xml_tei_files/`](https://github.com/john-papani/diploma/tree/master/xml_tei_files): Directory to store the generated TEI XML files.
- [`xml_to_rdf/`](https://github.com/john-papani/diploma/tree/master/xml_to_rdf): This directory contains the code for transforming the XML files into RDF triples.
- [`sparql_queries.txt`](https://github.com/john-papani/diploma/blob/master/sparql_queries.txt): This file provides a collection of example SPARQL queries that can be executed against the RDF data in Apache Fuseki.
- [`debates_papanikolaou_present.pdf`](https://github.com/john-papani/diploma/blob/master/debates_papanikolaou_present.pdf): Slides of presentation.
- [`diploma_debates_papanikolaou_ioannis.pdf`](https://github.com/john-papani/diploma/blob/master/diploma_debates_papanikolaou_ioannis.pdf): __Diploma Thesis (in Greek)__
- [`requirements.txt`](https://github.com/john-papani/diploma/blob/master/requirements.txt): This file lists the Python dependencies required to run the project.


## Sample

You can check a representative [sample of the Greek Parliament debate held on June 8, 2018](https://www.hellenicparliament.gr/UserFiles/a08fc2dd-61a9-4a83-b09a-09f4c564609d/es20180608_1.pdf), which has been converted into both XML/LegalDocML and TEI formats.

> The files are [es20180608000648.docx.xml](https://github.com/john-papani/diploma/blob/master/xml_akn_files/es20180608000648.docx.xml) and [es20180608000648.docx_tei.xml](https://github.com/john-papani/diploma/blob/master/xml_tei_files/es20180608000648.docx_tei.xml) respectively.


_*The rdf data for this file is distributed throughout the rdf files._

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

   This script will process the text files and generate corresponding XML files based on the LegalDocML standard.

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

8. If you want to create TEI files from the LegalDocML XML files, navigate to the `akn_to_tei` directory and run the following command:
   ```
   python create_tei_from_akn.py
   ```

   This script will generate TEI XML files based on the LegalDocML XML files.

9. If you want to create LDA results, navigate to `lda_topic_modeling` directory and run the folling command:
   ```
   python lda.py
   ```
   This script will generate all files for `wordcloud_img/` and results of the topic modelling process (`results/`) [per year]
</p>
</details>

## Acknowledgements

- The ANTLR4 library: [https://github.com/antlr/antlr4](https://github.com/antlr/antlr4)
- Apache Jena Fuseki: [https://jena.apache.org/documentation/fuseki2](https://jena.apache.org/documentation/fuseki2)
- OASIS LegalDocumentML (LegalDocML) TC: [https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=legaldocml](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=legaldocml)

- lxml - Processing XML and HTML with Python: [https://lxml.de](https://lxml.de/)
- cobalt - A lightweight python library for working with Akoma Ntoso (LegalDocML) documents.: [https://github.com/laws-africa/cobalt](https://github.com/laws-africa/cobalt)
- RDFLib is a pure Python package for working with RDF.: [https://rdflib.readthedocs.io/en/stable/](https://rdflib.readthedocs.io/en/stable/)
- Saxon XSLT : [https://www.saxonica.com/saxon-c/index.xml](https://www.saxonica.com/saxon-c/index.xml)
- Python library for interactive topic model visualization. Port of the R LDAvis package. : [https://github.com/bmabey/pyLDAvis](https://github.com/bmabey/pyLDAvis)

## Usage Guidelines
- Contribution: If you find issues with the project or have improvements to suggest, feel free to open an issue or create a pull request.
- Attribution: If you use this project in your research or applications, please provide appropriate attribution to this repository.
- Data Integrity: While efforts have been made to ensure the accuracy of the data, please note that no dataset is perfect. Verify the data according to your use case requirements.