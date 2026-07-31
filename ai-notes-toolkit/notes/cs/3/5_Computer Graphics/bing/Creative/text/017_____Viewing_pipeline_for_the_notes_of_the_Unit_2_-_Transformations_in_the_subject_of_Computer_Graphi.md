### Viewing pipeline for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- The viewing pipeline is a series of transformations that map geometric data from the world coordinate system to the device coordinate system, where they can be displayed on a screen or other output device .
- The viewing pipeline consists of the following stages  :
  - **Modeling transformation**: This stage transforms the geometric data from the object coordinate system (the local coordinate system of each object) to the world coordinate system (the global coordinate system of the scene).
  - **Viewing transformation**: This stage transforms the geometric data from the world coordinate system to the viewing coordinate system (the coordinate system of the camera or the eye).
  - **Projection transformation**: This stage transforms the geometric data from the viewing coordinate system to the normalized device coordinate system (a unit cube that represents the view volume).
  - **Viewport transformation**: This stage transforms the geometric data from the normalized device coordinate system to the device coordinate system (the coordinate system of the output device, such as pixels on a screen).
- The viewing pipeline can be applied to both 2D and 3D data, with some differences in the projection and viewport transformations  :
  - For 2D data, the projection transformation is usually a parallel projection that preserves the shape and size of the objects, and the viewport transformation is a scaling and translation that maps the view window (a rectangular region in the viewing coordinate system) to the view port (a rectangular region in the device coordinate system).
  - For 3D data, the projection transformation can be either a parallel projection or a perspective projection that creates a realistic sense of depth and perspective, and the viewport transformation is a scaling, translation and clipping that maps the view volume (a pyramidal or prismatic region in the viewing coordinate system) to the view port.
- The viewing pipeline can be implemented using matrices and matrix multiplication, which allow for easy concatenation and manipulation of the transformations .
- The viewing pipeline is an essential concept in computer graphics, as it enables the creation and display of realistic and interactive scenes and animations .