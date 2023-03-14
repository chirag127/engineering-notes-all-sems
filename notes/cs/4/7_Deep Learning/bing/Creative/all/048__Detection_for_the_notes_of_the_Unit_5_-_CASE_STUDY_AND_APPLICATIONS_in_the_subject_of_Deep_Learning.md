### Detection for the notes of the Unit 5 - CASE STUDY AND APPLICATIONS in the subject of Deep Learning

- Detection is the task of predicting the location and class of an object in an image using deep learning techniques.
- Detection can be useful for many applications, such as face recognition, security, autonomous driving, medical imaging, etc.
- Detection can be divided into two subtasks: localization and classification.
  - Localization is the process of finding the coordinates of a bounding box that encloses the object of interest in the image.
  - Classification is the process of assigning a label to the object based on its appearance and features.
- Detection can be performed using different deep learning architectures, such as:
  - Region-based Convolutional Neural Networks (R-CNN) and its variants, such as Fast R-CNN, Faster R-CNN, and Mask R-CNN. These methods use a two-stage approach, where the first stage generates a set of candidate regions using a region proposal network, and the second stage classifies each region using a convolutional neural network.
  - You Only Look Once (YOLO) and its variants, such as YOLO v2, YOLO v3, and YOLO v4 . These methods use a single-stage approach, where the image is divided into a grid of cells, and each cell predicts a fixed number of bounding boxes and class probabilities using a convolutional neural network.
  - Single Shot Detector (SSD) and its variants, such as SSD300 and SSD512. These methods also use a single-stage approach, but instead of using a fixed grid, they use multiple feature maps of different resolutions to predict bounding boxes and class probabilities using a convolutional neural network.
- Detection can be evaluated using different metrics, such as:
  - Intersection over Union (IoU), which measures the overlap between the predicted bounding box and the ground truth bounding box. A higher IoU indicates a better localization.
  - Average Precision (AP), which measures the precision and recall of the detection system for a given class. Precision is the ratio of true positives to all positives, and recall is the ratio of true positives to all relevant instances. A higher AP indicates a better classification.
  - Mean Average Precision (mAP), which measures the average of the APs over all classes. A higher mAP indicates a better overall performance of the detection system.

- A possible mnemonic to remember the difference between localization and classification is: **LOC**alization finds the **LOC**ation, and **CLASS**ification assigns the **CLASS**.
- A possible mnemonic to remember the difference between R-CNN, YOLO, and SSD is: R-CNN is **R**egion-based, YOLO is **YO**u **O**nly **L**ook **O**nce, and SSD is **S**ingle **S**hot **D**etector.