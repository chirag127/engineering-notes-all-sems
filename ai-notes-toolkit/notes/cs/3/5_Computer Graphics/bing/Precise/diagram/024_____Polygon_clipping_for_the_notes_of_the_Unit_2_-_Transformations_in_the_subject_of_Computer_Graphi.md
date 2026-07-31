### Polygon Clipping

Polygon clipping is the process of removing portions of a polygon that lie outside a clipping region. This is a fundamental operation in computer graphics, as it allows us to display only the visible portions of a polygon on the screen.

There are several algorithms for polygon clipping, including the Sutherland-Hodgman algorithm and the Weiler-Atherton algorithm. These algorithms work by intersecting the polygon with the clipping region and constructing a new polygon from the resulting points.

Some key points to remember about polygon clipping are:

1. The clipping region is typically defined by a rectangle, known as the clipping window.
2. The resulting polygon may have more vertices than the original polygon.
3. The resulting polygon may be disjoint, meaning it consists of multiple separate polygons.
4. The order of the vertices in the resulting polygon may be different from the order in the original polygon.

Polygon clipping is an important topic in the study of computer graphics and is covered in Unit 2 - Transformations. It is essential to understand the concepts and algorithms involved in polygon clipping in order to effectively manipulate and display graphical objects on the screen.