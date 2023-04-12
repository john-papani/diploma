<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:dc="http://purl.org/dc/elements/1.1/">
    <xsl:output method="xml" encoding="UTF-8" />

    <xsl:template match="/">
        <rdf:RDF>
            <xsl:apply-templates select="books/book" />
        </rdf:RDF>
    </xsl:template>

    <xsl:template match="book">
        <rdf:Description>
            <rdf:type rdf:resource="http://schema.org/Book" />
            <dc:title>
                <xsl:value-of select="title" />
            </dc:title>
            <dc:creator>
                <xsl:value-of select="author" />
            </dc:creator>
            <dc:date>
                <xsl:value-of select="year" />
            </dc:date>
            <dc:description>
                <xsl:value-of select="time" />
            </dc:description>
        </rdf:Description>
    </xsl:template>
</xsl:stylesheet>