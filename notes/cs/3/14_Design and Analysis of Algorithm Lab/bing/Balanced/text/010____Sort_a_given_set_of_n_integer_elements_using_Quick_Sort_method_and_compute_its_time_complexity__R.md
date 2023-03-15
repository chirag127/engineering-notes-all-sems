## Sort a given set of n integer elements using Quick Sort method and compute its time complexity. Run the program for varied values of n> 5000 and record the time taken to sort. Plot a graph of the time taken versus non graph sheet. The elements can be read from a file or can be generated using the random number generator. Demonstrate using Java how the divide and- conquer method works along with its time complexity analysis: worst case, average case and best case.

- Quick Sort is a sorting algorithm that uses the divide and conquer method to partition the array into two subarrays based on a pivot element, such that the elements in the left subarray are smaller than or equal to the pivot and the elements in the right subarray are larger than or equal to the pivot. Then, the algorithm recursively sorts the subarrays until the array is sorted.
- The time complexity of Quick Sort depends on the choice of the pivot element and the distribution of the elements in the array. The best case occurs when the pivot is the median of the array, which results in a balanced partition and a time complexity of O(n log n). The average case also has a time complexity of O(n log n), assuming that the pivot is chosen randomly or by using some heuristic. The worst case occurs when the pivot is the smallest or the largest element of the array, which results in an unbalanced partition and a time complexity of O(n^2).
- To implement Quick Sort in Java, we need to define a method that takes an array, a low index and a high index as parameters, and returns the index of the pivot after partitioning the array. The method can use any strategy to choose the pivot, such as the first element, the last element, the middle element, or a random element. The method can also use a swap method to exchange the elements in the array. The pseudocode of the partition method is as follows:

```
partition(array, low, high):
  pivot = array[low] // choose the first element as the pivot
  i = low + 1 // initialize the index of the first element larger than the pivot
  j = high // initialize the index of the last element smaller than the pivot
  while i <= j: // loop until the indices cross
    while i <= high and array[i] <= pivot: // find the first element larger than the pivot
      i = i + 1
    while j >= low and array[j] > pivot: // find the last element smaller than the pivot
      j = j - 1
    if i < j: // swap the elements if they are out of order
      swap(array, i, j)
  swap(array, low, j) // swap the pivot with the element at j
  return j // return the index of the pivot
```

- To sort the array using Quick Sort, we need to define another method that takes an array, a low index and a high index as parameters, and recursively calls the partition method and itself until the array is sorted. The pseudocode of the quickSort method is as follows:

```
quickSort(array, low, high):
  if low < high: // check if the array has more than one element
    pivot = partition(array, low, high) // partition the array and get the index of the pivot
    quickSort(array, low, pivot - 1) // sort the left subarray
    quickSort(array, pivot + 1, high) // sort the right subarray
```

- To measure the time taken to sort the array using Quick Sort, we need to use the System.nanoTime() method to get the current time in nanoseconds before and after calling the quickSort method, and calculate the difference. We also need to generate an array of n random integers using the Random class or read the elements from a file. The pseudocode of the main method is as follows:

```
main():
  n = input("Enter the size of the array: ") // get the size of the array from the user
  array = new int[n] // create an array of n integers
  random = new Random() // create a random number generator
  for i = 0 to n - 1: // loop through the array
    array[i] = random.nextInt(10000) // generate a random integer between 0 and 9999 and assign it to the array
  // alternatively, read the elements from a file using a Scanner or a BufferedReader
  startTime = System.nanoTime() // get the current time in nanoseconds
  quickSort(array, 0, n - 1) // sort the array using Quick Sort
  endTime = System.nanoTime() // get the current time in nanoseconds