# Matching SIFT Features

- SIFT stands for Scale-Invariant Feature Transform, a computer vision algorithm to detect, describe, and match local features in images.
- SIFT features are invariant to rotation, scale, and brightness changes, and are stable to some extent to perspective and affine transformations .
- SIFT features have a large amount of information and are suitable for fast and accurate matching in massive databases.
- SIFT feature matching can be used for various applications, such as image stitching, object recognition, scene detection, video tracking, etc .

## Steps for matching SIFT features

1. Detect keypoints and compute descriptors for each image using SIFT algorithm.
2. Create a feature matcher object, such as Brute-Force matcher or FLANN based matcher.
3. Match the descriptors of the two images using the matcher object.
4. Optionally, apply a filtering method to remove outliers, such as ratio test or symmetry test .
5. Draw the matched keypoints on the images and display the result.