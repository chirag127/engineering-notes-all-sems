### Wiener filtering

Wiener filtering is a technique for image restoration that aims to reduce the mean square error between the restored image and the original image. It is based on the assumption that the degradation process can be modeled as a linear and space-invariant system with additive noise.

The Wiener filter can be derived in the frequency domain as follows:

- Let $F(u,v)$ be the Fourier transform of the original image, $H(u,v)$ be the degradation function, $G(u,v)$ be the Fourier transform of the degraded image, and $N(u,v)$ be the Fourier transform of the noise.
- The degradation process can be written as:

$$G(u,v) = H(u,v)F(u,v) + N(u,v)$$

- The goal is to find an inverse filter $W(u,v)$ such that the restored image $R(u,v) = W(u,v)G(u,v)$ is as close as possible to the original image $F(u,v)$.
- The mean square error between $R(u,v)$ and $F(u,v)$ is given by:

$$\epsilon^2 = E\left[|R(u,v) - F(u,v)|^2\right]$$

- The Wiener filter minimizes this error by choosing $W(u,v)$ as:

$$W(u,v) = \frac{H^*(u,v)S_f(u,v)}{|H(u,v)|^2S_f(u,v) + S_n(u,v)}$$

- where $H^*(u,v)$ is the complex conjugate of $H(u,v)$, $S_f(u,v)$ is the power spectrum of the original image, and $S_n(u,v)$ is the power spectrum of the noise.
- The Wiener filter can be seen as a trade-off between inverse filtering and noise smoothing. When the noise power is zero, the Wiener filter reduces to the inverse filter. When the noise power is high, the Wiener filter suppresses the high-frequency components that are dominated by noise.

Some practical considerations for implementing the Wiener filter are:

- The degradation function $H(u,v)$ may be known or estimated from the image or some prior information.
- The power spectra of the original image and the noise, $S_f(u,v)$ and $S_n(u,v)$, may not be known exactly and need to be estimated from the image or some prior information.
- The Wiener filter can be applied in a cascade manner, where the degraded image is first smoothed by a low-pass filter to reduce the noise, and then the inverse filter is applied to the smoothed image to remove the blur.
- The Wiener filter can also be generalized to deal with non-linear and space-variant degradations by using an iterative algorithm that updates the restored image and the degradation function until convergence.

An example of Wiener filtering for image restoration is shown below:

- The original image is the standard 256x256 Lena test image.
- The image is blurred by a 9x9 uniform low-pass filter with a cutoff frequency of 0.1 cycles/pixel.
- The blurred image is corrupted by additive white Gaussian noise with zero mean and variance of 100.
- The Wiener filter is applied to the noisy blurred image with a cascade implementation of the noise smoothing and inverse filtering.
- The parameters of the Wiener filter are estimated as follows:
  - The degradation function $H(u,v)$ is assumed to be the same as the blurring filter.
  - The power spectrum of the original image $S_f(u,v)$ is estimated by the average power spectrum of several natural images.
  - The power spectrum of the noise $S_n(u,v)$ is estimated by the variance of the noise.
- The restored image is compared with the original image and the noisy blurred image in terms of the mean square error and the peak signal-to-noise ratio.

The results are shown in the following table and figure:

| Image | MSE | PSNR |
|-------|-----|------|
| Original | 0 | Inf |
| Noisy blurred | 1159.7 | 17.9 dB |
| Restored | 131.6 | 26.1 dB |

![Wiener filtering example](https://www.owlnet.rice.edu/~elec539/Projects99/BACH/proj2/wiener.gif)

: WIENER FILTERING - Rice University. https://www.owlnet.rice.edu/~elec539/Projects99/BACH/proj2/wiener.html