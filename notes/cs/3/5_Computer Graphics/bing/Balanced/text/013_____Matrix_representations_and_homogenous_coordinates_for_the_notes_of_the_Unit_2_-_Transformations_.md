### Matrix representations and homogeneous coordinates

- Matrix representations are a convenient way to express geometric transformations such as translation, rotation, scaling, and projection in computer graphics.
- A matrix can be multiplied by a vector to obtain a transformed vector, or by another matrix to obtain a composed transformation.
- Homogeneous coordinates are a way to extend the normal Cartesian coordinates with an extra dimension, usually denoted by w, to allow affine and projective transformations to be represented by matrices.
- Homogeneous coordinates have the property that any multiple of a coordinate vector represents the same point, as long as w is not zero. For example, (x, y, 1) and (2x, 2y, 2) are equivalent in homogeneous coordinates.
- To convert from homogeneous coordinates to Cartesian coordinates, we divide by w. For example, (2x, 2y, 2) becomes (x, y) in Cartesian coordinates.
- To convert from Cartesian coordinates to homogeneous coordinates, we append a 1 as the w component. For example, (x, y) becomes (x, y, 1) in homogeneous coordinates.
- Homogeneous coordinates are useful in computer graphics because they allow us to represent translation, rotation, scaling, and projection as matrix operations, and to compose them easily.
- For example, the matrix representation for translation by (tx, ty) in homogeneous coordinates is:

| 1  0  tx |
| 0  1  ty |
| 0  0  1  |

- To translate a point (x, y, 1) by (tx, ty), we multiply it by the translation matrix:

| 1  0  tx |   | x |   | x + tx |
| 0  1  ty | x | y | = | y + ty |
| 0  0  1  |   | 1 |   |   1    |

- The result is still a homogeneous coordinate, which can be converted back to Cartesian coordinates by dividing by 1.
- Similarly, the matrix representation for rotation by an angle θ in homogeneous coordinates is:

| cosθ  -sinθ  0 |
| sinθ   cosθ  0 |
|  0      0    1 |

- To rotate a point (x, y, 1) by an angle θ, we multiply it by the rotation matrix:

| cosθ  -sinθ  0 |   | x |   | x cosθ - y sinθ |
| sinθ   cosθ  0 | x | y | = | x sinθ + y cosθ |
|  0      0    1 |   | 1 |   |       1         |

- The result is still a homogeneous coordinate, which can be converted back to Cartesian coordinates by dividing by 1.
- Similarly, the matrix representation for scaling by a factor s in homogeneous coordinates is:

| s  0  0 |
| 0  s  0 |
| 0  0  1 |

- To scale a point (x, y, 1) by a factor s, we multiply it by the scaling matrix:

| s  0  0 |   | x |   | sx |
| 0  s  0 | x | y | = | sy |
| 0  0  1 |   | 1 |   |  1 |

- The result is still a homogeneous coordinate, which can be converted back to Cartesian coordinates by dividing by 1.
- Finally, the matrix representation for projection onto a plane z = d in homogeneous coordinates is:

| 1  0  0  0 |
| 0  1  0  0 |
| 0  0  0  0 |
| 0  0  1/d 1 |

- To project a point (x, y, z, 1) onto the plane z = d, we multiply it by the projection matrix:

| 1  0  0  0 |   | x |   |  x  |
| 0  1  0  0 | x | y | = |  y  |
| 0  0  0  0 |   | z |   |  0  |
| 0  0  1/d 1 |   | 1 |   | z/d |

- The result is a homogeneous coordinate, which