# Wiener filtering for image restoration

- Wiener filtering is a technique for restoring images that are degraded by a known linear filter and additive noise .
- Wiener filtering aims to minimize the mean square error between the restored image and the original image.
- Wiener filtering requires the knowledge of the power spectra of the original image, the noise, and the degradation filter .
- Wiener filtering can be implemented in the frequency domain by multiplying the Fourier transform of the degraded image by a Wiener filter function .
- Wiener filter function is given by :

$$
H_w(u,v) = \frac{H^*(u,v)S_f(u,v)}{|H(u,v)|^2S_f(u,v)+S_n(u,v)}
$$

where $H_w(u,v)$ is the Wiener filter function, $H(u,v)$ is the degradation filter, $S_f(u,v)$ is the power spectrum of the original image, $S_n(u,v)$ is the power spectrum of the noise, and $H^*(u,v)$ is the complex conjugate of $H(u,v)$.

- Wiener filtering can also be implemented in the spatial domain by using a convolution kernel that approximates the inverse of the degradation filter.
- Wiener filtering can be applied to different types of degradation filters, such as motion blur, Gaussian blur, or out-of-focus blur.
- Wiener filtering can produce better results than inverse filtering, especially when the noise is high or the degradation filter is ill-conditioned .
- Wiener filtering can also be extended to blind deconvolution, where the degradation filter is unknown or partially known.