# Basic Transformation for the Notes of the Unit 2 - Transformations in the Subject of Computer Graphics

- Transformations are operations that change the position, size, orientation, or shape of an object on a 2D or 3D plane.
- Transformations are useful for repositioning and resizing graphics on the screen, as well as for creating animations and effects.
- There are three basic types of transformations: translation, rotation, and scaling.
- Translation is the movement of an object from one location to another by adding a constant vector to its coordinates.
- Rotation is the change of orientation of an object around a fixed point or axis by a certain angle.
- Scaling is the change of size of an object by multiplying its coordinates by a constant factor.
- Transformations can be represented by matrices that can be multiplied with the coordinates of the object to obtain the transformed coordinates.
- The matrix for translation is:

| 1 0 tx |
| 0 1 ty |
| 0 0 1  |

where tx and ty are the translation factors along the x and y axes.

- The matrix for rotation is:

| cosθ -sinθ 0 |
| sinθ cosθ 0 |
| 0 0 1 |

where θ is the angle of rotation in the counterclockwise direction.

- The matrix for scaling is:

| sx 0 0 |
| 0 sy 0 |
| 0 0 1 |

where sx and sy are the scaling factors along the x and y axes.

- Transformations can be combined by multiplying the matrices in the order of the desired operations.
- For example, to translate an object by (tx, ty) and then rotate it by θ, the matrix is:

| cosθ -sinθ tx |
| sinθ cosθ ty |
| 0 0 1 |

- Transformations can also be applied to vectors, such as the direction and magnitude of a force or a velocity.
- Transformations can be implemented in computer graphics using various libraries and frameworks, such as OpenGL, which provides functions for translation, rotation, and scaling.