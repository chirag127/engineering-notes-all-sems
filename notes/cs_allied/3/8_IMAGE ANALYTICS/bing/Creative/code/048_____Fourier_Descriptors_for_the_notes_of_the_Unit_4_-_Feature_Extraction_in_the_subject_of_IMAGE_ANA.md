# Fourier Descriptors for Shape-Based Image Retrieval

- Fourier descriptors are a method of representing and comparing the shapes of objects in images .
- Fourier descriptors are derived from the Fourier series of the boundary points of the object.
- Fourier descriptors have the advantages of being invariant to translation, scale, rotation and starting point of the object .
- Fourier descriptors can be computed as follows:
  - Convert the boundary points of the object into a complex signal x(n) = x(n) + iy(n), where x(n) and y(n) are the coordinates of the n-th point.
  - Apply the discrete Fourier transform (DFT) to the complex signal to obtain the Fourier coefficients X(k) = a(k) + ib(k), where k is the frequency index.
  - The Fourier coefficients are the Fourier descriptors of the shape.
  - To make the Fourier descriptors invariant to translation, set X(0) = 0.
  - To make the Fourier descriptors invariant to scale, divide all the coefficients by X(1).
  - To make the Fourier descriptors invariant to rotation, use the magnitude of the coefficients |X(k)|.
  - To make the Fourier descriptors invariant to starting point, use the phase of the coefficients arg(X(k)).
- Fourier descriptors can be used to retrieve images based on shape similarity by computing the distance between the Fourier descriptors of different shapes .
- Fourier descriptors can also be used to reconstruct the shape of the object by applying the inverse DFT to the Fourier coefficients.
- Fourier descriptors are sensitive to noise and boundary irregularities, so smoothing and filtering techniques may be applied to improve the performance .
- Fourier descriptors can capture the global and local features of the shape, but the number of coefficients needed may vary depending on the complexity of the shape .