### Reflections and Shearing - Unit 2: Transformations in Computer Graphics

1. **Reflection** is a type of transformation that produces a mirror image of an object relative to a line or plane of reflection.
2. In 2D graphics, reflection can be achieved by negating the x or y coordinates of the points of the object, depending on the axis of reflection.
3. In 3D graphics, reflection can be achieved by negating one of the x, y, or z coordinates of the points of the object, depending on the plane of reflection.
4. **Shearing** is a type of transformation that distorts the shape of an object by sliding its points along a fixed line or plane.
5. In 2D graphics, shearing can be achieved by adding a constant value to the x or y coordinates of the points of the object, depending on the axis of shearing.
6. In 3D graphics, shearing can be achieved by adding a constant value to one of the x, y, or z coordinates of the points of the object, depending on the plane of shearing.
7. Both reflection and shearing can be represented using transformation matrices.
8. The transformation matrix for reflection is a diagonal matrix with -1 in the position corresponding to the axis or plane of reflection and 1 in the other positions.
9. The transformation matrix for shearing is an identity matrix with the shearing constant in the position corresponding to the axis or plane of shearing.
10. To apply a reflection or shearing transformation to an object, the coordinates of its points are multiplied by the corresponding transformation matrix.
