import os
from PIL import Image
import xml.dom.minidom
import numpy as np

AnnoPath = '/home/skyeagle/VOC2007/Annotations/'
ImgPath = '/home/skyeagle/VOC2007/JPEGImages/'
ProcessedPath = '/home/skyeagle/VOC2007/12_classes/'


annolist=os.listdir(AnnoPath)
for anno in annolist:
    anno_pre,ext = os.path.splitext(anno)
    xmlfile = AnnoPath + anno
    imgfile = ImgPath + anno_pre+".jpg"

    DomTree = xml.dom.minidom.parse(xmlfile)  #得到一个dom树，加载XML文件
    annotation = DomTree.documentElement #获取xml文档对象

    filenamelist = annotation.getElementsByTagName('filename')
    filename = filenamelist[0].childNodes[0].data  #提取filename的data


    objectlist = annotation.getElementsByTagName('object')

    i = 1
    for objects in objectlist:

        namelist = objects.getElementsByTagName('name')
        objectname = namelist[0].childNodes[0].data

        savepath = ProcessedPath + objectname

        if not os.path.exists(savepath):
            os.makedirs(savepath)


        boxlist = objects.getElementsByTagName('bndbox')

        for box in boxlist:
            x1_list = box.getElementsByTagName('xmin')
            x1 = int(x1_list[0].childNodes[0].data)
            y1_list = box.getElementsByTagName('ymin')
            y1 = int(y1_list[0].childNodes[0].data)
            x2_list = box.getElementsByTagName('xmax')
            x2 = int(x2_list[0].childNodes[0].data)
            y2_list = box.getElementsByTagName('ymax')
            y2 = int(y2_list[0].childNodes[0].data)

            cutbox = (x1, y1, x2, y2)

            img = Image.open(imgfile)
            cropedimg = img.crop(cutbox)
            cropedimg.save(savepath + '/' + anno_pre + '_'+ objectname + str(i) +'.jpg')
            i=i+1

