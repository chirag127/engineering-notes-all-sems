### Divide and Conquer with Examples Such as Convex Hull

- Divide and conquer is an algorithm design paradigm that recursively breaks down a problem into two or more sub-problems of the same or related type, until these become simple enough to be solved directly.
- The solutions to the sub-problems are then combined to give a solution to the original problem.
- Divide and conquer algorithms are naturally adapted for execution in multi-processor machines, especially shared-memory systems where the communication of data between processors does not need to be planned in advance because distinct sub-problems can be executed on different processors.
- Divide and conquer algorithms have three main steps:
  - Divide the problem into a number of sub-problems that are smaller instances of the same problem.
  - Conquer the sub-problems by solving them recursively. If they are small enough, solve the sub-problems as base cases.
  - Combine the solutions to the sub-problems into the solution for the original problem.
- Some examples of divide and conquer algorithms are:
  - Sorting algorithms such as merge sort, quick sort and heap sort.
  - Matrix multiplication algorithms such as Strassen's algorithm and Coppersmith–Winograd algorithm.
  - Convex hull algorithms such as Graham scan and Chan's algorithm.
  - Searching algorithms such as binary search and interpolation search.

- A convex hull of a set of points is the smallest convex polygon that contains all the points.
- A convex polygon is a polygon in which no line segment between two points on the boundary ever goes outside the polygon.
- Finding the convex hull of a set of points is a fundamental problem in computational geometry, with applications in pattern recognition, image processing, statistics, geographic information systems, robotics and more.
- There are many algorithms for finding the convex hull of a set of points, some of which are based on the divide and conquer approach.
- One such algorithm is the Graham scan, which works as follows:
  - Choose a point p with the lowest y-coordinate (if there are ties, choose the one with the lowest x-coordinate as well). This point is the first vertex of the convex hull and is called the pivot.
  - Sort the remaining points by the angle they make with the pivot and the positive x-axis, in counterclockwise order. If two points have the same angle, keep the one that is closer to the pivot.
  - Push the pivot and the first two sorted points onto a stack.
  - For each remaining point in the sorted order, do the following:
    - While the angle formed by the top two points on the stack and the current point makes a right turn or is collinear, pop the top point from the stack.
    - Push the current point onto the stack.
  - The points remaining on the stack form the vertices of the convex hull in counterclockwise order.