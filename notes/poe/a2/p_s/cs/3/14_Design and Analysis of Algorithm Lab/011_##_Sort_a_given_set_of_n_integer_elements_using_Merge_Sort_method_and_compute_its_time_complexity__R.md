 Here is the content in markdown format:

## Sort a given set of n integer elements using Merge Sort method and compute its time complexity.

Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves and then merges the two sorted halves. The following steps are followed in Merge Sort:

1. Divide the unsorted array into two halves
2. Recursively sort the two halves
3. Merge the two sorted halves into one sorted array

The time complexity of Merge Sort is:

- Worst Case: O(n log n)
- Average Case: O(n log n)
- Best Case: O(n log n)

The space complexity is O(n) as an additional array of size n is needed for merging.

To implement Merge Sort:

1. Divide the array into two halves: middle = (low + high) / 2
2. Sort the left half: mergeSort(arr, low, middle)
3. Sort the right half: mergeSort(arr, middle + 1, high)
4. Merge the two halves: merge(arr, low, middle, high)

The merge() function merges the two sorted halves into a single sorted array. It uses two pointers, one traversing the left half and one traversing the right half. At each step, the smaller element from either half is picked and added to the final sorted array.

To analyze the time complexity, the overall time taken is the summation of time taken for dividing the array and time taken for merging the halves. As the array is divided into halves in each step, the height of recursion tree will be log n. Also, each level of the recursion tree will do a merge operation whose time complexity is O(n). Therefore, the time complexity is O(n log n).

To run the program and plot a graph:

1. Take input for the size of the array n
2. Generate random integers to fill the array
3. Call mergeSort() on the array
4. Record the time taken to sort the array
5. Repeat steps 1-4 for different values of n (greater than 5000)
6. Plot a graph of time taken vs n

The graph will be a straight line showing the linearithmic time complexity of Merge Sort.