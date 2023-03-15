### Inverse Filtering

- Inverse filtering is a technique for image restoration that aims to undo the effects of a known blurring filter on an image .
- The basic idea of inverse filtering is to apply the inverse of the blurring filter to the blurred image, assuming that the filter is invertible .
- Inverse filtering can be performed in the frequency domain, by multiplying the Fourier transform of the blurred image by the inverse of the Fourier transform of the blurring filter .
- Inverse filtering can produce accurate results when the blurring filter is known and there is no noise in the image .
- However, inverse filtering is very sensitive to additive noise, as it tends to amplify the high-frequency components of the noise .
- To overcome this problem, some variations of inverse filtering have been proposed, such as truncated inverse filtering, Wiener filtering, and least squares filtering  .
- Truncated inverse filtering sets the inverse filter to zero for frequencies where the blurring filter is very small, to avoid dividing by very small numbers.
- Wiener filtering incorporates a prior model of the noise and the original image, and minimizes the mean squared error between the restored image and the original image.
- Least squares filtering minimizes the squared difference between the blurred image and the filtered image, subject to some regularization constraints.