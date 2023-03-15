### Polygon clipping for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- Polygon clipping is the process of removing the portions of a polygon that lie outside a given clipping window or region.
- Polygon clipping is used for various purposes in computer graphics, such as:
  - Preventing undesirable effects on the output device when rendering polygons that extend beyond the window boundaries.
  - Performing hidden surface removal and generating high-quality surface details using techniques such as beam tracing.
  - Distributing the objects of a scene to appropriate processors in multiprocessor raytracing systems to improve rendering speeds.
  - Applying two-dimensional transformations such as scaling, rotation, translation, and shearing to polygons.
- Polygon clipping can be performed by different algorithms, such as:
  - Sutherland-Hodgman algorithm: This algorithm clips a polygon against each edge of the clipping window in turn, generating a new polygon as the output. The algorithm uses the concept of inside and outside vertices, and generates new vertices at the intersection points of the polygon edges and the clipping window edges .
  - Weiler-Atherton algorithm: This algorithm clips a polygon against another polygon, generating one or more closed areas as the output. The algorithm uses the concept of entry and exit vertices, and generates new vertices at the intersection points of the polygon edges and the clipping polygon edges.
  - Greiner-Hormann algorithm: This algorithm clips a polygon against another polygon, generating one or more closed areas as the output. The algorithm uses the concept of winding numbers, and marks the vertices of the polygons as inside or outside based on their winding numbers.
- Polygon clipping can be implemented using various data structures, such as:
  - Linked lists: This data structure can store the vertices of the polygons and the clipping window, and allow easy insertion and deletion of new vertices during the clipping process.
  - Doubly connected edge lists: This data structure can store the vertices, edges, and faces of the polygons and the clipping window, and allow easy traversal and manipulation of the polygon boundaries during the clipping process.