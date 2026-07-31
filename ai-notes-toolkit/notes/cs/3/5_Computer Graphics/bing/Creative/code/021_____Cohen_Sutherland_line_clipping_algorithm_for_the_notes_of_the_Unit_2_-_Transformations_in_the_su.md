### Cohen Sutherland line clipping algorithm

- Line clipping is the process of removing the portions of a line that are outside a given rectangular window, while preserving the portions that are inside or on the boundary of the window.
- Cohen Sutherland algorithm is a line clipping algorithm that divides a two-dimensional space into 9 regions and then efficiently determines the lines and portions of lines that are visible in the central region of interest (the viewport).
- The algorithm can be outlined as follows:

  - Nine regions are created, eight "outside" regions and one "inside" region. Each region is assigned a 4-bit code, called the outcode, that indicates which of the four boundaries of the window the region is outside of. The outcode for the inside region is 0000, meaning it is not outside any boundary. The outcode for each outside region is obtained by bitwise ORing the codes for each boundary that the region is outside of. For example, the outcode for the top-right region is 1001, meaning it is outside the top and right boundaries.
  - For each line to be clipped, the outcodes of the two endpoints are computed. If both outcodes are 0000, the line is entirely inside the window and can be drawn without clipping. If the bitwise AND of the two outcodes is not 0000, the line is entirely outside the window and can be discarded. Otherwise, the line is partially inside the window and needs to be clipped.
  - To clip the line, one of the endpoints that is outside the window is selected and replaced by the intersection point of the line and the boundary that the endpoint is outside of. The outcode of the new endpoint is then recomputed and the process is repeated until the line is either accepted or rejected.

- The algorithm is efficient because it avoids unnecessary calculations and intersections by using the outcodes to quickly test the visibility of the line or its parts.
- The algorithm works only for rectangular windows. For other shapes of windows, other algorithms such as Cyrus Beck algorithm or Sutherland Hodgman algorithm are needed.
- The algorithm can be implemented using the following pseudocode:

```
function clipLine(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
  // compute the outcodes for the endpoints
  outcode1 = computeOutcode(x1, y1, xmin, ymin, xmax, ymax)
  outcode2 = computeOutcode(x2, y2, xmin, ymin, xmax, ymax)
  // loop until the line is either accepted or rejected
  while true:
    // if both outcodes are zero, the line is inside the window
    if outcode1 == 0 and outcode2 == 0:
      return (x1, y1, x2, y2) // accept the line
    // if the bitwise AND of the outcodes is not zero, the line is outside the window
    elif outcode1 & outcode2 != 0:
      return None // reject the line
    // otherwise, the line is partially inside the window and needs to be clipped
    else:
      // select one of the endpoints that is outside the window
      if outcode1 != 0:
        outcode = outcode1
      else:
        outcode = outcode2
      // find the intersection point of the line and the boundary that the endpoint is outside of
      if outcode & 1000: // top boundary
        x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
        y = ymax
      elif outcode & 0100: // bottom boundary
        x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
        y = ymin
      elif outcode & 0010: // right boundary
        x = xmax
        y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
      elif outcode & 0001: // left boundary
        x = xmin
        y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
      // replace the endpoint with the intersection point and recompute the outcode
      if outcode == outcode1:
        x1 = x
        y1 = y
        outcode1 = computeOutcode(x1, y1, xmin, ymin, xmax, ymax

```
