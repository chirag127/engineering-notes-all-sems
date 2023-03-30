
### Viewing Pipeline for the Notes of the Unit 2 - Transformations in the Subject of Computer Graphics

1. The viewing pipeline is a sequence of transformations that occur when a 3D object is rendered on a 2D screen.

2. The first step is to transform the 3D object from its model coordinates to the world coordinates. This is done by multiplying the object's vertices with a transformation matrix.

3. The next step is to transform the world coordinates to the camera coordinates. This is done by multiplying the object's vertices with the camera's view matrix.

4. The next step is to transform the camera coordinates to the projection coordinates. This is done by multiplying the object's vertices with the projection matrix.

5. The next step is to transform the projection coordinates to the screen coordinates. This is done by multiplying the object's vertices with the viewport matrix.

6. Finally, the object is rendered on the 2D screen.