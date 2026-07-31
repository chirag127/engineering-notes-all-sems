### Fourier Descriptor

- A method used in object recognition and image processing to represent the boundary shape of a segment in an image     .
- Based on the Fourier series of the boundary coordinates of the segment, which can be expressed as complex numbers   .
- The coefficients of the Fourier series are called Fourier descriptors, and they can be used as features to describe the shape of the segment   .
- Fourier descriptors have some desirable properties for shape representation, such as:
  - Invariance to translation, scaling, rotation and starting point by applying appropriate normalization    .
  - Ability to reconstruct the original shape from the descriptors by applying inverse Fourier transform   .
  - Ability to capture both global and local shape information by using different frequency components   .
  - Ability to reduce the dimensionality and noise by selecting a subset of descriptors   .
- Fourier descriptors can be computed as follows:
  - Extract the boundary of the segment and sample it with equal intervals.
  - Represent the boundary as a complex function of the arc length parameter, where the real and imaginary parts are the x and y coordinates of the boundary points.
  - Apply discrete Fourier transform to the complex function to obtain the Fourier descriptors.
  - Normalize the Fourier descriptors to make them invariant to translation, scaling, rotation and starting point.
- An example of Fourier descriptors for a star shape is shown below:

![Fourier descriptors for a star shape](https://docs.opencv.org/3.4/fourier_descriptors.png)