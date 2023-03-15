# Edge detection

- Edge detection is a fundamental tool in image processing, machine vision and computer vision, particularly in the areas of feature detection and feature extraction.
- Edge detection is a method of segmenting an image into regions of discontinuity, where there is a significant change in the gray level.
- Edge detection allows users to observe the features of an image, such as boundaries, contours, and outlines of objects.
- Edge detection is also used in various downstream tasks in computer vision, such as line detection, feature detection, and image classification.

## Edge properties

- The edges extracted from a two-dimensional image of a three-dimensional scene can be classified as either viewpoint dependent or viewpoint independent.
- Viewpoint dependent edges are those that change as the viewpoint changes, such as occlusion boundaries, shadows, and specular reflections.
- Viewpoint independent edges are those that remain constant regardless of the viewpoint, such as object boundaries, surface markings, and texture changes.
- Viewpoint independent edges are more desirable for image analysis and interpretation, as they are more robust and invariant to illumination and perspective changes.

## Edge detection operators

- Edge detection operators are mathematical functions that compute an image gradient to quantify the magnitude and direction of edges in an image.
- Image gradient is a vector that points in the direction of the most rapid change in intensity, and whose magnitude is the rate of change in that direction.
- Edge detection operators can be classified into two categories: first-order and second-order.
- First-order edge detection operators use the first derivative of the image intensity to detect edges, such as Sobel, Prewitt, and Roberts operators.
- Second-order edge detection operators use the second derivative of the image intensity to detect edges, such as Laplacian, Laplacian of Gaussian (LoG), and Canny operators.
- First-order edge detection operators are more sensitive to noise, as noise can cause rapid changes in intensity.
- Second-order edge detection operators are more robust to noise, as they can suppress noise by smoothing the image before applying the second derivative.
- Canny edge detection operator is one of the most widely used and optimal edge detection operators, as it satisfies the following criteria:
  - Good detection: the operator should detect as many real edges as possible.
  - Good localization: the detected edges should be as close as possible to the true edges.
  - Minimal response: the operator should return one response per edge and avoid multiple responses to a single edge.