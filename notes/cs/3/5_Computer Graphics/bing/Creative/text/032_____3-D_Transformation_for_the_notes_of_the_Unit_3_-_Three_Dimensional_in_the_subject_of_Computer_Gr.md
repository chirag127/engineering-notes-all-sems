### 3-D Transformation

- In computer graphics, transformation is a process of modifying and re-positioning the existing graphics.
- 3-D transformation takes place in a three dimensional plane, where each point is represented by a coordinate triplet (x, y, z).
- 3-D transformation can be classified into two types: affine and non-affine.
- Affine transformations preserve the parallelism and ratios of distances between points, but not the angles or lengths. Examples of affine transformations are translation, scaling, rotation, and shear.
- Non-affine transformations do not preserve any of the properties of the original shape. Examples of non-affine transformations are perspective projection, bending, and twisting.
- 3-D transformation can be performed using matrices, which are convenient for combining multiple transformations into one.
- A 3-D transformation matrix is a 4x4 matrix that operates on a 4D homogeneous coordinate vector, where the fourth coordinate is 1 for a point and 0 for a vector.
- The general form of a 3-D transformation matrix is:

| a | b | c | d |
|---|---|---|---|
| e | f | g | h |
| i | j | k | l |
| m | n | o | p |

- The matrix can be decomposed into three parts: a 3x3 linear transformation matrix, a 3x1 translation vector, and a 1x4 perspective vector.
- The linear transformation matrix affects the rotation, scaling, and shear of the shape, while the translation vector affects the position of the shape, and the perspective vector affects the projection of the shape.
- Some common 3-D transformation matrices are:

- Translation by (tx, ty, tz):

| 1 | 0 | 0 | tx |
|---|---|---|----|
| 0 | 1 | 0 | ty |
| 0 | 0 | 1 | tz |
| 0 | 0 | 0 | 1  |

- Scaling by (sx, sy, sz):

| sx | 0  | 0  | 0 |
|----|----|----|---|
| 0  | sy | 0  | 0 |
| 0  | 0  | sz | 0 |
| 0  | 0  | 0  | 1 |

- Rotation about x-axis by angle θ:

| 1 | 0      | 0       | 0 |
|---|--------|---------|---|
| 0 | cos θ  | -sin θ  | 0 |
| 0 | sin θ  | cos θ   | 0 |
| 0 | 0      | 0       | 1 |

- Rotation about y-axis by angle θ:

| cos θ  | 0 | sin θ  | 0 |
|--------|---|--------|---|
| 0      | 1 | 0      | 0 |
| -sin θ | 0 | cos θ  | 0 |
| 0      | 0 | 0      | 1 |

- Rotation about z-axis by angle θ:

| cos θ  | -sin θ | 0 | 0 |
|--------|--------|---|---|
| sin θ  | cos θ  | 0 | 0 |
| 0      | 0      | 1 | 0 |
| 0      | 0      | 0 | 1 |

- Shear along x-axis by factors shx and shy:

| 1  | shx | 0  | 0 |
|----|-----|----|---|
| shy| 1   | 0  | 0 |
| 0  | 0   | 1  | 0 |
| 0  | 0   | 0  | 1 |

- Shear along y-axis by factors shy and shz:

| 1  | 0  | 0  | 0 |
|----|----|----|---|
| 0  | 1  | shy| 0 |
| 0  | shz| 1  | 0 |
| 0  | 0  | 0  | 1 |

- Shear along z-axis by factors shz and shx:

| 1  | 0  | shx| 0 |
|----|----|----|---|
| 0  | 1  | 0  | 0 |
|