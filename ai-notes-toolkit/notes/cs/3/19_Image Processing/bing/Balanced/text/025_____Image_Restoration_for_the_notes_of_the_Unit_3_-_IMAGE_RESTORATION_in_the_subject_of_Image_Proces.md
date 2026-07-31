### Image Restoration

- Image restoration is the process of recovering an image that has been degraded by noise, blur, or other factors.
- Image restoration aims to restore the original image as closely as possible, while image enhancement aims to improve the visual quality of an image according to some criteria.
- Image restoration can be classified into two categories: spatial domain methods and frequency domain methods.
- Spatial domain methods operate directly on the pixel values of the image, while frequency domain methods transform the image into a different domain (such as Fourier or wavelet) and perform operations on the transformed coefficients.
- Some common spatial domain methods for image restoration are:
  - Mean filtering: Replaces each pixel with the average of its neighboring pixels. It reduces noise but also blurs edges and details.
  - Median filtering: Replaces each pixel with the median of its neighboring pixels. It preserves edges and details better than mean filtering, but can create artifacts such as salt-and-pepper noise.
  - Adaptive filtering: Adjusts the filter parameters according to the local characteristics of the image, such as variance or entropy. It can achieve better results than fixed filters, but requires more computation and complexity.
- Some common frequency domain methods for image restoration are:
  - Inverse filtering: Applies the inverse of the degradation function to the degraded image. It assumes that the degradation function is known and invertible, and that the noise is negligible. It can amplify noise and introduce ringing artifacts if these assumptions are violated.
  - Wiener filtering: Applies a filter that minimizes the mean square error between the restored image and the original image. It takes into account the degradation function and the noise power spectrum, and balances the trade-off between noise reduction and detail preservation.
  - Regularized filtering: Applies a filter that minimizes a cost function that includes a regularization term. The regularization term imposes some prior knowledge or constraints on the restored image, such as smoothness or sparsity. It can reduce noise and artifacts, but also introduce bias and blur.