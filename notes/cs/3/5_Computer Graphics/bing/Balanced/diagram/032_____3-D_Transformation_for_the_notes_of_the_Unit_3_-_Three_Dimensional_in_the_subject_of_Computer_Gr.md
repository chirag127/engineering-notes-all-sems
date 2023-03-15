### 3-D Transformation

- In computer graphics, transformation is a process of modifying and re-positioning the existing graphics.
- 3-D transformation takes place in a three dimensional plane, where each point is represented by a triplet of coordinates (x, y, z).
- 3-D transformation can be classified into two types: affine and non-affine.
- Affine transformations preserve parallelism, ratios of distances, and angles between lines. They include translation, scaling, rotation, and shear.
- Non-affine transformations do not preserve these properties. They include perspective and curved transformations.
- 3-D transformation can be performed using matrices, which are convenient for combining multiple transformations into one.
- A 3-D transformation matrix is a 4x4 matrix that operates on a 4D homogeneous coordinate vector, where the last coordinate is 1.
- The general form of a 3-D transformation matrix is:

| a | b | c | d |
|---|---|---|---|
| e | f | g | h |
| i | j | k | l |
| 0 | 0 | 0 | 1 |

- The matrix can be decomposed into three parts: a 3x3 linear transformation matrix, a 1x3 translation vector, and a 1x3 perspective vector.
- The linear transformation matrix can be further decomposed into a product of three basic rotation matrices, one for each axis of rotation.
- The basic rotation matrices are:

| 1 | 0 | 0 | 0 |
|---|---|---|---|
| 0 | cos(theta) | -sin(theta) | 0 |
| 0 | sin(theta) | cos(theta) | 0 |
| 0 | 0 | 0 | 1 |

for rotation about x-axis by angle theta,

| cos(phi) | 0 | sin(phi) | 0 |
|---|---|---|---|
| 0 | 1 | 0 | 0 |
| -sin(phi) | 0 | cos(phi) | 0 |
| 0 | 0 | 0 | 1 |

for rotation about y-axis by angle phi,

| cos(psi) | -sin(psi) | 0 | 0 |
|---|---|---|---|
| sin(psi) | cos(psi) | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 0 | 0 | 1 |

for rotation about z-axis by angle psi.

- The translation vector specifies the displacement of the origin of the coordinate system.
- The perspective vector specifies the perspective distortion of the coordinate system.
- To apply a 3-D transformation matrix to a point, we multiply the matrix by the point's homogeneous coordinate vector and divide the result by the last coordinate.
- For example, to translate a point (x, y, z) by a vector (tx, ty, tz), we use the matrix:

| 1 | 0 | 0 | tx |
|---|---|---|---|
| 0 | 1 | 0 | ty |
| 0 | 0 | 1 | tz |
| 0 | 0 | 0 | 1 |

and multiply it by the vector:

| x |
|---|
| y |
| z |
| 1 |

to get the vector:

| x + tx |
|---|
| y + ty |
| z + tz |
| 1 |

which represents the translated point.

- To combine multiple 3-D transformations, we multiply the corresponding matrices in the reverse order of the transformations.
- For example, to rotate a point (x, y, z) about the z-axis by angle psi, then translate it by a vector (tx, ty, tz), we use the matrix:

| cos(psi) | -sin(psi) | 0 | tx |
|---|---|---|---|
| sin(psi) | cos(psi) | 0 | ty |
| 0 | 0 | 1 | tz |
| 0 | 0 | 0 | 1 |

which is the product of the translation matrix and the rotation matrix.