# Fourier Descriptor

- Fourier descriptor is a method used in object recognition and image processing to represent the boundary shape of a segment in an image.
- It is based on the Fourier series, which is a mathematical tool to decompose a periodic function into a sum of simple sinusoidal functions.
- The boundary shape of an image segment can be considered as a periodic function, and the coefficients of the Fourier series can be used as the features to describe the shape.
- Fourier descriptor has some advantages over other shape representation methods, such as:
  - It can be designed to be invariant to scaling, translation, rotation and starting point  , which are common transformations in image processing.
  - It can capture both global and local shape information by using different frequency components of the Fourier series.
  - It can reduce the dimensionality of the shape feature vector by selecting only the most significant coefficients of the Fourier series.
- The basic steps to compute the Fourier descriptor of an image segment are:
  - Extract the boundary pixels of the image segment and store them in a complex vector, where the real and imaginary parts are the x and y coordinates of the pixels.
  - Apply the discrete Fourier transform (DFT) to the complex vector and obtain another complex vector, which contains the Fourier coefficients of the boundary function.
  - Normalize the Fourier coefficients to make them invariant to scaling, translation, rotation and starting point, by using the following formulas:

    - Translation invariance: set the first coefficient to zero.
    - Scale invariance: divide all the coefficients by the absolute value of the second coefficient.
    - Rotation invariance: use only the magnitudes of the coefficients and discard the phases.
    - Starting point invariance: shift the coefficients by a certain amount to align the starting point with the first coefficient.

  - Select a subset of the normalized coefficients as the Fourier descriptor, usually the low-frequency ones, which contain the global shape information.
- The Fourier descriptor can be used for shape-based image retrieval, which is the task of finding images that contain similar shapes to a given query image.
- The similarity between two shapes can be measured by the Euclidean distance between their Fourier descriptors, or by other metrics such as cosine similarity or correlation coefficient.
- The Fourier descriptor can also be used for shape classification, which is the task of assigning a label to an image segment based on its shape.
- The shape label can be determined by using a classifier, such as k-nearest neighbors, support vector machines, neural networks, etc., which are trained on a set of labeled shape examples.