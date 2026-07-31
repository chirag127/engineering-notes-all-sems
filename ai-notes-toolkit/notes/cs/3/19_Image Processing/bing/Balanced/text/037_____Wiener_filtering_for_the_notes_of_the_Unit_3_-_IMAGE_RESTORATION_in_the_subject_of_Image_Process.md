### Wiener filtering

Wiener filtering is a technique for image restoration that aims to reduce the mean square error between the restored image and the original image. It is based on the assumption that the degradation process can be modeled as a linear and space-invariant system with additive noise.

The Wiener filter can be derived in two ways: as a statistical filter that minimizes the expected value of the error, or as a spectral filter that operates on the frequency domain of the image.

The Wiener filter has the following form in the frequency domain:

$$
\hat{F}(u,v) = \frac{H^*(u,v)S_f(u,v)}{|H(u,v)|^2S_f(u,v)+S_n(u,v)}G(u,v)
$$

where $\hat{F}(u,v)$ is the restored image, $H(u,v)$ is the degradation function, $S_f(u,v)$ is the power spectrum of the original image, $S_n(u,v)$ is the power spectrum of the noise, $G(u,v)$ is the degraded image, and $H^*(u,v)$ is the complex conjugate of $H(u,v)$.

The Wiener filter requires the knowledge of the degradation function and the power spectra of the original image and the noise. However, in many cases, these are not known or difficult to estimate. Therefore, some approximations or estimations are needed to implement the Wiener filter in practice .

Some examples of Wiener filtering for image restoration are:

- Deblurring images using a Wiener filter. This example shows how to restore a blurred image that is corrupted by random noise, using the deconvwnr function in MATLAB. The function takes the degraded image, the point spread function of the blur, and optionally the noise-to-signal ratio as inputs, and returns the restored image. The example also shows how to estimate the point spread function and the noise-to-signal ratio from the degraded image, and how to compare the results of different restoration methods.
- Image restoration by blind-Wiener filter. This paper proposes a method for image restoration that does not require the knowledge of the degradation function or the noise power spectrum. The method uses a blind deconvolution algorithm to estimate the degradation function, and then applies a Wiener filter with an adaptive noise power spectrum. The paper shows that the proposed method can achieve better results than conventional Wiener filtering and other blind deconvolution methods.
- Image restoration using rolling ball algorithm. This is a method for removing background intensity variation from images, especially for fluorescence microscopy images. The method uses a ball-shaped kernel to estimate the background intensity, and then subtracts it from the original image. The method can be implemented using the rolling_ball function in scikit-image, which takes the image and the radius of the ball as inputs, and returns the background and the restored image. The method can also be combined with a Wiener filter to reduce noise in the restored image.