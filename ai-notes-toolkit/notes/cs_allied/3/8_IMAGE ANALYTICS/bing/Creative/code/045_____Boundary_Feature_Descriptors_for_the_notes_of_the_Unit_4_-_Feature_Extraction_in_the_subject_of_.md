### Boundary Feature Descriptors

- Boundary feature descriptors are methods that extract and represent the shape information of an object based on its boundary or contour.
- Boundary feature descriptors can be classified into two types: global and local.
- Global boundary feature descriptors use the whole boundary of the object to compute a single feature vector that describes its shape. Examples of global boundary feature descriptors are:
  - Fourier descriptors: transform the boundary points into a frequency domain using the discrete Fourier transform and use the magnitude and phase of the coefficients as features.
  - Moment invariants: compute the moments of the boundary points and use the invariant properties of the moments under translation, rotation and scaling as features.
  - Shape context: compute the relative position and orientation of each boundary point with respect to all other boundary points and use the histogram of these values as features.
- Local boundary feature descriptors use a part of the boundary of the object to compute a feature vector that describes its local shape. Examples of local boundary feature descriptors are:
  - Curvature scale space: compute the curvature of the boundary points at different scales and use the zero-crossing points of the curvature as features.
  - Edge orientation histograms: compute the orientation of the boundary points and use the histogram of these values as features.
  - Scale-invariant feature transform (SIFT): detect and describe the keypoints of the boundary points using the gradient magnitude and orientation at different scales and orientations as features  .