### Spatial Domain

- The spatial domain refers to the 2D image plane represented in terms of pixel intensities.
- Image enhancement in the spatial domain involves modifying the pixel values directly to improve the appearance or quality of the image.
- The spatial domain methods perform operations on pixels directly.
- The most common spatial domain techniques are:
  - Point processing: applying a function to each pixel individually, such as contrast stretching, histogram equalization, thresholding, etc.
  - Neighborhood processing: applying a function to a group of pixels, such as filtering, smoothing, sharpening, edge detection, etc.
  - Global processing: applying a function to the whole image, such as Fourier transform, wavelet transform, etc.
- The spatial domain methods are simple, fast, and intuitive, but they may not be able to handle complex or noisy images well.
- The spatial domain methods can be expressed as:

  `g(x,y) = T[f(x,y)]`

  where `f(x,y)` is the input image, `g(x,y)` is the output image, and `T` is the transformation function that operates on the spatial coordinates `x` and `y`.