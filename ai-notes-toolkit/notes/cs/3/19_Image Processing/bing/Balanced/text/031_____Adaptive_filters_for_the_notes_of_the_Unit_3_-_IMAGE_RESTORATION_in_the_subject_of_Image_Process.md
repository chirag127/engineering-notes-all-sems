### Adaptive filters for image restoration

- Adaptive filters are commonly used in image processing to enhance or restore data by removing noise without significantly blurring the structures in the image .
- Adaptive filters adjust their parameters or coefficients according to the characteristics of the input image or the noise model.
- Adaptive filters can be classified into two categories: spatial domain filters and frequency domain filters.
- Spatial domain filters operate directly on the pixel values of the image and use a local neighborhood of pixels to estimate the noise-free value.
- Frequency domain filters transform the image into the frequency domain and apply a filter function to the frequency components of the image.
- Some examples of spatial domain adaptive filters are adaptive median filter, adaptive Wiener filter, adaptive bilateral filter, and adaptive anisotropic diffusion filter  .
- Some examples of frequency domain adaptive filters are adaptive notch filter, adaptive bandpass filter, and adaptive lowpass filter.
- The main advantage of adaptive filters is that they can adapt to the varying noise and image characteristics and achieve better performance than fixed filters .
- The main challenge of adaptive filters is to design a suitable criterion or algorithm for updating the filter parameters or coefficients .