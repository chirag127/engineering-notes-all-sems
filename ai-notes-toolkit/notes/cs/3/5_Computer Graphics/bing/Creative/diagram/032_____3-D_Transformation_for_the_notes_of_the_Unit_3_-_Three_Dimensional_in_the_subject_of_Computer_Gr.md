### 3-D Transformation

- In computer graphics, transformation is a process of modifying and re-positioning the existing graphics.
- 3-D transformation takes place in a three dimensional plane, where each point is represented by a triplet of coordinates (x, y, z).
- 3-D transformation can be used to change the position, size, orientation, shape, etc. of the object.
- 3-D transformation can be classified into two types: affine and non-affine.
  - Affine transformations preserve parallelism, ratios of distances, and angles between lines. They include translation, scaling, rotation, and shear.
  - Non-affine transformations do not preserve these properties. They include perspective and curved transformations.
- 3-D transformation can be performed using matrices, which are convenient for combining multiple transformations into one.
- 3-D transformation matrices are 4x4 matrices, where the last row is always (0, 0, 0, 1).
- The general form of a 3-D transformation matrix is:

| a | b | c | d |
|---|---|---|---|
| e | f | g | h |
| i | j | k | l |
| 0 | 0 | 0 | 1 |

- To apply a 3-D transformation to a point (x, y, z), we need to convert it to a 4x1 matrix by adding a 1 as the fourth element, and then multiply it by the 3-D transformation matrix. The result is another 4x1 matrix, where the first three elements are the transformed coordinates and the fourth element is 1.
- For example, to translate a point (x, y, z) by a vector (tx, ty, tz), we can use the following 3-D translation matrix:

| 1 | 0 | 0 | tx |
|---|---|---|----|
| 0 | 1 | 0 | ty |
| 0 | 0 | 1 | tz |
| 0 | 0 | 0 | 1  |

- The multiplication is:

| 1 | 0 | 0 | tx |   | x |   | x + tx |
|---|---|---|----|---|---|---|--------|
| 0 | 1 | 0 | ty | x | y | = | y + ty |
| 0 | 0 | 1 | tz |   | z |   | z + tz |
| 0 | 0 | 0 | 1  |   | 1 |   | 1      |

- Similarly, other 3-D transformations can be represented by different matrices, such as scaling, rotation, and shear.
- 3-D rotation can be performed about any arbitrary axis, which can be specified by a unit vector (u, v, w) and an angle θ. The 3-D rotation matrix for this case is:

| u^2 + (1 - u^2)cosθ | uv(1 - cosθ) - wsinθ | uw(1 - cosθ) + vsinθ | 0 |
|---------------------|----------------------|----------------------|---|
| uv(1 - cosθ) + wsinθ | v^2 + (1 - v^2)cosθ | vw(1 - cosθ) - usinθ | 0 |
| uw(1 - cosθ) - vsinθ | vw(1 - cosθ) + usinθ | w^2 + (1 - w^2)cosθ | 0 |
| 0 | 0 | 0 | 1 |

- 3-D transformations can be combined by multiplying their matrices in the desired order. The order of multiplication matters, as matrix multiplication is not commutative. For example, rotating and then translating is not the same as translating and then rotating.
- 3-D transformations can be used for various purposes, such as modeling, animation, rendering, and viewing. They can create realistic and dynamic effects, such as perspective, lighting, shading, and texture mapping.