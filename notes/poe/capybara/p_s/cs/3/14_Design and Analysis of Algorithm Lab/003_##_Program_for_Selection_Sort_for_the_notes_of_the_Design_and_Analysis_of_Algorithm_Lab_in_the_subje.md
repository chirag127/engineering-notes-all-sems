## Program for Selection Sort

Selection sort is a simple sorting algorithm that works by repeatedly finding the minimum element from the unsorted part of the array and putting it at the beginning. This algorithm is easy to understand and implement, making it a good choice for small datasets.

The program for selection sort can be written in any programming language. Here, we will provide an example in Python:

```
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

This implementation takes an array as input and returns the sorted array using selection sort. The outer loop runs from 0 to n-1, indicating the range of the unsorted part of the array. The inner loop finds the minimum element from the unsorted part and swaps it with the first element of the unsorted part.

Advantages of Selection Sort:
- Simple and easy to understand and implement.
- Requires only a single extra memory space for the minimum element.
- Performs well for small datasets.

Disadvantages of Selection Sort:
- Inefficient for large datasets as it has a time complexity of O(n^2).
- Not stable, meaning that the relative order of equal elements may change.

Applications of Selection Sort:
- Useful when memory is limited and the dataset is small.
- Can be used as a subroutine in more complex sorting algorithms.

Overall, the program for selection sort is a basic yet effective sorting algorithm that can be used for small datasets. It is important to understand its advantages and disadvantages in order to choose the appropriate sorting algorithm for a given dataset.