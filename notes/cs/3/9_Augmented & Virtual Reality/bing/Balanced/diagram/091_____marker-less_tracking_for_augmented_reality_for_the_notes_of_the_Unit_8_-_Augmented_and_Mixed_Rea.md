Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on marker-less tracking for augmented reality for the notes of the Unit 8 - Augmented and Mixed Reality in the subject of Augmented & Virtual Reality:

### Marker-less tracking for augmented reality

- Marker-less tracking is a technique that allows developers to display augmented reality content without the need for predefined target images or objects (markers) in the real environment.
- Marker-less tracking relies on scanning the surrounding environment and detecting natural features such as edges, corners, textures, or planes that can be used as reference points for the virtual content.
- Marker-less tracking can be classified into two types: image-based and model-based.
  - Image-based tracking uses a database of images or video frames that are matched with the current camera view using feature detection and description algorithms such as ORB, FREAK, SIFT, SURF, etc. The matching features are then used to estimate the pose of the camera relative to the scene .
  - Model-based tracking uses a 3D model of the scene or object that is registered with the camera view using methods such as edge detection, contour matching, or point cloud alignment. The model can be either pre-built or reconstructed online using structure from motion or simultaneous localization and mapping (SLAM) techniques.
- Marker-less tracking has several advantages over marker-based tracking, such as:
  - It can work with any environment or object, without the need for artificial markers that may be occluded, damaged, or unavailable.
  - It can provide more realistic and immersive experiences, as the virtual content can be aligned with the natural features of the scene.
  - It can enable more interactive and dynamic applications, as the virtual content can respond to changes in the environment or user actions.
- Marker-less tracking also has some challenges and limitations, such as:
  - It requires more computational resources and processing power, as it involves complex algorithms and large amounts of data.
  - It may suffer from drift, noise, or inaccuracies, as it depends on the quality and stability of the features detected in the environment.
  - It may not work well in low-light, featureless, or cluttered environments, as it may fail to find enough or reliable features to track.
