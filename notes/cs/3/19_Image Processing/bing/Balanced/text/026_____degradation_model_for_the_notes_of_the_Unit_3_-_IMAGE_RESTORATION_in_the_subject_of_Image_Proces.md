### Degradation Model for Image Restoration

- Image restoration is the process of recovering an image that has been degraded by some factors, such as blurring, noise, distortion, etc.
- Image degradation is the process of reducing the quality or information content of an image due to some factors, such as optical aberrations, atmospheric turbulence, motion blur, sensor noise, etc.
- A degradation model is a mathematical or probabilistic representation of how an image is degraded by a degradation function and an additive noise term.
- A degradation function is a function that describes how the image is blurred or distorted by a physical phenomenon, such as a point spread function (PSF) or a geometric transformation.
- An additive noise term is a function that describes how the image is corrupted by random fluctuations or errors, such as Gaussian noise or salt-and-pepper noise.
- A degradation model can be expressed as:

  g(x,y) = h(x,y) * f(x,y) + n(x,y)

  where:

  - g(x,y) is the degraded image
  - h(x,y) is the degradation function
  - f(x,y) is the original image
  - n(x,y) is the additive noise term
  - * is the convolution operator

- The goal of image restoration is to estimate the original image f(x,y) from the degraded image g(x,y) and the degradation model h(x,y) and n(x,y).
- Image restoration can be performed using various methods, such as inverse filtering, Wiener filtering, blind deconvolution, regularization, etc.