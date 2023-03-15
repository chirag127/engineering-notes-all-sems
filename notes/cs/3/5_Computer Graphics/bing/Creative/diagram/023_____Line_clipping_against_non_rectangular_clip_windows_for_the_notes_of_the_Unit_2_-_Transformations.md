### Line clipping against non rectangular clip windows

- Line clipping is the process of removing the portions of a line that lie outside a given region of interest, such as a window or a viewport.
- Line clipping algorithms can be classified into two categories: rectangular and non-rectangular.
- Rectangular line clipping algorithms, such as Cohen-Sutherland and Liang-Barsky, are efficient and simple, but they can only handle rectangular windows.
- Non-rectangular line clipping algorithms, such as Cyrus-Beck and Sutherland-Hodgman, can handle arbitrary convex or concave polygons as windows, but they are more complex and require more computations.
- Non-rectangular line clipping algorithms are based on the concept of parametric representation of a line and the dot product of two vectors.
- A line segment can be represented as `P(t) = P0 + t(P1 - P0)`, where `P0` and `P1` are the endpoints of the line, and `t` is a parameter that varies from 0 to 1.
- A convex polygon can be represented as a set of `n` vertices `V0, V1, ..., Vn-1` and `n` edges `E0, E1, ..., En-1`, where `Ei = Vi - Vi+1` for `i = 0, 1, ..., n-2` and `En-1 = Vn-1 - V0`.
- A line segment intersects an edge of a polygon if and only if the parameter `t` satisfies the following equation:

  `t = (N.Ei) / (D.Ei)`

  where `N = Vi - P0`, `D = P1 - P0`, and `.` denotes the dot product of two vectors.

- A line segment is inside a convex polygon if and only if the parameter `t` satisfies the following inequalities for all `i = 0, 1, ..., n-1`:

  `0 <= t <= 1`
  
  `(N x Ei).(D x Ei) >= 0`

  where `x` denotes the cross product of two vectors.

- A line segment is inside a concave polygon if and only if the parameter `t` satisfies the following inequalities for all `i = 0, 1, ..., n-1`:

  `0 <= t <= 1`
  
  `(N x Ei).(D x Ei) >= 0` if `Ei` is a convex edge
  
  `(N x Ei).(D x Ei) <= 0` if `Ei` is a concave edge

- The Cyrus-Beck algorithm is a non-rectangular line clipping algorithm that works for convex polygons. It computes the values of `t` for all the edges of the polygon, and finds the maximum of the lower values (`tL`) and the minimum of the upper values (`tU`). If `tL <= tU`, then the line segment is partially inside the polygon, and the clipped portion is `P(tL)` to `P(tU)`. If `tL > tU`, then the line segment is completely outside the polygon.
- The Sutherland-Hodgman algorithm is a non-rectangular line clipping algorithm that works for both convex and concave polygons. It clips the line segment against each edge of the polygon in turn, and outputs the portion of the line segment that is inside the half-plane defined by the edge. The algorithm uses the following rules to determine the output:

  - If both endpoints of the line segment are inside the half-plane, output both endpoints.
  - If the first endpoint is inside and the second endpoint is outside, output the first endpoint and the intersection point.
  - If the first endpoint is outside and the second endpoint is inside, output the intersection point and the second endpoint.
  - If both endpoints are outside, output nothing.