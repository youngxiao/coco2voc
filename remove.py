# coding=utf-8

'''
remove the image do not in the categories.
''' 
import json
import os
 
nameStr = []
 
with open('coco_val.json','r+') as f:
    data = json.load(f)
    print('read ready')

# 其中 'filename' 取的 'image_id' 为图片序号，与图片名称不同
# 图片名称是对应 'image_id' 在其前面补0,保证12位的图片名称  
for i in data:
    count = 0
    imgName = str(i['filename'])
    for s in imgName:
        count = count + 1
    for j in range(12-count):
        imgName = '0' + imgName
    nameStr.append(imgName+'.jpg')

nameStr = set(nameStr)
print(len(nameStr))
 
path = '/home/alpha/dataset/COCO/val2017/'
 
for file in os.listdir(path):
    if(file not in nameStr):
        print(file)
        os.remove(path+file)
