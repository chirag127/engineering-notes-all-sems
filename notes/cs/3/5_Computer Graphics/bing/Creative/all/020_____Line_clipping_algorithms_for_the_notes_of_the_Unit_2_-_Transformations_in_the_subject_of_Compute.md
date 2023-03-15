# Line clipping algorithms

Line clipping algorithms are used to remove parts of lines that lie outside a specified region of interest, such as a viewport or a view volume. This is done to improve the efficiency and quality of rendering by avoiding unnecessary calculations and pixels. Line clipping algorithms typically work by testing the endpoints of each line segment against the boundaries of the clipping region, and then either discarding, accepting, or clipping the segment accordingly.

There are many line clipping algorithms, but two of the most common ones are:

- **Cohen–Sutherland algorithm**: This algorithm divides the 2D space into 9 regions, of which only the middle one is the visible viewport. Each region is assigned a 4-bit code, based on whether the point is above, below, left, or right of the viewport. The algorithm then compares the codes of the endpoints of each line segment, and applies one of the following rules:

  - If both codes are 0000, the segment is completely inside the viewport and is accepted.
  - If the bitwise AND of the codes is not 0000, the segment is completely outside the viewport and is rejected.
  - If neither of the above cases apply, the segment is partially inside the viewport and is clipped. The algorithm finds the intersection point of the segment with one of the viewport boundaries, and replaces the endpoint with the outside code with the intersection point. The new segment is then tested again with the same rules.

- **Liang–Barsky algorithm**: This algorithm is based on the parametric equation of a line segment, and uses four inequalities to test whether the segment is inside or outside the viewport. The algorithm then finds the minimum and maximum values of the parameter t that satisfy the inequalities, and uses them to clip the segment. The algorithm is more efficient than the Cohen–Sutherland algorithm, as it requires fewer calculations and comparisons.

Here is a pseudocode for the Liang–Barsky algorithm:

```
Input: x1, y1, x2, y2 // the endpoints of the line segment
       xmin, ymin, xmax, ymax // the boundaries of the viewport
Output: x1c, y1c, x2c, y2c // the clipped endpoints of the line segment, or null if rejected

// calculate the differences and the direction parameters
dx = x2 - x1
dy = y2 - y1
p = [-dx, dx, -dy, dy]
q = [x1 - xmin, xmax - x1, y1 - ymin, ymax - y1]

// initialize the minimum and maximum values of t
tmin = 0
tmax = 1

// loop through the four boundaries
for i = 0 to 3
  // if the line is parallel to the boundary
  if p[i] == 0
    // if the line is outside the boundary, reject it
    if q[i] < 0
      return null
  // if the line is not parallel to the boundary
  else
    // calculate the intersection parameter
    t = q[i] / p[i]
    // if the line is entering the boundary
    if p[i] < 0
      // update the minimum value of t
      tmin = max(tmin, t)
    // if the line is leaving the boundary
    else
      // update the maximum value of t
      tmax = min(tmax, t)
    // if the line is outside the boundary, reject it
    if tmin > tmax
      return null

// calculate the clipped endpoints using the minimum and maximum values of t
x1c = x1 + tmin * dx
y1c = y1 + tmin * dy
x2c = x1 + tmax * dx
y2c = y1 + tmax * dy

// return the clipped endpoints
return x1c, y1c, x2c, y2c
```