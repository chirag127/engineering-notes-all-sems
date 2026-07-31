# Wiener filtering for image restoration

Wiener filtering is a technique for restoring images that are degraded by a known linear filter and additive noise. It is based on minimizing the mean square error between the restored image and the original image.

## Theory

- The degradation model for an image can be expressed as:

  `g(x,y) = h(x,y) * f(x,y) + n(x,y)`

  where `g(x,y)` is the degraded image, `h(x,y)` is the degradation filter, `f(x,y)` is the original image, `n(x,y)` is the additive noise, and `*` denotes convolution.

- The goal of image restoration is to recover `f(x,y)` from `g(x,y)`, given some knowledge of `h(x,y)` and `n(x,y)`.

- The Wiener filter is derived from the frequency domain by applying the inverse filter to the degraded image and adding a regularization term to reduce the noise amplification:

  `F(u,v) = [H*(u,v) / (|H(u,v)|^2 + K)] G(u,v)`

  where `F(u,v)`, `G(u,v)`, and `H(u,v)` are the Fourier transforms of `f(x,y)`, `g(x,y)`, and `h(x,y)`, respectively, `H*(u,v)` is the complex conjugate of `H(u,v)`, and `K` is a constant that depends on the noise-to-signal ratio (NSR).

- The Wiener filter can also be expressed in terms of the power spectra of the original image, the noise, and the degradation filter:

  `F(u,v) = [S_f(u,v) / (S_f(u,v) + S_n(u,v))] [1 / H(u,v)] G(u,v)`

  where `S_f(u,v)`, `S_n(u,v)`, and `S_g(u,v)` are the power spectra of `f(x,y)`, `n(x,y)`, and `g(x,y)`, respectively.

- The Wiener filter yields the minimum mean square error between the restored image and the original image. However, to obtain an optimal result, there must be accurate knowledge of the power spectra of the original image and the noise, besides the degradation filter. Otherwise, it will lead to an undesirable restored result.

## Implementation

- To implement the Wiener filter in practice, we have to estimate the power spectra of the original image and the noise, as well as the degradation filter.

- One way to estimate the power spectrum of the original image is to use a local mean filter on the degraded image and assume that the local mean is equal to the global mean of the original image.

- One way to estimate the power spectrum of the noise is to use a high-pass filter on the degraded image and assume that the high-frequency components are dominated by the noise.

- One way to estimate the degradation filter is to use a blind deconvolution algorithm that iteratively updates the filter and the restored image until convergence.

- Alternatively, some prior information about the degradation filter, such as its shape, size, or orientation, can be used to constrain the estimation process.

- Once the power spectra and the degradation filter are estimated, the Wiener filter can be applied to the degraded image in the frequency domain and the restored image can be obtained by inverse Fourier transform.

## Example

- To illustrate the Wiener filtering in image restoration, we use the standard 256x256 Lena test image. We blur the image with a 9x9 Gaussian low-pass filter with a standard deviation of 2, then add white Gaussian noise with a variance of 100 to the blurred image. The Wiener filtering is applied to the image with a cascade implementation of the noise smoothing and inverse filtering.

- The following figure shows the original image, the blurred noisy image, and the restored image by the Wiener filter.

![Wiener filtering example](https://www.owlnet.rice.edu/~elec539/Projects99/BACH/proj2/wiener.gif)

- The following table shows the mean square error (MSE) and the peak signal-to-noise ratio (PSNR) of the blurred noisy image and the restored image, compared to the original image.

| Image | MSE | PSNR |
|-------|-----|------|
| Blurred noisy | 2080.8 | 16.9 dB |
| Restored |  144.1 |