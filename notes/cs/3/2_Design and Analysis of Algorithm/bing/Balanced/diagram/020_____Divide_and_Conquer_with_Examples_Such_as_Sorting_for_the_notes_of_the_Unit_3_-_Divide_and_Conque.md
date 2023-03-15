# Unit 3 - Divide and Conquer with Examples Such as Sorting, Matrix Multiplication, Convex Hull and Searching. Greedy Methods with Examples Such as Optimal Reliability Allocation, Knapsack, Minimum Spanning Trees – Prim’s and Kruskal’s Algorithms, Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms.

## Divide and Conquer

- Divide and conquer is a technique for solving problems that involve breaking the problem into smaller subproblems that are similar to the original problem, solving them recursively, and then combining the results.
- Divide and conquer can reduce the time complexity of some problems from polynomial to logarithmic or even constant.
- Some examples of divide and conquer algorithms are:

### Sorting

- Sorting is the problem of arranging a list of elements in a certain order, such as ascending or descending.
- Some sorting algorithms that use divide and conquer are:

#### Merge Sort

- Merge sort works by dividing the list into two halves, sorting each half recursively, and then merging the two sorted halves into one sorted list.
- The time complexity of merge sort is O(n log n), where n is the number of elements in the list.
- The space complexity of merge sort is O(n), as it requires an auxiliary array to store the merged results.

#### Quick Sort

- Quick sort works by choosing a pivot element from the list, partitioning the list into two sublists such that all elements less than the pivot are in the left sublist and all elements greater than or equal to the pivot are in the right sublist, and then sorting each sublist recursively.
- The time complexity of quick sort is O(n log n) on average, but can be O(n^2) in the worst case, where n is the number of elements in the list.
- The space complexity of quick sort is O(log n) on average, but can be O(n) in the worst case, as it requires a stack to store the recursive calls.

### Matrix Multiplication

- Matrix multiplication is the problem of multiplying two matrices of compatible dimensions and producing a third matrix as the result.
- The naive algorithm for matrix multiplication takes O(n^3) time, where n is the dimension of the square matrices.
- A divide and conquer algorithm for matrix multiplication is:

#### Strassen's Algorithm

- Strassen's algorithm works by dividing each matrix into four submatrices of equal size, computing seven products of submatrices using recursive calls, and then combining the results using addition and subtraction operations.
- The time complexity of Strassen's algorithm is O(n^log_2(7)), which is approximately O(n^2.81), where n is the dimension of the square matrices.
- The space complexity of Strassen's algorithm is O(n^2), as it requires auxiliary matrices to store the intermediate results.

### Convex Hull

- Convex hull is the problem of finding the smallest convex polygon that contains a given set of points in the plane.
- A convex polygon is a polygon that has no interior angles greater than 180 degrees, and a point is contained in a polygon if it is either on the boundary or in the interior of the polygon.
- A divide and conquer algorithm for convex hull is:

#### Graham Scan

- Graham scan works by finding the point with the lowest y-coordinate, called the pivot, sorting the rest of the points by the angle they make with the pivot and the x-axis, and then scanning the sorted points in a counterclockwise order, adding them to the convex hull if they make a left turn, and removing them if they make a right turn.
- The time complexity of Graham scan is O(n log n), where n is the number of points in the set.
- The space complexity of Graham scan is O(n), as it requires a stack to store the points in the convex hull.

### Searching

- Searching is the problem of finding a target element in a list of elements, or determining that it does not exist.
- Some searching algorithms that use divide and conquer are:

#### Binary Search

- Binary search works by comparing the target element with the middle element of the list, and then recursively searching the left or right half of the list depending on the comparison result.
- The time complexity of binary search is O(log n), where n is the number of elements in the list.
- The space complexity of binary search is O(log n), as it requires a stack to store the recursive calls.

#### Interpolation Search

- Interpolation search works by estimating the position of the target element in the list based on the values of the first and last elements and the target element, and then recursively searching the sublists around the estimated position depending on the comparison result.
- The time complexity of interpolation search is O(log log n) on average, but can be