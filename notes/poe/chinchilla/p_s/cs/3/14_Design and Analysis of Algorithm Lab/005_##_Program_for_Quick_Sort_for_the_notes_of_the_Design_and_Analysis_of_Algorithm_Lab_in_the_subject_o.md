## Program for Quick Sort

Quick Sort is a widely used sorting algorithm that follows the divide-and-conquer approach. It is based on the partitioning of an array or a list into smaller sub-arrays. In this algorithm, a pivot element is selected, and the list is partitioned into two sub-arrays, one containing elements less than the pivot and the other containing elements greater than the pivot. The pivot element is then placed in its final position, and the algorithm is applied recursively to the sub-arrays on either side of the pivot.

### Steps of Quick Sort Algorithm

The following are the steps involved in the Quick Sort Algorithm:

1. Choose a pivot element.
2. Partition the array into two sub-arrays, one containing elements less than the pivot, and the other containing elements greater than the pivot.
3. Recursively apply the Quick Sort Algorithm to the sub-arrays.
4. Combine the sorted sub-arrays.

### Pseudo Code for Quick Sort Algorithm

```
function quickSort(array)
    if length(array) ≤ 1
        return array
    pivot ← choose any element of the array
    left ← [element for element in array if element < pivot]
    middle ← [element for element in array if element == pivot]
    right ← [element for element in array if element > pivot]
    return quickSort(left) + middle + quickSort(right)
```

### Advantages of Quick Sort Algorithm

1. It is an efficient sorting algorithm, with an average time complexity of O(n log n).
2. It is an in-place sorting algorithm, which means that it does not require additional memory for sorting.
3. It is a stable sorting algorithm, which means that the relative order of equal elements is preserved.

### Disadvantages of Quick Sort Algorithm

1. It is not a stable sorting algorithm, which means that the relative order of equal elements may not be preserved in the sorted output.
2. It may exhibit poor performance in the worst-case scenario, i.e., when the array is already sorted or nearly sorted.

### Example of Quick Sort Algorithm

Suppose we have an unsorted array of integers:

```
[5, 2, 9, 3, 7, 6, 1, 8, 4]
```

We choose the pivot element as 5 and partition the array into two sub-arrays:

```
[2, 3, 1, 4]  [5]  [9, 7, 6, 8]
```

We then apply the Quick Sort Algorithm recursively to the sub-arrays:

```
[2, 3, 1, 4] → [1, 2, 3, 4]
[9, 7, 6, 8] → [6, 7, 8, 9]
```

Finally, we combine the sorted sub-arrays:

```
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Applications of Quick Sort Algorithm

Quick Sort is used in many applications, including:

1. Sorting large datasets in computer science and data analysis.
2. Implementing search algorithms such as binary search.
3. Partitioning datasets in machine learning algorithms.
4. In database indexing and query optimization.