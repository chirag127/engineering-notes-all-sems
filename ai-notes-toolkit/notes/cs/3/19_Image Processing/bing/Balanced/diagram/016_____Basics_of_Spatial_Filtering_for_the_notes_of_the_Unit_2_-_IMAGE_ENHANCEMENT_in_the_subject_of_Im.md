### Basics of Spatial Filtering

- Spatial filtering is a process by which we can alter properties of an optical image by selectively removing certain spatial frequencies that make up an object.
- Spatial filtering is performed by applying a filter or a mask, which is also known as a kernel, to an image. The filter is a small matrix that is moved over the image pixel by pixel, and at each position, the filter's response is calculated based on the specific content of the filter and the image .
- The filter's response is usually obtained by a convolution operation, which is a mathematical way of combining two functions. In image processing, the convolution of an image f(x,y) and a filter h(x,y) is defined as:

![Convolution formula](https://miro.medium.com/max/1400/1*Zx-ZMLKab7VOCQTxdZ1OAw.png)

- The convolution operation is commutative, associative, and distributive, which means that the order of the image and the filter does not matter, and that multiple filters can be applied in any order or combined into one filter.
- Spatial filtering can be used for various purposes, such as smoothing, sharpening, edge detection, noise reduction, and enhancement of an image   .
- Spatial filters can be classified into two main types: linear and nonlinear. Linear filters are those that satisfy the superposition principle, which means that the response to a sum of inputs is equal to the sum of responses to each input. Nonlinear filters are those that do not satisfy this principle, and their response depends on the relative order and magnitude of the inputs .
- Some examples of linear filters are mean filter, Gaussian filter, Laplacian filter, and Sobel filter. Some examples of nonlinear filters are median filter, max filter, min filter, and rank filter .
- Spatial filtering is a fundamental technique in image processing that involves the modification of pixel values in an image using a filter or kernel. The choice of the filter depends on the desired effect and the characteristics of the image.