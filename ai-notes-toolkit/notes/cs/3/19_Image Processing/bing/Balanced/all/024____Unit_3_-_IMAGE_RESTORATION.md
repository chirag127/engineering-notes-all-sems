## Unit 3 - IMAGE RESTORATION

- Image restoration is the process of improving the quality of an image that has been degraded by noise, blur, or other factors.
- Image restoration aims to recover the original image from the degraded image, or to estimate the degradation model and the original image simultaneously.
- Image restoration can be classified into two categories: spatial domain methods and frequency domain methods.
- Spatial domain methods operate directly on the pixels of the image, and apply filters or operators to enhance or suppress certain features of the image.
- Frequency domain methods transform the image into a different domain, such as the Fourier domain, and manipulate the coefficients or spectra of the image to remove or reduce the effects of degradation.
- Image restoration can be further divided into two types: deterministic methods and probabilistic methods.
- Deterministic methods assume that the degradation model and the original image are known or can be estimated, and use mathematical techniques to solve an inverse problem or an optimization problem.
- Probabilistic methods assume that the degradation model and the original image are unknown or uncertain, and use statistical techniques to model the prior knowledge and the likelihood of the image, and infer the most probable or optimal solution.
- Some common image restoration techniques are:
  - Inverse filtering: a frequency domain method that applies the inverse of the degradation filter to the degraded image, assuming that the degradation filter and the noise are known or negligible.
  - Wiener filtering: a frequency domain method that applies a filter that minimizes the mean squared error between the restored image and the original image, assuming that the degradation filter and the noise power spectrum are known or estimated.
  - Regularized filtering: a frequency domain method that applies a filter that balances the fidelity and smoothness of the restored image, assuming that the degradation filter is known or estimated, and using a regularization parameter to control the trade-off.
  - Blind deconvolution: a method that estimates the degradation filter and the original image simultaneously, using an iterative algorithm that alternates between deconvolution and filter estimation, and using some constraints or priors to guide the solution.
  - Maximum likelihood estimation: a probabilistic method that estimates the original image that maximizes the likelihood of the degraded image, assuming that the degradation model and the noise distribution are known or specified.
  - Maximum a posteriori estimation: a probabilistic method that estimates the original image that maximizes the posterior probability of the original image given the degraded image, assuming that the degradation model, the noise distribution, and the prior distribution of the original image are known or specified.
  - Bayesian estimation: a probabilistic method that estimates the posterior distribution of the original image given the degraded image, assuming that the degradation model, the noise distribution, and the prior distribution of the original image are known or specified, and using a Bayesian inference technique such as Markov chain Monte Carlo or variational inference.