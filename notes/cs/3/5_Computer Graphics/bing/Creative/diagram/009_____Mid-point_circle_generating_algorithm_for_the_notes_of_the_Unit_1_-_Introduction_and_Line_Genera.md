### Mid-point circle generating algorithm

The mid-point circle generating algorithm is an algorithm used to determine the points needed for rasterizing a circle . It is based on the mid-point theorem which states that if the points along the circumference of a circle are equidistant from the center of the circle, then the points will lie on the circle. The algorithm can be generalized to conic sections.

The algorithm works as follows:

- Assume the center of the circle is at the origin (0, 0) and the radius is R.
- Initialize the starting point coordinates (X0, Y0) as (0, R).
- Initialize the decision parameter P0 as 1 - R.
- Repeat the following steps until X >= Y:
  - Plot the current point (X, Y) and its mirror points in the other seven octants.
  - If P < 0, then the next point is (X + 1, Y) and P is updated as P + 2X + 3.
  - If P >= 0, then the next point is (X + 1, Y - 1) and P is updated as P + 2X - 2Y + 5.
  - Increment X by 1 and decrement Y by 1 if necessary.

The algorithm can be illustrated by the following diagram:

![Mid-point circle generating algorithm](https://media.geeksforgeeks.org/wp-content/uploads/20200319165048/Mid-Point-Circle-Drawing-Algorithm.png)

The algorithm has the following advantages:

- It is simple and easy to implement.
- It only uses integer arithmetic and avoids trigonometric functions.
- It is efficient and requires only one-eighth of the circle to be calculated.

The algorithm has the following disadvantages:

- It is not accurate for large circles as it suffers from round-off errors.
- It cannot handle circles with arbitrary center and radius.