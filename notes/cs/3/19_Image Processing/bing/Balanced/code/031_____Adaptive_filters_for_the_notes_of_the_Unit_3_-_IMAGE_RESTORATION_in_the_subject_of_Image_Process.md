### Adaptive filters for image restoration

- Adaptive filters are commonly used in image processing to enhance or restore data by removing noise without significantly blurring the structures in the image .
- Adaptive filters adjust their behavior based on the characteristics of the image under filter, such as the local statistics, the spatial location, or the frequency content .
- Adaptive filters can be classified into two main categories: spatial domain filters and frequency domain filters.
- Spatial domain filters operate directly on the pixel values of the image, and can be further divided into local or global filters.
- Local filters use a neighborhood of pixels around each pixel to determine the output value, such as adaptive median filters, adaptive mean filters, or adaptive Wiener filters .
- Global filters use the entire image or a large region to determine the output value, such as anisotropic diffusion filters, bilateral filters, or non-local means filters.
- Frequency domain filters operate on the Fourier transform of the image, and can be further divided into parametric or non-parametric filters.
- Parametric filters assume a model for the noise and the signal spectra, and use it to design an optimal filter, such as Wiener filters or Kalman filters.
- Non-parametric filters do not assume a model for the spectra, and use data-driven methods to estimate them, such as spectral subtraction filters or minimum mean square error filters.
- Adaptive filters have advantages over non-adaptive filters, such as better noise reduction, edge preservation, and detail enhancement .
- Adaptive filters also have some challenges, such as computational complexity, parameter selection, and performance evaluation.