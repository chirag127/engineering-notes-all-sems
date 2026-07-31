# Liang Barsky Algorithm

- The Liang Barsky algorithm is a line clipping algorithm that is used to determine which portion of a line should be drawn inside a given rectangular clipping window.
- The algorithm is based on the parametric equation of a line, which is given by:

  ```
  x = x1 + u * (x2 - x1)
  y = y1 + u * (y2 - y1)
  ```

  where `(x1, y1)` and `(x2, y2)` are the end points of the line, and `u` is a parameter that varies from 0 to 1.
- The algorithm also uses four inequalities that describe the range of the clipping window, which are given by:

  ```
  xwmin <= x <= xwmax
  ywmin <= y <= ywmax
  ```

  where `(xwmin, ywmin)` and `(xwmax, ywmax)` are the lower-left and upper-right corners of the window, respectively.
- The algorithm works by finding the values of `u` that satisfy the four inequalities, and then using the minimum and maximum values of `u` to compute the intersection points of the line and the window.
- The algorithm can be summarized by the following steps:

  1. Initialize `u1 = 0` and `u2 = 1`, which represent the lower and upper bounds of the visible portion of the line.
  2. For each of the four boundaries of the window, calculate the value of `u` that corresponds to the intersection of the line and the boundary, using the following formula:

     ```
     u = (p * q) / (p * r)
     ```

     where `p` and `q` are constants that depend on the boundary and the direction of the line, and `r` is the difference between the end points of the line along the boundary's axis. For example, for the left boundary, `p = x1 - x2`, `q = x1 - xwmin`, and `r = x2 - x1`.
  3. If `p * r < 0`, then the line is entering the window through the boundary. In this case, update `u1 = max(u1, u)`, which means taking the larger value of `u1` and `u`.
  4. If `p * r > 0`, then the line is leaving the window through the boundary. In this case, update `u2 = min(u2, u)`, which means taking the smaller value of `u2` and `u`.
  5. If `p * r = 0`, then the line is parallel to the boundary. In this case, if `q < 0`, then the line is completely outside the window and can be rejected. Otherwise, the line is completely inside the window and can be accepted.
  6. After checking all four boundaries, if `u1 > u2`, then the line is outside the window and can be rejected. Otherwise, the line is inside the window or partially inside the window, and can be accepted.
  7. If the line is accepted, then the visible portion of the line can be drawn by using the values of `u1` and `u2` to calculate the intersection points of the line and the window, using the parametric equation of the line.

- The algorithm is more efficient than the Cohen-Sutherland algorithm, and can be extended to 3-Dimensional clipping. The algorithm is considered to be the faster parametric line-clipping algorithm   .