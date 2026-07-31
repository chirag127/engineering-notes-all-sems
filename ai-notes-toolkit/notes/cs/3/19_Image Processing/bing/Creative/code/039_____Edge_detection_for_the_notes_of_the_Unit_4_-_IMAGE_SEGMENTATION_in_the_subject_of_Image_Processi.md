### Edge detection

Edge detection is a fundamental tool in image processing, machine vision and computer vision, particularly in the areas of feature detection and feature extraction. Edge detection allows users to observe the features of an image for a significant change in the gray level.

Some of the main points to know about edge detection are:

- Edge detection is one of the fundamental steps in image segmentation, which is the process of dividing an image into meaningful regions.
- The edges extracted from a two-dimensional image of a three-dimensional scene can be classified as either viewpoint dependent or viewpoint independent. Viewpoint dependent edges are caused by occlusion, reflection, or shadow, while viewpoint independent edges are due to the intrinsic properties of the objects in the scene, such as surface normal, depth, or reflectance.
- Edge detection involves computing an image gradient, which is a vector that quantifies the magnitude and direction of edges in an image. Image gradients are used in various downstream tasks in computer vision such as line detection, feature detection, and object recognition.
- There are many edge detection operators or algorithms that can be applied to an image, such as Sobel, Prewitt, Roberts, Canny, Laplacian of Gaussian, and Zero-crossing. Each operator has its own advantages and disadvantages in terms of accuracy, speed, noise sensitivity, and edge localization .
- Edge detection is a challenging problem due to the presence of noise, illumination variation, texture, and occlusion in real-world images. Therefore, edge detection operators often require some parameters to be tuned or some post-processing steps to be applied to obtain optimal results .