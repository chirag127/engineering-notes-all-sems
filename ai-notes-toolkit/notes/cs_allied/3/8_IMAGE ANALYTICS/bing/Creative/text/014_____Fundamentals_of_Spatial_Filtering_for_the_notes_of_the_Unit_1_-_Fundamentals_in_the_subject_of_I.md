### Fundamentals of Spatial Filtering

- Spatial filtering is a process by which we can alter properties of an optical image by selectively removing certain spatial frequencies that make up an object.
- Spatial filtering is the process of assigning the value of a pixel based on its neighbors. The filters or masks, which are also known as kernels, used in the process are small matrices run in the entire image through a convolution process.
- Spatial filtering can be used for various purposes, such as enhancing, smoothing, sharpening, or detecting edges in an image.
- Spatial filtering can be classified into two types: linear and nonlinear.
  - Linear spatial filtering is based on the principle of superposition, which means that the output of the filter is a linear combination of the input pixels and the filter coefficients.
  - Nonlinear spatial filtering does not follow the principle of superposition, and the output of the filter depends on the rank, order, or magnitude of the input pixels.
- Some examples of linear spatial filters are averaging filter, weighted averaging filter, Gaussian filter, and Laplacian filter.
  - Averaging filter is used to reduce the detail or noise in an image by replacing each pixel with the average of its neighboring pixels.
  - Weighted averaging filter is similar to averaging filter, but it assigns different weights to the neighboring pixels according to their distance from the center pixel.
  - Gaussian filter is a weighted averaging filter that uses a Gaussian function as the weight function. It is used to smooth an image while preserving the edges.
  - Laplacian filter is a second-order derivative filter that is used to enhance or sharpen an image by highlighting the regions of rapid intensity change.
- Some examples of nonlinear spatial filters are median filter, max filter, min filter, and adaptive filter.
  - Median filter is used to remove salt-and-pepper noise or impulse noise from an image by replacing each pixel with the median of its neighboring pixels.
  - Max filter is used to enhance the bright regions or highlight the maximum values in an image by replacing each pixel with the maximum of its neighboring pixels.
  - Min filter is used to enhance the dark regions or highlight the minimum values in an image by replacing each pixel with the minimum of its neighboring pixels.
  - Adaptive filter is a filter that adjusts its parameters according to the local characteristics of the image, such as noise level, contrast, or edge strength.