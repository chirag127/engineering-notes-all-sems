# Matrix representations and homogeneous coordinates

- Matrix representations are a convenient way to express geometric transformations such as translation, rotation, scaling, and projection in computer graphics.
- A matrix can be multiplied by a vector to obtain a transformed vector, or by another matrix to obtain a composed transformation.
- Homogeneous coordinates are a way to extend the normal Cartesian coordinates with an extra dimension, usually denoted by w, to allow affine and projective transformations to be represented by matrices.
- Homogeneous coordinates have the property that any multiple of a coordinate vector represents the same point, as long as w is not zero. For example, (x, y, 1) and (2x, 2y, 2) are equivalent in homogeneous coordinates.
- To convert from homogeneous coordinates to Cartesian coordinates, we divide by w. For example, (2x, 2y, 2) becomes (x, y) in Cartesian coordinates.
- To convert from Cartesian coordinates to homogeneous coordinates, we append a 1 as the w component. For example, (x, y) becomes (x, y, 1) in homogeneous coordinates.
- Homogeneous coordinates are useful in computer graphics because they allow us to represent translation, rotation, scaling, and projection as matrix operations, and to compose them easily by matrix multiplication.
- For example, the matrix representation for translation by (tx, ty) in homogeneous coordinates is:

| 1  0  tx |
| 0  1  ty |
| 0  0  1  |

- To translate a point (x, y, 1) by (tx, ty), we multiply it by the translation matrix:

| 1  0  tx |   | x |   | x + tx |
| 0  1  ty | * | y | = | y + ty |
| 0  0  1  |   | 1 |   |   1    |

- The result is still a homogeneous coordinate, which can be converted back to Cartesian coordinates by dividing by w (which is 1 in this case).
- Similarly, the matrix representation for rotation by an angle theta in homogeneous coordinates is:

| cos(theta)  -sin(theta)  0 |
| sin(theta)   cos(theta)  0 |
|     0            0       1 |

- To rotate a point (x, y, 1) by an angle theta, we multiply it by the rotation matrix:

| cos(theta)  -sin(theta)  0 |   | x |   | x cos(theta) - y sin(theta) |
| sin(theta)   cos(theta)  0 | * | y | = | x sin(theta) + y cos(theta) |
|     0            0       1 |   | 1 |   |             1               |

- The result is still a homogeneous coordinate, which can be converted back to Cartesian coordinates by dividing by w (which is 1 in this case).
- Similarly, the matrix representation for scaling by (sx, sy) in homogeneous coordinates is:

| sx  0  0 |
| 0  sy  0 |
| 0  0   1 |

- To scale a point (x, y, 1) by (sx, sy), we multiply it by the scaling matrix:

| sx  0  0 |   | x |   | sx x |
| 0  sy  0 | * | y | = | sy y |
| 0  0   1 |   | 1 |   |  1   |

- The result is still a homogeneous coordinate, which can be converted back to Cartesian coordinates by dividing by w (which is 1 in this case).
- Finally, the matrix representation for projection onto a plane with normal vector (a, b, c) and distance d from the origin in homogeneous coordinates is:

| a^2 + b^2  -a c  -a d |
| -a c  c^2 + b^2  -c d |
| -a d  -c d  a^2 + c^2 |

- To project a point (x, y, z, 1) onto the plane, we multiply it by the projection matrix:

| a^2 + b^2  -a c  -a d |   | x |   | (a^2 + b^2) x - a c z - a d |
| -a c  c^2 + b^2