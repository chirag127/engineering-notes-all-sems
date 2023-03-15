## Unit 3 - IMAGE RESTORATION

- Image restoration is the process of improving the quality of an image that has been degraded by noise, blur, or other factors.
- Image restoration aims to recover the original image from the degraded image, or to estimate the degradation model and the original image simultaneously.
- Image restoration can be classified into two categories: spatial domain methods and frequency domain methods.
- Spatial domain methods operate directly on the pixel values of the image, and apply filters or transformations to enhance or restore the image.
- Frequency domain methods operate on the Fourier transform of the image, and manipulate the frequency components to remove noise or blur.
- Some common image restoration techniques are:
  - Inverse filtering: A simple method that applies the inverse of the degradation filter to the degraded image. It is effective only when the degradation filter is known and has no zeros in its frequency response.
  - Wiener filtering: A more robust method that minimizes the mean square error between the restored image and the original image. It takes into account the noise and the degradation filter, and can be applied adaptively to different regions of the image.
  - Blind deconvolution: A method that estimates both the degradation filter and the original image from the degraded image. It is useful when the degradation filter is unknown or varies spatially. It can be formulated as an optimization problem or a Bayesian inference problem.
  - Regularization: A method that incorporates prior knowledge or constraints on the original image or the degradation filter to improve the restoration. It can reduce the ill-posedness or the instability of the restoration problem. Some examples of regularization are Tikhonov regularization, total variation regularization, and sparse representation regularization.