# coding=utf-8

'''
coco2017的数据集中label是1-90的，取 coco 的 80 类以及对应的标签
output: coco_train.json or coco_val.json
'''
import json

# 80 categories 
className = {
    1: 'person', 2: 'bicycle', 3: 'car', 4: 'motorcycle', 5: 'airplane', 6: 'bus', 7: 'train', 8: 'truck',
    9: 'boat', 10: 'traffic light', 11: 'fire hydrant', 13: 'stop sign', 14: 'parking meter', 15: 'bench',
    16: 'bird', 17: 'cat', 18: 'dog', 19: 'horse', 20: 'sheep', 21: 'cow', 22: 'elephant', 23: 'bear',
    24: 'zebra', 25: 'giraffe', 27: 'backpack', 28: 'umbrella', 31: 'handbag', 32: 'tie', 33: 'suitcase',
    34: 'frisbee', 35: 'skis', 36: 'snowboard', 37: 'sports ball', 38: 'kite', 39: 'baseball bat',
    40: 'baseball glove', 41: 'skateboard', 42: 'surfboard', 43: 'tennis racket', 44: 'bottle', 46: 'wine glass',
    47: 'cup', 48: 'fork', 49: 'knife', 50: 'spoon', 51: 'bowl', 52: 'banana', 53: 'apple', 54: 'sandwich',
    55: 'orange', 56: 'broccoli', 57: 'carrot', 58: 'hot dog', 59: 'pizza', 60: 'donut', 61: 'cake', 62: 'chair',
    63: 'couch', 64: 'potted plant', 65: 'bed', 67: 'dining table', 70: 'toilet', 72: 'tv', 73: 'laptop',
    74: 'mouse', 75: 'remote', 76: 'keyboard', 77: 'cell phone', 78: 'microwave', 79: 'oven', 80: 'toaster',
    81: 'sink', 82: 'refrigerator', 84: 'book', 85: 'clock', 86: 'vase', 87: 'scissors', 88: 'teddy bear',
    89: 'hair drier', 90: 'toothbrush'
}
 
classNum = [1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,27,
            28,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,48,49,50,51,52,
            53,54,55,56,57,58,59,60,61,62,63,64,65,67,70,72,73,74,75,76,77,78,
            79,80,81,82,84,85,86,87,88,89,90]
 
def writeNum(Num):
    with open('coco_val.json','a+') as f:
        f.write(str(Num))
 
inputfile = []
inner = {}
# write to json
# modify the path, instances_train2017.json or instances_val2017.json
with open('/home/alpha/dataset/COCO/annotations/instances_train2017.json','r+') as f:
    allData = json.load(f)
    data = allData['annotations']
    print('read ready')

# 其中取的 'image_id' 为图片序号，与图片名称不同
# 图片名称是对应 'image_id' 在其前面补0,保证12位的图片名称 
for i in data:
    if(i['category_id'] in classNum):
        inner = {
            'filename': str(i['image_id']).zfill(6),
            'name': className[i['category_id']],
            'bndbox':i['bbox']
        }
        inputfile.append(inner)
inputfile = json.dumps(inputfile)
writeNum(inputfile)
