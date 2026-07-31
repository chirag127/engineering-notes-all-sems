# Boundary Feature Descriptors

- Boundary feature descriptors are methods that extract and represent the shape information of an object based on its boundary or contour.
- Boundary feature descriptors can be classified into two types: global and local.
  - Global descriptors use the whole boundary of the object to compute a single feature vector that characterizes the shape of the object. Examples of global descriptors are Fourier descriptors, moment invariants, and shape context.
  - Local descriptors use a part of the boundary of the object to compute a feature vector that characterizes the local shape of the object. Examples of local descriptors are curvature, corner, and edge detectors.
- Boundary feature descriptors are useful for shape analysis and measurement, such as object recognition, classification, segmentation, and retrieval .
- Boundary feature descriptors have some advantages and disadvantages compared to region feature descriptors, which use the interior pixels of the object to extract shape information.
  - Advantages: boundary feature descriptors are more compact, less sensitive to noise and occlusion, and more invariant to translation, rotation, and scaling.
  - Disadvantages: boundary feature descriptors are more sensitive to boundary segmentation errors, shape deformation, and articulation.