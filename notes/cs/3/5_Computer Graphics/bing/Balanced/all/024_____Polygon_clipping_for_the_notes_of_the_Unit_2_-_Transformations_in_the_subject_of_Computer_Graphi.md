# Polygon clipping for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- Polygon clipping is the process of removing the portions of a polygon that lie outside a given clipping window or region.
- Polygon clipping is used for various purposes in computer graphics, such as:
  - To prevent undesirable effects when rendering polygons that extend beyond the output device's window.
  - To perform hidden surface removal and generate realistic 3D images by clipping polygons against other polygons or planes.
  - To produce high-quality surface details using techniques such as beam tracing or texture mapping by clipping polygons against light sources or textures.
  - To distribute the objects of a scene to appropriate processors in multiprocessor ray tracing systems to improve rendering speeds by clipping polygons against the processor's boundaries.
- Polygon clipping can be performed by different algorithms, such as:
  - Sutherland-Hodgman algorithm: This algorithm clips a polygon against a convex clipping window by processing each edge of the polygon against each edge of the window in a clockwise order. The output of this algorithm is a sequence of vertices that define the clipped polygon boundaries. This algorithm is simple and efficient, but it can only handle convex clipping windows and it may introduce degenerate cases such as self-intersecting polygons or zero-area polygons.
  - Weiler-Atherton algorithm: This algorithm clips a polygon against a convex or concave clipping window by finding the intersection points between the polygon edges and the window edges, and then tracing the boundary of the clipped polygon by following the intersection points and the original vertices in a clockwise order. The output of this algorithm is a list of polygons that represent the clipped regions. This algorithm can handle concave clipping windows and it preserves the original topology of the polygon, but it is more complex and requires more memory and computation than the Sutherland-Hodgman algorithm.
  - Greiner-Hormann algorithm: This algorithm clips a polygon against a convex or concave clipping window by finding the intersection points between the polygon edges and the window edges, and then marking the entry and exit points of the polygon with respect to the window. The output of this algorithm is a list of polygons that represent the clipped regions. This algorithm can handle concave clipping windows and it is faster and simpler than the Weiler-Atherton algorithm, but it may produce incorrect results for self-intersecting polygons or polygons with holes.
- Polygon clipping can be illustrated by the following diagrams:

  - Sutherland-Hodgman algorithm:

  ```
  +---------------------+
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  +---------------------+

  +---------------------+
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |   +-----------+     |
  |   |           |     |
  |   |           |     |
  |   |           |     |
  +---+-----------+-----+

  +---------------------+
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |   +-----------+     |
  |   |           |     |
  |   |           |     |
  |   |           |     |
  |   +-----------+     |
  +---------------------+
  ```

  - Weiler-Atherton algorithm:

  ```
  +---------------------+
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  +---------------------+

  +---------------------+
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |   +-----+   +---+   |
  |   |     |   |   |   |
  |   |     +---+   |   |
  |   |             |   |
  |   +-------------+   |
  +---------------------+

  +---------------------+
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |   +-----+   +---