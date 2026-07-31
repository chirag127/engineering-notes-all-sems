# Sharpening Spatial Filters

- Sharpening spatial filters are used to enhance the edges and fine details of an image by increasing the contrast between pixels.
- Sharpening filters are also called high-pass filters because they pass the high-frequency components of the image and attenuate the low-frequency components.
- Sharpening filters can be implemented by using the convolution operation, which involves multiplying a kernel matrix with a neighborhood of pixels in the image.
- Some common sharpening filters are:
  - Laplacian filter: A second-order derivative filter that produces a double response at the edge locations and a zero response in flat regions. The Laplacian filter can be expressed as:

  ```
  | 0  1  0 |
  | 1 -4  1 |
  | 0  1  0 |
  ```

  - Sobel filter: A first-order derivative filter that approximates the gradient of the image in horizontal and vertical directions. The Sobel filter can be expressed as two kernels:

  ```
  Horizontal kernel:    Vertical kernel:
  | -1  0  1 |          | -1 -2 -1 |
  | -2  0  2 |          |  0  0  0 |
  | -1  0  1 |          |  1  2  1 |
  ```

  - Prewitt filter: A first-order derivative filter that is similar to the Sobel filter but uses simpler coefficients. The Prewitt filter can be expressed as two kernels:

  ```
  Horizontal kernel:    Vertical kernel:
  | -1  0  1 |          | -1 -1 -1 |
  | -1  0  1 |          |  0  0  0 |
  | -1  0  1 |          |  1  1  1 |
  ```

  - Roberts filter: A first-order derivative filter that uses diagonal masks to detect the edge orientation. The Roberts filter can be expressed as two kernels:

  ```
  Diagonal kernel 1:    Diagonal kernel 2:
  |  0  0  0 |          |  0  0  0 |
  |  0  1  0 |          |  0  0 -1 |
  |  0  0 -1 |          |  0  1  0 |
  ```

- Sharpening filters can be used for various applications, such as enhancing the visibility of edges, improving the quality of blurred images, detecting the boundaries of objects, and highlighting the fine details of textures.