# Marker-less Tracking for Augmented Reality

- Marker-less tracking is a technique that allows augmented reality (AR) applications to display virtual content on top of real-world scenes without the need for predefined markers, such as images or objects.
- Marker-less tracking relies on detecting and tracking natural features in the environment, such as edges, corners, textures, or colors, and using them as reference points for estimating the camera pose and orientation.
- Marker-less tracking can be classified into two main categories: model-based and appearance-based.
  - Model-based tracking uses a 3D model of the scene or the object of interest to match the features extracted from the camera image and compute the camera pose. This method requires prior knowledge of the scene geometry and appearance, and can handle occlusions and changes in illumination. However, it also requires more computational resources and storage space.
  - Appearance-based tracking uses a set of 2D images of the scene or the object of interest to match the features extracted from the camera image and compute the camera pose. This method does not require prior knowledge of the scene geometry and appearance, and can handle dynamic and complex scenes. However, it also requires more images to cover different viewpoints and lighting conditions, and can be affected by occlusions and changes in illumination.
- Marker-less tracking can also use different algorithms for feature detection, description, and matching, such as ORB, FREAK, SIFT, SURF, etc. These algorithms vary in their speed, accuracy, robustness, and scalability.
- Marker-less tracking can also use different classifiers for the tracking task, such as KNN, Random Forest, Extremely Randomized Trees, SVM, and Bayes classifier. These classifiers vary in their performance, complexity, and generalization ability.
- Marker-less tracking has many advantages over marker-based tracking, such as:
  - It can work with any scene or object, without the need for artificial markers or triggers.
  - It can provide a more immersive and realistic AR experience, as the virtual content can blend seamlessly with the natural environment.
  - It can handle larger and more diverse scenes, as it does not depend on the visibility and orientation of the markers.
  - It can enable more interactive and dynamic AR applications, as the virtual content can respond to the changes in the environment or the user's actions.
- Marker-less tracking also has some challenges and limitations, such as:
  - It requires more computational power and memory, as it has to process more features and images, and store more data.
  - It requires more calibration and initialization, as it has to estimate the camera parameters and the initial pose.
  - It can be affected by noise, blur, motion, occlusions, and changes in illumination, as it relies on the quality and consistency of the features and images.
  - It can be less accurate and stable, as it can suffer from drift and jitter, especially in long-term tracking scenarios.

: Markerless Tracking for Augmented Reality Using Different Classifiers
: Markerless AR: Use Cases and How-to - Wikitude Blog
: Real-time markerless tracking for augmented reality: the virtual visual servoing framework
: Marker-based vs markerless augmented reality: pros, cons, examples - Overly
: Markerless Tracking for Augmented Reality | SpringerLink