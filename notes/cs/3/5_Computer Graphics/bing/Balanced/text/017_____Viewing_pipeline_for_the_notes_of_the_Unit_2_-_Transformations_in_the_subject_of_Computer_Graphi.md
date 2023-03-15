### Viewing pipeline for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- The term **viewing pipeline** describes a series of transformations, which are passed by geometry data to end up as image data being displayed on a device .
- The 2D viewing pipeline describes this process for 2D data: norm. object- world- viewing- device- device coord.
- The 3D viewing pipeline describes this process for 3D data: norm. object- world- viewing- projection- clipping- device- device coord.
- The viewing pipeline consists of the following stages   :
  - **Normalization**: The object coordinates are transformed into a standard coordinate system, called the normalized device coordinate (NDC) system, which is independent of the device resolution and aspect ratio.
  - **World transformation**: The NDC coordinates are transformed into the world coordinate system, which represents the position and orientation of the objects in the scene relative to a common origin.
  - **Viewing transformation**: The world coordinates are transformed into the viewing coordinate system, which represents the position and orientation of the camera (or the eye) relative to the scene.
  - **Projection transformation**: The viewing coordinates are transformed into the projection coordinate system, which represents the projection of the scene onto a 2D plane, called the view plane or the near clipping plane. The projection can be either parallel or perspective, depending on the type of camera used.
  - **Clipping**: The projection coordinates are clipped against the boundaries of the view plane and the far clipping plane, which define the visible region of the scene. The clipped coordinates are also divided by the homogeneous coordinate to obtain the normalized projection coordinates.
  - **Device transformation**: The normalized projection coordinates are transformed into the device coordinate system, which represents the pixel coordinates on the display device. The device coordinates are usually integer values that correspond to the physical pixels on the screen.
  - **Device rendering**: The device coordinates are used to draw the pixels on the screen, using various techniques such as rasterization, shading, texturing, etc.