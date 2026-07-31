# Basics of Spatial Filtering

- Spatial filtering is a technique for modifying or enhancing an image based on the values of neighboring pixels.
- Spatial filtering can be used for various purposes, such as smoothing, sharpening, edge detection, noise reduction, etc.
- Spatial filtering involves applying a filter or a kernel to an image, which is a small matrix of numbers that defines how the output pixel value is computed from the input pixel values in a neighborhood.
- Spatial filtering can be classified into two types: linear and nonlinear.
- Linear filtering is also known as convolution, which is a mathematical operation that combines two functions to produce a third function. In image processing, convolution is performed by sliding the filter over the image and multiplying the corresponding pixel values and adding them up to get the output pixel value.
- Nonlinear filtering is a more general form of spatial filtering that does not follow the principle of superposition, which means that the output is not a linear combination of the inputs. Nonlinear filtering can be used to perform operations such as median filtering, which replaces the output pixel value with the median of the pixel values in the neighborhood. Median filtering is useful for removing salt-and-pepper noise from an image.