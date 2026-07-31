### Basic transformation for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- Transformations are operations that change the position, size, orientation, or shape of an object on a 2D or 3D plane.
- There are three basic types of transformations: translation, rotation, and scaling.
- Translation is the movement of an object from one location to another without changing its size or orientation. It can be represented by a 2x2 matrix that adds a translation vector to the original coordinates of the object. For example, if the translation vector is (tx, ty), then the translation matrix is:

| 1  0  tx |
| 0  1  ty |
| 0  0  1  |

- Rotation is the change of orientation of an object around a fixed point or axis. It can be represented by a 2x2 matrix that multiplies the original coordinates of the object by a rotation angle. For example, if the rotation angle is θ, then the rotation matrix is:

| cosθ  -sinθ  0 |
| sinθ  cosθ   0 |
| 0     0      1 |

- Scaling is the change of size of an object by a scaling factor. It can be represented by a 2x2 matrix that multiplies the original coordinates of the object by a scaling factor. For example, if the scaling factor is (sx, sy), then the scaling matrix is:

| sx  0  0 |
| 0  sy  0 |
| 0  0   1 |

- These basic transformations can be combined to form more complex transformations, such as reflection, shear, and dilation. They can also be applied to 3D objects by using 3x3 or 4x4 matrices.