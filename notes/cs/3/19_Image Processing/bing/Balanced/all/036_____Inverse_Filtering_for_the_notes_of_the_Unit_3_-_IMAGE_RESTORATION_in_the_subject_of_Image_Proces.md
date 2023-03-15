# Inverse Filtering

- Inverse filtering is a technique for image restoration that aims to undo the effects of a known blurring filter on an image .
- Inverse filtering assumes that the degradation process can be modeled as a linear and space-invariant system, and that the blurring filter and the noise characteristics are known .
- Inverse filtering can be performed in the frequency domain, by applying the inverse of the blurring filter's frequency response to the degraded image's spectrum .
- Inverse filtering can be expressed as:

$$\hat{F}(u,v) = \frac{G(u,v)}{H(u,v)}$$

where $\hat{F}(u,v)$ is the restored image spectrum, $G(u,v)$ is the degraded image spectrum, and $H(u,v)$ is the blurring filter's frequency response .

- Inverse filtering can recover the original image exactly if the blurring filter is invertible and there is no noise in the degraded image .
- However, inverse filtering is very sensitive to additive noise, as it tends to amplify the high-frequency components of the noise, resulting in ringing artifacts and noise amplification in the restored image .
- To reduce the noise sensitivity of inverse filtering, some modifications can be applied, such as truncated inverse filtering, Wiener filtering, constrained least squares filtering, or iterative methods   .
- Truncated inverse filtering sets the inverse filter to zero for frequencies where the blurring filter is close to zero, to avoid dividing by very small numbers .
- Wiener filtering incorporates a priori knowledge of the noise and the original image spectra, and minimizes the mean square error between the restored and the original image .
- Constrained least squares filtering imposes a smoothness constraint on the restored image, and minimizes a cost function that balances the fidelity and the smoothness terms .
- Iterative methods update the restored image iteratively, using gradient descent or other optimization techniques, until a convergence criterion is met  .