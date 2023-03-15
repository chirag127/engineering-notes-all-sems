# Viewing pipeline for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- The viewing pipeline is a series of transformations that convert the geometry data of a scene into the image data that can be displayed on a device .
- The viewing pipeline consists of the following stages:
  - Object coordinates: The coordinates of the vertices and primitives that define the objects in the scene.
  - World coordinates: The coordinates of the objects after applying the modeling transformation, which positions and orientates them in the 3D space.
  - Viewing coordinates: The coordinates of the objects after applying the viewing transformation, which defines the position and orientation of the camera or the eye.
  - Projection coordinates: The coordinates of the objects after applying the projection transformation, which maps the 3D scene onto a 2D plane.
  - Normalized device coordinates: The coordinates of the objects after applying the normalization transformation, which scales and translates the projected scene to fit into a unit cube.
  - Device coordinates: The coordinates of the objects after applying the viewport transformation, which maps the normalized device coordinates to the actual device coordinates, such as pixels on a screen.
- The following diagram illustrates the viewing pipeline for 3D graphics:

![Viewing pipeline diagram](https://docs.microsoft.com/en-us/visualstudio/debugger/graphics/graphics-pipeline-stages/_static/graphics-pipeline-stages.png?view=vs-2022)

- The following diagram illustrates the viewing pipeline for 2D graphics :

![Viewing pipeline diagram](https://i.ytimg.com/vi/gAO83z6D6W0/maxresdefault.jpg)

- The viewing pipeline allows the computer graphics system to display complex scenes with different objects, perspectives, and projections on various devices.
- The viewing pipeline also enables the manipulation of the scene by changing the parameters of the transformations, such as the position and orientation of the camera, the type and parameters of the projection, and the size and location of the viewport.