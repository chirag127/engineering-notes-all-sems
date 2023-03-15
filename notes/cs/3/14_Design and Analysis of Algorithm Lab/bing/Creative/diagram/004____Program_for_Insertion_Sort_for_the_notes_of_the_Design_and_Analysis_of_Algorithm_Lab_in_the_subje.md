## Program for Insertion Sort

Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time by comparisons. It works similar to the way you sort playing cards in your hands. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort. However, insertion sort provides several advantages:

- It is easy to implement and understand.
- It is stable, meaning that it preserves the relative order of equal elements.
- It is adaptive, meaning that it performs well on partially sorted arrays.
- It requires constant extra space, meaning that it only uses one additional variable to store the current element.
- It can sort the array as it receives it, meaning that it is suitable for online or streaming data.

The main idea of insertion sort is to divide the array into two parts: a sorted part and an unsorted part. Initially, the sorted part contains only the first element of the array, and the unsorted part contains the rest of the elements. Then, the algorithm picks one element from the unsorted part and inserts it into the correct position in the sorted part, shifting the elements that are greater than it to the right. This process is repeated until the unsorted part is empty and the array is sorted.

The pseudocode for insertion sort is as follows:

```
insertion_sort(array)
  for i = 1 to array.length - 1
    key = array[i] // store the current element
    j = i - 1 // start from the previous element
    while j >= 0 and array[j] > key // compare with the elements in the sorted part
      array[j + 1] = array[j] // shift the greater elements to the right
      j = j - 1 // move to the next element
    array[j + 1] = key // insert the current element into the correct position
  end for
end insertion_sort
```

The following diagram illustrates how insertion sort works on an example array [12, 11, 13, 5, 6]:

![insertion sort diagram](https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif)

The time complexity of insertion sort is O(n^2) in the worst case, when the array is in reverse order, and O(n) in the best case, when the array is already sorted. The average case is also O(n^2), but with a smaller constant factor than the worst case. The space complexity of insertion sort is O(1), since it only uses one additional variable.