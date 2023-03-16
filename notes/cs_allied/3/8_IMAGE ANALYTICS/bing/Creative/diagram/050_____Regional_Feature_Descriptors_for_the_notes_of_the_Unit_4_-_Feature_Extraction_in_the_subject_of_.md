### Regional Feature Descriptors

- Regional feature descriptors are methods to extract and describe distinctive and invariant features from a region of interest in an image.
- Regional features can be used for various image analysis tasks, such as image matching, registration, retrieval, and classification.
- Regional features can capture the local geometric and semantic information of the image content, and reduce the influence of noise, occlusion, and illumination changes.
- Regional feature descriptors can be divided into two categories: hand-crafted and learned.

#### Hand-crafted Regional Feature Descriptors

- Hand-crafted regional feature descriptors are designed based on human knowledge and intuition, and often rely on low-level image properties, such as edges, corners, gradients, and textures.
- Some examples of hand-crafted regional feature descriptors are:
  - Scale-Invariant Feature Transform (SIFT) : SIFT detects keypoints at different scales and orientations, and computes a 128-dimensional vector for each keypoint based on the gradient histograms of its local neighborhood.
  - Speeded Up Robust Features (SURF) : SURF is a faster and more robust version of SIFT, which uses integral images and Haar wavelets to compute the keypoints and descriptors.
  - Binary Robust Independent Elementary Features (BRIEF) : BRIEF is a binary descriptor that compares the intensity values of pairs of pixels randomly sampled from a patch around the keypoint.
  - Oriented FAST and Rotated BRIEF (ORB) : ORB is a combination of FAST (Features from Accelerated Segment Test) detector and BRIEF descriptor, with modifications to ensure rotation invariance and resistance to noise.

#### Learned Regional Feature Descriptors

- Learned regional feature descriptors are obtained by training deep neural networks on large-scale image datasets, and often capture high-level semantic and abstract information of the image content.
- Some examples of learned regional feature descriptors are:
  - Convolutional Neural Network (CNN) features : CNN features are the activations of the convolutional layers or the fully connected layers of a pre-trained CNN, such as VGG, ResNet, or AlexNet. CNN features can be extracted from the whole image or from regions of interest detected by a region proposal network (RPN).
  - Local Deep Descriptor (LDD) : LDD is a deep learning framework that learns a local descriptor for each pixel in an image, based on a Siamese network and a triplet loss function. LDD can handle large viewpoint and illumination changes, and can be used for remote sensing image feature matching.
  - Region-Wise Deep Feature Representation (RDWR) : RDWR is a deep learning framework that learns a region-wise feature representation for remote sensing images, based on a region proposal network, a region-wise feature extraction network, and an improved vector of locally aggregated descriptors (VLAD) algorithm. RDWR can be used for remote sensing image classification and retrieval.