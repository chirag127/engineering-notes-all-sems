### Basics of Spatial Filtering

- Spatial filtering is a process by which we can alter properties of an optical image by selectively removing certain spatial frequencies that make up an object.
- Spatial filtering is performed by applying a filter or a mask, which is also known as a kernel, to an image. The filter is a small matrix that is moved over the image pixel by pixel, and the output image is formed by the filter's response at each pixel  .
- The filter's response is calculated by a predefined relationship called a template, which involves multiplying the filter values with the corresponding image values and adding them up. This operation is also known as convolution.
- Spatial filtering can be used for various purposes, such as smoothing, sharpening, edge detection, noise reduction, and enhancement of an image  .
- Spatial filters can be classified into two types: linear and nonlinear. Linear filters have the property that the output image is a linear function of the input image, and they can be easily implemented by convolution. Nonlinear filters do not have this property, and they may involve other operations such as sorting, median, or maximum .