### 3-D Clipping

- 3-D clipping is the process of removing objects or parts of objects that are outside the viewing volume or the region of interest in a 3-D scene .
- The main purpose of 3-D clipping is to reduce the computational effort and improve the rendering performance by discarding invisible or irrelevant objects .
- 3-D clipping can be done in two basic steps:
  - Discard objects that cannot be viewed, such as objects that are behind the camera, outside the field of view, or too far away. This can be done by comparing the object's bounding box or sphere against the dimensions of the view volume .
  - Clip objects that intersect with any clipping plane, such as the near and far planes, or the left, right, top and bottom planes of the view volume. This can be done by using algorithms such as Cohen-Sutherland, Liang-Barsky, or Sutherland-Hodgman, which are extensions of the 2-D clipping algorithms  .
- 3-D clipping can be done before or after projection, depending on the coordinate system and the clipping algorithm used .
- 3-D clipping can use outcodes to track the in/out status of each vertex with respect to each clipping plane. An outcode is a binary number that indicates which side of each plane the vertex lies on.
- 3-D clipping can use the following rules to determine the trivial accept, trivial reject, or non-trivial cases for a line segment or a polygon:
  - Trivial accept: both endpoints or all vertices have outcodes of zero, meaning they are inside the view volume.
  - Trivial reject: the bitwise AND of the outcodes of the endpoints or the vertices is non-zero, meaning they are outside the same plane or region.
  - Non-trivial: the bitwise AND of the outcodes is zero, but some outcodes are non-zero, meaning the line segment or the polygon intersects with one or more clipping planes.
- 3-D clipping can use parametric equations to find the intersection points of a line segment or a polygon edge with a clipping plane. For example, if v is a vertex inside the view volume and w is a vertex outside the view volume, then the intersection point r can be found by solving for the parameter λ in the equation r = v + λ (v - w).