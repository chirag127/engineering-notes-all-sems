### Divide and Conquer with Examples Such as Convex Hull

- Divide and conquer is an algorithm design paradigm that recursively breaks down a problem into two or more sub-problems of the same or related type, until these become simple enough to be solved directly.
- The solutions to the sub-problems are then combined to give a solution to the original problem.
- Divide and conquer algorithms are naturally adapted for execution in multi-processor machines, especially shared-memory systems where the communication of data between processors does not need to be planned in advance because distinct sub-problems can be executed on different processors.
- Some examples of divide and conquer algorithms are:

  - Sorting algorithms such as merge sort, quick sort and heap sort.
  - Matrix multiplication algorithms such as Strassen's algorithm and Coppersmith–Winograd algorithm.
  - Convex hull algorithms such as Graham scan and Chan's algorithm.
  - Searching algorithms such as binary search and interpolation search.

- A convex hull of a set of points is the smallest convex polygon that contains all the points.
- A convex polygon is a polygon in which no line segment between two points on the boundary ever goes outside the polygon.
- Finding the convex hull of a set of points is a fundamental problem in computational geometry, with applications in pattern recognition, image processing, statistics, geographic information systems, etc.
- There are several divide and conquer algorithms for finding the convex hull of a set of points, such as:

  - Graham scan: This algorithm sorts the points by their polar angle with respect to a reference point, and then scans them in a counterclockwise order, discarding those that would create a clockwise turn. The time complexity of this algorithm is O(n log n), where n is the number of points.
  - Chan's algorithm: This algorithm combines the ideas of Graham scan and Jarvis march, another convex hull algorithm. It partitions the points into groups of size m, computes the convex hull of each group using Graham scan, and then merges the hulls using Jarvis march. The time complexity of this algorithm is O(n log h), where h is the number of points on the convex hull. The value of m is chosen iteratively, starting from a small value and doubling it until the algorithm succeeds or fails.