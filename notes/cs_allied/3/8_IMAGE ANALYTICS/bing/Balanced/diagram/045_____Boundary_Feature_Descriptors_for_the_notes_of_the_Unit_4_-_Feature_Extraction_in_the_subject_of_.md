### Boundary Feature Descriptors

- Boundary feature descriptors are methods that extract and represent the shape information of an object based on its boundary or contour.
- Boundary feature descriptors can be classified into two types: global and local.
- Global boundary feature descriptors use the whole boundary of the object to compute a single feature vector that describes its shape. Examples of global boundary feature descriptors are:
  - Fourier descriptors: transform the boundary points into a frequency domain using the discrete Fourier transform and use the magnitude and phase of the coefficients as features.
  - Shape context: compute a histogram of relative positions of boundary points for each point and use the histograms as features.
  - Moment invariants: compute the moments of the boundary points and use the invariant combinations of the moments as features.
- Local boundary feature descriptors use a part of the boundary of the object to compute a feature vector that describes its local shape. Examples of local boundary feature descriptors are:
  - Curvature scale space: compute the curvature of the boundary points at different scales and use the extrema of the curvature as features.
  - Edge orientation histograms: compute the orientation of the boundary edges and use the histograms of the orientations as features.
  - Differential invariants: compute the derivatives of the boundary points and use the invariant combinations of the derivatives as features.
- Boundary feature descriptors can be used for various applications such as shape recognition, shape matching, shape retrieval, and shape analysis .