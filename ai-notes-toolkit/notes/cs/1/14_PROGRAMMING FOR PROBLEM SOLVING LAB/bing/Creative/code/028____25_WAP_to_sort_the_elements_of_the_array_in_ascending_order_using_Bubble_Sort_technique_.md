Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write a program to sort the elements of the array in ascending order using Bubble Sort technique. Here is the content in markdown format:

## 25.WAP to sort the elements of the array in ascending order using Bubble Sort technique.

Bubble Sort is a simple sorting algorithm that compares adjacent elements in an array and swaps them if they are in the wrong order. The algorithm repeats this process until the array is sorted. The name comes from the fact that the smaller elements "bubble" to the top of the array.

The steps of the algorithm are:

- Start from the first element of the array and compare it with the next element. If the first element is greater than the second element, swap them. Otherwise, leave them as they are.
- Move to the next pair of elements and repeat the same comparison and swapping process.
- Continue this process until the end of the array is reached. This completes one pass of the algorithm.
- Repeat the same process for the remaining passes, but reduce the size of the array by one element each time, as the last element of each pass is already in its correct position.
- The algorithm stops when no swaps are made in a pass, which means the array is sorted.

Here is an example of how the algorithm works on an array of five elements:

| Pass | Array | Comparisons | Swaps |
| --- | --- | --- | --- |
| 0 | [5, 3, 4, 2, 1] | - | - |
| 1 | [3, 4, 2, 1, 5] | 5 - 3, 5 - 4, 4 - 2, 2 - 1 | 4 |
| 2 | [3, 2, 1, 4, 5] | 3 - 2, 3 - 1, 2 - 4 | 3 |
| 3 | [2, 1, 3, 4, 5] | 2 - 1, 2 - 3 | 1 |
| 4 | [1, 2, 3, 4, 5] | 1 - 2 | 0 |
| 5 | [1, 2, 3, 4, 5] | - | 0 |

The algorithm takes 5 passes and 8 swaps to sort the array.

Here is a pseudocode of the algorithm:

```
bubble_sort(array)
  n = length of array
  repeat
    swapped = false
    for i = 0 to n - 2
      if array[i] > array[i + 1]
        swap array[i] and array[i + 1]
        swapped = true
    n = n - 1
  until swapped is false
```

Here is a possible implementation of the algorithm in Python:

```python
def bubble_sort(array):
  n = len(array)
  while True:
    swapped = False
    for i in range(n - 1):
      if array[i] > array[i + 1]:
        array[i], array[i + 1] = array[i + 1], array[i]
        swapped = True
    n = n - 1
    if not swapped:
      break
  return array
```

Here is a sample input and output of the program:

```
Input: [5, 3, 4, 2, 1]
Output: [1, 2, 3, 4, 5]
```

The time complexity of the algorithm is O(n^2) in the worst case, when the array is in reverse order. The space complexity is O(1), as the algorithm only uses constant extra space. The algorithm is stable, meaning it preserves the relative order of equal elements. The algorithm is adaptive, meaning it performs better on nearly sorted arrays. However, the algorithm is not efficient for large arrays, as it makes many unnecessary comparisons and swaps. There are other sorting algorithms that are faster and more suitable for large arrays, such as Merge Sort, Quick Sort, or Heap Sort.