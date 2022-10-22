#salvss@outlook.com
import os as OS
from xml.etree import ElementTree as ET

filename = f'\\NacerEdit1.xml'
header = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!-- python script by Salvatore Scalia https://github.com/SalvatoreScalia/problem_with_waveformPro -->\n"

current_path = OS.getcwd()
print( "steop 1: " + str(current_path) + filename)
tracktionedit_tree = ET.parse(current_path + filename)
root = tracktionedit_tree.getroot()

elements = root.findall('./TRACK')
for element in elements:
    if element.get('id')=='1038':
        plugins = element.findall('./PLUGIN')
        for p in plugins:
            print(p.attrib['type'])
            sounds = p.findall('./SOUND')
            i = 0
            for s in sounds:
                print(str(s.attrib['name'] + "\t" + s.attrib['keyNote']  + "\t" + s.attrib['minNote'] + "\t" + s.attrib['maxNote']))
                s.set('keyNote',str(i+48))
                s.set('minNote',str(i+48))
                s.set('maxNote',str(i+48))
                print(str(s.attrib['name'] + "\t" + s.attrib['keyNote']  + "\t" + s.attrib['minNote'] + "\t" + s.attrib['maxNote']))
                i=i+1

ET.indent(tracktionedit_tree)
#ET.register_namespace('',"Waveform 11.1.0")
xmlstr_tracktionedit_tree = ET.tostring(root).decode()
# Create a file with header + xmlstr
with open(OS.getcwd() + filename, "w", encoding='UTF-8') as out:
    out.write(header + xmlstr_tracktionedit_tree)
