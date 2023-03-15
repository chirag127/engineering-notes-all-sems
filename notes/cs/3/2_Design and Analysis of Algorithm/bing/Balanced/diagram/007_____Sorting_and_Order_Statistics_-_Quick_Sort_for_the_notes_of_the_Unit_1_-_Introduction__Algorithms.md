### Sorting and Order Statistics - Quick Sort

- Quick sort is a **divide-and-conquer** algorithm that sorts an array of elements by recursively partitioning it into two subarrays around a **pivot** element.
- The pivot element is chosen randomly or by some heuristic, such as the median of the first, middle, and last elements of the array.
- The partitioning step rearranges the array such that all elements less than or equal to the pivot are in the left subarray, and all elements greater than the pivot are in the right subarray.
- The pivot element is then placed in its correct position in the sorted array, and the subarrays are recursively sorted by the same procedure.
- The algorithm has an average-case running time of **O(n log n)**, where n is the number of elements in the array, and a worst-case running time of **O(n^2)**, which occurs when the pivot element is always the smallest or the largest element in the array.
- The algorithm is **in-place**, meaning that it does not require additional memory to sort the array, and **unstable**, meaning that it does not preserve the relative order of equal elements.
- The algorithm can be implemented as follows:

```python
# A function to partition an array around a pivot element
def partition(A, p, r):
  # Choose the last element as the pivot
  x = A[r]
  # Initialize the index of the smaller element
  i = p - 1
  # Loop through the array from p to r - 1
  for j in range(p, r):
    # If the current element is less than or equal to the pivot
    if A[j] <= x:
      # Increment the index of the smaller element
      i = i + 1
      # Swap the current element with the smaller element
      A[i], A[j] = A[j], A[i]
  # Swap the pivot element with the element at i + 1
  A[i + 1], A[r] = A[r], A[i + 1]
  # Return the index of the pivot element
  return i + 1

# A function to sort an array using quick sort
def quick_sort(A, p, r):
  # If the array has more than one element
  if p < r:
    # Partition the array around a pivot element
    q = partition(A, p, r)
    # Recursively sort the left subarray
    quick_sort(A, p, q - 1)
    # Recursively sort the right subarray
    quick_sort(A, q + 1, r)
```
- An example of quick sort on an array of 10 elements is shown below:

![Quick sort example](https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Quicksort-diagram.svg/1200px-Quicksort-diagram.svg.png)

- The advantages of quick sort are that it is fast on average, it does not require extra space, and it can be easily parallelized or adapted to different data structures.
- The disadvantages of quick sort are that it is sensitive to the choice of the pivot element, it has a poor worst-case performance, and it is unstable.