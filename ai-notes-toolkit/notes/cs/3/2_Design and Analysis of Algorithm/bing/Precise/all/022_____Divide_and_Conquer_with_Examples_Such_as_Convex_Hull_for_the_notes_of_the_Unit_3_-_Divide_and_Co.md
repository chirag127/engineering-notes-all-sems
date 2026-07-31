# Divide and Conquer with Examples Such as Convex Hull

Divide and Conquer is an algorithmic paradigm that solves a problem by dividing it into smaller subproblems and solving them recursively. The subproblems are then combined to form the solution to the original problem. This approach is commonly used in computer science and is the basis for many algorithms.

One example of an algorithm that uses the divide and conquer approach is the Convex Hull algorithm. The Convex Hull of a set of points is the smallest convex polygon that contains all the points. The algorithm works by dividing the set of points into two smaller sets, finding the Convex Hull of each set, and then merging the two Convex Hulls to form the final solution.

The steps of the Convex Hull algorithm are as follows:
1. Divide the set of points into two smaller sets by drawing a vertical line through the middle of the set.
2. Find the Convex Hull of each set recursively.
3. Merge the two Convex Hulls to form the final solution.

This algorithm has a time complexity of O(n log n) and is an efficient way to solve the Convex Hull problem.