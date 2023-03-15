### 3-D Transformation

Three-dimensional (3-D) transformations are used to manipulate 3-D objects in computer graphics. These transformations are applied to the coordinates of the object's vertices to change its position, orientation, or size. The most common 3-D transformations are translation, rotation, and scaling.

1. **Translation**: Translation moves an object along a straight line from one position to another. This is achieved by adding a translation vector to the coordinates of each vertex of the object.

2. **Rotation**: Rotation rotates an object around a fixed point, called the center of rotation. This is achieved by multiplying the coordinates of each vertex of the object by a rotation matrix.

3. **Scaling**: Scaling changes the size of an object. This is achieved by multiplying the coordinates of each vertex of the object by a scaling factor.

These transformations can be combined to create more complex transformations, such as reflection, shear, and taper. They can also be applied in sequence to achieve a desired result.

In computer graphics, 3-D transformations are typically represented using 4x4 matrices. These matrices can be multiplied together to combine multiple transformations into a single transformation matrix. This matrix can then be applied to the coordinates of the object's vertices to perform the transformation.