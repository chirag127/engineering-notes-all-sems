### Scale-Invariant Feature Transform (SIFT) for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Scale-Invariant Feature Transform (SIFT) is a computer vision algorithm to detect, describe, and match local features in images.
- Local features are distinctive points or regions in an image that can be used to represent the image content and structure.
- SIFT features are invariant to scale and orientation of images and robust to illumination fluctuations, noise, partial occlusion, and minor viewpoint changes in the images.
- SIFT features can be used for various applications such as object recognition, image stitching, 3D modeling, video tracking, and individual identification of wildlife.
- The main steps of SIFT algorithm are:
  - Scale-space extrema detection: finding potential interest points across different scales and orientations using a Difference of Gaussians (DoG) function.
  - Keypoint localization: refining the location and scale of each candidate point and discarding low-contrast and edge points.
  - Orientation assignment: assigning one or more dominant orientations to each keypoint based on the local image gradient directions.
  - Keypoint descriptor: computing a 128-dimensional vector for each keypoint that captures the local image gradient magnitudes and orientations around the keypoint.
  - Keypoint matching: finding the nearest neighbors of each keypoint in another image using a distance metric such as Euclidean distance or cosine similarity.