### 2-D Clipping Algorithms

Clipping is the process of removing or hiding the parts of a graphical object that lie outside a specified region of interest, such as the viewport or the window. Clipping is useful for improving the efficiency and the quality of computer graphics rendering.

There are different types of clipping algorithms depending on the type of graphical object and the shape of the clipping region. Some of the common 2-D clipping algorithms are:

- **Point clipping**: This algorithm determines whether a given point lies inside or outside the clipping region, which is usually a rectangular window. A point is inside the window if it satisfies the following conditions:

  - xwmin ≤ x ≤ xwmax
  - ywmin ≤ y ≤ ywmax

  where x and y are the coordinates of the point, and xwmin, xwmax, ywmin, ywmax are the coordinates of the window boundaries.

- **Line clipping**: This algorithm determines which portions of a given line segment are visible or invisible inside the clipping region. There are several line clipping algorithms, such as:

  - **Cohen-Sutherland algorithm**: This algorithm divides the 2-D space into nine regions, of which only the middle part is the visible window. Each region is assigned a 4-bit code, called the outcode, based on the position of the region relative to the window. The algorithm compares the outcodes of the endpoints of the line segment and decides whether the segment is trivially accepted (both endpoints are inside the window), trivially rejected (both endpoints are in the same outside region), or needs further subdivision (one or both endpoints are in different outside regions). The algorithm then clips the line segment against the window boundaries until it is either accepted or rejected.

  - **Liang-Barsky algorithm**: This algorithm uses a parametric form of the line segment equation and four inequalities that define the window boundaries. The algorithm computes the values of the parameter t that correspond to the intersections of the line segment with the window edges. The algorithm then finds the minimum and maximum values of t that lie within the window, and clips the line segment accordingly.

  - **Nicholl-Lee-Nicholl algorithm**: This algorithm is an improvement of the Cohen-Sutherland algorithm that reduces the number of calculations and comparisons. The algorithm uses a 16-bit code, called the region code, for each endpoint of the line segment, which encodes the position and the direction of the endpoint relative to the window. The algorithm then applies a series of logical operations on the region codes to determine the visibility of the line segment.

- **Polygon clipping**: This algorithm determines which parts of a given polygon are visible or invisible inside the clipping region. There are several polygon clipping algorithms, such as:

  - **Sutherland-Hodgman algorithm**: This algorithm clips a polygon against each edge of the clipping window in turn, and generates a new polygon as the output. The algorithm uses a point-to-point method, which means that it processes each vertex of the polygon and decides whether to output it, discard it, or replace it with an intersection point with the window edge.

  - **Weiler-Atherton algorithm**: This algorithm clips a polygon by finding all the intersection points of the polygon edges with the window edges, and then tracing the visible parts of the polygon along the window boundaries. The algorithm uses a point-to-edge method, which means that it processes each intersection point and decides which edge to follow next, either the polygon edge or the window edge.

  - **Greiner-Hormann algorithm**: This algorithm clips a polygon by finding all the intersection points of the polygon edges with the window edges, and then linking them in a circular list. The algorithm then traverses the list and marks each intersection point as an entry or an exit point, depending on the direction of the polygon edge. The algorithm then outputs the visible parts of the polygon by following the entry and exit points.

- **Curve clipping**: This algorithm determines which parts of a given curve, such as a circle, an ellipse, or a spline, are visible or invisible inside the clipping region. There are several curve clipping algorithms, such as:

  - **Midpoint algorithm**: This algorithm clips a circle by using the midpoint of the circle as the center of a square window, and then testing the four quadrants of the window for intersection with the circle. The algorithm uses a symmetry property of the circle to reduce the number of calculations.

  - **Cyrus-Beck algorithm**: This algorithm clips a general