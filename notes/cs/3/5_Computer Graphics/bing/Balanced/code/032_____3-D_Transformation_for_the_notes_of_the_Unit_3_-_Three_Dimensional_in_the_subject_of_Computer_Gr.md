### 3-D Transformation

- In computer graphics, transformation is a process of modifying and re-positioning the existing graphics.
- 3-D transformation takes place in a three dimensional plane, where each point is represented by a triplet of coordinates (x, y, z).
- 3-D transformation can be classified into two types: affine and non-affine.
- Affine transformations preserve parallelism, ratios of distances, and angles between lines. They include translation, scaling, rotation, reflection, and shear.
- Non-affine transformations do not preserve these properties. They include perspective projection, bending, twisting, and warping.
- 3-D transformation can be performed by using a 4x4 matrix, where the last row is (0, 0, 0, 1). This allows for homogeneous coordinates, which enable translation and perspective projection.
- 3-D transformation can be composed by multiplying the matrices of each individual transformation in a specific order. The order of multiplication affects the final result.
- 3-D transformation can be applied to objects, coordinate systems, or viewing parameters. Depending on the context, the transformation can be interpreted as moving the object, changing the coordinate system, or changing the viewpoint.