### 3-D Clipping

- 3-D clipping is the process of removing objects or parts of objects that are outside the viewing volume or the region of interest in a 3-D scene.
- The purpose of 3-D clipping is to reduce the computational effort and improve the rendering performance by discarding invisible or irrelevant objects .
- 3-D clipping can be done in two basic steps:
  - Discard objects that cannot be viewed, such as objects that are behind the camera, outside the field of view, or too far away.
  - Clip objects that intersect with any clipping plane, such as the near and far planes, or the left, right, top and bottom planes of the viewing volume.
- 3-D clipping can be done before or after projection, depending on the coordinate system and the clipping algorithm used .
- 3-D clipping algorithms can be classified into two categories:
  - Point clipping: clipping a single point against a clipping region, such as a cube or a sphere.
  - Polygon clipping: clipping a polygon, such as a triangle or a quadrilateral, against a clipping region, such as a pyramid or a frustum.
- Some common 3-D clipping algorithms are  :
  - Cohen-Sutherland algorithm: a point clipping algorithm that uses outcodes to determine the position of a point relative to a clipping region.
  - Liang-Barsky algorithm: a line clipping algorithm that uses parametric equations to find the intersection points of a line segment with a clipping region.
  - Sutherland-Hodgman algorithm: a polygon clipping algorithm that uses a series of 2-D clipping operations to clip a polygon against a convex clipping region.
  - Cyrus-Beck algorithm: a line clipping algorithm that uses normal vectors to find the intersection points of a line segment with a convex clipping region.
  - Weiler-Atherton algorithm: a polygon clipping algorithm that uses a doubly-linked list to store the vertices of a polygon and clip it against a convex or concave clipping region.