### Viewing pipeline for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- The viewing pipeline is a series of transformations that convert geometry data into image data that can be displayed on a device.
- The viewing pipeline consists of the following stages :
  - **Object coordinates**: The coordinates of the vertices and edges of the objects in the scene, defined by the modeler or the programmer.
  - **World coordinates**: The coordinates of the objects after applying the modeling transformation, which positions and orientates the objects in the scene relative to a common origin.
  - **Viewing coordinates**: The coordinates of the objects after applying the viewing transformation, which defines the position and orientation of the camera or the eye relative to the scene.
  - **Projection coordinates**: The coordinates of the objects after applying the projection transformation, which maps the 3D scene onto a 2D plane, either parallel (orthographic) or perspective.
  - **Normalized device coordinates**: The coordinates of the objects after applying the normalization transformation, which scales and translates the projected scene to fit within a unit cube, with the origin at the center and the range of each axis from -1 to 1.
  - **Device coordinates**: The coordinates of the objects after applying the viewport transformation, which maps the normalized device coordinates to the actual pixel coordinates of the display device, such as a monitor or a printer.
- The following diagram illustrates the viewing pipeline for 2D graphics  :

![Viewing pipeline diagram](https://i.imgur.com/3Zl7l0y.png)

- The viewing pipeline can be implemented using matrices and matrix multiplication, which allows for efficient and flexible manipulation of the geometry data.
- The viewing pipeline can also be modified or extended to include additional stages, such as clipping, lighting, shading, rasterization, etc., depending on the requirements and capabilities of the graphics system.