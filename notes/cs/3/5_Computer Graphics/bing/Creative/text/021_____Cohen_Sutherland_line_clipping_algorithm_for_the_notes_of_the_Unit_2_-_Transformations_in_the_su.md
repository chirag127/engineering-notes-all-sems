### Cohen Sutherland line clipping algorithm

- Line clipping is a process of removing the portions of a line that are outside a given rectangular window, while preserving the portions that are inside or on the boundary of the window.
- Cohen Sutherland algorithm is a line clipping algorithm that divides a two-dimensional space into 9 regions and then efficiently determines the lines and portions of lines that are visible in the central region of interest (the viewport).
- The algorithm can be outlined as follows:
  - Nine regions are created, eight "outside" regions and one "inside" region. Each region is assigned a 4-bit code, called the outcode, that indicates its position relative to the window boundaries. The outcode is computed by testing the x and y coordinates of the endpoints of the line against the window boundaries.
  - If both endpoints have the same outcode, and it is not zero, then the line is completely outside the window and can be discarded.
  - If both endpoints have a zero outcode, then the line is completely inside the window and can be drawn.
  - If the endpoints have different outcodes, then the line may be partially inside the window and needs to be clipped. The algorithm finds an intersection point between the line and one of the window boundaries, and replaces the endpoint that is outside the window with the intersection point. The outcode of the new endpoint is then recomputed and the process is repeated until one of the previous cases is encountered.
- The algorithm is efficient because it performs only simple bit operations and comparisons, and avoids unnecessary calculations of intersection points.
- The algorithm works only for rectangular windows. For other shapes of windows, other algorithms such as Cyrus Beck algorithm or Sutherland Hodgman algorithm are needed.
- The algorithm can be implemented using the following pseudocode:

```
function clipLine(x1, y1, x2, y2, xmin, ymin, xmax, ymax)
  // compute the outcodes for the endpoints
  outcode1 = computeOutcode(x1, y1, xmin, ymin, xmax, ymax)
  outcode2 = computeOutcode(x2, y2, xmin, ymin, xmax, ymax)
  // loop until the line is either accepted or rejected
  while true
    // if both outcodes are zero, the line is inside the window
    if outcode1 == 0 and outcode2 == 0
      return (x1, y1, x2, y2) // accept the line
    // if the logical AND of the outcodes is not zero, the line is outside the window
    else if outcode1 & outcode2 != 0
      return null // reject the line
    // otherwise, the line is partially inside the window and needs to be clipped
    else
      // choose an endpoint that is outside the window
      if outcode1 != 0
        outcode = outcode1
      else
        outcode = outcode2
      // find the intersection point with the window boundary
      // using the slope of the line (m = (y2 - y1) / (x2 - x1))
      // and the bitwise operations to test the outcode bits
      if outcode & TOP // point is above the window
        x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
        y = ymax
      else if outcode & BOTTOM // point is below the window
        x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
        y = ymin
      else if outcode & RIGHT // point is to the right of the window
        x = xmax
        y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
      else if outcode & LEFT // point is to the left of the window
        x = xmin
        y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
      // replace the endpoint that is outside the window with the intersection point
      if outcode == outcode1
        x1 = x
        y1 = y
        outcode1 = computeOutcode(x1, y1, xmin, ymin, xmax, ymax)
      else
        x2 = x
        y2 = y
        outcode2 = computeOutcode(x2, y2, xmin, ymin,

```
