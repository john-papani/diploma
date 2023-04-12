<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:akn="https://www.akomantoso.org/3.0">
    
    <xsl:output method="xml" indent="yes"/>

    <xsl:template match="/">
        <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:akn="https://www.akomantoso.org/3.0">
            <rdf:Description rdf:about="http://example.com/debate/_0">
                <rdf:type rdf:resource="http://example.com/ontology/Debate"/>
                <rdf:value><xsl:value-of select="akn:debate/akn:meta/akn:identification/akn:FRBRWork/akn:FRBRalias"/></rdf:value>
                <rdf:meta>
                    <rdf:type rdf:resource="http://example.com/ontology/DebateMeta"/>
                    <rdf:source><xsl:value-of select="akn:debate/akn:meta/akn:source/akn:name"/></rdf:source>
                    <rdf:date><xsl:value-of select="akn:debate/akn:meta/akn:source/akn:date"/></rdf:date>
                </rdf:meta>
                <rdf:Statement>
                    <rdf:subject rdf:resource="http://example.com/debate/_0"/>
                    <rdf:predicate rdf:resource="http://example.com/ontology/hasSpeech"/>
                    <rdf:object rdf:resource="http://example.com/speaker/_1"/>
                </rdf:Statement>
            </rdf:Description>
            <xsl:apply-templates select="akn:debate//akn:speech"/>
        </rdf:RDF>
    </xsl:template>

    <xsl:template match="akn:speech">
        <rdf:Description rdf:about="http://example.com/speech/{generate-id()}">
            <rdf:type rdf:resource="http://example.com/ontology/Speech"/>
            <rdf:value><xsl:value-of select="normalize-space(.)"/></rdf:value>
            <rdf:Statement>
                <rdf:subject rdf:resource="http://example.com/debate/_0"/>
                <rdf:predicate rdf:resource="http://example.com/ontology/hasSpeaker"/>
                <rdf:object rdf:resource="http://example.com/speaker/{generate-id(akn:speaker)}"/>
            </rdf:Statement>
        </rdf:Description>
        <rdf:Description rdf:about="http://example.com/speaker/{generate-id(akn:speaker)}">
            <rdf:type rdf:resource="http://example.com/ontology/Speaker"/>
            <rdf:name><xsl:value-of select="akn:speaker"/></rdf:name>
        </rdf:Description>
    </xsl:template>

</xsl:stylesheet>