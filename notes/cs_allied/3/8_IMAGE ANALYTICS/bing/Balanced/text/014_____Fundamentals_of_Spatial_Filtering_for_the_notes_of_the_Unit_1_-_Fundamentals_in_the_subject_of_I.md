### Fundamentals of Spatial Filtering

- Spatial filtering is a technique for modifying or enhancing an image by applying a filter or a mask to each pixel of the image.
- A filter or a mask is a small matrix of numbers, usually of odd size, such as 3x3, 5x5, etc.
- The filter or mask is moved over the image, pixel by pixel, and a new value for each pixel is calculated based on the values of its neighbors and the filter coefficients.
- The new value of a pixel is usually the weighted average of its neighbors, where the weights are given by the filter coefficients.
- The process of applying a filter or a mask to an image is also called convolution or correlation, depending on how the filter coefficients are arranged and multiplied with the pixel values.
- Convolution and correlation are mathematically equivalent, except for a 180-degree rotation of the filter matrix.
- Spatial filtering can be used for various purposes, such as smoothing, sharpening, edge detection, noise reduction, etc.
- Different types of filters or masks can produce different effects on the image, such as low-pass, high-pass, band-pass, etc.
- Low-pass filters are used to smooth or blur an image by removing high-frequency components, such as edges and details.
- High-pass filters are used to sharpen or enhance an image by emphasizing high-frequency components, such as edges and details.
- Band-pass filters are used to retain or extract a specific range of frequencies from an image, such as textures or patterns.
- Spatial filtering can be performed in either the spatial domain or the frequency domain, depending on the complexity and efficiency of the filter or the mask.
- Spatial domain filtering is more intuitive and simple, but may require more computations and iterations for complex filters or large images.
- Frequency domain filtering is more efficient and flexible, but may require more preprocessing and postprocessing steps, such as Fourier transform and inverse Fourier transform.