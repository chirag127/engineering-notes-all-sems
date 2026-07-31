### Sharpening Spatial Filters

- Sharpening spatial filters are used to enhance the edges and fine details of an image by increasing the contrast between neighboring pixels .
- Sharpening spatial filters are also called high-pass filters because they attenuate the low-frequency components and preserve the high-frequency components of the image spectrum .
- Sharpening spatial filters can be implemented by using the convolution operation of the image with a kernel, which is a small matrix that defines the filter effect .
- Some common sharpening spatial filters are:

  - Laplacian filter: A second-order derivative filter that produces a double response at the edge locations and a strong response to fine details . The kernel of a Laplacian filter is usually a 3x3 matrix with a negative value at the center and positive values at the neighbors, such as:

    ```
    | 0  1  0 |
    | 1 -4  1 |
    | 0  1  0 |
    ```

  - Sobel filter: A first-order derivative filter that approximates the gradient magnitude of the image by using two 3x3 kernels, one for the horizontal direction and one for the vertical direction. The kernels of a Sobel filter are:

    ```
    Horizontal kernel:    Vertical kernel:
    | -1 -2 -1 |          | -1  0  1 |
    |  0  0  0 |          | -2  0  2 |
    |  1  2  1 |          | -1  0  1 |
    ```

  - Unsharp masking filter: A filter that subtracts a smoothed version of the image from the original image to enhance the edges . The kernel of an unsharp masking filter is usually a 3x3 matrix with a positive value at the center and negative values at the neighbors, such as:

    ```
    | -1 -1 -1 |
    | -1  9 -1 |
    | -1 -1 -1 |
    ```

- Sharpening spatial filters can improve the quality and clarity of an image, but they can also introduce noise and artifacts if applied excessively . Therefore, it is important to choose the appropriate filter and parameters for the desired effect.