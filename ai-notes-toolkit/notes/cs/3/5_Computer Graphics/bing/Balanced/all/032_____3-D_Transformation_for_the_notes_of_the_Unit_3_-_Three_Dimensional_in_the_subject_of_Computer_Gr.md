# 3-D Transformation

- In computer graphics, transformation is a process of modifying and re-positioning the existing graphics.
- 3-D transformation takes place in a three dimensional plane, where each point is represented by a triplet of coordinates (x, y, z).
- 3-D transformation can be classified into two types: affine and non-affine.
- Affine transformations preserve the parallelism and ratios of distances between points, but not the angles or lengths. Examples of affine transformations are translation, scaling, rotation, and shear.
- Non-affine transformations do not preserve any of the properties of the original shape. Examples of non-affine transformations are perspective and distortion.

## Translation
- Translation is the simplest affine transformation that moves every point of a shape by a fixed distance in a given direction.
- Translation can be represented by a 3x3 matrix, where the last row is (0, 0, 1).
- The translation matrix for moving a point (x, y, z) by (tx, ty, tz) is:

| 1 | 0 | 0 | tx |
| 0 | 1 | 0 | ty |
| 0 | 0 | 1 | tz |
| 0 | 0 | 0 | 1  |

- The result of applying the translation matrix to a point (x, y, z, 1) is:

| x + tx |
| y + ty |
| z + tz |
| 1      |

## Scaling
- Scaling is an affine transformation that changes the size of a shape by multiplying the coordinates of each point by a scaling factor.
- Scaling can be represented by a 3x3 matrix, where the last row is (0, 0, 1).
- The scaling matrix for scaling a point (x, y, z) by (sx, sy, sz) is:

| sx | 0  | 0  | 0 |
| 0  | sy | 0  | 0 |
| 0  | 0  | sz | 0 |
| 0  | 0  | 0  | 1 |

- The result of applying the scaling matrix to a point (x, y, z, 1) is:

| sx * x |
| sy * y |
| sz * z |
| 1      |

## Rotation
- Rotation is an affine transformation that rotates a shape around an axis by a given angle.
- Rotation can be represented by a 3x3 matrix, where the last row is (0, 0, 1).
- The rotation matrix for rotating a point (x, y, z) around the x-axis by an angle θ is:

| 1 | 0      | 0       | 0 |
| 0 | cos θ  | -sin θ  | 0 |
| 0 | sin θ  | cos θ   | 0 |
| 0 | 0      | 0       | 1 |

- The rotation matrix for rotating a point (x, y, z) around the y-axis by an angle θ is:

| cos θ  | 0 | sin θ  | 0 |
| 0      | 1 | 0      | 0 |
| -sin θ | 0 | cos θ  | 0 |
| 0      | 0 | 0      | 1 |

- The rotation matrix for rotating a point (x, y, z) around the z-axis by an angle θ is:

| cos θ  | -sin θ | 0 | 0 |
| sin θ  | cos θ  | 0 | 0 |
| 0      | 0      | 1 | 0 |
| 0      | 0      | 0 | 1 |

- The result of applying the rotation matrix to a point (x, y, z, 1) is:

| x * cos θ - y * sin θ |
| x * sin θ + y * cos θ |
| z                     |
| 1                     |

- For rotation around an arbitrary axis, the axis vector needs to be normalized and the rotation matrix can be derived using the Rodrigues' rotation formula.

## Shear
- Shear is an affine transformation that distorts a shape by sliding one plane parallel to another.
- Shear can be represented by a 3x3 matrix, where the last row is (0, 0, 1