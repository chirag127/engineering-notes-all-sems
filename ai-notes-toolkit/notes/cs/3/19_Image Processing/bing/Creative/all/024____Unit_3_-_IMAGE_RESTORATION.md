## Unit 3 - IMAGE RESTORATION

- Image restoration is the process of recovering an image that has been degraded by some factors such as noise, blur, or distortion.
- Image restoration aims to restore the original image as closely as possible, while image enhancement aims to improve the visual quality of an image according to some criteria.
- Image restoration can be classified into two categories: spatial domain methods and frequency domain methods.
- Spatial domain methods operate directly on the pixel values of the image, while frequency domain methods transform the image into a different domain (such as Fourier or wavelet) and perform operations on the transformed coefficients.
- Some common spatial domain methods are:
  - Inverse filtering: a simple method that applies the inverse of the degradation function to the degraded image. However, it is very sensitive to noise and may amplify it.
  - Wiener filtering: a more robust method that takes into account the noise characteristics and the power spectra of the original and degraded images. It minimizes the mean square error between the restored and original images.
  - Regularized filtering: a method that introduces a regularization term to the inverse filtering to reduce the noise amplification. The regularization term can be based on some prior knowledge or assumptions about the image, such as smoothness or sparsity.
- Some common frequency domain methods are:
  - Homomorphic filtering: a method that separates the illumination and reflectance components of an image and enhances the contrast and details of the reflectance component. It is useful for images with non-uniform illumination or shadows.
  - Blind deconvolution: a method that estimates both the original image and the degradation function from the degraded image. It is useful for images with unknown or varying degradation functions, such as motion blur or defocus blur.
  - Wavelet-based methods: methods that use wavelet transform to decompose an image into different frequency bands and perform restoration on each band separately. They can exploit the multi-resolution and sparsity properties of wavelets to achieve better results.