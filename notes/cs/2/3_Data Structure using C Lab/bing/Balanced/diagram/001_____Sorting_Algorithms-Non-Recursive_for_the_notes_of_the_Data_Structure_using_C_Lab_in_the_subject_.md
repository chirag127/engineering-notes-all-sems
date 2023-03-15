### Sorting Algorithms-Non-Recursive

- Sorting algorithms are a set of instructions that take an array or list as an input and arrange the items into a particular order.
- Sorting algorithms can be classified into two categories: recursive and non-recursive.
- Recursive sorting algorithms work by splitting the input into two or more smaller inputs and then sorting those, then combining the results. Merge sort and quick sort are examples of recursive sorting algorithms .
- Non-recursive sorting algorithms do not use recursion to sort the input. They use loops, pointers, or other techniques to sort the input in one pass or multiple passes. Insertion sort, selection sort, and bubble sort are examples of non-recursive sorting algorithms .
- Some sorting algorithms, such as merge sort, can be implemented using both recursive and non-recursive techniques.
- Non-recursive sorting algorithms are generally simpler and easier to understand than recursive sorting algorithms, but they may be less efficient or require more memory.
- In C, non-recursive sorting algorithms can be implemented using arrays, pointers, and loops. Here are some examples of non-recursive sorting algorithms in C:

#### Insertion Sort

- Insertion sort is a simple sorting algorithm that works by inserting each element of the input array into its correct position in a sorted subarray.
- The algorithm starts with the first element of the array as the sorted subarray, and then iterates over the remaining elements, inserting each one into the sorted subarray in the correct position.
- The algorithm maintains two pointers: one for the current element to be inserted, and one for the position where the element should be inserted.
- The algorithm shifts the elements of the sorted subarray to the right to make room for the new element, and then inserts the element at the correct position.
- The algorithm repeats this process until all the elements of the input array are inserted into the sorted subarray.
- The algorithm has a time complexity of O(n^2) in the worst case, where n is the number of elements in the input array.
- The algorithm has a space complexity of O(1), as it does not require any extra memory.
- Here is an example of insertion sort in C:

```c
// A function to sort an array using insertion sort
void insertionSort(int arr[], int n) {
  // Loop over the elements of the array, starting from the second element
  for (int i = 1; i < n; i++) {
    // Store the current element in a temporary variable
    int temp = arr[i];
    // Initialize a pointer to the position where the element should be inserted
    int j = i - 1;
    // Loop over the elements of the sorted subarray, starting from the end
    while (j >= 0 && arr[j] > temp) {
      // Shift the elements of the sorted subarray to the right
      arr[j + 1] = arr[j];
      // Decrement the pointer
      j--;
    }
    // Insert the element at the correct position
    arr[j + 1] = temp;
  }
}
```

#### Selection Sort

- Selection sort is a simple sorting algorithm that works by selecting the smallest or largest element of the input array and swapping it with the first or last element of the array, respectively.
- The algorithm then repeats this process for the remaining subarray, excluding the already sorted element.
- The algorithm maintains two pointers: one for the current element to be swapped, and one for the smallest or largest element in the remaining subarray.
- The algorithm iterates over the elements of the remaining subarray, updating the pointer to the smallest or largest element as it finds a smaller or larger element.
- The algorithm then swaps the current element with the smallest or largest element in the remaining subarray.
- The algorithm repeats this process until all the elements of the input array are sorted.
- The algorithm has a time complexity of O(n^2) in the worst case, where n is the number of elements in the input array.
- The algorithm has a space complexity of O(1), as it does not require any extra memory.
- Here is an example of selection sort in C:

```c
// A function to sort an array using selection sort
void selectionSort(int arr[], int n) {
  // Loop over the elements of the array, starting from the first element
  for (int i = 0; i < n - 1; i++) {
    // Initialize a pointer to the smallest element in the remaining