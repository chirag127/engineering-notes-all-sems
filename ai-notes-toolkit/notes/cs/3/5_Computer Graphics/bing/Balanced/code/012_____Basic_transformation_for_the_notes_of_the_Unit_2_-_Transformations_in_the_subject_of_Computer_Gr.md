### Basic transformation for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- Transformations are operations that change the position, size, orientation, or shape of an object on a 2D or 3D plane.
- There are three basic types of transformations: translation, rotation, and scaling.
- Translation is the movement of an object from one location to another without changing its size or orientation. It can be represented by a 2x2 matrix that adds a translation vector to the original coordinates of the object. For example, the matrix below translates an object by tx units along the x-axis and ty units along the y-axis.

| 1  0  tx |
| 0  1  ty |
| 0  0  1  |

- Rotation is the change of orientation of an object around a fixed point or axis. It can be represented by a 2x2 matrix that multiplies the original coordinates of the object by a rotation angle. For example, the matrix below rotates an object by θ degrees counterclockwise around the origin.

| cosθ  -sinθ  0 |
| sinθ  cosθ   0 |
| 0     0      1 |

- Scaling is the change of size of an object by a scaling factor. It can be represented by a 2x2 matrix that multiplies the original coordinates of the object by a scaling factor. For example, the matrix below scales an object by sx along the x-axis and sy along the y-axis.

| sx  0  0 |
| 0  sy  0 |
| 0  0   1 |

- These basic transformations can be combined to form more complex transformations, such as reflection, shear, and dilation. They can also be applied to different coordinate systems, such as Cartesian, polar, or homogeneous coordinates.
- Transformations play an important role in computer graphics to reposition, resize, or reshape the graphics on the screen and change their perspective or appearance. They are also used for animation, modeling, rendering, and image processing.