### Mid-point circle generating algorithm for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- The mid-point circle generating algorithm is a technique to draw a circle on a raster display using only integer arithmetic.
- The algorithm is based on the observation that a circle with radius r and center (xc, yc) can be divided into eight symmetrical parts, each corresponding to an octant of the circle.
- The algorithm starts from the point (xc + r, yc) and moves counter-clockwise along the circle, drawing one pixel per octant, until it reaches the starting point again.
- The algorithm uses the following variables:
  - x and y: the coordinates of the current pixel on the circle
  - d: the decision parameter that determines whether to move vertically or diagonally
  - deltaE: the change in d when moving vertically
  - deltaSE: the change in d when moving diagonally
- The algorithm can be summarized as follows:
  - Initialize x = r, y = 0, d = 1 - r, deltaE = 3, deltaSE = -2r + 5
  - Repeat until x >= y
    - Draw the pixel (xc + x, yc + y) and its seven symmetrical pixels in the other octants
    - If d < 0, then
      - d = d + deltaE
      - deltaE = deltaE + 2
      - deltaSE = deltaSE + 2
      - x = x + 1
    - Else
      - d = d + deltaSE
      - deltaE = deltaE + 2
      - deltaSE = deltaSE + 4
      - x = x + 1
      - y = y - 1
- The algorithm can be illustrated by the following diagram:

```
   y ^
     |
     |       (x, y)
     |     /   |
     |   /     |
     | /       |
     |/        |
-----+---------+-----> x
     |         |
     |         |
     |         |
     |         |
     |         |
     |         |
     |         |
     |         |
     |         |
     |         |
     |         |
     |         |
     |         |
     |         |
     |         |
     |         |
     |         |
     |         |
     |(xc, yc) |
     +---------+
```
- The algorithm has the following advantages and disadvantages:
  - Advantages:
    - It is simple and efficient, requiring only integer arithmetic and no trigonometric functions
    - It produces a smooth circle with no gaps or jagged edges
    - It can be easily modified to draw ellipses, arcs, or other shapes based on circles
  - Disadvantages:
    - It requires a square grid of pixels, which may not match the aspect ratio of the display device
    - It may produce aliasing artifacts, such as Moiré patterns, when the circle is not aligned with the pixel grid
    - It may not be suitable for drawing circles with very large or very small radii, as it may cause overflow or underflow errors in the calculations