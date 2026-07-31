# Adaptive filters for image restoration

- Adaptive filters are commonly used in image processing to enhance or restore data by removing noise without significantly blurring the structures in the image .
- Adaptive filters adjust their behavior based on the characteristics of the image under filter, such as the local statistics, the spatial frequency, or the edge information .
- Adaptive filters can be classified into two categories: spatial domain filters and frequency domain filters.
- Spatial domain filters operate directly on the pixel values of the image, and can be further divided into local and global filters.
- Local filters use a neighborhood window around each pixel to compute the output value, while global filters use the entire image or a large region.
- Examples of local spatial domain adaptive filters are adaptive median filter, adaptive mean filter, adaptive Wiener filter, and adaptive bilateral filter .
- Examples of global spatial domain adaptive filters are anisotropic diffusion filter, total variation filter, and non-local means filter.
- Frequency domain filters operate on the Fourier transform of the image, and can be further divided into parametric and non-parametric filters.
- Parametric filters assume a model for the noise and the signal spectra, and use it to design an optimal filter, such as the Wiener filter.
- Non-parametric filters do not assume a model, but estimate the spectra from the data, such as the spectral subtraction filter.
- Adaptive filters can be applied to various image restoration problems, such as denoising, deblurring, inpainting, super-resolution, and compression artifact removal.