# Basics of Spatial Filtering

- Spatial filtering is a process by which we can alter properties of an optical image by selectively removing certain spatial frequencies that make up an object.
- Spatial filtering can be used for various purposes, such as enhancing, smoothing, sharpening, or detecting edges in an image   .
- Spatial filtering involves the use of a filter or a mask, which is a small matrix of coefficients that is applied to each pixel and its neighbors in an image  .
- The filter or mask is moved point-by-point in the image so that the center of the filter coincides with the pixel of interest  .
- At each point, the filter's response is calculated based on the specific content of the filter and through a predefined relationship called a template.
- The template defines how the filter coefficients are multiplied and summed with the pixel values in the image.
- The result of the filter's response is then assigned to the pixel of interest, creating a new image  .
- The process of moving the filter over the image and applying the template is called convolution  .
- Convolution can be expressed mathematically as:

$$g(x,y) = \sum_{s=-a}^{a} \sum_{t=-b}^{b} w(s,t) f(x+s, y+t)$$

where $g(x,y)$ is the filtered image, $f(x,y)$ is the original image, $w(s,t)$ is the filter coefficients, and $(2a+1) \times (2b+1)$ is the size of the filter.

- Spatial filters can be classified into two types: linear and nonlinear  .
- Linear filters are those that satisfy the superposition principle, which means that the filtered image is a linear combination of the original image and the filter  .
- Nonlinear filters are those that do not satisfy the superposition principle, which means that the filtered image depends on some nonlinear function of the original image and the filter  .
- Examples of linear filters are average, Gaussian, and Laplacian filters  .
- Examples of nonlinear filters are median, max, and min filters  .
- Linear filters are easier to implement and analyze, but they may produce undesirable effects such as blurring or ringing  .
- Nonlinear filters are more complex and difficult to analyze, but they may preserve edges and remove noise better than linear filters  .