# Scan Line Method for Hidden Surface Removal

- A scan line method of hidden surface removal is an image space method that processes one line at a time rather than one pixel at a time.
- It is an extension of the scan line algorithm for filling polygon interiors, but it deals with more than one surface.
- As each scan line is processed, it examines all polygon surfaces intersecting that line to determine which are visible.
- The scan line method of hidden surface removal also stores a flag for each surface that is set on or off to indicate whether a position along a scan line is inside or outside of the surface.
- Scan lines are processed from left to right, and the depth values of the visible surfaces are compared to find the closest one at each pixel position.
- The scan line method of hidden surface removal can be summarized as follows:

  - For each scan line, find the intersections of the scan line with all polygon edges.
  - Sort the intersections by increasing x value.
  - Initialize the depth buffer and the surface flag buffer.
  - For each pair of intersections, determine which surface is visible by comparing the depth values and the surface flags.
  - Fill the pixel positions between the pair of intersections with the color of the visible surface.
  - Update the depth buffer and the surface flag buffer accordingly.