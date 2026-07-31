# Scene Understanding for the notes of the Unit 5 - CASE STUDY AND APPLICATIONS in the subject of Deep Learning

- Scene understanding is the task of interpreting a visual scene by recognizing its objects, actions, events, and other semantic information.
- Scene understanding is a prerequisite for autonomous driving, as it enables the perception of the surrounding environment and the prediction of future scenarios.
- Scene understanding can be divided into several subtasks, such as image classification, object detection, semantic segmentation, instance segmentation, and action and event recognition.
- Image classification is the task of assigning a label to an image based on its content, such as "cat", "dog", or "car".
- Object detection is the task of locating and identifying the objects in an image, such as drawing bounding boxes around them and assigning labels to them.
- Semantic segmentation is the task of assigning a label to each pixel in an image based on its semantic category, such as "sky", "road", or "person".
- Instance segmentation is the task of assigning a label and an instance ID to each pixel in an image based on its semantic category and its individual object, such as "person 1", "person 2", or "car 1".
- Action and event recognition is the task of identifying the actions and events that are happening in an image or a video, such as "running", "jumping", or "playing soccer".
- Deep learning is a branch of machine learning that uses neural networks to learn from data and perform complex tasks.
- Deep learning has significantly improved the performance of scene understanding, as it can learn high-level features and representations from raw data, such as images and videos.
- Deep learning-based approaches for scene understanding typically use convolutional neural networks (CNNs), which are composed of layers of neurons that apply convolutional filters to the input data and extract features at different levels of abstraction.
- Some examples of deep learning-based approaches for scene understanding are:

  - ResNet, which is a CNN architecture that uses residual connections to enable deeper networks and avoid the problem of vanishing gradients.
  - Faster R-CNN, which is a CNN architecture that combines region proposal network (RPN) and region of interest (ROI) pooling to perform fast and accurate object detection.
  - Mask R-CNN, which is a CNN architecture that extends Faster R-CNN by adding a branch for predicting pixel-wise masks for each object instance, thus achieving instance segmentation.
  - I3D, which is a CNN architecture that inflates 2D convolutional filters to 3D convolutional filters to capture spatiotemporal features for action and event recognition in videos.

- TensorFlow 3D (TF 3D) is a library that provides 3D deep learning capabilities in TensorFlow, such as 3D data processing, 3D model architectures, 3D loss functions, and 3D evaluation metrics.
- TF 3D can be used for 3D scene understanding tasks, such as 3D object detection, 3D semantic segmentation, and 3D instance segmentation.
- TF 3D supports various 3D data formats, such as point clouds, meshes, and voxel grids, and provides efficient data pipelines and preprocessing methods for them.
- TF 3D also provides state-of-the-art 3D model architectures, such as PointNet, PointNet++, and 3D-SSD, which can be easily customized and trained on 3D datasets, such as Waymo Open Dataset and ScanNet.