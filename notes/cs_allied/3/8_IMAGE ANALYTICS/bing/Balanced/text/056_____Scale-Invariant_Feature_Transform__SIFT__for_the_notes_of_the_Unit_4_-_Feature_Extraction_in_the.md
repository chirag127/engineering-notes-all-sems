### Scale-Invariant Feature Transform (SIFT) for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Scale-Invariant Feature Transform (SIFT) is a computer vision algorithm to detect, describe, and match local features in images.
- Local features are distinctive points or regions in an image that can be used to identify or compare images, such as corners, edges, blobs, etc.
- SIFT is invariant to scale and orientation of images and robust to illumination fluctuations, noise, partial occlusion, and minor viewpoint changes in the images .
- SIFT can be used for various applications, such as object recognition, image stitching, 3D modeling, video tracking, etc.
- SIFT consists of four main steps :
  - Scale-space extrema detection: This step finds potential interest points in the image by applying a Difference of Gaussians (DoG) filter to different scales and octaves of the image and looking for local maxima and minima.
  - Keypoint localization: This step refines the location and scale of each candidate point by fitting a 3D quadratic function to the DoG values and discarding low-contrast or edge-like points.
  - Orientation assignment: This step assigns one or more orientations to each keypoint based on the gradient magnitude and direction of a local neighborhood around the keypoint. This ensures that the keypoint descriptor is rotation-invariant.
  - Keypoint descriptor: This step computes a 128-dimensional vector for each keypoint based on the gradient magnitude and orientation of a 16x16 region around the keypoint. The vector is normalized and thresholded to enhance contrast and reduce the effects of illumination changes.
- SIFT keypoints and descriptors can be matched between different images using a nearest-neighbor or a ratio test to find the best matches .
- SIFT is a powerful and popular feature extraction method, but it also has some limitations, such as high computational cost, sensitivity to blur and non-affine distortions, and patent issues .