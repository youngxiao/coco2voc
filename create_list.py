# coding=utf-8
'''
create list of train2017 or val2017
the output is train2017.txt val2017.txt
在train2017.txt中保存的格式是每一行　path-to-img/imagename.jpg  path-to-xml/xml.jpg 
'''
import os

def create_list(img_path, xml_path, outlist):
    # get image list
    imglist = []
    for file in os.listdir(img_path):
        if file.split('.')[-1] == 'jpg':
            imglist.append(str(file))

    # imglist loop
    for img in imglist:
        # print(img)
        name = img.split('.')[0]
        fd = open(outlist, 'a')
        img_dir = img_path + name + '.jpg'
        xml_dir = xml_path + name + '.xml'
        line = img_dir + ' ' + xml_dir
        fd.write(line)
        fd.write('\n')
    fd.close()


if __name__ == '__main__':
    img_path = 'JPEGImages/train2017/'
    xml_path = 'Annotations/train2017/'
    outlist = '/home/alpha/dataset/COCO/train2017_list.txt'
    create_list(img_path, xml_path, outlist)