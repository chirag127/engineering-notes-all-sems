### Smoothing and Sharpening Spatial Filtering

- Spatial filtering is a technique for modifying or enhancing an image by applying a filter to each pixel and its neighbors.
- A filter is a matrix of coefficients, also called a kernel, that determines how the output pixel value is calculated from the input pixel values.
- The process of applying a filter to an image is called convolution, which involves multiplying the filter coefficients with the corresponding pixel values and adding them up to get the output pixel value.
- Smoothing and sharpening are two common types of spatial filtering that have different effects on an image.
- Smoothing filters are used to blur an image, reduce noise, and remove small details .
- Sharpening filters are used to enhance the contrast of an image, highlight edges, and emphasize small details.
- Smoothing filters are usually low-pass filters, which means they allow low-frequency components (such as smooth regions) to pass through and attenuate high-frequency components (such as edges and noise).
- Sharpening filters are usually high-pass filters, which means they allow high-frequency components to pass through and attenuate low-frequency components.
- Commonly seen smoothing filters include average smoothing, Gaussian smoothing, and adaptive smoothing.
- Commonly seen sharpening filters include Laplacian, Sobel, and Prewitt.
- Smoothing and sharpening filters can be combined to achieve different effects, such as unsharp masking, which sharpens an image by subtracting a smoothed version of the image from the original image.