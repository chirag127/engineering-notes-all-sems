### Sorting Algorithms-Recursive

- Sorting algorithms are used to rearrange a given array or list of elements according to a comparison operator on the elements.
- Recursive sorting algorithms are those that use recursion to divide the problem into smaller subproblems and then combine the solutions to get the final result.
- Some examples of recursive sorting algorithms are:
  - Recursive Selection Sort
  - Recursive Insertion Sort
  - Recursive Bubble Sort
  - Merge Sort
  - Quick Sort
  - Heap Sort

#### Recursive Selection Sort

- Selection sort is a sorting algorithm that iterates an array from the beginning and replaces each element with the smallest element in the list.
- As we move forward the left array is sorted, and the right array is unsorted.
- The recursive version of selection sort works as follows:
  - Base case: If the array has one or zero elements, it is already sorted. Return the array.
  - Recursive case: Find the minimum element in the array and swap it with the first element. Then, sort the remaining array (from the second element to the end) recursively and return the sorted array.
- The time complexity of recursive selection sort is O(n^2), where n is the number of elements in the array.
- The space complexity of recursive selection sort is O(n), where n is the number of elements in the array, due to the recursive call stack.
- The advantage of recursive selection sort is that it is simple and easy to implement.
- The disadvantage of recursive selection sort is that it is inefficient and does not perform well on large arrays.

#### Recursive Insertion Sort

- Insertion sort is a sorting algorithm that works by placing each element in its position in the sorted sub-array, i.e., the sub-array preceding the element which is a sorted sub-array.
- The recursive version of insertion sort works as follows:
  - Base case: If the array has one or zero elements, it is already sorted. Return the array.
  - Recursive case: Sort the array from the second element to the end recursively. Then, insert the first element in its correct position in the sorted sub-array and return the sorted array.
- The time complexity of recursive insertion sort is O(n^2), where n is the number of elements in the array, in the worst case, and O(n) in the best case, when the array is already sorted.
- The space complexity of recursive insertion sort is O(n), where n is the number of elements in the array, due to the recursive call stack.
- The advantage of recursive insertion sort is that it is stable, i.e., it preserves the relative order of equal elements, and it performs well on nearly sorted arrays.
- The disadvantage of recursive insertion sort is that it is inefficient and does not perform well on large or reverse sorted arrays.

#### Recursive Bubble Sort

- Bubble sort is a sorting algorithm that works by comparing the adjacent elements and swapping them if they are in the wrong order.
- The recursive version of bubble sort works as follows:
  - Base case: If the array has one or zero elements, it is already sorted. Return the array.
  - Recursive case: Compare the first and second elements and swap them if they are in the wrong order. Then, sort the remaining array (from the second element to the end) recursively and return the sorted array.
- The time complexity of recursive bubble sort is O(n^2), where n is the number of elements in the array, in the worst case, and O(n) in the best case, when the array is already sorted.
- The space complexity of recursive bubble sort is O(n), where n is the number of elements in the array, due to the recursive call stack.
- The advantage of recursive bubble sort is that it is simple and easy to implement.
- The disadvantage of recursive bubble sort is that it is inefficient and does not perform well on large or reverse sorted arrays.

Some possible mnemonics and learning tricks for the topic are:

- For selection sort, you can remember the phrase "Select the smallest and swap".
- For insertion sort, you can remember the phrase "Insert in the right place".
- For bubble sort, you can remember the phrase "Bubble up the largest".
- For merge sort, you can remember the phrase "Divide and conquer".
- For quick sort, you can remember the phrase "Pick a pivot and partition".
- For heap sort, you can remember the phrase "Heapify and extract".