### Scale-Invariant Feature Transform (SIFT) for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Scale-Invariant Feature Transform (SIFT) is a computer vision algorithm to detect, describe, and match local features in images.
- Local features are distinctive points or regions in an image that can be used to identify or compare images, such as corners, edges, blobs, etc.
- SIFT is invariant to scale and orientation of images and robust to illumination fluctuations, noise, partial occlusion, and minor viewpoint changes in the images .
- SIFT can be used for various applications, such as object recognition, image stitching, 3D modeling, video tracking, etc.
- SIFT consists of four main steps :
  - Scale-space extrema detection: This step aims to find potential interest points that are invariant to scale and orientation by using a Difference of Gaussians (DoG) function applied to different scales of the image.
  - Keypoint localization: This step aims to refine the candidate points by eliminating low-contrast or edge points and assigning accurate locations and scales to the remaining points.
  - Orientation assignment: This step aims to assign one or more orientations to each keypoint based on the local image gradient directions. This ensures that the keypoint descriptor is invariant to image rotation.
  - Keypoint descriptor: This step aims to compute a local image descriptor for each keypoint based on the image gradients in a 16x16 neighborhood around the keypoint. The descriptor is a 128-dimensional vector that captures the dominant orientations and magnitudes of the gradients.
- SIFT keypoints and descriptors can be matched between different images using a nearest-neighbor search algorithm, such as k-d tree or brute-force .
- SIFT is a powerful and popular feature extraction method, but it also has some limitations, such as high computational cost, patent issues, and sensitivity to non-affine transformations .