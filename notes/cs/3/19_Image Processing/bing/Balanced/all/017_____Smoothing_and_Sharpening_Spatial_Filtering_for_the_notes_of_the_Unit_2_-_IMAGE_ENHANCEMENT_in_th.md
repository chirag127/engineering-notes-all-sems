# Smoothing and Sharpening Spatial Filtering

- Smoothing and sharpening are two types of spatial filtering techniques that can be applied to enhance digital images.
- Spatial filtering is the process of modifying the pixel values of an image based on a mathematical operation involving a neighborhood of pixels, called a filter or a kernel.
- Smoothing filters are used to reduce noise and blur details, while sharpening filters are used to enhance edges and contrast.

## Smoothing Filters

- Smoothing filters are also known as low-pass filters, because they allow low-frequency components of the image to pass through, while attenuating high-frequency components, such as noise and edges.
- Smoothing filters can be linear or nonlinear. Linear smoothing filters perform a weighted average of the pixel values in the neighborhood, while nonlinear smoothing filters use a different function, such as median or mode, to determine the output value.
- Common linear smoothing filters include:

  - Average filter: The output value is the mean of the pixel values in the neighborhood. The filter kernel is a matrix of ones divided by the number of elements. For example, a 3x3 average filter kernel is:

    ```
    1/9 1/9 1/9
    1/9 1/9 1/9
    1/9 1/9 1/9
    ```

  - Gaussian filter: The output value is the weighted mean of the pixel values in the neighborhood, where the weights are determined by a Gaussian function. The filter kernel is a matrix of Gaussian values, which can be computed using the formula:

    ```
    G(x,y) = (1/(2*pi*sigma^2))*exp(-((x-x0)^2+(y-y0)^2)/(2*sigma^2))
    ```

    where x0 and y0 are the coordinates of the center of the kernel, and sigma is the standard deviation of the Gaussian function. For example, a 3x3 Gaussian filter kernel with sigma = 1 is:

    ```
    0.075 0.124 0.075
    0.124 0.204 0.124
    0.075 0.124 0.075
    ```

- Common nonlinear smoothing filters include:

  - Median filter: The output value is the median of the pixel values in the neighborhood. The filter kernel is a matrix of ones. For example, a 3x3 median filter kernel is:

    ```
    1 1 1
    1 1 1
    1 1 1
    ```

  - Mode filter: The output value is the mode of the pixel values in the neighborhood. The filter kernel is a matrix of ones. For example, a 3x3 mode filter kernel is:

    ```
    1 1 1
    1 1 1
    1 1 1
    ```

- Smoothing filters can be applied to grayscale or color images. For color images, the smoothing operation can be performed on each color channel separately, or on a different color space, such as HSV or Lab.

## Sharpening Filters

- Sharpening filters are also known as high-pass filters, because they allow high-frequency components of the image to pass through, while attenuating low-frequency components, such as smooth regions.
- Sharpening filters can be linear or nonlinear. Linear sharpening filters perform a weighted difference of the pixel values in the neighborhood, while nonlinear sharpening filters use a different function, such as Laplacian or Sobel, to determine the output value.
- Common linear sharpening filters include:

  - Unsharp masking: The output value is the sum of the original pixel value and a scaled difference between the original pixel value and a smoothed pixel value. The filter kernel is a matrix of negative values, except for the center element, which is positive. For example, a 3x3 unsharp masking filter kernel is:

    ```
    -1 -1 -1
    -1  9 -1
    -1 -1 -1
    ```

  - High-boost filtering: The output value is the sum of the original pixel value and a scaled difference between the original pixel value and a smoothed pixel value, where the scale factor is greater than one. The filter kernel is a matrix of negative values, except for the center element, which is positive and larger than the sum of the absolute values of the other elements. For example, a 3x3 high-boost filter kernel with a scale factor of 2