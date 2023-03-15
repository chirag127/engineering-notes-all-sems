# 2-D Clipping Algorithms

- Clipping is the process of removing parts of graphics primitives that lie outside a specified region, called the clipping boundary or the clipping window .
- Clipping is useful for optimizing the rendering performance, avoiding unnecessary calculations for invisible objects, and improving the visual quality by removing unwanted artifacts.
- In 2-D, the clipping process can be applied to a variety of graphics primitives such as points, lines, polygons and curves.
- The clipping boundary can be a convex or a concave polygon, or a simple rectangle.
- There are different algorithms for clipping different types of primitives, such as:
  - Point clipping: This algorithm checks whether a given point lies inside or outside the clipping boundary, and discards the point if it is outside .
  - Line clipping: This algorithm finds the intersection points of a given line segment with the clipping boundary, and retains only the part of the line that lies inside the boundary. Some examples of line clipping algorithms are Cohen-Sutherland algorithm, Liang-Barsky algorithm, and Cyrus-Beck algorithm.
  - Polygon clipping: This algorithm clips a given polygon against the clipping boundary, and produces a new polygon or a set of polygons that lie inside the boundary. Some examples of polygon clipping algorithms are Sutherland-Hodgman algorithm, Weiler-Atherton algorithm, and Greiner-Hormann algorithm.
  - Curve clipping: This algorithm clips a given curve, such as a Bézier curve or a B-spline curve, against the clipping boundary, and produces a new curve or a set of curves that lie inside the boundary. Some examples of curve clipping algorithms are Cohen-Sutherland algorithm for parametric curves, and de Casteljau algorithm for Bézier curves.