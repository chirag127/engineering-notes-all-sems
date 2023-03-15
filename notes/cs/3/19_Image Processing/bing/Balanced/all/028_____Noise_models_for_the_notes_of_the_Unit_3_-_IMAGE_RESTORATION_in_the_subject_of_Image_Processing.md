# Noise models for the notes of the Unit 3 - IMAGE RESTORATION in the subject of Image Processing

- Image restoration is the process of recovering an original image from a degraded image that has been corrupted by noise, blur, or other distortions.
- Image degradation can be modeled as a linear system, where the degraded image g(x,y) is the result of the convolution of the original image f(x,y) with a degradation function h(x,y), plus an additive noise term n(x,y):

  g(x,y) = h(x,y) * f(x,y) + n(x,y)

- In the frequency domain, the degradation model can be written as:

  G(u,v) = H(u,v) F(u,v) + N(u,v)

- The goal of image restoration is to estimate the original image f(x,y) or F(u,v) from the degraded image g(x,y) or G(u,v), given some knowledge of the degradation function h(x,y) or H(u,v) and the noise term n(x,y) or N(u,v).
- The noise term n(x,y) or N(u,v) represents the random fluctuations in the image intensity that are not part of the original image. The noise can be introduced during the image acquisition or transmission process, and can be affected by various factors such as sensor quality, lighting conditions, atmospheric interference, etc. .
- There are several noise models that are commonly used in digital image processing, each with a different probability density function (PDF) that describes the distribution of the noise values. Some of the most widely used noise models are :

  - Gaussian noise: The noise values follow a normal or Gaussian distribution with a mean of zero and a standard deviation of sigma. The PDF of Gaussian noise is given by:

    p(z) = (1 / sqrt(2 pi sigma^2)) exp(-z^2 / 2 sigma^2)

  - Rayleigh noise: The noise values follow a Rayleigh distribution with a mode of zero and a parameter of sigma. The PDF of Rayleigh noise is given by:

    p(z) = (z / sigma^2) exp(-z^2 / 2 sigma^2), z >= 0

  - Gamma noise: The noise values follow a gamma distribution with a shape parameter of alpha and a scale parameter of beta. The PDF of gamma noise is given by:

    p(z) = (beta^alpha / Gamma(alpha)) z^(alpha-1) exp(-beta z), z >= 0

  - Exponential noise: The noise values follow an exponential distribution with a parameter of lambda. The PDF of exponential noise is given by:

    p(z) = lambda exp(-lambda z), z >= 0

  - Uniform noise: The noise values follow a uniform distribution with a lower bound of a and an upper bound of b. The PDF of uniform noise is given by:

    p(z) = 1 / (b - a), a <= z <= b

  - Salt-and-pepper noise: The noise values are either 0 (black) or 255 (white) with a probability of p/2 each, and the original image values with a probability of 1-p. The PDF of salt-and-pepper noise is given by:

    p(z) = p/2, z = 0 or 255
    p(z) = 1 - p, 0 < z < 255

  - Speckle noise: The noise values are multiplicative, meaning that they are proportional to the original image values. The noise values follow a Gaussian distribution with a mean of zero and a variance of sigma^2. The PDF of speckle noise is given by:

    p(z) = (1 / sqrt(2 pi sigma^2)) exp(-(z - f)^2 / 2 sigma^2)

- Different noise models have different effects on the image quality and require different restoration techniques. Some of the common restoration methods are inverse filtering, Wiener filtering, constrained least squares filtering, maximum likelihood estimation, maximum a posteriori estimation, etc. .
- Image restoration is an important and challenging task in image processing, as it can improve the visual quality and usability of the images for various applications such as medical imaging, remote sensing, astronomy, etc. .