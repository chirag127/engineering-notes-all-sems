### Edge detection

- Edge detection is a fundamental tool in image processing, machine vision and computer vision, particularly in the areas of feature detection and feature extraction.
- Edge detection is a method of segmenting an image into regions of discontinuity, where there is a significant change in the gray level.
- Edge detection allows users to observe the features of an image, such as boundaries, contours, corners, and textures.
- Edge detection is used for various downstream tasks in computer vision, such as line detection, feature detection, object detection, segmentation, and recognition .
- Edge detection involves computing an image gradient, which is a vector that quantifies the magnitude and direction of edges in an image.
- Edge detection operators are mathematical filters that are applied to an image to enhance the edges and reduce the noise.
- Some common edge detection operators are:
  - Sobel operator: uses a pair of 3x3 convolution kernels to estimate the horizontal and vertical gradients of an image.
  - Prewitt operator: similar to Sobel operator, but uses simpler kernels that give less weight to the diagonal pixels.
  - Roberts operator: uses a pair of 2x2 convolution kernels to estimate the diagonal gradients of an image.
  - Canny operator: uses a multi-stage algorithm that involves smoothing, gradient computation, non-maximum suppression, and hysteresis thresholding to produce optimal edges.
  - Laplacian operator: uses a second-order derivative to detect the zero-crossings of the image gradient, where the edges are located.
  - LoG operator: uses a Laplacian of Gaussian filter to smooth the image and then detect the zero-crossings.
  - DoG operator: uses a Difference of Gaussian filter to approximate the LoG filter with less computational cost.
- Edge detection is a challenging problem, as it depends on various factors, such as image quality, noise level, edge strength, edge orientation, and edge continuity.
- Edge detection is an active research area, with many papers proposing new methods, benchmarks, and datasets.