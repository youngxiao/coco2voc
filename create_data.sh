cur_dir=$(cd $( dirname ${BASH_SOURCE[0]} ) && pwd )
root_dir="$HOME/caffe"

cd $root_dir

redo=1
data_root_dir="$HOME/dataset/COCO"
dataset_name="COCO"
mapfile="$HOME/dataset/COCO/labelmap_coco.prototxt"
anno_type="detection"
db="lmdb"
min_dim=0
max_dim=0
width=0
height=0

extra_cmd="--encode-type=jpg --encoded"
if [ $redo ]
then
  extra_cmd="$extra_cmd --redo"
fi
for subset in val2017 train2017
do
  python $root_dir/scripts/create_annoset.py \
    --anno-type=$anno_type \
    --label-map-file=$mapfile \
    --min-dim=$min_dim --max-dim=$max_dim --resize-width=$width --resize-height=$height \
    --check-label $extra_cmd $data_root_dir \
    $data_root_dir/$subset"_list".txt \
    $data_root_dir/$db/$dataset_name"_"$subset"_"$db \
    $root_dir/examples/$dataset_name
done
