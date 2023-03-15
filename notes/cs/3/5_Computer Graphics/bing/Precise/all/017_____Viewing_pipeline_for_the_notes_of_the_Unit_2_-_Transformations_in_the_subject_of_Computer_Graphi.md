### Viewing pipeline for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

The viewing pipeline is a sequence of steps that are used to transform the 3D world coordinates of an object into 2D screen coordinates. The steps in the viewing pipeline are as follows:

1. **Modeling Transformation**: This step involves transforming the object from its own local coordinate system to the world coordinate system. This is done using modeling transformations such as translation, rotation, and scaling.

2. **Viewing Transformation**: This step involves transforming the world coordinates of the object to the camera or eye coordinate system. This is done using viewing transformations such as the look-at transformation.

3. **Projection Transformation**: This step involves transforming the camera coordinates of the object to normalized device coordinates. This is done using projection transformations such as perspective or orthographic projection.

4. **Viewport Transformation**: This step involves transforming the normalized device coordinates of the object to screen coordinates. This is done using the viewport transformation.

Each of these steps involves the use of transformation matrices to perform the necessary transformations. The final result is a 2D representation of the 3D object on the screen.