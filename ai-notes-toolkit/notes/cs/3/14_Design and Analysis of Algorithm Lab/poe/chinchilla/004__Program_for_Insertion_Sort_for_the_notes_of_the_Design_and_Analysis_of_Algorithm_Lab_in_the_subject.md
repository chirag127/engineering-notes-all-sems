## Program for Insertion Sort

Insertion Sort is a simple sorting algorithm that works by iteratively building a sorted sublist from an unsorted list. It is an efficient algorithm for small data sets or lists that are almost sorted. In this lab, we will learn how to implement the Insertion Sort algorithm using a program.

### Steps for implementing Insertion Sort

1. Start by defining a function called `insertion_sort` that takes an array of integers as input.

2. The first step in the Insertion Sort algorithm is to iterate through the unsorted list, starting from the second element. For each element, we need to compare it with the elements before it and insert it in the correct position in the sorted sublist.

3. To do this, we need to define a variable called `key` that will hold the value of the current element being sorted.

4. We then iterate through the sorted sublist, starting from the last element and moving towards the beginning. For each element, we compare it with the `key`. If the element is greater than the `key`, we move the element one position to the right.

5. We continue this process until we find an element that is less than or equal to the `key`. We then insert the `key` at the position immediately after this element.

6. Once we have sorted the entire list in this manner, we return the sorted array.

### Sample implementation of Insertion Sort in Python

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

### Conclusion

Insertion Sort is a simple yet effective sorting algorithm that can be implemented easily using a program. By iterating through the unsorted list and building a sorted sublist, we can quickly sort small data sets or lists that are almost sorted.