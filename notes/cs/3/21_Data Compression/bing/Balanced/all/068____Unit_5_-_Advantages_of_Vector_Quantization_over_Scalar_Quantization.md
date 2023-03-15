## Unit 5 - Advantages of Vector Quantization over Scalar Quantization

- Vector quantization (VQ) is a technique that compresses data by representing a set of similar vectors by a single representative vector called a codebook vector.
- Scalar quantization (SQ) is a technique that compresses data by representing each scalar value by a discrete level called a quantization level.
- VQ has several advantages over SQ, such as:

  - VQ can achieve higher compression ratios than SQ by exploiting the correlation among the vectors in the data set.
  - VQ can reduce the quantization noise or distortion by minimizing the mean squared error (MSE) between the original and the reconstructed vectors.
  - VQ can adapt to the statistics of the data set by using variable-length codebook vectors and variable-rate encoding schemes.
  - VQ can handle multidimensional data more efficiently than SQ by avoiding the curse of dimensionality, which is the exponential increase in the number of quantization levels required to maintain a given distortion level as the dimensionality increases.
  - VQ can provide better visual quality than SQ for image and video compression by preserving the edges and textures of the original data.