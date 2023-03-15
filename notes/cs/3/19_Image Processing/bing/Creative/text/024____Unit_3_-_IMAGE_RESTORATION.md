## Unit 3 - IMAGE RESTORATION

- Image restoration is the operation of taking a corrupt/noisy image and estimating the clean, original image.
- Corruption may come in many forms such as motion blur, noise, camera mis-focus, haze, JPEG compression, etc .
- Image restoration is performed by reversing the process that blurred the image and such is performed by imaging a point source and use the point source image, which is called the **Point Spread Function (PSF)** to restore the image information lost to the blurring process.
- Image restoration is different from image enhancement, which aims to improve the visual quality of an image without considering the source of degradation.
- Image restoration is a challenging and active research area in computer vision and image processing, with many applications such as medical imaging, remote sensing and video monitoring .
- Image restoration techniques can be classified into two categories: **blind** and **non-blind**. Blind image restoration does not assume any prior knowledge of the degradation model or the PSF, while non-blind image restoration requires such information .
- Some of the common methods for image restoration are:

  - **Wiener filter**: A linear filter that minimizes the mean square error between the restored image and the original image, assuming additive Gaussian noise and a known PSF.
  - **Richardson-Lucy algorithm**: An iterative algorithm that uses maximum likelihood estimation to restore an image from a blurred and noisy observation, assuming a known PSF and Poisson noise.
  - **Total variation (TV) regularization**: A non-linear method that imposes a smoothness constraint on the restored image, based on the assumption that natural images have sparse gradients.
  - **Deep learning**: A data-driven approach that uses neural networks to learn the mapping from corrupted images to clean images, either with or without a known PSF.