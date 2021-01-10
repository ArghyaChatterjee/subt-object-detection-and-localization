# SubT-Object-Detection
It's a repository which preserves Artifact detection model in order to detect object using YOLO v3 inside SubT simulator / real world SubT World.
## Training Demo:
```
./build-release/darknet detector train data/train.data cfg/yolov3_train.cfg darknet53.conv.74
```
## Testing Demo:
```
./build-release/darknet detector demo data/train.data cfg/yolov3_train.cfg backup/yolov3_train_9000.weights -c 0
```
