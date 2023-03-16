### Boundary Feature Descriptors

Boundary feature descriptors are used to describe the shape of an object in an image by analyzing its boundary or contour. These descriptors can be used to classify objects based on their shape, or to compare the similarity of two shapes. Some common boundary feature descriptors include:

1. **Chain codes:** A chain code is a sequence of numbers that represents the direction of the boundary of an object. The boundary is traced and at each point, the direction of the next point is recorded using a predefined set of directions. This results in a compact representation of the shape of the object.

2. **Fourier descriptors:** Fourier descriptors are used to represent the shape of an object by decomposing its boundary into a weighted sum of trigonometric functions. The coefficients of these functions can be used as features to describe the shape of the object.

3. **Shape context:** Shape context is a descriptor that captures the relative distribution of points on the boundary of an object. It is computed by creating a histogram of the relative positions of points on the boundary, and can be used to compare the similarity of two shapes.

4. **Curvature scale space (CSS):** CSS is a technique used to represent the shape of an object by analyzing its curvature at different scales. The curvature of the boundary is computed at different scales, and the resulting curves are used as features to describe the shape of the object.

These are some of the boundary feature descriptors used in the field of image analytics for feature extraction. They can be used to extract meaningful information from images and can be useful for tasks such as object recognition and classification.