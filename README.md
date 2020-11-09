# License-Plate-Detection-Using-YOLOv4

### **License Plate Detection using YOLOv4**

Train YOLOv4 to detect license plates in the image. 

![car1_result_r](images/car1_result_r.jpg)

**Requirements**

1. Clone Darknet (YOLOv4) repo: [https://github.com/AlexeyAB/](https://github.com/AlexeyAB/darknet)[darknet](https://github.com/AlexeyAB/darknet)
2. Download yolo4.weights to test installation of darknet from [here](https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights)
3. Download license plates weights from this [link](https://drive.google.com/file/d/13G5sPHnPc-Ubm-H-iba_RCjoI3EwxC3r/view?usp=sharing).
4. To train YOLOv4 for license plate detection download starting weights from [here](https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.conv.137).
5. Download license plate dataset from [here](https://github.com/RobertLucian/license-plate-dataset)

**Train YOLOv4**

You can start training of YOLOv4 for license plate detection after successful build of Darknet. To build Darknet according to your system configuration please follow instruction from this [link](https://github.com/AlexeyAB/darknet#how-to-compile-on-linux-using-cmake). 

In *TrainDarknet\cfg\yolov4-class1.cfg* following changes were made to train YOLOv4.

batch=64

subdivisions=64

width=640

height=640

max_batches = 2000 # classes*2000

steps=1600,1800

Change [filters=255] to filters=(classes + 5)x3 in the 3 [convolutional] before each [yolo] layer. In our case its 18

filters=18

Use this command for training:

Start training by:
`./darknet detector train "obj/obj.data" "cfg/yolov4-class1.cfg" "weights/yolov4.conv.137"`

Resume training by:
`./darknet detector train "obj/obj.data" "cfg/yolov4-class1.cfg" "backup/ yolov4-class1_last.weights"` 

Directory Structure

```bash
├── backup
├── cfg
│   └── yolov4-class1.cfg
├── img
├── obj
│   ├── obj.data
│   └── obj.names
├── test.txt
├── train.txt
└── weights
    └── yolov4.conv.137
```

Test trained weight or pre-trained weight by using `licenseplate_yolo4.py` provided in **LicensePlateDetection** folder.

**References**

* https://pjreddie.com/darknet/yolo/
* https://github.com/AlexeyAB/darknet

**Cite**

```
@misc{darknet13,
  author =   {Joseph Redmon},
  title =    {Darknet: Open Source Neural Networks in C},
  howpublished = {\url{http://pjreddie.com/darknet/}},
  year = {2013--2016}
}
```









