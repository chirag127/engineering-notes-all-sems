# Circle generating algorithms

A circle is one of the fundamental shapes used in computer graphics and it is generated through a circle generation algorithm. A circle generation algorithm is an algorithm used to create a circle on a computer screen. It is used in various applications such as computer-aided design (CAD) software, animation software, games, and scientific visualization.

There are several algorithms used for generating circles on a computer screen, such as:

- Bresenham's algorithm
- Midpoint circle algorithm
- Trigonometric method
- Polar coordinates method

## Bresenham's algorithm

Bresenham's algorithm is an efficient and simple algorithm for drawing a circle. It is based on the idea of using only integer arithmetic and exploiting the symmetry of the circle. The algorithm works as follows:

- Given the center (xc, yc) and radius r of the circle, initialize an error variable e = 3 - 2r and a point (x, y) = (0, r).
- Plot the initial point (xc + x, yc + y) and its symmetric points in the other seven octants of the circle.
- Repeat the following steps until x <= y:
  - If e < 0, then increment x by 1 and update e as e = e + 4x + 6.
  - If e >= 0, then increment x by 1, decrement y by 1 and update e as e = e + 4(x - y) + 10.
  - Plot the new point (xc + x, yc + y) and its symmetric points in the other seven octants of the circle.

The algorithm can be illustrated by the following pseudocode:

```
Input: center (xc, yc) and radius r of the circle
Output: a set of points on the circle

Initialize e = 3 - 2r and (x, y) = (0, r)
Plot (xc + x, yc + y) and its symmetric points
While x <= y
  If e < 0
    x = x + 1
    e = e + 4x + 6
  Else
    x = x + 1
    y = y - 1
    e = e + 4(x - y) + 10
  Plot (xc + x, yc + y) and its symmetric points
End while
```

The algorithm has a time complexity of O(r) and a space complexity of O(1).

## Midpoint circle algorithm

Midpoint circle algorithm is another efficient and simple algorithm for drawing a circle. It is based on the idea of using the midpoint of the line segment joining the current point and the next point on the circle as a decision parameter. The algorithm works as follows:

- Given the center (xc, yc) and radius r of the circle, initialize a point (x, y) = (0, r) and a decision parameter p = 1 - r.
- Plot the initial point (xc + x, yc + y) and its symmetric points in the other seven octants of the circle.
- Repeat the following steps until x <= y:
  - If p < 0, then increment x by 1 and update p as p = p + 2x + 3.
  - If p >= 0, then increment x by 1, decrement y by 1 and update p as p = p + 2(x - y) + 5.
  - Plot the new point (xc + x, yc + y) and its symmetric points in the other seven octants of the circle.

The algorithm can be illustrated by the following pseudocode:

```
Input: center (xc, yc) and radius r of the circle
Output: a set of points on the circle

Initialize (x, y) = (0, r) and p = 1 - r
Plot (xc + x, yc + y) and its symmetric points
While x <= y
  If p < 0
    x = x + 1
    p = p + 2x + 3
  Else
    x = x + 1
    y = y - 1
    p = p + 2(x - y) + 5
  Plot (xc + x, yc + y) and its symmetric points
End while
```

The algorithm has a time complexity of O(r) and a space complexity of O(1).

## Trigonometric method

Trigonometric method is a simple but less efficient algorithm for