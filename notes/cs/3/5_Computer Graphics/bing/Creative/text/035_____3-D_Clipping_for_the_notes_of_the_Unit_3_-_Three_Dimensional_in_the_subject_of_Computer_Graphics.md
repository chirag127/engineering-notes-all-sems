### 3-D Clipping

- 3-D clipping is the process of removing objects or parts of objects that are outside the viewing volume or the region of interest in a 3-D scene.
- The purpose of 3-D clipping is to reduce the computational effort and improve the rendering performance by discarding invisible or irrelevant objects.
- 3-D clipping can be done in two basic steps:
  - Discard objects that cannot be viewed, such as objects that are behind the camera, outside the field of view, or too far away.
  - Clip objects that intersect with any clipping plane, such as the near and far planes, or the left, right, top and bottom planes of the viewing volume.
- 3-D clipping can be done before or after projection, depending on the coordinate system and the clipping algorithm used .
- 3-D clipping algorithms can use various techniques, such as outcodes, parametric equations, homogeneous coordinates, or Sutherland-Hodgman algorithm, to determine the intersection points of the objects with the clipping planes and generate the clipped polygons  .