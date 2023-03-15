### Divide and Conquer with Examples Such as Sorting for the notes of the Unit 3 - Divide and Conquer with Examples Such as Sorting, Matrix Multiplication, Convex Hull and Searching. Greedy Methods with Examples Such as Optimal Reliability Allocation, Knapsack, Minimum Spanning Trees – Prim’s and Kruskal’s Algorithms, Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms. in the subject of Design and Analysis of Algorithm

#### Divide and Conquer
- Divide and conquer is a technique for solving problems by breaking them into smaller and simpler subproblems, solving them recursively, and combining their solutions to obtain the solution for the original problem.
- Divide and conquer can reduce the time complexity of some problems from polynomial to logarithmic or even constant.
- Divide and conquer can also reduce the space complexity of some problems by using less memory or auxiliary data structures.
- Some examples of problems that can be solved by divide and conquer are:

##### Sorting
- Sorting is the problem of arranging a sequence of elements in a certain order, such as ascending or descending.
- Sorting can be done by divide and conquer by splitting the sequence into two halves, sorting each half recursively, and merging the two sorted halves into one sorted sequence.
- Some sorting algorithms that use divide and conquer are:
  - Merge sort: splits the sequence into two equal halves, sorts each half, and merges them using a linear scan.
  - Quick sort: chooses a pivot element, partitions the sequence into two sub-sequences such that all elements less than the pivot are in the left sub-sequence and all elements greater than or equal to the pivot are in the right sub-sequence, sorts each sub-sequence recursively, and concatenates them.
  - Heap sort: builds a heap (a binary tree where each node is greater than or equal to its children) from the sequence, repeatedly extracts the maximum element from the heap and appends it to the end of the sorted sequence, and restores the heap property after each extraction.

##### Matrix Multiplication
- Matrix multiplication is the problem of multiplying two matrices of compatible dimensions and obtaining their product matrix.
- Matrix multiplication can be done by divide and conquer by splitting each matrix into four sub-matrices of equal size, multiplying each pair of sub-matrices recursively, and adding or subtracting the results to obtain the product sub-matrices.
- Some matrix multiplication algorithms that use divide and conquer are:
  - Strassen's algorithm: reduces the number of recursive multiplications from eight to seven by using clever algebraic identities, and achieves a time complexity of O(n^2.807).
  - Coppersmith-Winograd algorithm: further reduces the number of recursive multiplications by using more sophisticated algebraic identities, and achieves a time complexity of O(n^2.376).

##### Convex Hull
- Convex hull is the problem of finding the smallest convex polygon that contains a given set of points in the plane.
- Convex hull can be done by divide and conquer by splitting the set of points into two halves by a vertical line, finding the convex hull of each half recursively, and merging the two convex hulls by finding their upper and lower tangents.
- Some convex hull algorithms that use divide and conquer are:
  - Graham scan: sorts the points by their polar angle with respect to the lowest point, and scans them in a counterclockwise order, adding each point to the convex hull and removing any previous point that makes a right turn with the last two points, until the starting point is reached again.
  - Jarvis march: starts with the leftmost point, and repeatedly finds the next point that forms the smallest positive angle with the last edge, until the starting point is reached again.

##### Searching
- Searching is the problem of finding an element in a sequence or a data structure that satisfies a given condition or matches a given value.
- Searching can be done by divide and conquer by splitting the sequence or the data structure into two halves, checking which half contains the element or satisfies the condition, and searching that half recursively.
- Some searching algorithms that use divide and conquer are:
  - Binary search: assumes that the sequence is sorted, and compares the middle element with the target value, discarding the half that does not contain the target, and repeating until the target is found or the sequence is empty.
  - Interpolation search: assumes that the sequence is sorted and uniformly distributed, and estimates the position of the target value based on the first and last elements, discarding the half that does not contain the target, and repeating until the target is found or the sequence is empty.
  - Bisection method: assumes that the sequence is a continuous function that changes sign at the target value, and finds the midpoint of the interval, discarding the