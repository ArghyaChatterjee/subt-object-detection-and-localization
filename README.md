# SubT Object Detection and Localization
It's a repository for preserving Artifact detection model in order to detect object using YOLO v3 inside SubT simulator / real world SubT Environment. 

<p align="center">
    <a href="https://www.youtube.com/watch?v=wtAtQa4P74U" target="_blank">
    <img src="asset/Custom_object_detection.gif" alt="Video Thumbnail" width="100%">
  </a>
</p>

## Artifact Classes:
No. of Artifact Classes: 5 <br>
Name of the Artifact Classes: Backpack, Survivor, Cell Phone, Fire Extinguisher, Drill.
## Artifact Localization Points:
You can see the Artifacts Specification in details [here](https://www.subtchallenge.com/resources/SubT_Cave_Artifacts_Specification.pdf).
<p align="center">
    <img src="asset/Artifact.png", width="400">
</p>

## Darknet Installation:
You need to install darknet on your Ubuntu 18.04 machine. Follow the tutorial [here](https://github.com/AlexeyAB/darknet) to install darknet in order to use YOLO V3/v4. Check the installation with your webcam to reassure that you have installed it properly.  
## Training Data:
Training & Validation Dataset (i.e `train` & `valid` folder) with proper labeling should be kept inside `~/darknet/data` directory. You can download the training and validation dataset from [here](https://drive.google.com/drive/folders/1vJiqT4SQExbuHGb6kJoW2MeFRDpF8kJq?usp=sharing). Download pre-trained weight file for convolutional layer from [darknet53.conv.74](https://pjreddie.com/media/files/darknet53.conv.74) & keep it inside `~/darknet` directory. 
## Labelling Data:
In order to label data collected from different sources, install `labelImg`. You can find the corresponding download & installation proccedure [here](https://github.com/tzutalin/labelImg). Just remember when using 'labelImg', change the image labeling format from pascal to YOLO (by clicking on the side button 'pascal') and save the corresponding 'img.txt' labeled files accordingly. Each labeled image will produce a 'x.txt' file where the value 'x' will be the name of the original image. 
## Creating Text files for Training & Testing:
To create `train.txt` and `test.txt`, download `train_txt_creator.py` & `test_txt_creator.py` files from this repository, put them inside `Home` directory and run in the terminal:
```
## To create train.txt file, don't forget to change the path mentioned inside train_txt_creator.py file
python train_txt_creator.py

## To create test.txt file, don't forget to change the path mentioned inside test_txt_creator.py file
python test_txt_creator.py
```
## Training Demo:
```
cd ~/darknet
./build-release/darknet detector train data/train.data cfg/yolov3_train.cfg darknet53.conv.74
```
## Training Loss Curve:
<p align="center">
    <img src="asset/chart.png", width="400">
</p>

## Generate Weight File:
The default weight file will be saved after every 1000 iterations inside `~/darknet/backup` directory during training. You can use your own weight file or you can use mine. In my case, I have trained for around 9000 iterations. It took around 26 hours for training purpose. You can download the weight file from [here](https://drive.google.com/drive/folders/1vJiqT4SQExbuHGb6kJoW2MeFRDpF8kJq?usp=sharing).  
## Testing Demo:
```
cd ~/darknet
./build-release/darknet detector demo data/train.data cfg/yolov3_test.cfg backup/yolov3_train_9000.weights -c 0
```
## Testing Result:
<p align="center">
    <img src="asset/detected_artifacts.png", width="400">
</p>

## Resources Used During Training & Testing:
The data were trained inside Ubuntu 18.04 with Nvidia Graphics GTX 1070, Driver version 440.82 & CUDA version 10.2. I took around 300 images for each class totalling to 1500 images of which 1350 (90%) images were used as training dataset & 150 images (10%) were used as validation dataset. The testing was done both with a logitech webcam in real life environment & with an Intel RealSense in virtual environment. In both the time, the detection frame rate was 15 fps.  

<p align="center">
  <a href="https://www.youtube.com/watch?v=3e3ne0HYJ2U" target="_blank">
    <img src="asset/ANYmal.gif" alt="Video Thumbnail" width="100%">
  </a>
</p>

## Image Copyright: 
Some of the images used in this repo are properties of DARPA. The images used in this work during training are taken from the internet. Respective people can claim copyright for the images.     
