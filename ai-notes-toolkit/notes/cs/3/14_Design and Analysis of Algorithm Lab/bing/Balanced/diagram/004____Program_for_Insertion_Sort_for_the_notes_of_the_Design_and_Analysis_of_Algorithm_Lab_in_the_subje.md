Hello, I am Sydney, your AI assistant. I can help you with your topic.

## Program for Insertion Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Insertion sort is a simple sorting algorithm that works by inserting each element of the array into its correct position in a sorted subarray.
- The algorithm starts with the first element as the sorted subarray and then iterates over the remaining elements, inserting each one into the sorted subarray in the right place.
- The algorithm can be implemented using a loop or a recursion.
- The algorithm has a time complexity of O(n^2) in the worst case, where n is the number of elements in the array.
- The algorithm is stable, meaning that it preserves the relative order of equal elements.
- The algorithm is adaptive, meaning that it performs better on partially sorted arrays.
- The algorithm is in-place, meaning that it does not require extra space to sort the array.

Here is a pseudocode for the insertion sort algorithm using a loop:

```
insertion_sort(array)
  for i from 1 to length(array) - 1
    key = array[i]
    j = i - 1
    while j >= 0 and array[j] > key
      array[j + 1] = array[j]
      j = j - 1
    array[j + 1] = key
  return array
```

Here is a pseudocode for the insertion sort algorithm using a recursion:

```
insertion_sort(array, n)
  if n <= 1
    return array
  insertion_sort(array, n - 1)
  key = array[n - 1]
  j = n - 2
  while j >= 0 and array[j] > key
    array[j + 1] = array[j]
    j = j - 1
  array[j + 1] = key
  return array
```

Here is a diagram to illustrate the insertion sort algorithm:

![Insertion Sort Diagram](https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif)