### Basics of Spatial Filtering

- Spatial filtering is a process by which we can alter properties of an optical image by selectively removing certain spatial frequencies that make up an object.
- Spatial filtering can be used for various purposes, such as enhancing, smoothing, sharpening, or detecting edges in an image.
- Spatial filtering involves applying a filter or a mask, which is also known as a kernel, to each pixel of an image and computing a new pixel value based on the neighboring pixels  .
- The filter or the mask is a small matrix of coefficients that defines the relationship between the input and the output pixels.
- The process of applying a filter or a mask to an image is called convolution, which is a mathematical operation that combines two functions to produce a third function.
- Convolution can be expressed as:

$$g(x,y) = \sum_{s=-a}^{a} \sum_{t=-b}^{b} w(s,t) f(x-s, y-t)$$

where $g(x,y)$ is the output image, $f(x,y)$ is the input image, $w(s,t)$ is the filter or the mask, and $(s,t)$ are the offsets of the filter from the center pixel $(x,y)$.
- The size of the filter or the mask is usually odd, such as 3x3, 5x5, or 7x7, so that it has a specific center pixel.
- The filter or the mask is moved on the image such that the center of the filter coincides with each pixel of the image, and the output pixel value is calculated based on the filter coefficients and the input pixel values.
- The output pixel value can be obtained by multiplying the filter coefficients with the corresponding input pixel values and adding them up, or by applying some other function, such as minimum, maximum, median, or mode.
- Spatial filtering can be classified into two types: linear and nonlinear.
  - Linear filtering is when the output pixel value is a linear combination of the input pixel values, such as the convolution operation. Linear filtering preserves the linearity and additivity properties of the image, but it may produce negative or out-of-range pixel values that need to be clipped or scaled.
  - Nonlinear filtering is when the output pixel value is a nonlinear function of the input pixel values, such as the minimum, maximum, median, or mode operations. Nonlinear filtering does not preserve the linearity and additivity properties of the image, but it can handle noise and outliers better than linear filtering.
- Spatial filtering can also be classified into two categories: low-pass and high-pass .
  - Low-pass filtering is when the filter or the mask attenuates or removes the high-frequency components of the image, such as edges, corners, or details, and preserves or enhances the low-frequency components, such as smooth regions or average values. Low-pass filtering can be used for smoothing, blurring, or reducing noise in an image.
  - High-pass filtering is when the filter or the mask attenuates or removes the low-frequency components of the image, such as smooth regions or average values, and preserves or enhances the high-frequency components, such as edges, corners, or details. High-pass filtering can be used for sharpening, enhancing, or detecting edges in an image.
- Some examples of spatial filters or masks are:
  - Mean filter: a low-pass linear filter that replaces each pixel value with the average of its neighboring pixel values. It can be used for smoothing or blurring an image.
  - Gaussian filter: a low-pass linear filter that replaces each pixel value with a weighted average of its neighboring pixel values, where the weights are determined by a Gaussian function. It can be used for smoothing or blurring an image with less loss of details than the mean filter.
  - Laplacian filter: a high-pass linear filter that replaces each pixel value with the sum of the second-order derivatives of the input image. It can be used for sharpening or enhancing an image by adding the output of the Laplacian filter to the original image.
  - Sobel filter: a high-pass linear filter that replaces each pixel value with the magnitude of the gradient of the input image. It can be used for detecting edges or boundaries in an image.
  - Median filter: a low-pass nonlinear filter that replaces each pixel value with the median of its neighboring pixel values. It can be used for reducing noise or preserving edges in an image.
  - Max filter: a low-pass nonlinear filter that replaces each