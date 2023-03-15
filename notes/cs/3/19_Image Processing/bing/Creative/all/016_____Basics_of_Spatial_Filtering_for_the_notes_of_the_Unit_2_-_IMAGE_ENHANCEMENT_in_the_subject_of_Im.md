# Basics of Spatial Filtering

- Spatial filtering is a process by which we can alter properties of an optical image by selectively removing certain spatial frequencies that make up an object.
- Spatial filtering can be used for various purposes, such as enhancing, smoothing, sharpening, or detecting edges in an image   .
- Spatial filtering involves the use of a filter or a mask, which is a small matrix of coefficients that is applied to a neighborhood of pixels in the image   .
- The filter or mask is moved point-by-point in the image so that the center of the filter coincides with the point (x, y). At each point (x, y), the filter's response is calculated based on the specific content of the filter and through a predefined relationship called a template.
- The template can be either linear or nonlinear. A linear template is a weighted sum of the pixel values in the neighborhood, while a nonlinear template is a function of the pixel values in the neighborhood that is not a weighted sum  .
- The result of applying a filter or mask to an image is a new image, called the filtered image or the output image   .
- The process of applying a filter or mask to an image can be mathematically expressed as a convolution operation, which is denoted by the symbol *   .
- The convolution operation can be defined as follows:

  - Let f(x, y) be the input image and h(x, y) be the filter or mask. Then the output image g(x, y) is given by:

    g(x, y) = f(x, y) * h(x, y) = ∑∑ h(s, t) f(x - s, y - t)

  - where the summation is over the coordinates (s, t) of the filter or mask   .

- The convolution operation has some important properties, such as commutativity, associativity, distributivity, and linearity  .
- The convolution operation can be implemented efficiently using the fast Fourier transform (FFT) algorithm, which converts the spatial domain filtering into the frequency domain filtering  .
- The choice of the filter or mask depends on the desired effect and the characteristics of the input image. Some common types of filters or masks are:

  - Smoothing filters: These filters reduce noise and blur details in an image by averaging the pixel values in the neighborhood. Examples of smoothing filters are mean filter, median filter, Gaussian filter, etc   .
  - Sharpening filters: These filters enhance edges and fine details in an image by increasing the contrast between the pixel values in the neighborhood. Examples of sharpening filters are Laplacian filter, Sobel filter, Prewitt filter, etc   .
  - Edge detection filters: These filters identify the boundaries of objects in an image by detecting the changes in pixel values across the neighborhood. Examples of edge detection filters are gradient filters, Canny filter, Roberts filter, etc   .

- Spatial filtering is a fundamental technique in image processing that can be used for various applications, such as image enhancement, image restoration, image segmentation, image compression, image recognition, etc   .