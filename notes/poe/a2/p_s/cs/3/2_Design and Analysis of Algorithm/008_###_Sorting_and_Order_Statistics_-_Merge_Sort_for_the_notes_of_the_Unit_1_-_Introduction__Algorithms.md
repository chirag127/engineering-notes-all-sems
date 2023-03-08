 Here is the content in markdown format for the topic **Sorting and Order Statistics - Merge Sort** for the notes of **Unit 1 - Introduction: Algorithms, Analyzing Algorithms, Complexity of Algorithms, Growth of Functions, Performance Measurements, Sorting and Order Statistics - Shell Sort, Quick Sort, Merge Sort, Heap Sort, Comparison of Sorting Algorithms, Sorting in Linear Time** in the subject of **Design and Analysis of Algorithm**:

### Sorting and Order Statistics - Merge Sort

- Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves recursively, and then merges the two sorted halves into one sorted array.
- The steps are:

1. Divide the array into two halves
2. Sort the left half
3. Sort the right half
4. Merge the two sorted halves into one sorted array

- Pseudocode:

mergeSort(arr):
   if len(arr) <= 1:
       return arr
   mid = len(arr) // 2
   left = mergeSort(arr[:mid])
   right = mergeSort(arr[mid:])
   return merge(left, right)

merge(left, right):
   result = []
   i, j = 0, 0
   while i < len(left) and j < len(right):
       if left[i] <= right[j]:
           result.append(left[i])
           i += 1
       else:
           result.append(right[j])
           j += 1
   result += left[i:]
   result += right[j:]
   return result

- Time Complexity: O(n log n) since the array is divided into halves in each recursive call.
- Space Complexity: O(n) for the recurrsion stack space. O(n) for the merge subroutine due to the result array.
- Applications: Used to sort linked lists. Useful for sorting arrays that cannot fit into memory (by sorting chunks and then merging). Used in databases.
- Advantages: Guaranteed to be stable. Worst and average case performance is O(n log n).
- Disadvantages: Requires O(n) extra space. Not in-place, requires additional arrays.