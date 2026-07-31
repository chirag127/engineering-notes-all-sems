### Spatial Domain

- The spatial domain refers to the 2D image plane represented in terms of pixel intensities.
- Image enhancement in the spatial domain involves modifying the pixel values directly to improve the appearance or quality of the image .
- The general form of a spatial domain operation is:

$$g(x,y) = T[f(x,y)]$$

where $f(x,y)$ is the input image, $g(x,y)$ is the output image, and $T$ is an operator on $f$ defined over a neighborhood of $(x,y)$.

- The operator $T$ can be either linear or nonlinear, and can be applied globally or locally.
- Some common spatial domain techniques are:
  - Point processing: The output pixel value depends only on the input pixel value, such as contrast stretching, thresholding, and histogram equalization .
  - Neighborhood processing: The output pixel value depends on a neighborhood of input pixel values, such as spatial filtering, smoothing, and sharpening .
  - Geometric transformations: The output pixel location depends on the input pixel location, such as scaling, rotation, and warping.
- The advantages of spatial domain methods are:
  - They are simple and intuitive to implement and understand.
  - They can be tailored to specific image characteristics and applications.
  - They can preserve the spatial resolution and details of the image.
- The disadvantages of spatial domain methods are:
  - They may not be effective for some types of noise or distortions.
  - They may introduce unwanted artifacts or side effects.
  - They may not exploit the frequency characteristics of the image.