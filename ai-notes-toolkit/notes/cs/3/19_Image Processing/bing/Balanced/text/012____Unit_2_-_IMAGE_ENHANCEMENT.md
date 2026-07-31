## Unit 2 - IMAGE ENHANCEMENT

- Image enhancement is the process of improving the quality or appearance of an image by modifying its features, such as contrast, brightness, sharpness, noise, etc.
- Image enhancement can be done in two domains: spatial domain and frequency domain.
- Spatial domain techniques operate directly on the pixels of the image, while frequency domain techniques transform the image into a different representation, such as Fourier transform, and manipulate the coefficients of the transform.
- Some common spatial domain techniques are:
  - Point processing: applying a function to each pixel independently, such as negative, log, power-law, etc.
  - Histogram processing: adjusting the distribution of pixel values, such as histogram equalization, histogram matching, etc.
  - Spatial filtering: applying a mask or kernel to a neighborhood of pixels, such as smoothing, sharpening, edge detection, etc.
- Some common frequency domain techniques are:
  - Low-pass filtering: attenuating the high-frequency components of the image, such as Gaussian, Butterworth, etc.
  - High-pass filtering: attenuating the low-frequency components of the image, such as Laplacian, Sobel, etc.
  - Band-pass filtering: attenuating the components outside a certain frequency range, such as notch, band-reject, etc.
  - Homomorphic filtering: separating the illumination and reflectance components of the image, and enhancing the contrast and details of the image.