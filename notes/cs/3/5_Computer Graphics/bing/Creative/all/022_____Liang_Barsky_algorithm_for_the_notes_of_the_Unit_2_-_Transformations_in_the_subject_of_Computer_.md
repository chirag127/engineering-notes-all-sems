# Liang Barsky Algorithm

- The Liang Barsky algorithm is a line clipping algorithm that is used to determine which portion of a line should be drawn inside a given rectangular clipping window .
- The algorithm is more efficient than the Cohen–Sutherland algorithm and can be extended to 3-Dimensional clipping. It is considered to be the faster parametric line-clipping algorithm.
- The algorithm uses the parametric equation of a line and inequalities describing the range of the clipping window to find the intersections between the line and the window  .
- The parametric equation of a line is given by:

    ```
    x = x1 + u * (x2 - x1)
    y = y1 + u * (y2 - y1)
    ```

    where `(x1, y1)` and `(x2, y2)` are the end points of the line and `u` is a parameter that varies from 0 to 1.
- The inequalities describing the range of the clipping window are given by:

    ```
    xmin <= x <= xmax
    ymin <= y <= ymax
    ```

    where `(xmin, ymin)` and `(xmax, ymax)` are the coordinates of the lower-left and upper-right corners of the window respectively.
- The algorithm works by finding the values of `u` that satisfy the inequalities for each edge of the window and then taking the maximum of the lower values and the minimum of the upper values as the final values of `u` that define the visible portion of the line .
- The algorithm can be summarized as follows:

    1. Initialize the lower and upper values of `u` as `u1 = 0` and `u2 = 1`.
    2. For each edge of the window, calculate the values of `p` and `q` as:

        ```
        p = -(x2 - x1) for the left edge
        p = (x2 - x1) for the right edge
        p = -(y2 - y1) for the bottom edge
        p = (y2 - y1) for the top edge

        q = x1 - xmin for the left edge
        q = xmax - x1 for the right edge
        q = y1 - ymin for the bottom edge
        q = ymax - y1 for the top edge
        ```

    3. For each edge, check the following cases:

        - If `p = 0` and `q < 0`, then the line is parallel to and outside the edge, so reject the line and exit the algorithm.
        - If `p < 0`, then the line is entering the window through the edge, so calculate `r = q / p` and update `u1 = max(u1, r)`.
        - If `p > 0`, then the line is leaving the window through the edge, so calculate `r = q / p` and update `u2 = min(u2, r)`.
        - If `p = 0` and `q >= 0`, then the line is parallel to and inside the edge, so do nothing.

    4. After checking all the edges, check the final values of `u1` and `u2`:

        - If `u1 > u2`, then the line is outside the window, so reject the line and exit the algorithm.
        - If `u1 <= u2`, then the line is partially or completely inside the window, so accept the line and calculate the visible end points as:

            ```
            x'1 = x1 + u1 * (x2 - x1)
            y'1 = y1 + u1 * (y2 - y1)
            x'2 = x1 + u2 * (x2 - x1)
            y'2 = y1 + u2 * (y2 - y1)
            ```

- The following diagram illustrates an example of the Liang Barsky algorithm:

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
    ``