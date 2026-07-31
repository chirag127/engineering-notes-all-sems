Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of Sorting Algorithms-Non-Recursive for the notes of the Data Structure using C Lab in the subject of Data Structure using C:

```markdown
### Sorting Algorithms-Non-Recursive

- Sorting is the process of arranging a set of data items in a specific order, such as ascending or descending, based on some comparison criteria.
- Sorting algorithms are methods of implementing sorting operations in a computer program, using a sequence of instructions or steps.
- Non-recursive sorting algorithms are those that do not use recursion, which is a technique of calling a function within itself, to sort the data items.
- Some examples of non-recursive sorting algorithms are:

  - Selection sort: This algorithm repeatedly finds the smallest or largest element in the unsorted part of the array and places it at the end or beginning of the sorted part, respectively.
  - Bubble sort: This algorithm repeatedly compares and swaps adjacent elements in the array, until no more swaps are needed.
  - Insertion sort: This algorithm iterates over the array and inserts each element into its correct position in the sorted part of the array, by shifting the larger or smaller elements to the right or left, respectively.
  - Merge sort: This algorithm divides the array into two halves, recursively sorts each half, and then merges the two sorted halves into one sorted array.
  - Quick sort: This algorithm chooses a pivot element in the array, partitions the array into two subarrays such that all the elements less than or equal to the pivot are in the left subarray and all the elements greater than the pivot are in the right subarray, and then recursively sorts each subarray.
  - Heap sort: This algorithm builds a heap data structure from the array, and then repeatedly extracts the maximum or minimum element from the heap and places it at the end or beginning of the sorted array, respectively.

- The performance of non-recursive sorting algorithms depends on several factors, such as the size and distribution of the data items, the complexity and efficiency of the algorithm, and the memory and time constraints of the program.
- Some common measures of performance are:

  - Time complexity: This is the measure of how the running time of the algorithm grows as a function of the input size. It is usually expressed using the big O notation, which gives the upper bound of the worst-case scenario. For example, O(n^2) means that the running time of the algorithm is proportional to the square of the input size.
  - Space complexity: This is the measure of how much extra memory the algorithm requires to sort the data items. It is also expressed using the big O notation, which gives the upper bound of the worst-case scenario. For example, O(n) means that the algorithm requires memory proportional to the input size.
  - Stability: This is the property of the algorithm that preserves the relative order of the data items with equal values. For example, if the input array is [a, b, c, d, e, f, g, h] and the values of b and e are equal, then a stable sorting algorithm will produce the output array as [a, b, c, d, e, f, g, h], while an unstable sorting algorithm may produce the output array as [a, e, c, d, b, f, g, h].
  - Adaptability: This is the property of the algorithm that adjusts its behavior according to the characteristics of the input data. For example, an adaptive sorting algorithm will perform faster if the input array is already partially or fully sorted, while a non-adaptive sorting algorithm will perform the same regardless of the input array.

- The following table summarizes the time complexity, space complexity, stability, and adaptability of some non-recursive sorting algorithms:

| Algorithm   | Time complexity | Space complexity | Stability | Adaptability |
| ----------- | --------------- | ---------------- | --------- | ------------ |
| Selection   | O(n^2)          | O(1)             | No        | No           |
| Bubble      | O(n^2)          | O(1)             | Yes       | Yes          |
| Insertion   | O(n^2)          | O(1)             | Yes       | Yes          |
| Merge       | O(n log n)      | O(n)             | Yes       | No           |
| Quick       | O(n log n)      | O(log n)         | No        | No           |
| Heap        | O(n log n)      | O(1)             | No        | No           |

- To implement non-recursive sorting algorithms in C, we need to use arrays, loops, conditional statements, functions, and

```
