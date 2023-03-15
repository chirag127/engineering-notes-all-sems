### Liang Barsky algorithm

- The Liang Barsky algorithm is a line clipping algorithm that is used to determine which portion of a line should be drawn inside a given rectangular clipping window .
- The algorithm is more efficient than the Cohen–Sutherland algorithm and can be extended to 3-Dimensional clipping. It is considered to be the faster parametric line-clipping algorithm.
- The algorithm uses the parametric equation of a line and inequalities describing the range of the clipping window to find the intersections between the line and the window  .
- The parametric equation of a line is given by:

    ```
    x = x1 + u * (x2 - x1)
    y = y1 + u * (y2 - y1)
    ```

    where `(x1, y1)` and `(x2, y2)` are the end points of the line and `u` is a parameter that varies from `0` to `1`.
- The inequalities describing the range of the clipping window are given by:

    ```
    xmin <= x <= xmax
    ymin <= y <= ymax
    ```

    where `(xmin, ymin)` and `(xmax, ymax)` are the coordinates of the lower-left and upper-right corners of the window respectively.
- The algorithm works by finding the values of `u` that satisfy the inequalities for each edge of the window and then taking the maximum of the lower values and the minimum of the upper values as the final values of `u` that define the visible portion of the line .
- The algorithm can be summarized as follows:

    1. Initialize `u1 = 0` and `u2 = 1`.
    2. For each edge of the window, calculate the value of `p` and `q` as follows:

        ```
        p = -(x2 - x1) for left edge
        p = (x2 - x1) for right edge
        p = -(y2 - y1) for bottom edge
        p = (y2 - y1) for top edge

        q = x1 - xmin for left edge
        q = xmax - x1 for right edge
        q = y1 - ymin for bottom edge
        q = ymax - y1 for top edge
        ```

    3. If `p = 0` and `q < 0`, the line is parallel to and outside the edge, so reject the line and exit the algorithm.
    4. If `p < 0`, the line intersects the edge from inside to outside, so calculate `u = q / p` and update `u1 = max(u1, u)`.
    5. If `p > 0`, the line intersects the edge from outside to inside, so calculate `u = q / p` and update `u2 = min(u2, u)`.
    6. If `u1 > u2`, the line is outside the window, so reject the line and exit the algorithm.
    7. Otherwise, the line is partially or completely inside the window, so accept the line and clip it using the values of `u1` and `u2` to find the new end points of the line.
- The algorithm can be illustrated by the following diagram:

    ```
    +-----------------+ ymax
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    +-----------------+ ymin
    xmin             xmax
    ```

    Suppose the line has end points `(x1, y1) = (2, 8)` and `(x2, y2) = (12, 2)` and the window has coordinates `(xmin, ymin) = (4, 4)` and `(xmax, ymax) = (10, 10)`. Then the algorithm proceeds as follows:

    1. Initialize `u1 = 0` and `u2 = 1`.
    2. For the left edge, `p = -(x2 - x1) = -10` and `q = x1 - xmin = -2`, so `u = q / p = 0.2` and `u1 = max