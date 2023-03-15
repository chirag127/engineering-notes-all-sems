# Edge detection

Edge detection is a fundamental tool in image processing, machine vision and computer vision, particularly in the areas of feature detection and feature extraction. Edge detection allows users to observe the features of an image for a significant change in the gray level.

## Motivations

- Edges are the boundaries of objects within images. They can be used to segment an image into regions of interest, such as foreground and background, or different objects.
- Edges can also provide information about the shape, size, orientation, and texture of objects in an image.
- Edges can help reduce the amount of data to be processed, by focusing on the most salient parts of an image.
- Edges can enhance the visual appearance of an image, by highlighting the contrast and details of the objects.

## Edge properties

- The edges extracted from a two-dimensional image of a three-dimensional scene can be classified as either viewpoint dependent or viewpoint independent.
- Viewpoint dependent edges are those that change with the perspective of the camera, such as occlusion boundaries, shadows, and specular reflections.
- Viewpoint independent edges are those that remain constant regardless of the camera position, such as object boundaries, surface markings, and texture changes.
- Edge detection algorithms aim to find the viewpoint independent edges, as they are more robust and meaningful for image analysis.

## Edge detection operators

- Edge detection operators are mathematical functions that take an input image and produce an output image that highlights the edges.
- Edge detection operators typically involve computing an image gradient, which is a vector that quantifies the magnitude and direction of edges in an image.
- Edge detection operators can be classified into two categories: first-order and second-order.
- First-order edge detection operators use the first derivative of the image intensity function to detect edges, such as the Sobel, Prewitt, and Roberts operators.
- Second-order edge detection operators use the second derivative of the image intensity function to detect edges, such as the Laplacian, Laplacian of Gaussian, and Canny operators.
- Edge detection operators have different properties and performance, depending on the noise level, edge orientation, edge thickness, and edge continuity of the input image.

## Edge detection challenges

- Edge detection is a challenging problem in image processing, as there is no clear definition of what constitutes an edge, and different applications may require different types of edges.
- Edge detection is also sensitive to noise, which can create false or missing edges, or blur the edge boundaries.
- Edge detection is also affected by the scale, resolution, and contrast of the image, which can influence the edge detection results.
- Edge detection is also an ill-posed problem, as there may be multiple possible solutions for the same input image, depending on the edge detection criteria and parameters.

## References

: Edge detection - Wikipedia. https://en.wikipedia.org/wiki/Edge_detection
: Image Edge Detection Operators in Digital Image Processing. https://www.geeksforgeeks.org/image-edge-detection-operators-in-digital-image-processing/
: Edge Detection | Papers With Code. https://paperswithcode.com/task/edge-detection