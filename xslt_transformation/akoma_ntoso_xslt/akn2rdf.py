from lxml import etree
file_name = "c:/Users/johnp/Documents/ECE_NTUA/diploma/dipoma_code/diploma_python_data_scrapping/xmls_files/es20190211000784.docx.xml"
xslt = etree.parse("akoma2rdf.xslt")
transform = etree.XSLT(xslt)
result = transform(etree.parse(file_name))
result.write("test_rdf.rdf", encoding="UTF-8", xml_declaration=True)
