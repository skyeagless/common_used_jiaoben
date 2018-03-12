import os
import xml.etree.ElementTree as ET

folder_src="E:/data/Annotations"
folder_dst="E:/data/annotations-Brace_sleeve_screw"


for root,dira,files in os.walk(folder_src):
    for file in files:
        tree=ET.parse(folder_src+'/'+file)
        root=tree.getroot()
        for obj in root.findall("object"):
            name=str(obj.find("name").text)
            if name !="Brace_sleeve_screw":
                root.remove(obj)
        tree.write(folder_dst+"/"+file)








