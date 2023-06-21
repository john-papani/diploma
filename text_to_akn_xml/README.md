# Text to Akoma Ntoso XML Conversion

This directory contains the code for converting Greek Parliament debate text files to XML files based on the Akoma Ntoso standard.

## File Description

- `convert_to_xml.py`: This script is responsible for converting the input text files to XML files following the Akoma Ntoso schema. It utilizes the ANTLR4 grammar and parsing rules defined in the `./antlr4_grammar` directory to parse the text files and generate the corresponding XML output.

- `no_xml_files.txt`: This file lists the names of text files that could not be converted to XML. If any text files fail to convert, they will be listed in this file along with the reason for the failure.

## Usage

To convert the Greek Parliament debate text files to Akoma Ntoso XML format:
- Just run the `convert_to_xml.py` script with the following command:
   ```
   python convert_to_xml.py 
   ```
The script will process each text file, parse its contents using the ANTLR4 grammar, and generate the corresponding XML file in the specified output directory.