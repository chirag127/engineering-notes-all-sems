### Matrix representations and homogeneous coordinates

- Matrix representations are a convenient way to express geometric transformations such as translation, rotation, scaling, and projection in computer graphics.
- A matrix can be multiplied by a vector to obtain a transformed vector, or by another matrix to obtain a composed transformation.
- Homogeneous coordinates are a way to extend the usual Cartesian coordinates with an extra dimension, such that any point (x, y) can be represented by a triple (xh, yh, h) where h is any non-zero scalar.
- Homogeneous coordinates allow affine transformations and projective transformations to be represented by a single matrix form, which simplifies the computation and implementation of these transformations.
- Homogeneous coordinates also enable the use of perspective division, which is a technique to map a three-dimensional point (x, y, z) to a two-dimensional point (x/z, y/z) on the image plane, simulating the effect of perspective projection.
- Homogeneous coordinates have some applications in computer graphics, such as displaying three-dimensional objects on two-dimensional screens, performing clipping and culling operations, and applying lighting and shading effects.

Some examples of matrix representations and homogeneous coordinates are:

- Translation: To translate a point (x, y) by a vector (tx, ty), we can use the matrix

```
| 1  0  tx |
| 0  1  ty |
| 0  0  1  |
```

and multiply it by the homogeneous coordinate (x, y, 1) to obtain the translated point (x + tx, y + ty, 1).

- Rotation: To rotate a point (x, y) by an angle θ around the origin, we can use the matrix

```
| cosθ  -sinθ  0 |
| sinθ   cosθ  0 |
| 0      0     1 |
```

and multiply it by the homogeneous coordinate (x, y, 1) to obtain the rotated point (x cosθ - y sinθ, x sinθ + y cosθ, 1).

- Scaling: To scale a point (x, y) by a factor sx along the x-axis and sy along the y-axis, we can use the matrix

```
| sx  0  0 |
| 0  sy  0 |
| 0  0   1 |
```

and multiply it by the homogeneous coordinate (x, y, 1) to obtain the scaled point (sx x, sy y, 1).

- Projection: To project a point (x, y, z) onto the image plane at z = d, we can use the matrix

```
| 1  0  0  0 |
| 0  1  0  0 |
| 0  0  1  0 |
| 0  0  1/d 0 |
```

and multiply it by the homogeneous coordinate (x, y, z, 1) to obtain the projected point (x, y, z, z/d). Then, we can apply perspective division by dividing the first three coordinates by the last one, to get the final point (x/z, y/z, 1). This point lies on the image plane and has the same x and y coordinates as the original point, but its depth is normalized to 1.