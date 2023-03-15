# Line clipping against non rectangular clip windows

- Line clipping is the process of removing the portions of a line that lie outside a given region of interest, such as a rectangular window or a convex polygon.
- Line clipping algorithms are useful for computer graphics applications, such as rendering, clipping, and visibility testing.
- There are different line clipping algorithms for different types of regions. For rectangular regions, the Cohen-Sutherland algorithm is a popular and efficient method that uses a region code to classify the endpoints of a line and determine whether it is trivially accepted, trivially rejected, or needs further clipping.
- For non-rectangular regions, such as convex polygons, the Cyrus-Beck algorithm is a generalization of the Cohen-Sutherland algorithm that uses a parametric equation of a line and the normal vectors of the polygon edges to find the intersection points and clip the line .
- The Cyrus-Beck algorithm works as follows:
  - Input: A convex polygon defined by a set of coordinates given in a clockwise fashion, and a line segment defined by two endpoints.
  - Output: The clipped line segment, or none if the line is completely outside the polygon.
  - Algorithm:
    - Initialize the parameter t of the line segment as t0 = 0 and t1 = 1.
    - For each edge of the polygon, do the following:
      - Compute the dot product of the normal vector of the edge and the direction vector of the line segment.
      - If the dot product is zero, the line is parallel to the edge and does not intersect it.
      - If the dot product is negative, the line enters the polygon through the edge.
      - If the dot product is positive, the line exits the polygon through the edge.
      - Compute the intersection point of the line and the edge using the parametric equation of the line.
      - Compute the parameter value of the intersection point using the parametric equation of the line.
      - If the dot product is negative, update t0 as the maximum of t0 and the parameter value.
      - If the dot product is positive, update t1 as the minimum of t1 and the parameter value.
    - If t0 > t1, the line is completely outside the polygon and no clipping is done.
    - If t0 <= t1, the line is partially or completely inside the polygon and the clipped line segment is given by the points corresponding to t0 and t1 using the parametric equation of the line.
- The Cyrus-Beck algorithm allows line clipping for non-rectangular windows, unlike Cohen-Sutherland or Nicholl Lee Nicholl. It also removes the repeated clipping needed in Cohen-Sutherland.
- The Cyrus-Beck algorithm is illustrated in the following figure:

![Cyrus-Beck algorithm example](https://media.geeksforgeeks.org/wp-content/uploads/20190813172436/Cyrus-Beck-Algorithm.png)

- The Cyrus-Beck algorithm can be extended to clip lines against non-convex polygons by using a convex decomposition of the polygon and applying the algorithm to each convex sub-polygon.