### Scene Understanding for the notes of the Unit 5 - CASE STUDY AND APPLICATIONS in the subject of Deep Learning

- Scene understanding is the task of analyzing a scene captured by a sensor (such as a camera, a lidar, a radar, etc.) and extracting semantic information from it, such as the objects, actions, and events present in the scene  .
- Scene understanding is a prerequisite for autonomous driving, as it enables the vehicle to perceive its surroundings and make decisions accordingly .
- Scene understanding can be divided into several subtasks, such as image classification, object detection, semantic segmentation, instance segmentation, and action and event recognition .
- Image classification is the task of assigning a label to an image based on its content, such as "cat", "dog", "car", etc. Image classification is the simplest form of scene understanding, as it does not provide any spatial information about the objects in the image .
- Object detection is the task of locating and identifying the objects in an image, usually by drawing bounding boxes around them and assigning labels to them, such as "cat", "dog", "car", etc. Object detection provides more spatial information than image classification, but it does not distinguish between different instances of the same object class, nor does it capture the shape and boundaries of the objects .
- Semantic segmentation is the task of assigning a label to each pixel in an image based on the object it belongs to, such as "cat", "dog", "car", etc. Semantic segmentation provides more detailed information than object detection, as it captures the shape and boundaries of the objects, but it does not distinguish between different instances of the same object class .
- Instance segmentation is the task of assigning a label and an instance ID to each pixel in an image based on the object it belongs to, such as "cat_1", "cat_2", "dog_1", etc. Instance segmentation provides the most detailed information among the subtasks, as it captures the shape, boundaries, and identity of the objects, and it can distinguish between different instances of the same object class .
- Action and event recognition is the task of identifying the actions and events that are occurring in a scene, such as "running", "jumping", "fighting", etc. Action and event recognition can be applied to static images or dynamic videos, and it can provide temporal information about the scene .

- Deep learning is a powerful technique for scene understanding, as it can learn complex and hierarchical features from large amounts of data, and it can handle various types of sensors and modalities, such as images, videos, point clouds, etc    .
- Deep learning models for scene understanding are usually based on convolutional neural networks (CNNs), which are composed of layers of neurons that apply convolutional filters to the input data, and can extract local and global features from the data .
- Deep learning models for scene understanding can be trained in a supervised, semi-supervised, or unsupervised manner, depending on the availability and quality of the labels for the data .
- Deep learning models for scene understanding can be evaluated using various metrics, such as accuracy, precision, recall, F1-score, mean average precision (mAP), mean intersection over union (mIoU), etc., depending on the subtask and the application  .

- Some examples of deep learning models for scene understanding are:

  - ResNet, a CNN model for image classification that uses residual connections to enable deeper networks and avoid the vanishing gradient problem.
  - YOLO, a CNN model for object detection that divides the image into a grid and predicts bounding boxes and class probabilities for each grid cell in a single pass.
  - Mask R-CNN, a CNN model for instance segmentation that extends the Faster R-CNN model for object detection by adding a branch for predicting pixel-wise masks for each object.
  - PointNet, a neural network model for point cloud processing that can perform tasks such as semantic segmentation, object detection, and classification on 3D point