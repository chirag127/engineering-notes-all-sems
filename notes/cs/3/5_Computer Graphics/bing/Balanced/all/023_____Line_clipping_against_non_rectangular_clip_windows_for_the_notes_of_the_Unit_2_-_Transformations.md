# Line clipping against non rectangular clip windows

- Line clipping is the process of removing the portions of a line that lie outside a given region of interest, such as a window or a viewport.
- Line clipping algorithms can be classified into two categories: rectangular and non-rectangular.
- Rectangular line clipping algorithms, such as Cohen-Sutherland and Liang-Barsky, are efficient and simple, but they can only handle rectangular windows.
- Non-rectangular line clipping algorithms, such as Cyrus-Beck and Sutherland-Hodgman, can handle arbitrary convex or concave polygons as windows, but they are more complex and require more computations.

## Cyrus-Beck Algorithm

- Cyrus-Beck is a line clipping algorithm that is made for convex polygons. It allows line clipping for non-rectangular windows, unlike Cohen-Sutherland or Nicholl Le Nicholl. It also removes the repeated clipping needed in Cohen-Sutherland.
- The algorithm works as follows:

  1. Define the convex area of interest by a set of coordinates given in a clockwise fashion.
  2. Assign a normal vector to each edge of the polygon, pointing outward from the polygon.
  3. For each line to be clipped, calculate the parameter t for each intersection point with the polygon edges, using the formula:

     `t = (P - Pe) . n / D . n`

     where P is any point on the line, Pe is any point on the edge, n is the normal vector of the edge, D is the direction vector of the line, and . is the dot product operator.
  4. Discard the intersection points with t < 0 or t > 1, as they lie outside the line segment.
  5. Discard the intersection points with D . n > 0, as they lie on the wrong side of the edge (inside the polygon).
  6. Sort the remaining intersection points by increasing values of t.
  7. The visible portion of the line is between the first and the last intersection points in the sorted list.

- The algorithm can be extended to handle concave polygons by using the parity rule: a point is inside the polygon if it crosses an odd number of edges to reach infinity.

## Sutherland-Hodgman Algorithm

- Sutherland-Hodgman is a polygon clipping algorithm that can handle any polygon as a window, convex or concave. It clips a polygon against each edge of the window polygon, one at a time, and outputs a new polygon that is inside the window.
- The algorithm works as follows:

  1. Define the window polygon by a set of coordinates given in a clockwise fashion.
  2. Assign a normal vector to each edge of the window polygon, pointing inward from the window.
  3. For each edge of the window polygon, do the following:
     - Initialize an empty list of output vertices.
     - For each edge of the polygon to be clipped, do the following:
       - Let S and P be the start and end points of the edge, respectively.
       - If S is inside the window edge, add S to the output list.
       - If S and P are on opposite sides of the window edge, add the intersection point of the edge and the window edge to the output list.
     - Replace the polygon to be clipped with the output list of vertices.
  4. The final output list of vertices is the clipped polygon.

- The algorithm can be modified to handle non-simple polygons (with self-intersections) by using the even-odd rule: a point is inside the polygon if it crosses an even number of edges to reach infinity.