# Adaptive filters for image restoration

- Adaptive filters are commonly used in image processing to enhance or restore data by removing noise without significantly blurring the structures in the image .
- Adaptive filters adjust their parameters according to the characteristics of the image under filter, such as the local statistics, the spatial frequency, or the edge information .
- Adaptive filters can be classified into two categories: spatial domain adaptive filters and frequency domain adaptive filters.
- Spatial domain adaptive filters operate directly on the pixel values of the image, and can be further divided into local adaptive filters and global adaptive filters.
- Local adaptive filters use a small neighborhood around each pixel to determine the filter parameters, such as the mean, the variance, or the median . Examples of local adaptive filters are adaptive mean filters, adaptive median filters, and adaptive Wiener filters .
- Global adaptive filters use the entire image or a large region to determine the filter parameters, such as the noise power spectrum or the image model. Examples of global adaptive filters are adaptive Fourier filters, adaptive wavelet filters, and adaptive Kalman filters.
- Frequency domain adaptive filters transform the image into a frequency representation, such as the Fourier transform or the wavelet transform, and apply filtering operations on the frequency coefficients.
- Frequency domain adaptive filters can exploit the spectral properties of the image and the noise, and can perform selective filtering on different frequency bands.
- Frequency domain adaptive filters can also be local or global, depending on whether they use a windowed transform or a global transform.
- The advantages of adaptive filters are that they can adapt to the varying noise and image characteristics, and that they can preserve the image details better than non-adaptive filters .
- The disadvantages of adaptive filters are that they require more computational resources and more prior knowledge about the image and the noise .