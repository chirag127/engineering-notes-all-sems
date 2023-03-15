### Liang Barsky algorithm

- The Liang Barsky algorithm is a line clipping algorithm that is used to determine which portion of a line should be drawn inside a given rectangular clipping window .
- The algorithm is more efficient than the Cohen–Sutherland algorithm and can be extended to 3-Dimensional clipping. It is considered to be the faster parametric line-clipping algorithm.
- The algorithm uses the parametric equation of a line and inequalities describing the range of the clipping window to find the intersections between the line and the window  .
- The parametric equation of a line is given by:

    `x = x1 + u * (x2 - x1)`

    `y = y1 + u * (y2 - y1)`

    where `(x1, y1)` and `(x2, y2)` are the end points of the line and `u` is a parameter that varies from 0 to 1.
- The inequalities describing the range of the clipping window are given by:

    `xwmin <= x <= xwmax`

    `ywmin <= y <= ywmax`

    where `(xwmin, ywmin)` and `(xwmax, ywmax)` are the lower-left and upper-right corners of the window respectively.
- The algorithm works by finding the values of `u` that satisfy the inequalities for each edge of the window and then taking the maximum of the lower values and the minimum of the upper values as the final values of `u` that define the visible portion of the line .
- The algorithm can be summarized by the following steps:

    1. Initialize `u1 = 0` and `u2 = 1` as the lower and upper values of `u`.
    2. For each edge of the window, calculate the values of `p` and `q` as follows:

        `p = -(x2 - x1)` for the left edge

        `p = (x2 - x1)` for the right edge

        `p = -(y2 - y1)` for the bottom edge

        `p = (y2 - y1)` for the top edge

        `q = x1 - xwmin` for the left edge

        `q = xwmax - x1` for the right edge

        `q = y1 - ywmin` for the bottom edge

        `q = ywmax - y1` for the top edge

    3. For each edge, if `p = 0`, the line is parallel to the edge. If `q < 0`, the line is outside the window and can be rejected. If `q >= 0`, the line is inside or intersects the edge and can be clipped.
    4. For each edge, if `p < 0`, the line intersects the edge from inside to outside. Calculate `r = q / p` and update `u2 = min(u2, r)` as the upper value of `u`.
    5. For each edge, if `p > 0`, the line intersects the edge from outside to inside. Calculate `r = q / p` and update `u1 = max(u1, r)` as the lower value of `u`.
    6. If `u1 > u2`, the line is outside the window and can be rejected. Otherwise, the line is inside or partially inside the window and can be clipped using the values of `u1` and `u2` to find the new end points of the line as follows:

        `x'1 = x1 + u1 * (x2 - x1)`

        `y'1 = y1 + u1 * (y2 - y1)`

        `x'2 = x1 + u2 * (x2 - x1)`

        `y'2 = y1 + u2 * (y2 - y1)`

- The algorithm can be illustrated by the following example:

    ![Liang Barsky example](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Liang-Barsky.svg/1200px-Liang-Barsky.svg.png)

    In this example, the line has end points `(x1, y1) = (50, 50)` and `(x2, y2) = (150,