### 3-D Transformation

- In computer graphics, transformation is a process of modifying and re-positioning the existing graphics.
- 3-D transformation takes place in a three dimensional plane, where each point is represented by a triplet of coordinates (x, y, z).
- 3-D transformation can be classified into two types: affine and non-affine.
- Affine transformations preserve the parallelism and ratios of distances between points, but not the angles or lengths. Examples of affine transformations are translation, scaling, rotation, and shear.
- Non-affine transformations do not preserve any of the properties of the original shape. Examples of non-affine transformations are perspective and distortion.
- 3-D transformation can be performed using matrices, which are convenient for combining multiple transformations into one.
- A 3-D transformation matrix is a 4x4 matrix that operates on a 4D homogeneous coordinate vector, where the fourth coordinate is 1 for a point and 0 for a vector.
- The general form of a 3-D transformation matrix is:

| a | b | c | d |
|---|---|---|---|
| e | f | g | h |
| i | j | k | l |
| m | n | o | p |

- The matrix can be decomposed into four parts: a 3x3 linear transformation matrix, a 3x1 translation vector, a 1x3 perspective vector, and a scalar value.
- The linear transformation matrix can be further decomposed into three parts: a rotation matrix, a scaling matrix, and a shear matrix.
- The rotation matrix can be obtained by rotating the coordinate axes around an arbitrary axis by a given angle. The rotation matrix can be expressed as:

| cosθ + u<sub>x</sub><sup>2</sup>(1 - cosθ) | u<sub>x</sub>u<sub>y</sub>(1 - cosθ) - u<sub>z</sub>sinθ | u<sub>x</sub>u<sub>z</sub>(1 - cosθ) + u<sub>y</sub>sinθ |
|---|---|---|
| u<sub>y</sub>u<sub>x</sub>(1 - cosθ) + u<sub>z</sub>sinθ | cosθ + u<sub>y</sub><sup>2</sup>(1 - cosθ) | u<sub>y</sub>u<sub>z</sub>(1 - cosθ) - u<sub>x</sub>sinθ |
| u<sub>z</sub>u<sub>x</sub>(1 - cosθ) - u<sub>y</sub>sinθ | u<sub>z</sub>u<sub>y</sub>(1 - cosθ) + u<sub>x</sub>sinθ | cosθ + u<sub>z</sub><sup>2</sup>(1 - cosθ) |

where θ is the angle of rotation and u<sub>x</sub>, u<sub>y</sub>, u<sub>z</sub> are the components of the unit vector along the axis of rotation.

- The scaling matrix can be obtained by multiplying the coordinate axes by different factors. The scaling matrix can be expressed as:

| s<sub>x</sub> | 0 | 0 |
|---|---|---|
| 0 | s<sub>y</sub> | 0 |
| 0 | 0 | s<sub>z</sub> |

where s<sub>x</sub>, s<sub>y</sub>, s<sub>z</sub> are the scaling factors along the x, y, and z axes respectively.

- The shear matrix can be obtained by shifting the coordinate axes by different amounts. The shear matrix can be expressed as:

| 1 | sh<sub>x</sub>y | sh<sub>x</sub>z |
|---|---|---|
| sh<sub>y</sub>x | 1 | sh<sub>y</sub>z |
| sh<sub>z</sub>x | sh<sub>z</sub>y | 1 |

where sh<sub>x</sub>y, sh<sub>x</sub>z, sh<sub>y</sub>x, sh<sub>y</sub>z, sh<sub>z</sub>x, sh<sub>z</sub>y are the shearing factors along the xy, xz, yx, yz, zx, and zy