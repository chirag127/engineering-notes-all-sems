# Sorting and Order Statistics - Shell Sort

- Shell sort is a highly efficient sorting algorithm that is based on the insertion sort algorithm .
- It avoids large shifts of elements, as in insertion sort, where the smaller value is on the far right and must be moved to the far left .
- It first sorts elements that are far apart from each other and successively reduces the interval between the elements to be sorted .
- The interval between the elements is reduced based on the sequence used . A common sequence is N/2, N/4, ..., 1, where N is the size of the array .
- An array is said to be h-sorted if all sublists of every h'th element are sorted .
- The algorithm works as follows :
  - Start with a large value of h and sort the sublists of h elements using insertion sort.
  - Reduce the value of h and repeat the process until h becomes 1.
  - At the end, the array will be fully sorted.
- The time complexity of shell sort depends on the choice of the sequence. The worst-case time complexity is O(N^2), where N is the size of the array.
- The space complexity of shell sort is O(1), as it only requires constant extra space.
- Shell sort is an adaptive, unstable, and in-place sorting algorithm.
  - Adaptive: It adapts to the data and performs better on partially sorted arrays.
  - Unstable: It does not preserve the relative order of elements with equal keys.
  - In-place: It does not require extra space to sort the array.