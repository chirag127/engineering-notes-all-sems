## Program for Selection Sort

Selection Sort is a simple sorting algorithm that sorts an array by repeatedly finding the minimum element from the unsorted part of the array and putting it at the beginning. In this lab, we will learn how to implement Selection Sort in a program and analyze its time complexity.

### Algorithm

The algorithm for Selection Sort is as follows:

1. Set the first element as the minimum.
2. Compare the minimum with the second element. If the second element is smaller than the minimum, set the second element as the new minimum.
3. Continue until the end of the array is reached.
4. If the minimum element is not the first element, swap the minimum element with the first element.
5. Repeat the above steps for the remaining elements of the array.

### Pseudo Code

```
selectionSort(arr, n)
  for i = 1 to n-1
    min_index = i
    for j = i+1 to n
      if arr[j] < arr[min_index]
        min_index = j
    swap(arr[min_index], arr[i])
```

### Time Complexity

The time complexity of Selection Sort is O(n^2), where n is the number of elements in the array. This is because the algorithm requires two nested loops to traverse the array and find the minimum element.

### Advantages

- Simple and easy to implement.
- Memory efficient as it requires only one additional memory space for swapping.

### Disadvantages

- Inefficient for large data sets.
- Time complexity is O(n^2), which makes it slower than other sorting algorithms like Quick Sort and Merge Sort.

### Example

Let's consider an array of integers: {64, 25, 12, 22, 11}

1. First iteration: 11 25 12 22 64
2. Second iteration: 11 12 25 22 64
3. Third iteration: 11 12 22 25 64
4. Fourth iteration: 11 12 22 25 64
5. Array is sorted.

### Applications

Selection Sort can be used in situations where the data set is small or where memory space is limited. It is often used as a sub-routine for other sorting algorithms like Quick Sort and Merge Sort.