## Program for Insertion Sort

Insertion Sort is one of the simplest sorting algorithms that works by iterating through the array and inserting each element into its proper position in a new sorted array. 

### Algorithm

The algorithm for Insertion Sort is as follows:
1. Iterate from arr[1] to arr[n] over the array.
2. Compare the current element (key) to its predecessor.
3. If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.
4. Repeat the above steps until the entire array is sorted.

### Pseudo Code

```
insertionSort(arr, n)
   for i = 1 to n-1
      key = arr[i]
      j = i-1
      while j >= 0 and arr[j] > key
         arr[j+1] = arr[j]
         j = j-1
      arr[j+1] = key
```

### Complexity

- Time Complexity: O(n^2)
- Space Complexity: O(1)

### Advantages

- Simple and easy to implement
- Efficient for small data sets
- In-place sorting algorithm, meaning no additional temporary space is needed

### Disadvantages

- Inefficient for large data sets
- Performs poorly with reverse-ordered or almost sorted data sets

### Example

Let's consider the following array:

```
arr[] = {5, 2, 4, 6, 1, 3}
```

After the first iteration, the array will be:

```
arr[] = {2, 5, 4, 6, 1, 3}
```

After the second iteration, the array will be:

```
arr[] = {2, 4, 5, 6, 1, 3}
```

And so on, until the entire array is sorted.

### Applications

Insertion Sort can be useful in situations where:

- The data set is small
- The data set is already partially sorted
- The data set is almost sorted

It is commonly used as a subroutine in more complex sorting algorithms such as QuickSort and MergeSort.