# Cohen Sutherland line clipping algorithm

- It is an algorithm used for line clipping in computer graphics.
- Line clipping is the process of removing the portions of a line that are outside a given rectangular region of interest (the viewport).
- The algorithm divides a two-dimensional space into 9 regions: one inside region and eight outside regions.
- Each region is assigned a 4-bit code, called the outcode, based on the position of the region relative to the viewport boundaries.
- The outcode is computed as follows:

  - The first bit is 1 if the region is above the viewport, 0 otherwise.
  - The second bit is 1 if the region is below the viewport, 0 otherwise.
  - The third bit is 1 if the region is to the right of the viewport, 0 otherwise.
  - The fourth bit is 1 if the region is to the left of the viewport, 0 otherwise.

- For example, the outcode for the region above and to the right of the viewport is 1001, and the outcode for the inside region is 0000.
- The algorithm proceeds in three steps:

  - If both endpoints of the line have the same outcode, and it is not 0000, then the line is entirely outside the viewport and can be discarded.
  - If both endpoints of the line have the outcode 0000, then the line is entirely inside the viewport and can be drawn.
  - If the endpoints of the line have different outcodes, then the line may be partially inside the viewport and needs to be clipped. To do this, the algorithm finds an intersection point between the line and one of the viewport boundaries, and replaces the endpoint that is outside the viewport with the intersection point. Then, the algorithm repeats the process with the new line segment until one of the first two cases applies.

- The algorithm is efficient because it avoids unnecessary calculations and comparisons by using the outcode information.
- The algorithm works only for rectangular viewports. For other shapes, other algorithms such as Cyrus-Beck or Sutherland-Hodgman are needed.