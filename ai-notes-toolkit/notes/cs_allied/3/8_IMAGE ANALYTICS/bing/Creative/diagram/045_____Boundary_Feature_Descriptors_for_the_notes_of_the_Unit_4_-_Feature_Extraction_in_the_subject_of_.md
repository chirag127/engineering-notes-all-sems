### Boundary Feature Descriptors

- Boundary feature descriptors are methods that extract and represent the shape information of an object based on its boundary or contour.
- Boundary feature descriptors can be classified into two types: global and local.
- Global boundary feature descriptors use the whole boundary of the object to compute a single feature vector that characterizes the shape of the object. Examples of global boundary feature descriptors are:
  - Fourier descriptors: they use the discrete Fourier transform to convert the boundary points into a frequency domain representation that is invariant to translation, rotation and scaling.
  - Shape signatures: they use a function that maps each boundary point to a scalar value that reflects some property of the shape, such as curvature, distance to the centroid, angle, etc.
  - Shape context: they use a histogram-based representation that captures the relative position and orientation of the boundary points with respect to a reference point.
- Local boundary feature descriptors use a part of the boundary of the object to compute a feature vector that describes the local shape of the object. Examples of local boundary feature descriptors are:
  - Edge descriptors: they use the gradient magnitude and orientation of the boundary pixels to encode the local edge information.
  - Corner detectors: they use the second-order derivatives or the eigenvalues of the structure tensor to detect the points where the boundary has a high curvature or a significant change in direction.
  - Interest point detectors: they use various criteria such as Harris, SIFT, SURF, FAST, etc. to detect the points that are distinctive and invariant to some transformations.
  - Interest region descriptors: they use various methods such as SIFT, SURF, ORB, BRIEF, etc. to extract a feature vector that describes the local appearance of the region around an interest point.