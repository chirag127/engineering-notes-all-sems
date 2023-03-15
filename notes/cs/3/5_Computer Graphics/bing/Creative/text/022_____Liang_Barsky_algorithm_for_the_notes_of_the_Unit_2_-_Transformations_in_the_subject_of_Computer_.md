### Liang Barsky algorithm

- The Liang Barsky algorithm is a line clipping algorithm that is used to determine which portion of a line should be drawn inside a given rectangular clipping window .
- The algorithm is based on the parametric equation of a line, which is given by:

    `x = x1 + u * (x2 - x1)`

    `y = y1 + u * (y2 - y1)`

    where `(x1, y1)` and `(x2, y2)` are the end points of the line, and `u` is a parameter that varies from 0 to 1.

- The algorithm also uses four inequalities that describe the range of the clipping window, which are:

    `xwmin <= x <= xwmax`

    `ywmin <= y <= ywmax`

    where `(xwmin, ywmin)` and `(xwmax, ywmax)` are the lower-left and upper-right corners of the window, respectively.

- The algorithm works by finding the values of `u` that satisfy the four inequalities, and then using the minimum and maximum values of `u` to compute the intersection points of the line and the window.

- The algorithm can be summarized by the following steps :

    1. Initialize `u1 = 0` and `u2 = 1`, which represent the lower and upper bounds of the visible portion of the line.
    2. For each of the four boundaries of the window, calculate the value of `u` that corresponds to the intersection of the line and the boundary, using the parametric equation and the inequality. Let `p` and `q` be the coefficients of `u` in the inequality, such that `p * u + q <= 0` or `p * u + q >= 0`, depending on the boundary.
    3. If `p < 0`, then the line is entering the window. Update `u1 = max(u1, q / p)`.
    4. If `p > 0`, then the line is leaving the window. Update `u2 = min(u2, q / p)`.
    5. If `p = 0` and `q < 0`, then the line is parallel to and outside the window. Reject the line and exit the algorithm.
    6. If `u1 > u2`, then the line is outside the window. Reject the line and exit the algorithm.
    7. Otherwise, the line is partially or completely inside the window. Accept the line and calculate the intersection points using the parametric equation and the values of `u1` and `u2`.

- The algorithm is more efficient than the Cohen–Sutherland algorithm and can be extended to 3-Dimensional clipping. It is considered to be the fastest parametric line-clipping algorithm.

- An example of the algorithm is shown below, where the line `(x1, y1) = (10, 10)` and `(x2, y2) = (80, 80)` is clipped by the window `(xwmin, ywmin) = (20, 20)` and `(xwmax, ywmax) = (60, 60)`.

    ![Liang Barsky example](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Liang-Barsky.svg/1200px-Liang-Barsky.svg.png)

    - The values of `p` and `q` for each boundary are:

        | Boundary | Inequality | p | q |
        |----------|------------|---|---|
        | Left | x >= xwmin | x2 - x1 | xwmin - x1 |
        | Right | x <= xwmax | x1 - x2 | x2 - xwmax |
        | Bottom | y >= ywmin | y2 - y1 | ywmin - y1 |
        | Top | y <= ywmax | y1 - y2 | y2 - ywmax |

    - The values of `u` for each boundary are:

        | Boundary | u |
        |----------|---|
        | Left | 0.125 |
        | Right | 0.625 |
        | Bottom | 0.125 |
        | Top | 0.625 |

    - The values of `u1` and `