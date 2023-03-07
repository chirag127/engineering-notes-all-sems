 Here is the content in markdown format for the given topic:

## Program for Insertion Sort

Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It iterates through the list, and compares each item to the ones before it. If the item being looked at is smaller than the item before it, the two items swap positions. This continues until the list is sorted.

The steps for insertion sort are:

1. Start at index 1 (the first index is already sorted)
2. Take the current element and store it in a temp variable
3. Compare the current element to the previous element. If the current element is smaller, move the previous element to the next position.
4. Repeat step #3 until either the current element is larger than the previous element, or you reach the first element.
5. Insert the current element into the correct position.
6. Repeat steps #2 through #5 until the list is sorted.

**Pseudocode:**

```
for i = 1 to length(array)
    temp = array[i]
    j = i - 1
    while j >= 0 and temp < array[j]
        array[j + 1] = array[j]
        j = j - 1
    array[j + 1] = temp
end for
```

**Advantages:**

- Simple implementation
- Efficient for (quite) small data sets
- Adaptive - efficient for data sets that are already substantially sorted: it does not have to start all over again when it finds a value in the wrong place

**Disadvantages:**

- Inefficient on large lists/arrays
- Quadatic time complexity in the worst and average cases

**Examples:**

- [4, 3, 2, 1] -> Insertion sort will sort this array in 4 steps
- [8, 3, 5, 7, 1] -> Insertion sort will sort this array in 8 steps

**Applications:**

- Sorting small arrays/sub-arrays
- As a sub-routine in other sorting algorithms like Timsort
- When memory write is a costly operation ( Insertion sort uses fewer writes than other algorithms)