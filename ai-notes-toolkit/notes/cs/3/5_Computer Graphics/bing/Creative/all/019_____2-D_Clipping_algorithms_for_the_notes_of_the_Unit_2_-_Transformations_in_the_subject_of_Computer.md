# 2-D Clipping Algorithms

- Clipping is the process of removing or hiding the parts of graphics primitives that lie outside a specified region of interest, such as the viewport or the window.
- Clipping is necessary to avoid rendering unnecessary or invisible pixels, to improve the performance and the quality of the graphics output.
- Clipping can be applied to various graphics primitives, such as points, lines, polygons and curves.
- Clipping algorithms are methods to determine which parts of the primitives are inside or outside the clipping region, and how to modify them accordingly.
- There are different types of clipping regions, such as rectangular, circular, polygonal, convex or concave. Each type may require a different clipping algorithm.
- Some of the common 2-D clipping algorithms are:

  - Point clipping: This algorithm checks whether a given point lies inside or outside the clipping region, and discards it if it is outside. This is the simplest form of clipping, and can be done by comparing the coordinates of the point with the boundaries of the clipping region.
  - Line clipping: This algorithm clips a given line segment by finding the intersections of the line with the boundaries of the clipping region, and discarding the parts that are outside. There are several line clipping algorithms, such as Cohen-Sutherland, Liang-Barsky, Cyrus-Beck, Nicholl-Lee-Nicholl, etc. Each algorithm has its own advantages and disadvantages in terms of efficiency, accuracy and complexity   .
  - Polygon clipping: This algorithm clips a given polygon by finding the intersections of the polygon edges with the boundaries of the clipping region, and creating new vertices and edges to form a clipped polygon. There are several polygon clipping algorithms, such as Sutherland-Hodgman, Weiler-Atherton, Greiner-Hormann, etc. Each algorithm has its own advantages and disadvantages in terms of efficiency, accuracy and complexity.
  - Curve clipping: This algorithm clips a given curve by finding the intersections of the curve with the boundaries of the clipping region, and discarding the parts that are outside. There are several curve clipping algorithms, such as Bezier clipping, B-spline clipping, etc. Each algorithm has its own advantages and disadvantages in terms of efficiency, accuracy and complexity.