# Viewing pipeline for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- The viewing pipeline is a series of transformations that convert the geometry data of a scene into the image data that can be displayed on a device .
- The viewing pipeline consists of the following stages:
  - Object coordinates: The coordinates of the vertices and primitives that define the objects in the scene.
  - World coordinates: The coordinates of the objects after applying the modeling transformations, such as translation, rotation, scaling, etc. These transformations position and orient the objects in the global coordinate system of the scene.
  - Viewing coordinates: The coordinates of the objects after applying the viewing transformation, which defines the position and orientation of the camera or the eye. This transformation maps the scene to a view volume, which is a region of space that is visible to the camera.
  - Projection coordinates: The coordinates of the objects after applying the projection transformation, which defines the type of projection to be used, such as parallel or perspective. This transformation maps the view volume to a canonical view volume, which is a standard region of space that is independent of the projection type.
  - Normalized device coordinates: The coordinates of the objects after applying the normalization transformation, which scales and translates the canonical view volume to a unit cube with the origin at the center and the range of [-1, 1] for each axis.
  - Device coordinates: The coordinates of the objects after applying the viewport transformation, which maps the unit cube to the physical device coordinate system, such as the screen or the printer. This transformation defines the size and position of the viewport, which is the region of the device where the image is displayed.
- The following diagram illustrates the viewing pipeline for 2D graphics :

![2D viewing pipeline](https://i.imgur.com/0wz1j0y.png)

- The following diagram illustrates the viewing pipeline for 3D graphics:

![3D viewing pipeline](https://i.imgur.com/4J1yj0s.png)

- The viewing pipeline can be implemented using matrices and vectors, which allow for efficient and compact representation and manipulation of the transformations. The final image data can be obtained by multiplying the object coordinates by the composite transformation matrix, which is the product of the individual transformation matrices in the pipeline.