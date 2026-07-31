# Inverse Filtering

- Inverse filtering is a technique for image restoration that aims to undo the effects of a known degradation process, such as blurring or noise, on an image .
- Inverse filtering assumes that the degradation process can be modeled by a linear and shift-invariant system, and that its frequency response (or transfer function) is known .
- Inverse filtering can be performed in the frequency domain, by multiplying the Fourier transform of the degraded image by the inverse of the transfer function of the degradation system .
- Inverse filtering can also be performed in the spatial domain, by convolving the degraded image with the inverse filter, which is the inverse Fourier transform of the inverse transfer function .
- Inverse filtering can recover the original image exactly if the degradation system is invertible and there is no noise in the image .
- However, inverse filtering is very sensitive to noise, because it tends to amplify the high-frequency components of the noise, which may dominate the low-frequency components of the image .
- To reduce the noise amplification, inverse filtering can be modified by truncating the inverse transfer function at a certain threshold, or by applying a regularization term to the inverse filter .
- Alternatively, inverse filtering can be replaced by more robust methods, such as Wiener filtering, which takes into account the power spectra of the image and the noise, or constrained least squares filtering, which minimizes the mean squared error between the restored image and the original image subject to some constraints .
- Inverse filtering can also be performed iteratively, by updating the restored image based on the error between the degraded image and the image obtained by applying the degradation system to the restored image.
- Inverse filtering can be extended to spatially adaptive algorithms, which adjust the inverse filter according to the local characteristics of the image, such as edges or textures.