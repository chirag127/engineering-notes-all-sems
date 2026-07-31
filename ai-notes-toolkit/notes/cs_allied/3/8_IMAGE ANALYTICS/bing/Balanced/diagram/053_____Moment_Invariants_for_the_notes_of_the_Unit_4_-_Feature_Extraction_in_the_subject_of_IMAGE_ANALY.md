### Moment Invariants for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Moment invariants are numerical values that are derived from the moments of an image and are invariant to certain geometric transformations, such as translation, scaling and rotation    .
- Moments are scalar quantities that describe the distribution of pixel values or intensities in an image. They can be computed for the whole image or for a region of interest. Moments can be classified into different types, such as geometric moments, central moments, normalized central moments, Zernike moments, Legendre moments, etc .
- Moment invariants are useful for image analysis and pattern recognition, as they can capture the shape and appearance of an object or a region in an image, regardless of its position, size and orientation. Moment invariants can be used as features for image classification, object recognition, shape matching, image retrieval, etc  .
- One of the most widely used sets of moment invariants was proposed by Hu in 1962, based on the normalized central moments of an image. Hu derived seven moment invariants that are invariant to translation, scaling and rotation. They are given by the following expressions   :

```
I1 = n20 + n02
I2 = (n20 - n02)^2 + 4n11^2
I3 = (n30 - 3n12)^2 + (3n21 - n03)^2
I4 = (n30 + n12)^2 + (n21 + n03)^2
I5 = (n30 - 3n12)(n30 + n12)[(n30 + n12)^2 - 3(n21 + n03)^2] + (3n21 - n03)(n21 + n03)[3(n30 + n12)^2 - (n21 + n03)^2]
I6 = (n20 - n02)[(n30 + n12)^2 - (n21 + n03)^2] + 4n11(n30 + n12)(n21 + n03)
I7 = (3n21 - n03)(n30 + n12)[(n30 + n12)^2 - 3(n21 + n03)^2] - (n30 - 3n12)(n21 + n03)[3(n30 + n12)^2 - (n21 + n03)^2]
```

where nij are the normalized central moments of order (i + j) of the image, defined as:

```
nij = eta_ij / eta_00^(1 + (i + j) / 2)
```

and eta_ij are the central moments of order (i + j) of the image, defined as:

```
eta_ij = sum(x, y)[(x - x_bar)^i (y - y_bar)^j f(x, y)]
```

where f(x, y) is the pixel value at (x, y), x_bar and y_bar are the coordinates of the centroid of the image, and the summation is over all the pixels in the image or the region of interest   .

- The seven Hu moment invariants can be computed for any image or region of interest, and can be used as a feature vector to represent the shape and appearance of the image or region. The feature vector can then be compared with other feature vectors using a similarity or distance measure, such as Euclidean distance, cosine similarity, etc. The comparison can be used to classify, recognize, match or retrieve images or regions based on their moment invariants  .
- However, the moment invariants are not perfect, and they may vary slightly over image geometric transformations, especially for discrete images. This is because the moments are strictly invariant for continuous functions, but in practical applications images are discrete. Therefore, some errors may occur when computing the moments and the moment invariants for discrete images. To minimize the fluctuation of moment invariants, some factors should be considered, such as the image resolution, the image size, the image centering, the image rotation angle, the image interpolation method, etc [^4^