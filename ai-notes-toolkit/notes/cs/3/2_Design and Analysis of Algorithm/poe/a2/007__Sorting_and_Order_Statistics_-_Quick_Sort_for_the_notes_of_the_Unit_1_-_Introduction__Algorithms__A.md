 Here is the content in Markdown format without any emojis or external links:

### Sorting and Order Statistics - Quick Sort

- Quicksort is a divide and conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot.
- It recursively sorts the sub-array of elements with smaller values than the pivot (left partition) and sub-array of elements with greater values than the pivot (right partition).
- The key process in quicksort is the partition(). It takes last element as pivot, places the pivot at its correct position in the sorted array, and places all smaller elements (smaller than pivot) before the pivot and all greater elements after it.
- The partition process continues on left and right partitions recursively until the array is sorted.
- Time complexity of quicksort is O(nlogn) in average and worst case. The worst case occurs when the array is already sorted and the pivot always divides the array into two unequal partitions which leads to O(n2) time complexity.
- To avoid worst case, we can randomly choose the pivot element from the array.
- Quicksort is a preferred sorting algorithm as it is efficient for large-sized data and also has an advantage of performing in-place sorting (i.e. it requires O(log n) extra space).

The content is written in a formal tone with points in Markdown format as requested. Please let me know if you would like me to modify or add anything.