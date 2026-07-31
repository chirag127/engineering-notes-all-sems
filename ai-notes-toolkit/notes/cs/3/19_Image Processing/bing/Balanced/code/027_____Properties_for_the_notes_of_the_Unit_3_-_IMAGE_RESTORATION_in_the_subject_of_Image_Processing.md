# Properties of Image Restoration

- Image restoration is the process of recovering an image from a degraded version, usually a blurred and noisy image .
- Image restoration is a fundamental problem in image processing, and it also provides a testbed for more general inverse problems.
- Image restoration techniques are oriented toward modeling the degradation and applying the inverse process in order to recover the original image.
- Image restoration can be formulated as an optimization problem, where the objective function consists of a data fidelity term and a regularization term .
- The data fidelity term measures the agreement between the observed image and the restored image, and the regularization term imposes some prior knowledge or constraints on the restored image .
- Image restoration techniques can be classified into two categories: spatial domain methods and frequency domain methods.
- Spatial domain methods operate directly on the pixel values of the image, and they can be further divided into point processing methods, neighborhood processing methods, and variational methods.
- Frequency domain methods transform the image into a different domain, such as the Fourier domain, and perform operations on the transformed coefficients, such as filtering, deconvolution, and spectral analysis.
- Image restoration techniques can also be categorized based on the type of degradation they aim to remove, such as denoising, deblurring, super-resolution, inpainting, and dehazing .
- Image restoration techniques can benefit from the use of image hierarchies, which capture the cross-scale similarity and anisotropic features of natural images.
- Image restoration techniques can be evaluated using various metrics, such as peak signal-to-noise ratio (PSNR), structural similarity index (SSIM), and perceptual quality measures .