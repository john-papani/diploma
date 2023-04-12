from lxml import etree

xslt = etree.parse("akoma2rdf.xslt")
transform = etree.XSLT(xslt)
result = transform(etree.parse("20-2-2019.xml"))
result.write("2022019.rdf", encoding="UTF-8", xml_declaration=True)