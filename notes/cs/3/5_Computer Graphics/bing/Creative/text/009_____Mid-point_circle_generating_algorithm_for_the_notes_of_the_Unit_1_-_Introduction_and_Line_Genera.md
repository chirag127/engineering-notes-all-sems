### Mid-point circle generating algorithm

- The mid-point circle generating algorithm is an algorithm used to determine the points needed for rasterizing a circle  .
- It is based on the mid-point theorem which states that if the points along the circumference of a circle are equidistant from the center of the circle, then the points will lie on the circle.
- The algorithm uses the symmetry of the circle to reduce the computation to the first octant only, and then prints the points along with their mirror points in the other octants .
- The algorithm works as follows:

  - Step 1: Assign the starting point coordinates (X0, Y0) as:

    - X0 = 0
    - Y0 = R

  - Step 2: Calculate the value of initial decision parameter P0 as:

    - P0 = 1 - R

  - Step 3: Suppose the current point is (Xk, Yk) and the next point is (Xk+1, Yk+1).

    - If Pk < 0, then the next point is (Xk+1, Yk) and the new decision parameter is:

      - Pk+1 = Pk + 2Xk+1 + 1

    - If Pk >= 0, then the next point is (Xk+1, Yk-1) and the new decision parameter is:

      - Pk+1 = Pk + 2Xk+1 + 1 - 2Yk+1

  - Step 4: Repeat step 3 until Xk >= Yk.

  - Step 5: Print the points (Xk, Yk) along with their mirror points in the other octants using the following relations:

    - (Xk, Yk) -> (Xk, Yk), (-Xk, Yk), (Xk, -Yk), (-Xk, -Yk)
    - (Yk, Xk) -> (Yk, Xk), (-Yk, Xk), (Yk, -Xk), (-Yk, -Xk)

- The algorithm can be generalized to conic sections.
- The algorithm is efficient and simple to implement .
- The algorithm is derived from Bresenham's circle algorithm.