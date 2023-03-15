### Inverse Filtering

- Inverse filtering is a technique for image restoration that aims to undo the effects of a known blurring filter on an image .
- Inverse filtering assumes that the degradation process can be modeled as a linear and space-invariant system, and that the blurring filter and the noise characteristics are known .
- Inverse filtering can be performed in the frequency domain, by applying the inverse of the blurring filter's transfer function to the degraded image's spectrum .
- Inverse filtering can be expressed as:

$$
\hat{F}(u,v) = \frac{G(u,v)}{H(u,v)}
$$

where $\hat{F}(u,v)$ is the restored image's spectrum, $G(u,v)$ is the degraded image's spectrum, and $H(u,v)$ is the blurring filter's transfer function .

- Inverse filtering can recover the original image perfectly if the blurring filter is invertible and there is no noise in the image .
- However, inverse filtering is very sensitive to additive noise, because it tends to amplify the high-frequency components of the noise, resulting in ringing artifacts and noise amplification in the restored image .
- To reduce the noise sensitivity of inverse filtering, some modifications can be applied, such as truncated inverse filtering, Wiener filtering, constrained least squares filtering, or iterative methods  .
- Truncated inverse filtering sets the inverse filter to zero for frequencies where the blurring filter's magnitude is below a threshold, to avoid dividing by very small numbers.
- Wiener filtering incorporates a statistical model of the noise and the original image, and minimizes the mean squared error between the restored image and the original image.
- Constrained least squares filtering adds a regularization term to the inverse filtering, to penalize high-frequency components in the restored image.
- Iterative methods update the restored image iteratively, using a gradient descent algorithm or a conjugate gradient algorithm, to minimize an objective function that measures the restoration error and the smoothness of the image.