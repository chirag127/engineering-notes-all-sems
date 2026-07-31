# Sharpening Spatial Filters

- Sharpening spatial filters are used to enhance the edges and fine details of an image by removing blur and smoothing.
- Sharpening spatial filters operate in the spatial domain by directly manipulating the image pixels.
- Sharpening spatial filters are based on the first and second order derivatives of the image intensity function.
- The first order derivative sharpening filters are also called gradient filters. They highlight the transitions in intensity by computing the magnitude and direction of the image gradient.
- The second order derivative sharpening filters are also called Laplacian filters. They highlight the fine details by computing the zero crossings of the image Laplacian.
- Sharpening spatial filters can be implemented by using convolution masks or kernels that are applied to the image neighborhood.
- Some examples of sharpening spatial filters are:

  - Roberts cross operator: a 2x2 gradient filter that approximates the diagonal components of the image gradient.
  - Sobel operator: a 3x3 gradient filter that approximates the horizontal and vertical components of the image gradient.
  - Prewitt operator: a 3x3 gradient filter that is similar to the Sobel operator but uses simpler coefficients.
  - Laplacian operator: a 3x3 Laplacian filter that computes the sum of the second order derivatives in the horizontal and vertical directions.
  - Laplacian of Gaussian (LoG) operator: a Laplacian filter that is preceded by a Gaussian smoothing filter to reduce noise and enhance the zero crossings.