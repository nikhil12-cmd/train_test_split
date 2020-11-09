import cv2 as cv
import argparse
from os import path
from PIL import Image

# YOLO network configuration
yolo_config = 'cfg/yolov4-class1.cfg'
yolo_weights = 'cfg/yolov4-class1.weights'
yolo_class = 'cfg/class.names'

# Parse command line arguments
parser = argparse.ArgumentParser(
    description='Pass image for detection.')
parser.add_argument('--image', required=False,
                    metavar="",
                    help="")
args = parser.parse_args()
print("Image: ", args.image)

# Check for image
if not path.exists(args.image):
    print("Image not found.")
    exit(1)

net = cv.dnn_DetectionModel(yolo_config, yolo_weights)
# Set input size for frame
net.setInputSize(640, 640)
# Set scale factor for frame
net.setInputScale(1.0 / 255)
net.setInputSwapRB(True)

# Read YOLO class file
with open(yolo_class, 'rt') as f:
    names = f.read().rstrip('\n').split('\n')

frame = cv.imread(args.image)

# Try to predict class
classes, confidences, boxes = net.detect(frame, confThreshold=0.1, nmsThreshold=0.4)

# Check prediction
if len(classes) == 0:
    print("No class found.")
    exit(1)

# Create box and write confidence
for classId, confidence, box in zip(classes.flatten(), confidences.flatten(), boxes):
    label = '%.2f' % confidence
    label = '%s: %s' % (names[classId], label)
    labelSize, baseLine = cv.getTextSize(label, cv.FONT_HERSHEY_SIMPLEX, 0.5, 1)
    left, top, width, height = box
    top = max(top, labelSize[1])
    cv.rectangle(frame, box, color=(0, 255, 0), thickness=3)
    cv.rectangle(frame, (left, top - labelSize[1]), (left + labelSize[0], top + baseLine), (255, 255, 255), cv.FILLED)
    cv.putText(frame, label, (left, top), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

# Image
img_tmp = args.image.split('/')
img_out = 'result/' + img_tmp[-1][:-4] + '_result.jpg'

#cv.imshow('out', frame)

cv.imwrite(img_out, frame)
img_pil = Image.open(img_out)
img_pil.show()
