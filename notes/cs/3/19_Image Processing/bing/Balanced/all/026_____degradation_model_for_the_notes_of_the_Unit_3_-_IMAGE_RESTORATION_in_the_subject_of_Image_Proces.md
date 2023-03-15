# Degradation Model for Image Restoration

- Image restoration is the process of recovering an image that has been degraded by some factors, such as blurring, noise, distortion, etc.
- Image degradation is the process of reducing the quality or information content of an image due to various sources of degradation.
- A degradation model is a mathematical or probabilistic representation of how an image is degraded by a degradation function and an additive noise term.
- A degradation model can be expressed as:

  `g(x,y) = h(x,y) * f(x,y) + n(x,y)`

  where:

  - `g(x,y)` is the degraded image
  - `f(x,y)` is the original image
  - `h(x,y)` is the degradation function
  - `n(x,y)` is the additive noise term
  - `*` denotes the convolution operation

- The degradation function `h(x,y)` can be spatially invariant or spatially variant, depending on whether it is constant or varying across the image.
- The additive noise term `n(x,y)` can be modeled by different distributions, such as Gaussian, Poisson, salt-and-pepper, etc.
- The goal of image restoration is to estimate the original image `f(x,y)` from the degraded image `g(x,y)` and the degradation model.
- Image restoration can be performed by different methods, such as inverse filtering, Wiener filtering, blind deconvolution, regularization, etc.