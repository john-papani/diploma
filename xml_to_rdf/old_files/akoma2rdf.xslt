<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:akn="http://docs.oasis-open.org/legaldocml/ns/akn/3.0"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
    xmlns:greek_lp="http://purl.org/greeklinkedpolitics/vocabulary/"
>
    <!-- Match the root element -->
    <xsl:template match="akn:akomaNtoso">
        <rdf:RDF>
            <!-- Convert metadata -->
            <!-- <xsl:apply-templates select="akn:meta"/> -->

            <!-- Convert debate body -->
            <xsl:apply-templates select="akn:debate" />
            <xsl:message select="akn:debate/debateBody" />
        </rdf:RDF>
    </xsl:template>
    <!-- Convert debate body -->
    <xsl:template match="akn:debate">
        <!-- Convert debateBody sections -->
        <xsl:apply-templates select="akn:debateBody" />
    </xsl:template>

    <!-- Convert debate body -->
    <xsl:template match="akn:debateBody">
        <xsl:apply-templates select="akn:debateSection" />
    </xsl:template>

    <xsl:template match="akn:debateSection">
        <rdf:Description
            rdf:about="http://purl.org/greek_linkedpolitics/eu/plenary/1999-07-20-Speech-2-002">
            <rdfs:label>
                <xsl:value-of select="@name" />
            </rdfs:label>
            <!-- Convert speeches -->
            <xsl:apply-templates select="akn:speech" />
        </rdf:Description>
    </xsl:template>

    <!-- Convert speeches -->
    <xsl:template match="akn:speech">
        <rdf:Description>
            <rdf:type/>
            <!-- Convert speaker -->
            <xsl:apply-templates select="akn:from" />
            <!-- Convert speech content -->
            <rdf:value>
                <xsl:for-each select="akn:p">
                    <xsl:value-of select="." />
                    <!-- Add a new line character -->
                        <xsl:text>&#10;</xsl:text>
                    <!-- <xsl:text> </xsl:text> -->

                </xsl:for-each>
            </rdf:value>
        </rdf:Description>
    </xsl:template>


</xsl:stylesheet>