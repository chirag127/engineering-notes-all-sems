### Sharpening Spatial Filters

- Sharpening spatial filters are used to enhance the edges and fine details of an image by removing blur and increasing the contrast of intensity transitions .
- Sharpening spatial filters are also known as high-pass filters or derivative filters, as they are based on the first or second order derivatives of the image intensity function .
- Sharpening spatial filters can be implemented in the spatial domain by using convolution masks or kernels that have negative coefficients that sum to zero  .
- Some examples of sharpening spatial filters are:
  - Laplacian filter: A second order derivative filter that computes the sum of the second derivatives of the image intensity function. It produces a double response at the edges and zero response at the constant regions or isolated points .
  - Sobel filter: A first order derivative filter that approximates the gradient of the image intensity function in the horizontal and vertical directions. It produces a single response at the edges and a stronger response to the gray level changes .
  - Unsharp masking: A technique that subtracts a smoothed version of the image from the original image to obtain a sharpened image. It can be done by using a low-pass filter such as a Gaussian filter to smooth the image and then subtracting it from the original image .
- Sharpening spatial filters can improve the quality and visibility of an image, but they can also introduce noise and artifacts, such as ringing or halo effects, if not used carefully .