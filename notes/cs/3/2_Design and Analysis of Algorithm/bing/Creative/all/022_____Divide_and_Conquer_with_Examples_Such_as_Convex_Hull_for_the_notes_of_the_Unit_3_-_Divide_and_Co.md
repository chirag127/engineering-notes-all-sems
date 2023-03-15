# Divide and Conquer with Examples Such as Convex Hull

- Divide and conquer is a paradigm for designing algorithms that solve a problem by recursively breaking it into smaller subproblems of the same type, until they become simple enough to be solved directly.
- The solutions of the subproblems are then combined to give a solution to the original problem.
- Divide and conquer algorithms have three main steps: divide, conquer, and combine.
- Divide: This step involves splitting the problem into smaller and simpler subproblems, typically of the same size and structure.
- Conquer: This step involves solving each subproblem recursively, either directly or by applying the divide and conquer approach again.
- Combine: This step involves merging the solutions of the subproblems to obtain the solution of the original problem.
- Divide and conquer algorithms are often efficient and elegant, as they reduce the problem size exponentially and exploit the subproblem structure.
- Some examples of divide and conquer algorithms are:

## Merge Sort
- Merge sort is a sorting algorithm that sorts an array of n elements by recursively dividing it into two halves, sorting each half, and then merging the two sorted halves.
- The divide step splits the array into two subarrays of roughly equal size.
- The conquer step sorts each subarray recursively using merge sort.
- The combine step merges the two sorted subarrays into one sorted array using a linear-time merging procedure.
- Merge sort has a time complexity of O(n log n) and a space complexity of O(n) in the worst case.
- Merge sort is stable, meaning that it preserves the relative order of equal elements in the input array.
- Merge sort is an example of a divide and conquer algorithm that uses a balanced divide, where the subproblems have the same size, and a trivial combine, where the subproblem solutions are simply concatenated.

## Binary Search
- Binary search is a search algorithm that finds the position of a target value within a sorted array of n elements by repeatedly comparing the target value with the middle element of the array and discarding half of the array based on the comparison result.
- The divide step reduces the search space to either the left or the right half of the current array, depending on whether the target value is smaller or larger than the middle element, respectively.
- The conquer step checks if the middle element is equal to the target value, and if so, returns its position. Otherwise, it recursively applies binary search to the remaining half of the array.
- The combine step is trivial, as there is nothing to merge or combine.
- Binary search has a time complexity of O(log n) and a space complexity of O(1) in the worst case.
- Binary search is an example of a divide and conquer algorithm that uses an unbalanced divide, where the subproblems have different sizes, and a trivial combine, where the subproblem solutions are simply returned.

## Convex Hull
- Convex hull is a geometric problem that finds the smallest convex polygon that contains a given set of n points in the plane.
- A convex polygon is a polygon whose interior angles are all less than 180 degrees, and a point is contained in a polygon if it lies on the boundary or in the interior of the polygon.
- The divide step partitions the set of points into two subsets by drawing a vertical line through the median x-coordinate of the points.
- The conquer step recursively computes the convex hull of each subset using the same algorithm.
- The combine step merges the two convex hulls into one convex hull using a linear-time merging procedure that discards the points that are not part of the final convex hull.
- The merging procedure works by finding the upper and lower tangent lines that connect the two convex hulls, and removing the points that lie below the upper tangent line or above the lower tangent line.
- Convex hull has a time complexity of O(n log n) and a space complexity of O(n) in the worst case.
- Convex hull is an example of a divide and conquer algorithm that uses a balanced divide, where the subproblems have the same size, and a non-trivial combine, where the subproblem solutions are merged using a sophisticated procedure.