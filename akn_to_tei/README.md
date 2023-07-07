# Akoma Ntoso to TEI XML Converter

This Python script converts XML Akoma Ntoso files to XML files based on the TEI schema provided by the [ParlaMint repository](https://github.com/clarin-eric/ParlaMint). It provides a convenient way to transform parliamentary data into a format compatible with the TEI Schema. 

## Folder Structure
The folder structure for the project is as follows:
-   `schema_dir/`: 
	- `Schema/`: Directory containing the Akoma Ntoso schema files
    - `akn2tei.xsl `: XSLT file for converting Akoma Ntoso to TEI XML
-   `create_tei_from_akn.py`: Python script for converting Akoma Ntoso to TEI XML
-  ` no_xml_tei_files.txt`: Log file to track TEI XML files that were not generated

## Prerequisites
To use this script, ensure that you have the following:
- Python 3.11 installed on your system.
- The required Python dependency installed - [Saxon/C](https://www.saxonica.com/saxon-c/index.xml). You can find it in the [requirements.txt](https://github.com/john-papani/diploma/blob/master/requirements.txt) file.
 

## Getting Started
1. Place your XML Akoma Ntoso files in the [input directory](https://github.com/john-papani/diploma/tree/master/xmls_files).
2. Open a terminal or command prompt and navigate to the folder where the script is located.
	```
	cd akn_to_tei
	```
3. Run the script using the following command:
	```
	python create_tei_from_akn.py
	```
4. The converted TEI XML files will be generated in the [output directory](https://github.com/john-papani/diploma/tree/master/xml_tei_files).

## Acknowledgments
- This script was developed based on the TEI schema provided by the [ParlaMint repository](https://github.com/clarin-eric/ParlaMint). 