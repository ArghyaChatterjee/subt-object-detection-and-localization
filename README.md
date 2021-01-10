# SubT-Object-Detection
It's a repository which preserves Artifact detection model in order to detect object using YOLO v3 inside SubT simulator / real world SubT Environment.
## Training Demo:
```
cd ~/darknet
./build-release/darknet detector train data/train.data cfg/yolov3_train.cfg darknet53.conv.74
```
## Training Loss Curve:
<p align="center">
    <img src="asset/chart.png", width="400">
</p>

## Testing Demo:
```
cd ~/darknet
./build-release/darknet detector demo data/train.data cfg/yolov3_train.cfg backup/yolov3_train_9000.weights -c 0
```
