### 1. download coco2017 dataset

### 2. select categories
```
python select_categories.py
```

### 3. remove others
```
python remove.py
```

### 4. convert .json to .xml
```shell
python create_xml.py
```

### 5. create image and annotation list
```shell
python create_list.py
```

### 6. create data --> lmdb format
```shell
./create_data.sh
```
