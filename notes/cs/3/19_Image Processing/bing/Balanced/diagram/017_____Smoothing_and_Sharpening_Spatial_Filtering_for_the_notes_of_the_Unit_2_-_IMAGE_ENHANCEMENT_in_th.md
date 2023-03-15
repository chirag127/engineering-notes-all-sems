# Smoothing and Sharpening Spatial Filtering

- Spatial filtering is a technique for modifying or enhancing an image by applying a filter (also called a kernel or a mask) to each pixel of the image.
- The filter is a small matrix of numbers that defines how the pixel value is computed from its neighbors.
- The filter is moved over the image, and at each position, the pixel value is replaced by the weighted sum of the neighboring pixel values, where the weights are given by the filter coefficients.
- The process of spatial filtering is also known as convolution.

## Smoothing Spatial Filtering

- Smoothing spatial filtering is a technique for reducing and suppressing image noises, such as random variations, salt-and-pepper noise, or Gaussian noise.
- Smoothing filters are also called low-pass filters, because they allow low-frequency components (such as smooth regions) to pass through, while attenuating high-frequency components (such as edges or details).
- Smoothing filters are usually based on averaging, which means that the pixel value is replaced by the mean of the neighboring pixel values.
- Commonly seen smoothing filters include:

  - Average smoothing: The filter coefficients are all equal, and the filter size determines the degree of smoothing. A larger filter size means more smoothing, but also more blurring.
  - Gaussian smoothing: The filter coefficients are given by a Gaussian function, which gives more weight to the central pixel and less weight to the distant pixels. This results in a smoother and less blurred image than average smoothing.
  - Adaptive smoothing: The filter coefficients are adjusted according to the local image characteristics, such as variance or entropy. This allows for more smoothing in homogeneous regions and less smoothing in heterogeneous regions.

## Sharpening Spatial Filtering

- Sharpening spatial filtering is a technique for enhancing the image visual appearance and the details and edges of the image.
- Sharpening filters are also called high-pass filters, because they allow high-frequency components to pass through, while attenuating low-frequency components.
- Sharpening filters are usually based on derivatives, which means that the pixel value is replaced by the difference of the neighboring pixel values.
- Commonly seen sharpening filters include:

  - First-order derivative filters: The filter coefficients are given by the first-order partial derivatives of the image, such as the Sobel, Prewitt, or Roberts operators. These filters can detect the edges and their orientations in the image.
  - Second-order derivative filters: The filter coefficients are given by the second-order partial derivatives of the image, such as the Laplacian operator. These filters can detect the zero-crossings of the image, which correspond to the edge locations.
  - Unsharp masking: The filter coefficients are given by subtracting a smoothed version of the image from the original image. This enhances the edges and details of the image by increasing the contrast.

## Example

- The following diagram shows an example of applying different spatial filters to an image.

![Diagram of spatial filtering example](https://www.dynamsoft.com/blog/wp-content/uploads/2020/05/spatial-filters.png)

- The original image is a grayscale image of a cat.
- The average smoothing filter is a 3x3 matrix of 1/9, which means that each pixel value is replaced by the average of the 9 neighboring pixel values.
- The Gaussian smoothing filter is a 3x3 matrix of [0.0625, 0.125, 0.0625; 0.125, 0.25, 0.125; 0.0625, 0.125, 0.0625], which means that each pixel value is replaced by the weighted average of the 9 neighboring pixel values, where the weights are given by a Gaussian function.
- The Sobel filter is a 3x3 matrix of [-1, -2, -1; 0, 0, 0; 1, 2, 1], which means that each pixel value is replaced by the difference of the 6 neighboring pixel values along the vertical direction. This can detect the vertical edges in the image.
- The Laplacian filter is a 3x3 matrix of [0, -1, 0; -1, 4, -1; 0, -1, 0], which means that each pixel value is replaced by the difference of the 4 neighboring pixel values along the horizontal and vertical directions. This can detect the zero-crossings in the image.
-