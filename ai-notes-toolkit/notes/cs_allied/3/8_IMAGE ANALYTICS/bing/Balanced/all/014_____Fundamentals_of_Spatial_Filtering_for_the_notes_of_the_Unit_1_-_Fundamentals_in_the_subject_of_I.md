# Fundamentals of Spatial Filtering

Spatial filtering is a process by which we can alter properties of an optical image by selectively removing certain spatial frequencies that make up an object. Spatial filtering is the process of assigning the value of a pixel based on its neighbors. The filters or masks, which are also known as kernels, used in the process are small matrices run in the entire image through a convolution process.

Some of the objectives of spatial filtering are:

- To enhance the image quality by removing noise, blurring, or sharpening the edges.
- To extract features or regions of interest from the image for further analysis or recognition.
- To transform the image into a different domain for compression, encryption, or other purposes.

Some of the basic concepts of spatial filtering are:

- The spatial domain is the plane of the image where each pixel has a coordinate (x, y) and an intensity value f(x, y).
- The frequency domain is the plane of the image where each pixel has a coordinate (u, v) and a magnitude F(u, v) that represents the contribution of a sinusoidal wave of frequency (u, v) to the image.
- The Fourier transform is a mathematical operation that converts an image from the spatial domain to the frequency domain, and the inverse Fourier transform converts it back.
- A filter or kernel is a small matrix of coefficients that is applied to a neighborhood of pixels in the image to produce a new pixel value.
- A convolution is a mathematical operation that slides the filter over the image and computes the sum of products of the filter coefficients and the corresponding pixel values.
- A correlation is a similar operation to convolution, except that the filter is not flipped before sliding over the image.

Some of the types of spatial filters are:

- Linear filters: These are filters that produce a linear combination of the pixel values in the neighborhood. The output of a linear filter is the convolution of the filter and the image. Examples of linear filters are averaging filter, Gaussian filter, Laplacian filter, etc.
- Non-linear filters: These are filters that produce a non-linear combination of the pixel values in the neighborhood. The output of a non-linear filter is not the convolution of the filter and the image. Examples of non-linear filters are median filter, max filter, min filter, etc.
- Adaptive filters: These are filters that adjust their coefficients or parameters based on the local characteristics of the image, such as the variance or the gradient. Examples of adaptive filters are adaptive median filter, adaptive Wiener filter, etc.