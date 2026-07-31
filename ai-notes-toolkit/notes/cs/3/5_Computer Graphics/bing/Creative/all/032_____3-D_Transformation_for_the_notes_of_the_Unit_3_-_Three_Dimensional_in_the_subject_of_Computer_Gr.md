# 3-D Transformation

- In computer graphics, transformation is a process of modifying and re-positioning the existing graphics.
- 3-D transformation takes place in a three dimensional plane, where each point is represented by a triplet of coordinates (x, y, z).
- 3-D transformation can be used to change the position, size, orientation, shape, etc. of the object.
- 3-D transformation can be classified into two types: affine and non-affine.
  - Affine transformations preserve parallelism, distances, and angles between lines, but not necessarily lengths and areas.
  - Non-affine transformations do not preserve any of these properties.
- Some common 3-D transformations are:
  - Translation: moving the object along a given direction by a given distance.
  - Scaling: changing the size of the object by a given factor along each axis.
  - Rotation: rotating the object around a given axis by a given angle.
  - Shear: slanting the object along a given plane by a given factor.
  - Reflection: mirroring the object across a given plane.
  - Projection: mapping the object from a higher dimensional space to a lower dimensional space.
- 3-D transformation can be represented by a 4x4 matrix, where the last row is always (0, 0, 0, 1).
- 3-D transformation can be performed by multiplying the matrix with the homogeneous coordinates of the point (x, y, z, 1).
- 3-D transformation can be composed by multiplying the matrices of the individual transformations in the desired order.