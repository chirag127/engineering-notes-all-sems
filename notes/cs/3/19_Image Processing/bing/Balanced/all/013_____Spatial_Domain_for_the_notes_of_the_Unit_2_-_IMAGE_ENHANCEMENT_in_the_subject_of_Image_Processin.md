# Spatial Domain

- The spatial domain refers to the 2D image plane represented in terms of pixel intensities.
- Image enhancement in the spatial domain involves modifying the pixel values directly to improve the appearance or quality of the image .
- The general form of a spatial domain operation is:

$$g(x,y) = T[f(x,y)]$$

where $f(x,y)$ is the input image, $g(x,y)$ is the output image, and $T$ is an operator on $f$ defined over a neighborhood of $(x,y)$.

- There are two main types of spatial domain operations: point processing and neighborhood processing.
- Point processing is when the output pixel value depends only on the input pixel value at the same location, such as:

$$g(x,y) = T[f(x,y)]$$

where $T$ is a function of one variable.
- Examples of point processing are contrast stretching, histogram equalization, and thresholding.
- Neighborhood processing is when the output pixel value depends on the input pixel values in a neighborhood of the same location, such as:

$$g(x,y) = T[f(x,y),f(x-1,y),f(x+1,y),f(x,y-1),f(x,y+1),...]$$

where $T$ is a function of multiple variables.
- Examples of neighborhood processing are filtering, smoothing, sharpening, and edge detection.
- Spatial domain methods are simple, fast, and intuitive, but they may not be able to handle complex or global image features.