# Degradation Model for Image Restoration

- Image restoration is the process of recovering an image that has been degraded by some factors, such as blurring, noise, distortion, etc.  
- Image degradation is the process of reducing the quality or clarity of an image due to some factors, such as motion, defocus, atmospheric turbulence, sensor noise, etc.  
- A degradation model is a mathematical or probabilistic representation of how an image is degraded by a degradation function and an additive noise term.   
- A degradation model can be expressed as:

  g(x,y) = h(x,y) * f(x,y) + n(x,y)

  where:

  - g(x,y) is the degraded image
  - h(x,y) is the degradation function
  - f(x,y) is the original image
  - n(x,y) is the additive noise term
  - * is the convolution operator

- The degradation function h(x,y) can be linear or nonlinear, spatially invariant or variant, deterministic or stochastic, depending on the type and source of degradation.  
- The additive noise term n(x,y) can be modeled by different distributions, such as Gaussian, Poisson, salt-and-pepper, etc., depending on the nature and level of noise.  
- The goal of image restoration is to estimate the original image f(x,y) from the degraded image g(x,y) by using some knowledge of the degradation model.   
- Image restoration can be performed by different methods, such as inverse filtering, Wiener filtering, blind deconvolution, regularization, etc., depending on the availability and accuracy of the degradation model.   
- Image restoration can also be performed by learning-based methods, such as deep neural networks, that can learn the degradation model from data and handle complex and unknown degradation patterns.