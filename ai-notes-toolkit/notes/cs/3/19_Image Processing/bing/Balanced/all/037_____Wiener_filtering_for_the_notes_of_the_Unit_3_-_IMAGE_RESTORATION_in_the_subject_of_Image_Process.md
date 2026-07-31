# Wiener filtering for image restoration

Wiener filtering is a technique for restoring images that are degraded by a known linear filter and additive noise. It is based on minimizing the mean square error between the restored image and the original image.

## Theory

The degradation model for an image can be expressed as:

$$
g(x,y) = h(x,y) \ast f(x,y) + n(x,y)
$$

where $g(x,y)$ is the degraded image, $h(x,y)$ is the degradation filter, $f(x,y)$ is the original image, $n(x,y)$ is the additive noise, and $\ast$ denotes convolution.

The goal of image restoration is to recover $f(x,y)$ from $g(x,y)$. One possible solution is to use inverse filtering, which is based on applying the inverse of the degradation filter to the degraded image:

$$
\hat{f}(x,y) = \frac{G(u,v)}{H(u,v)}
$$

where $\hat{f}(x,y)$ is the restored image, $G(u,v)$ and $H(u,v)$ are the Fourier transforms of $g(x,y)$ and $h(x,y)$, respectively.

However, inverse filtering is very sensitive to noise, since it can amplify the high-frequency components of the noise. A better solution is to use Wiener filtering, which is based on applying a filter that minimizes the mean square error between the restored image and the original image:

$$
\hat{f}(x,y) = \frac{H^*(u,v)S_f(u,v)}{|H(u,v)|^2 + S_n(u,v)/S_f(u,v)}G(u,v)
$$

where $H^*(u,v)$ is the complex conjugate of $H(u,v)$, $S_f(u,v)$ and $S_n(u,v)$ are the power spectra of the original image and the noise, respectively.

## Implementation

To implement the Wiener filter in practice, we have to estimate the power spectra of the original image and the noise. One possible method is to use the local mean and variance of the degraded image as estimates of the signal and noise power, respectively. Another possible method is to use a blind-Wiener filter, which iteratively estimates the degradation filter and the power spectra of the original image and the noise.

## Example

To illustrate the Wiener filtering in image restoration, we use the standard 256x256 Lena test image. We blur the image with a 9x9 Gaussian filter with a standard deviation of 2, then add white Gaussian noise with a variance of 100. The Wiener filtering is applied to the image with a cascade implementation of the noise smoothing and inverse filtering. The results are shown below.

Original image:

![Original image](https://www.owlnet.rice.edu/~elec539/Projects99/BACH/proj2/lena.gif)

Degraded image:

![Degraded image](https://www.owlnet.rice.edu/~elec539/Projects99/BACH/proj2/lena_blur.gif)

Restored image:

![Restored image](https://www.owlnet.rice.edu/~elec539/Projects99/BACH/proj2/lena_wiener.gif)

## References

: [WIENER FILTERING - Rice University](https://www.owlnet.rice.edu/~elec539/Projects99/BACH/proj2/wiener.html)

: [Deblur Images Using a Wiener Filter - MATLAB & Simulink Example - MathWorks](https://www.mathworks.com/help/images/deblurring-images-using-a-wiener-filter.html)

: [Image restoration by blind‐Wiener filter - Yoo - 2014 - IET Image Processing](https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/iet-ipr.2013.0693)