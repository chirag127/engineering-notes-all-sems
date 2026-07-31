# Degradation Model for Image Restoration

- Image restoration is the process of recovering an image that has been degraded by some factors, such as blurring, noise, distortion, etc.
- Image degradation can be modeled by a linear system, where the degraded image g(x,y) is related to the original image f(x,y) by the following equation:

g(x,y) = h(x,y) * f(x,y) + n(x,y)

- In this equation, h(x,y) is the degradation function, which represents the effect of blurring or distortion on the image, * is the convolution operator, and n(x,y) is the additive noise term, which represents the random fluctuations in the image intensity.
- The degradation function h(x,y) can be determined by the physical characteristics of the imaging system, such as the lens, the sensor, the motion, etc. The noise term n(x,y) can be modeled by a statistical distribution, such as Gaussian, Poisson, salt-and-pepper, etc.
- The goal of image restoration is to estimate the original image f(x,y) from the degraded image g(x,y), given some knowledge of the degradation function h(x,y) and the noise term n(x,y).
- Image restoration can be performed in different domains, such as the spatial domain or the frequency domain. In the spatial domain, the restoration is based on direct manipulation of the pixel values, such as filtering, interpolation, inpainting, etc. In the frequency domain, the restoration is based on transforming the image into a different representation, such as Fourier, wavelet, etc, and applying operations on the coefficients, such as deconvolution, denoising, etc.
- Image restoration can be classified into two categories, depending on the availability of the degradation model: blind and non-blind. Blind image restoration is the case where the degradation function h(x,y) and/or the noise term n(x,y) are unknown or partially known, and need to be estimated from the degraded image g(x,y). Non-blind image restoration is the case where the degradation function h(x,y) and the noise term n(x,y) are known or can be measured, and can be used to design the restoration algorithm.