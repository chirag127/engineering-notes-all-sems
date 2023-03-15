# Mid-point circle generating algorithm

The mid-point circle generating algorithm is an algorithm used to determine the points needed for rasterizing a circle. It is based on the midpoint theorem which states that if the points along the circumference of a circle are equidistant from the center of the circle, then the points will lie on the circle  .

The algorithm works as follows:

- Start with the point (0, r) on the x-axis, where r is the radius of the circle.
- Calculate the initial decision parameter p0 as 1 - r.
- For each point (xk, yk) in the first octant of the circle, do the following:
  - Plot the point (xk, yk) and its symmetric points in the other seven octants.
  - If pk < 0, then the next point is (xk+1, yk) and pk+1 = pk + 2xk+1 + 1.
  - If pk >= 0, then the next point is (xk+1, yk-1) and pk+1 = pk + 2xk+1 + 1 - 2yk+1.
  - Repeat until xk >= yk.

The algorithm can be generalized to conic sections.

The following diagram illustrates the algorithm for a circle with radius 5:

![Mid-point circle generating algorithm](https://www.gatevidyalay.com/wp-content/uploads/2018/08/Mid-Point-Circle-Drawing-Algorithm-Example.png)

: https://www.geeksforgeeks.org/computer-graphics-circle-generation-algorithm/
: https://www.geeksforgeeks.org/mid-point-circle-drawing-algorithm/
: https://en.wikipedia.org/wiki/Midpoint_circle_algorithm
: https://www.gatevidyalay.com/mid-point-circle-drawing-algorithm/