### Mid-point circle generating algorithm

The mid-point circle generating algorithm is an algorithm used to determine the points needed for rasterizing a circle. It is based on the following steps:

- Assume the center of the circle is at the origin (0, 0) and the radius is R.
- Start from the point (0, R) on the circle and move clockwise along the first octant of the circle.
- At each point (x, y), calculate the decision parameter P as P = x^2 + y^2 - R^2.
- If P < 0, then the next point is (x + 1, y) and P is updated as P = P + 2x + 3.
- If P >= 0, then the next point is (x + 1, y - 1) and P is updated as P = P + 2x - 2y + 5.
- Repeat the above steps until x >= y.
- Use the symmetry of the circle to generate the points in the other seven octants by reflecting the points in the first octant.

The following diagram illustrates the algorithm:

![Mid-point circle generating algorithm](https://www.geeksforgeeks.org/wp-content/uploads/midpoint-circle-algorithm.png)

The advantages of this algorithm are:

- It is simple and easy to implement.
- It only uses integer arithmetic and avoids trigonometric functions and square roots.
- It is efficient and reduces the number of calculations by exploiting the symmetry of the circle.

The disadvantages of this algorithm are:

- It may produce gaps or overlaps in the circle due to rounding errors.
- It may not produce smooth curves due to aliasing effects.