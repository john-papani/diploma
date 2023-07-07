import os
from saxonche import PySaxonProcessor

def transform_xml2tei_with_xslt(xml_filename, xslt_filename, result_filename):
    log_file = open('./no_xml_tei_files.txt', 'a', encoding="utf8")

    with PySaxonProcessor(license=False) as proc:
        try:
            xsltproc = proc.new_xslt30_processor()
            document = proc.parse_xml(xml_file_name=xml_filename)
            executable = xsltproc.compile_stylesheet(stylesheet_file=xslt_filename)
            output = executable.transform_to_string(xdm_node=document)
            
            with open(result_filename, "w",encoding="utf-8") as file:
                    file.write(output)
        except Exception as e:
            log_file.write(f'{filename}: {str(e)}\n')


datapath = "C:/Users/johnp/Documents/ECE_NTUA/diploma/diploma_github/xmls_files/"
filenames = sorted([f for f in os.listdir(datapath) if not f.startswith('.')])
xslt_filename = "./schema_dir/akn2tei.xsl"
for counter, filename in enumerate(filenames):
    if (counter % 100 == 0):
                print("File "+str(counter)+' from ' +
                  str(len(filenames)) + ' '+filename)
    new_filename = filename.rsplit(".", 1)[0]
    result_filename = f"../xml_tei_files/{new_filename}_tei.xml"
    transform_xml2tei_with_xslt(datapath+filename, xslt_filename, result_filename)