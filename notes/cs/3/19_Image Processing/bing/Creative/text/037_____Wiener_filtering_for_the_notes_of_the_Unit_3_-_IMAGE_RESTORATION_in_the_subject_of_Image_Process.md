### Wiener filtering

- Wiener filtering is a technique for image restoration that aims to reduce the mean square error between the restored image and the original image .
- Wiener filtering can be applied to images that are degraded by a known linear filter and additive noise .
- Wiener filtering involves estimating the power spectra of the original image and the noise, and using them to design a filter that minimizes the restoration error .
- Wiener filtering can be implemented in the frequency domain by multiplying the Fourier transform of the degraded image by a Wiener filter function .
- The Wiener filter function is given by :

$$
H_w(u,v) = \frac{H^*(u,v)S_f(u,v)}{|H(u,v)|^2S_f(u,v)+S_n(u,v)}
$$

where $H(u,v)$ is the degradation function, $H^*(u,v)$ is its complex conjugate, $S_f(u,v)$ is the power spectrum of the original image, and $S_n(u,v)$ is the power spectrum of the noise.

- Wiener filtering can also be implemented in the spatial domain by using a convolution kernel that approximates the inverse of the degradation function.
- Wiener filtering can improve the quality of images that are blurred and noisy, but it requires accurate knowledge of the degradation function and the noise characteristics .
- Wiener filtering can also be extended to blind deconvolution, where the degradation function is unknown and has to be estimated from the degraded image.