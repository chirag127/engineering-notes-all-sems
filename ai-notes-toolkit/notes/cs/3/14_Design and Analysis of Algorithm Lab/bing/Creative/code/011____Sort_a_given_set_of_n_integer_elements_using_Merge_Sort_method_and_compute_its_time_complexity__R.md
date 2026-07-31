Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is the content in markdown format:

## Sort a given set of n integer elements using Merge Sort method and compute its time complexity. Run the program for varied values of n> 5000, and record the time taken to sort. Plot a graph of the time taken versus non graph sheet. The elements can be read from a file or can be generated using the random number generator. Demonstrate how the divide and- conquer method works along with its time complexity analysis: worst case, average case and best case.

### Merge Sort
- Merge sort is a sorting algorithm that uses the divide and conquer technique to sort a given set of n integer elements.
- The algorithm works as follows:
  - Divide the input array into two halves, left and right, recursively until each subarray has only one element.
  - Merge the two sorted subarrays into one sorted array by comparing the elements from each subarray and picking the smaller one.
  - Return the sorted array as the final output.
- The pseudocode for merge sort is:

```
merge_sort(array, low, high):
  if low < high:
    mid = (low + high) / 2
    merge_sort(array, low, mid)
    merge_sort(array, mid + 1, high)
    merge(array, low, mid, high)

merge(array, low, mid, high):
  n1 = mid - low + 1
  n2 = high - mid
  create two temporary arrays left and right of size n1 and n2
  copy the elements from array[low..mid] to left[0..n1-1]
  copy the elements from array[mid+1..high] to right[0..n2-1]
  i = 0, j = 0, k = low
  while i < n1 and j < n2:
    if left[i] <= right[j]:
      array[k] = left[i]
      i = i + 1
    else:
      array[k] = right[j]
      j = j + 1
    k = k + 1
  while i < n1:
    array[k] = left[i]
    i = i + 1
    k = k + 1
  while j < n2:
    array[k] = right[j]
    j = j + 1
    k = k + 1
```

### Time Complexity
- The time complexity of merge sort is O(n log n) for the worst case, average case and best case scenarios.
- This is because the algorithm divides the input array into two halves at each level of recursion, resulting in log n levels of recursion.
- At each level, the algorithm merges two subarrays of size n/2, resulting in n comparisons and n assignments, resulting in O(n) time complexity at each level.
- Therefore, the total time complexity is O(n log n) for all cases.

### Experiment
- To run the program for varied values of n > 5000, and record the time taken to sort, we can use the following steps:
  - Import the time module in Python to measure the execution time of the program.
  - Import the random module in Python to generate random numbers for the input array.
  - Define a function to generate an array of n random numbers in the range [1, 10000].
  - Define a function to write the array to a file named input.txt.
  - Define a function to read the array from the file input.txt.
  - Define a function to plot a graph of the time taken versus n using matplotlib.pyplot module in Python.
  - Define a list of values for n, such as [5000, 10000, 15000, 20000, 25000, 30000].
  - For each value of n, do the following:
    - Generate an array of n random numbers and write it to the file input.txt.
    - Read the array from the file input.txt and store it in a variable named array.
    - Start a timer using time.time() and store the value in a variable named start.
    - Call the merge_sort function on the array and store the sorted array in a variable named sorted_array.
    - Stop the timer using time.time() and store the value in a variable named end.
    - Calculate the time taken to sort the array by subtracting start from end and store the value in a variable named time_taken.
    - Print the value of n and time_taken to the console.
    - Append the value of n and time_taken to two lists named x and y respectively.
  - Call the