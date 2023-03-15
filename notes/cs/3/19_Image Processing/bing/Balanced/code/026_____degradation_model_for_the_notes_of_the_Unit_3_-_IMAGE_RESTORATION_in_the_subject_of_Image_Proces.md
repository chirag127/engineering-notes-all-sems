### Degradation Model for Image Restoration

- Image restoration is the process of recovering an image that has been degraded by some factors, such as blurring, noise, or distortion.
- Image degradation is the process of reducing the quality or clarity of an image due to some factors, such as camera motion, defocus, atmospheric turbulence, or sensor noise.
- A degradation model is a mathematical or probabilistic representation of how an image is degraded by a degradation function and an additive noise term.
- A degradation model can be expressed as:

```
g(x,y) = h(x,y) * f(x,y) + n(x,y)
```

where:

  - `g(x,y)` is the degraded image
  - `h(x,y)` is the degradation function
  - `f(x,y)` is the original image
  - `n(x,y)` is the additive noise term
  - `*` is the convolution operator

- The degradation function `h(x,y)` can be linear or nonlinear, spatially invariant or variant, deterministic or stochastic, depending on the type and source of degradation.
- The additive noise term `n(x,y)` can be modeled by different probability distributions, such as Gaussian, Poisson, or salt-and-pepper, depending on the nature and level of noise.
- The goal of image restoration is to estimate the original image `f(x,y)` from the degraded image `g(x,y)` by using some knowledge of the degradation model.
- Image restoration can be performed by different methods, such as inverse filtering, Wiener filtering, blind deconvolution, or deep learning, depending on the availability and accuracy of the degradation model  .