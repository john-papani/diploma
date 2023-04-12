from lxml import etree

xslt = etree.parse("rules_for_catalogs.xslt")
transform = etree.XSLT(xslt)
result = transform(etree.parse("catalogs.xml"))
result.write("calatogs.rdf", encoding="UTF-8", xml_declaration=True)