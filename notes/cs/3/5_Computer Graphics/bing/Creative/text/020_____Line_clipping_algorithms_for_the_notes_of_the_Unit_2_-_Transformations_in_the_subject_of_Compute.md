### Line clipping algorithms

- Line clipping is the process of removing (clipping) lines or portions of lines outside an area of interest (a viewport or view volume) in computer graphics.
- Line clipping is useful for rendering only the visible parts of a scene, reducing the computational cost and improving the performance of graphics applications.
- There are many algorithms for line clipping, but two of the most common ones are Cohen–Sutherland and Liang–Barsky.
- Cohen–Sutherland algorithm:
  - It divides a 2D space into 9 regions, of which only the middle part (viewport) is visible.
  - It assigns a 4-bit code to each endpoint of a line, based on its position relative to the viewport boundaries (top, bottom, left, right).
  - It uses bitwise operations to determine if a line is trivially accepted (both endpoints inside the viewport), trivially rejected (both endpoints outside the viewport and on the same side), or partially clipped (one or both endpoints outside the viewport and on different sides).
  - It uses the parametric equation of a line to find the intersection points of the line with the viewport edges, and replaces the outside endpoints with the intersection points.
  - It repeats the process until all lines are either accepted or rejected.
- Liang–Barsky algorithm:
  - It uses the parametric equation of a line and the inequalities of the viewport boundaries to find four parameters that define the visible portion of the line.
  - It compares the four parameters to determine if a line is trivially accepted, trivially rejected, or partially clipped.
  - It uses the four parameters to calculate the intersection points of the line with the viewport edges, and replaces the outside endpoints with the intersection points.
  - It is more efficient than Cohen–Sutherland algorithm, as it requires fewer calculations and comparisons.