Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of viewing pipeline for the unit 2 - transformations in the subject of computer graphics.

### Viewing pipeline

- The term viewing pipeline describes a series of transformations, which are passed by geometry data to end up as image data being displayed on a device.
- The 2D viewing pipeline describes this process for 2D data: norm. object- world- viewing- device- device coord.
- The 3D viewing pipeline describes this process for 3D data: norm. object- world- viewing- projection- clipping- norm. device- device coord.
- The viewing pipeline consists of the following stages:

  - **Object representation**: The geometry data of the objects are represented in a normalized object coordinate system, which is independent of the world coordinate system.
  - **Modeling transformation**: The objects are transformed from the normalized object coordinate system to the world coordinate system, which is a common reference frame for all the objects in the scene.
  - **Viewing transformation**: The objects are transformed from the world coordinate system to the viewing coordinate system, which is defined by the position and orientation of the camera or the eye.
  - **Projection transformation**: The objects are transformed from the viewing coordinate system to the projection coordinate system, which is a 2D representation of the 3D scene on a projection plane.
  - **Clipping**: The objects are clipped to the boundaries of the projection plane, which defines the view volume or the region of interest.
  - **Normalization**: The objects are transformed from the projection coordinate system to the normalized device coordinate system, which is a unit square that maps to the device coordinate system.
  - **Viewport transformation**: The objects are transformed from the normalized device coordinate system to the device coordinate system, which is the physical display device such as a monitor or a printer.

- The following diagram illustrates the 2D viewing pipeline:

![2D viewing pipeline](https://i.ytimg.com/vi/gAO83z6D6W0/maxresdefault.jpg)

- The following diagram illustrates the 3D viewing pipeline:

![3D viewing pipeline](https://i.ytimg.com/vi/6-ei6-D4ayA/maxresdefault.jpg)