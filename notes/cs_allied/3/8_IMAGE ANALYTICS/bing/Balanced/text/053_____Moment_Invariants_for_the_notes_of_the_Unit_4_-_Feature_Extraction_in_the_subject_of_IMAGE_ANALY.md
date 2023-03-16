### Moment Invariants for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Moment invariants are numerical values that are derived from the moments of an image and are invariant to certain geometric transformations, such as translation, scaling and rotation  .
- Moment invariants are useful for image analysis and pattern recognition, as they can capture the shape and appearance of an object regardless of its position, size and orientation  .
- Moment invariants can be computed from different types of moments, such as geometric moments, central moments, normalized central moments, Zernike moments, Legendre moments, etc .
- One of the most widely used sets of moment invariants was proposed by Hu in 1962, which consists of seven invariant values derived from the second and third order central moments of an image  .
- Hu's moment invariants are defined as follows:

  - I1 = η20 + η02
  - I2 = (η20 - η02)^2 + 4η11^2
  - I3 = (η30 - 3η12)^2 + (3η21 - η03)^2
  - I4 = (η30 + η12)^2 + (η21 + η03)^2
  - I5 = (η30 - 3η12)(η30 + η12)[(η30 + η12)^2 - 3(η21 + η03)^2] + (3η21 - η03)(η21 + η03)[3(η30 + η12)^2 - (η21 + η03)^2]
  - I6 = (η20 - η02)[(η30 + η12)^2 - (η21 + η03)^2] + 4η11(η30 + η12)(η21 + η03)
  - I7 = (3η21 - η03)(η30 + η12)[(η30 + η12)^2 - 3(η21 + η03)^2] - (η30 - 3η12)(η21 + η03)[3(η30 + η12)^2 - (η21 + η03)^2]

  where ηij are the normalized central moments of the image, defined as:

  - ηij = μij / μ00^(1 + (i + j) / 2)

  and μij are the central moments of the image, defined as:

  - μij = ∑x∑y (x - x̄)^i (y - ȳ)^j f(x, y)

  where f(x, y) is the pixel intensity at (x, y), x̄ and ȳ are the coordinates of the centroid of the image, and μ00 is the area of the image.

- Hu's moment invariants are theoretically invariant to translation, scaling and rotation of the image, but in practice they may vary slightly due to the discretization and quantization of the image pixels .
- To minimize the fluctuation of moment invariants, some factors should be considered, such as the image resolution, the image size, the image centering, the image normalization, the image noise, the moment order, the moment type, etc .
- Moment invariants can be used as features for image classification, recognition, retrieval, segmentation, registration, etc, by comparing the similarity or distance between the moment invariants of different images  .