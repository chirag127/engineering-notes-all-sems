### Properties of Image Restoration

- Image restoration is the process of recovering an image from a degraded version, usually a blurred and noisy image .
- Image restoration is a fundamental problem in image processing, and it also provides a testbed for more general inverse problems.
- Image restoration techniques are oriented toward modeling the degradation and applying the inverse process in order to recover the original image.
- Image restoration techniques can be classified into two categories: spatial domain methods and frequency domain methods.
- Spatial domain methods operate directly on the pixels of the image, while frequency domain methods transform the image into its frequency components and then apply filters to remove the noise and blur.
- Image restoration techniques can also be categorized into deterministic methods and probabilistic methods.
- Deterministic methods assume that the degradation model and the parameters are known or can be estimated, and they use mathematical formulas or algorithms to obtain the restored image.
- Probabilistic methods assume that the degradation model and the parameters are unknown or uncertain, and they use statistical or Bayesian methods to infer the restored image based on prior knowledge and likelihood functions.
- Ideally, an image restoration technique will deliver an image that is consistent with available data and constraints (e.g., positivity), and which is free of obvious artifacts.
- Any technique that achieves this should be taken seriously, regardless of whether it is based on an ad hoc procedure or justified by a formalism such as maximum entropy.
- Image restoration techniques should also consider the properties of natural images, such as cross-scale similarity and anisotropic image features, and model them explicitly or implicitly in the restoration process.