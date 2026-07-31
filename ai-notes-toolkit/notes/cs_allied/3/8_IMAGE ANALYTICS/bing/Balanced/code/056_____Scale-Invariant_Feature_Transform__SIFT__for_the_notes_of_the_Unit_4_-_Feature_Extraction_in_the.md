### Scale-Invariant Feature Transform (SIFT) for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Scale-Invariant Feature Transform (SIFT) is a computer vision algorithm to detect, describe, and match local features in images.
- Local features are distinctive points or regions in an image that can be used to identify or compare images, such as corners, edges, blobs, etc.
- SIFT features are invariant to scale and orientation of images and robust to illumination fluctuations, noise, partial occlusion, and minor viewpoint changes in the images.
- SIFT algorithm consists of four main steps:
  - Scale-space extrema detection: Finding potential interest points across different scales and locations in the image using a Difference of Gaussians (DoG) function.
  - Keypoint localization: Refining the location and scale of each candidate point and eliminating low-contrast and edge points using a Taylor series expansion and a Hessian matrix.
  - Orientation assignment: Assigning one or more orientations to each keypoint based on the local image gradient directions and magnitudes.
  - Keypoint descriptor: Computing a 128-dimensional vector for each keypoint based on the local image gradients at selected scales and orientations, and applying normalization and thresholding to enhance the contrast invariance and reduce the influence of illumination changes.
- SIFT features can be used for various applications in image analytics, such as object recognition, image stitching, 3D modeling, video tracking, etc.