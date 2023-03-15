### Inverse Filtering

Inverse filtering is a technique used in image restoration to recover an original image that has been degraded by a known degradation function. It is a process that attempts to reverse the degradation by applying an inverse filter to the degraded image.

1. The degradation function is usually modeled as a linear, space-invariant system, which can be represented by a convolution operation between the original image and the point spread function (PSF) of the degradation.
2. The inverse filter is designed to undo the effect of the degradation by deconvolving the degraded image with the PSF.
3. In the frequency domain, this is equivalent to dividing the Fourier transform of the degraded image by the Fourier transform of the PSF.
4. However, the inverse filter is highly sensitive to noise, as it can amplify the noise present in the degraded image, resulting in a poor restoration.
5. To mitigate this issue, various regularization techniques, such as the Wiener filter or the constrained least squares filter, can be used to stabilize the inverse filter and improve the restoration.