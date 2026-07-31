### Matrix representations and homogenous coordinates

- Matrix representations are a convenient way to express geometric transformations such as translation, rotation, scaling and perspective projection in computer graphics.
- Matrix representations allow us to perform multiple transformations in a single operation by multiplying the matrices of each transformation.
- Homogeneous coordinates are a way to extend the normal Cartesian coordinates by adding an extra dimension, usually denoted by w.
- Homogeneous coordinates allow us to represent affine transformations (such as translation) and projective transformations (such as perspective projection) as matrix multiplications, which are not possible in Cartesian coordinates.
- Homogeneous coordinates also allow us to represent points at infinity, which are useful for perspective projection and parallel lines.
- To convert a Cartesian coordinate (x, y) to a homogeneous coordinate, we use the formula (x, y, 1).
- To convert a homogeneous coordinate (x, y, w) to a Cartesian coordinate, we use the formula (x/w, y/w), if w is not zero.
- The matrix representation for translation by (tx, ty) in homogeneous coordinates is:

| 1  0  tx |
| 0  1  ty |
| 0  0  1  |

- The matrix representation for rotation by an angle θ in homogeneous coordinates is:

| cosθ  -sinθ  0 |
| sinθ  cosθ   0 |
| 0     0      1 |

- The matrix representation for scaling by (sx, sy) in homogeneous coordinates is:

| sx  0   0 |
| 0   sy  0 |
| 0   0   1 |

- The matrix representation for perspective projection with a focal length f in homogeneous coordinates is:

| 1  0  0  0 |
| 0  1  0  0 |
| 0  0  1  0 |
| 0  0  1/f 0 |

- To apply a matrix transformation M to a point P in homogeneous coordinates, we multiply them as column vectors: P' = M * P
- To apply a sequence of matrix transformations M1, M2, ..., Mn to a point P in homogeneous coordinates, we multiply them from right to left: P' = Mn * ... * M2 * M1 * P