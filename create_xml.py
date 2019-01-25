# coding=utf-8
 
import xml.dom
import xml.dom.minidom
import os
import cv2
import json

_IMAGE_PATH= '/home/alpha/dataset/COCO/train2017'
 
_INDENT= ''*4
_NEW_LINE= '\n'
_FOLDER_NODE= 'train2017'
_ROOT_NODE= 'annotation'
_DATABASE_NAME= 'COCO'
_ANNOTATION= 'train2017'
_DIFFICULT= '0'
_TRUNCATED= '0'
_POSE= 'Unspecified'
# 保存的目录
_ANNOTATION_SAVE_PATH= 'Annotations/train2017'
 
# 创建节点
def createElementNode(doc,tag, attr):  # 创建一个元素节点
    element_node = doc.createElement(tag)
    # 创建一个文本节
    text_node = doc.createTextNode(attr)
    # 将文本节点作为元素节点的子节
    element_node.appendChild(text_node)
    return element_node
 
# 创建子节点
def createChildNode(doc,tag, attr,parent_node):
    child_node = createElementNode(doc, tag, attr)
    parent_node.appendChild(child_node)
 
 
# 创建 object 节点以及子节点
def createObjectNode(doc,attrs):
    object_node = doc.createElement('object')
    createChildNode(doc, 'name', attrs['name'], object_node)
    createChildNode(doc, 'pose', _POSE, object_node)
    createChildNode(doc, 'truncated', _TRUNCATED, object_node)
    createChildNode(doc, 'difficult', _DIFFICULT, object_node)
    bndbox_node = doc.createElement('bndbox')
    createChildNode(doc, 'xmin', str(int(attrs['bndbox'][0])), bndbox_node)
    createChildNode(doc, 'ymin', str(int(attrs['bndbox'][1])), bndbox_node)
    createChildNode(doc, 'xmax', str(int(attrs['bndbox'][0]+attrs['bndbox'][2])), bndbox_node)
    createChildNode(doc, 'ymax', str(int(attrs['bndbox'][1]+attrs['bndbox'][3])), bndbox_node)
    object_node.appendChild(bndbox_node)
    return object_node
 
# 写入 xml 文件
def writeXMLFile(doc,filename):
    tmpfile =open('tmp.xml','w')
    doc.writexml(tmpfile, addindent=''*4,newl = '\n',encoding = 'utf-8')
    tmpfile.close()
    # 删除第一行默认添加的标记
    fin =open('tmp.xml')
    fout =open(filename, 'w') 
    lines = fin.readlines()
 
    for line in lines[1:]: 
        if line.split():
            fout.writelines(line)

    fin.close()
    fout.close()
 
 
if __name__ == '__main__':
    img_path = '/home/alpha/dataset/COCO/train2017/'
    fileList = os.listdir(img_path)
    if fileList == 0:
        os._exit(-1)
 
    with open('coco_val.json', 'r') as f:
        ann_data = json.load(f)
 
    current_dirpath = os.path.dirname(os.path.abspath('__file__'))
 
    if not os.path.exists(_ANNOTATION_SAVE_PATH):
        os.mkdir(_ANNOTATION_SAVE_PATH)

    for imageName in fileList:
        saveName= imageName.strip('.jpg')
        print(saveName)
        xml_file_name = os.path.join(_ANNOTATION_SAVE_PATH, (saveName + '.xml'))
        img=cv2.imread(os.path.join(img_path,imageName))
        print(os.path.join(img_path,imageName))
        height,width,channel=img.shape
        print(height,width,channel)
 
 
        my_dom = xml.dom.getDOMImplementation()
        doc = my_dom.createDocument(None,_ROOT_NODE,None)
 
        # root node
        root_node = doc.documentElement
 
        # folder node
        createChildNode(doc, 'folder',_FOLDER_NODE, root_node)
 
        # filename node
        createChildNode(doc, 'filename', saveName+'.jpg',root_node)
 
        # source node
        source_node = doc.createElement('source')
        # source child node
        createChildNode(doc, 'database',_DATABASE_NAME, source_node) 
        root_node.appendChild(source_node)
 
        # size node  
        size_node = doc.createElement('size') 
        createChildNode(doc, 'width',str(width), size_node) 
        createChildNode(doc, 'height',str(height), size_node) 
        createChildNode(doc, 'depth',str(channel), size_node) 
        root_node.appendChild(size_node)

        # object node 
        # 'coco_train.json' 文件中的 filename 取的是 'image_id'
        # 比如 image_id = '342112',　实际对应的图片是 '00000034112.jpg'
        # 因此要将 ann_data 中的 filename 补 0 
        for ann in ann_data:
            count = 0
            imgName = str(ann['filename'])
            for s in imgName:
                count = count + 1
            for j in range(12-count):
                imgName = '0' + imgName

            if(saveName==imgName):
                object_node = createObjectNode(doc, ann)
                root_node.appendChild(object_node)
            else:
                continue
 
        # 构建XML文件名称
        print(xml_file_name)

        # 写入文件
        writeXMLFile(doc, xml_file_name)