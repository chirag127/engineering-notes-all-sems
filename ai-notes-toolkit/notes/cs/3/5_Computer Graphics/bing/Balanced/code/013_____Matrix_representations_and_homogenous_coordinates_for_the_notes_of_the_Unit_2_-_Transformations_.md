### Matrix representations and homogenous coordinates for computer graphics

- Matrix representations are a convenient way to express geometric transformations such as translation, rotation, scaling, and projection in a compact and consistent form.
- Matrices can be used to transform vectors in cartesian coordinates by taking them as column vectors and multiplying them by the transformation matrix.
- Homogeneous coordinates are a way to extend the cartesian coordinates by adding an extra dimension, usually denoted by w, to represent points and vectors in a projective space.
- Homogeneous coordinates allow all geometric transformation equations to be represented as matrix multiplication, and also enable the representation of points at infinity and perspective projection.
- Homogeneous coordinates have a range of applications in computer graphics, such as displaying three-dimensional objects on two-dimensional image planes, performing affine and projective transformations, and manipulating curves and surfaces.
- To convert a point (x, y) in cartesian coordinates to a point (x, y, w) in homogeneous coordinates, we can set w to any non-zero value, usually 1. To convert back, we can divide x and y by w.
- To convert a vector (x, y) in cartesian coordinates to a vector (x, y, w) in homogeneous coordinates, we can set w to zero. To convert back, we can ignore w.
- The matrix representation for translation by (tx, ty) in homogeneous coordinates is:

| 1  0  tx |
| 0  1  ty |
| 0  0  1  |

- The matrix representation for scaling by (sx, sy) in homogeneous coordinates is:

| sx 0  0 |
| 0  sy 0 |
| 0  0  1 |

- The matrix representation for rotation by an angle θ in homogeneous coordinates is:

| cosθ -sinθ 0 |
| sinθ cosθ  0 |
| 0    0     1 |

- The matrix representation for projection onto the line y = mx + b in homogeneous coordinates is:

| 1-m^2 2m   -2mb |
| 2m    1-m^2 2b  |
| 0     0     1   |

- The advantage of using homogeneous coordinates is that multiple transformations can be combined into a single matrix by multiplying the individual matrices. For example, to perform a translation followed by a rotation, we can multiply the translation matrix by the rotation matrix.