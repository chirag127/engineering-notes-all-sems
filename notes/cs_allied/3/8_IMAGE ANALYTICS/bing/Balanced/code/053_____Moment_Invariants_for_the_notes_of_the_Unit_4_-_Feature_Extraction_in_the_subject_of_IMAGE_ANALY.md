### Moment Invariants for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Moment invariants are numerical values that are derived from the moments of an image function and are invariant to certain geometric transformations, such as translation, scaling and rotation .
- Moment invariants are useful for image pattern recognition and classification, as they can capture the shape and appearance of an object regardless of its position, size and orientation .
- Moment invariants can be computed from different types of moments, such as geometric moments, central moments, normalized central moments, Zernike moments, Legendre moments, etc .
- One of the most widely used sets of moment invariants was proposed by Hu in 1962, which consists of seven algebraic combinations of the normalized central moments of order up to three .
- Hu's moment invariants are given by the following expressions:

```
I1 = n20 + n02
I2 = (n20 - n02)^2 + 4n11^2
I3 = (n30 - 3n12)^2 + (3n21 - n03)^2
I4 = (n30 + n12)^2 + (n21 + n03)^2
I5 = (n30 - 3n12)(n30 + n12)[(n30 + n12)^2 - 3(n21 + n03)^2] + (3n21 - n03)(n21 + n03)[3(n30 + n12)^2 - (n21 + n03)^2]
I6 = (n20 - n02)[(n30 + n12)^2 - (n21 + n03)^2] + 4n11(n30 + n12)(n21 + n03)
I7 = (3n21 - n03)(n30 + n12)[(n30 + n12)^2 - 3(n21 + n03)^2] - (n30 - 3n12)(n21 + n03)[3(n30 + n12)^2 - (n21 + n03)^2]
```

where nij are the normalized central moments of order (i + j).

- Hu's moment invariants are theoretically invariant for continuous functions, but in practice, they may vary slightly due to the discretization and quantization of digital images .
- To minimize the fluctuation of moment invariants, some factors should be considered, such as the image resolution, the image size, the image center, the image orientation, the image noise, etc .
- Moment invariants can be used as features for various image analysis tasks, such as object recognition, face recognition, character recognition, shape matching, image retrieval, etc  .
- Moment invariants can also be combined with other features, such as texture, color, edge, etc, to improve the performance of image analysis systems .