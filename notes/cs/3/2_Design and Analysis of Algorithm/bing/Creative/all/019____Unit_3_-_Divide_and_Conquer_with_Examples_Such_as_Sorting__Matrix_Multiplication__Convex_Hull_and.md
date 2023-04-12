# Unit 3 - Divide and Conquer with Examples Such as Sorting, Matrix Multiplication, Convex Hull and Searching. Greedy Methods with Examples Such as Optimal Reliability Allocation, Knapsack, Minimum Spanning Trees – Prim’s and Kruskal’s Algorithms, Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms.

## Divide and Conquer

- Divide and conquer is a paradigm for designing algorithms that solve a problem by breaking it into smaller subproblems, solving them recursively, and combining their solutions to get the solution for the original problem  .
- Divide and conquer algorithms have three steps:
  - **Divide**: Split the problem into smaller and simpler subproblems, typically of the same type as the original problem.
  - **Conquer**: Solve the subproblems recursively, either directly or by applying the divide and conquer approach again.
  - **Combine**: Merge the solutions of the subproblems to obtain the solution for the original problem.
- Divide and conquer algorithms are often efficient, as they reduce the problem size exponentially at each level of recursion, and they are suitable for parallel and distributed computing.
- Some examples of divide and conquer algorithms are:
  - **Binary search**: An algorithm that searches for a target value in a sorted array by repeatedly dividing the search interval in half and comparing the target with the middle element .
    - The algorithm can be implemented as follows:

    ```python
    # A recursive function that returns the index of the target value in the array, or -1 if not found
    def binary_search(array, low, high, target):
      # Base case: the search interval is empty
      if low > high:
        return -1
      
      # Find the middle index
      mid = (low + high) // 2
      
      # Compare the target with the middle element
      if target == array[mid]:
        # Found the target
        return mid
      elif target < array[mid]:
        # Target is in the left half
        return binary_search(array, low, mid - 1, target)
      else:
        # Target is in the right half
        return binary_search(array, mid + 1, high, target)
    ```
    - The time complexity of binary search is O(log n), where n is the size of the array, as the search interval is halved at each recursive call.
    - The space complexity of binary search is O(log n), as the maximum depth of the recursion tree is log n.
  - **Merge sort**: An algorithm that sorts an array by dividing it into two halves, sorting them recursively, and then merging the sorted halves .
    - The algorithm can be implemented as follows:

    ```python
    # A helper function that merges two sorted arrays into one sorted array
    def merge(array, low, mid, high):
      # Create temporary arrays to store the left and right halves
      left = array[low:mid + 1]
      right = array[mid + 1:high + 1]
      
      # Initialize indices for the left, right, and merged arrays
      i = 0
      j = 0
      k = low
      
      # Merge the elements from the left and right arrays in sorted order
      while i < len(left) and j < len(right):
        if left[i] <= right[j]:
          # Left element is smaller or equal
          array[k] = left[i]
          i += 1
        else:
          # Right element is smaller
          array[k] = right[j]
          j += 1
        k += 1
      
      # Copy the remaining elements from the left array, if any
      while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1
      
      # Copy the remaining elements from the right array, if any
      while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1
    
    # A recursive function that sorts an array using merge sort
    def merge_sort(array, low, high):
      # Base case: the array has one or zero elements
      if low >= high:
        return
      
      # Find the middle index
      mid = (low + high) // 2
      
      # Sort the left and right halves recursively
      merge_sort(array, low, mid)
      merge_sort(array, mid + 1

```
