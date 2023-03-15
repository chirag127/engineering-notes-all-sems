# Mid-point circle generating algorithm

The mid-point circle generating algorithm is an algorithm used to determine the points needed for rasterizing a circle. It is based on the following properties of a circle:

- A circle is symmetric about its center, so the points in one octant can be mirrored to the other seven octants.
- A circle has a constant radius, so the distance from any point on the circle to the center is equal to the radius.

The algorithm works as follows:

- Given the center (h, k) and the radius r of the circle, start from the point (0, r) on the positive y-axis and move clockwise along the circle perimeter.
- At each step, calculate the next point (x, y) using the decision parameter p, which is the difference between the squared radius and the squared distance from the center to the current point.
- If p is negative, the next point is (x + 1, y), which is closer to the circle. If p is positive, the next point is (x + 1, y - 1), which is farther from the circle. If p is zero, the next point can be either (x + 1, y) or (x + 1, y - 1).
- Update the value of p using the following formula:

  - p = p + 2x + 3, if p < 0
  - p = p + 2x - 2y + 5, if p >= 0

- Stop when x >= y, which means the algorithm has reached the 45-degree line in the first octant.
- For each point (x, y) generated, plot the corresponding points in the other seven octants using the symmetry property of the circle. The points are:

  - (x, y), (y, x), (-x, y), (-y, x), (x, -y), (y, -x), (-x, -y), (-y, -x)

The following diagram illustrates the algorithm:

![Mid-point circle generating algorithm](https://www.geeksforgeeks.org/wp-content/uploads/midpoint_circle.png)

The algorithm has the following advantages:

- It is simple and easy to implement.
- It only uses integer arithmetic, which is faster and more accurate than floating-point arithmetic.
- It minimizes the number of calculations by using the previous value of p and the symmetry property of the circle.

The algorithm has the following disadvantages:

- It generates redundant points when p is zero, which can be avoided by using a modified formula for p.
- It may produce gaps or overlaps in the circle perimeter, depending on the resolution of the raster device. This can be improved by using anti-aliasing techniques.