# Program for Insertion Sort

- Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time by comparisons .
- It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort .
- However, insertion sort provides several advantages:
  - It is easy to implement and understand.
  - It is stable, meaning that it preserves the relative order of equal elements.
  - It is adaptive, meaning that it performs well on nearly sorted lists.
  - It requires constant space and no auxiliary data structures.
  - It can sort a list as it receives it, making it suitable for online or streaming problems.
- The basic idea of insertion sort is to divide the list into two parts: a sorted part and an unsorted part .
- Initially, the sorted part contains only the first element of the list, and the unsorted part contains the rest of the elements.
- The algorithm then iterates over the unsorted part, picking one element at a time and inserting it into the correct position in the sorted part.
- To insert an element into the sorted part, the algorithm shifts all the elements that are greater than the element to the right, making space for the element to be inserted.
- The algorithm repeats this process until the unsorted part is empty and the sorted part contains all the elements of the list.
- The following pseudocode illustrates the insertion sort algorithm:

```
insertion_sort(list)
  for i = 1 to length(list) - 1
    key = list[i] // the element to be inserted
    j = i - 1 // the index of the last element in the sorted part
    while j >= 0 and list[j] > key
      list[j + 1] = list[j] // shift the element to the right
      j = j - 1 // move to the next element in the sorted part
    end while
    list[j + 1] = key // insert the element into the correct position
  end for
end insertion_sort
```

- The following is an example of insertion sort on a list of numbers:

```
list = [5, 2, 4, 6, 1, 3]

// i = 1, key = 2, j = 0
// list[j] > key, so shift 5 to the right and insert 2 at the beginning
list = [2, 5, 4, 6, 1, 3]

// i = 2, key = 4, j = 1
// list[j] > key, so shift 5 to the right and insert 4 after 2
list = [2, 4, 5, 6, 1, 3]

// i = 3, key = 6, j = 2
// list[j] < key, so no shifting is needed and 6 stays in place
list = [2, 4, 5, 6, 1, 3]

// i = 4, key = 1, j = 3
// list[j] > key, so shift 6, 5, 4, and 2 to the right and insert 1 at the beginning
list = [1, 2, 4, 5, 6, 3]

// i = 5, key = 3, j = 4
// list[j] > key, so shift 6 and 5 to the right and insert 3 after 4
list = [1, 2, 4, 3, 5, 6]

// the unsorted part is empty and the sorted part contains all the elements
list = [1, 2, 4, 3, 5, 6]
```

- The time complexity of insertion sort is O(n^2) in the worst case and O(n) in the best case, where n is the number of elements in the list .
- The worst case occurs when the list is in reverse order, and the best case occurs when the list is already sorted.
- The space complexity of insertion sort is O(1), as it only requires constant space for the key and the indices .