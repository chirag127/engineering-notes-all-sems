# Mid-point circle generating algorithm

The mid-point circle generating algorithm is an algorithm used to determine the points needed for rasterizing a circle. It is based on the following idea:

- A circle is symmetric about its center, so we only need to calculate the points in one octant (e.g., the first octant where x >= 0 and y >= 0) and then reflect them to the other octants.
- A circle with radius r and center (0, 0) has the equation x^2 + y^2 = r^2. We can use this equation to check whether a point (x, y) is on the circle, inside the circle, or outside the circle.
- We start from the point (0, r) and move along the circle in a counter-clockwise direction. At each step, we have two possible choices for the next point: (x + 1, y) or (x + 1, y - 1). We choose the one that is closer to the circle.
- We can use a decision parameter p to determine which point to choose. Initially, p = 1 - r. If p < 0, then the point (x + 1, y) is closer to the circle, so we choose it and update p as p = p + 2x + 3. If p >= 0, then the point (x + 1, y - 1) is closer to the circle, so we choose it and update p as p = p + 2x - 2y + 5.
- We repeat this process until x >= y, which means we have reached the end of the first octant.

The algorithm can be summarized as follows:

- Input: radius r of the circle
- Output: the points on the circle in the first octant
- Algorithm:
  - Set x = 0 and y = r
  - Set p = 1 - r
  - While x < y
    - Plot the point (x, y) and its reflections in the other octants
    - If p < 0
      - Set x = x + 1
      - Set p = p + 2x + 3
    - Else
      - Set x = x + 1 and y = y - 1
      - Set p = p + 2x - 2y + 5
  - If x == y
    - Plot the point (x, y) and its reflections in the other octants

The following figure shows an example of the algorithm for r = 5:

![midpoint circle algorithm example](https://www.geeksforgeeks.org/wp-content/uploads/midpoint_circle_drawing_algorithm.png)

Source: