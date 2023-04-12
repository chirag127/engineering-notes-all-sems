### Sorting Algorithms-Recursive

Sorting algorithms are methods of arranging data in a specific order, such as ascending or descending. Sorting algorithms can be classified into two types: recursive and non-recursive. Recursive sorting algorithms work by splitting the input into two or more smaller inputs and then sorting those, then combining the results. Non-recursive sorting algorithms work by sorting the input in one pass, without dividing it into subproblems. Some examples of recursive sorting algorithms are:

- **Merge sort**: This algorithm divides the input array into two halves, recursively sorts each half, and then merges the two sorted halves into one sorted array. The merge operation requires an auxiliary array to store the merged elements. The time complexity of merge sort is O(n log n) in the average and worst cases, and the space complexity is O(n) in the worst case.
- **Quick sort**: This algorithm chooses a pivot element from the input array, partitions the array into two subarrays such that all the elements less than the pivot are in the left subarray and all the elements greater than or equal to the pivot are in the right subarray, and then recursively sorts the two subarrays. The choice of the pivot element affects the performance of quick sort. The time complexity of quick sort is O(n log n) in the average case and O(n^2) in the worst case, and the space complexity is O(log n) in the average case and O(n) in the worst case.
- **Heap sort**: This algorithm builds a binary heap from the input array, and then repeatedly extracts the maximum element from the heap and places it at the end of the array, reducing the size of the heap by one. The heapify operation maintains the heap property by swapping the parent node with the larger child node if necessary. The time complexity of heap sort is O(n log n) in the average and worst cases, and the space complexity is O(1) in the worst case.

Some examples of non-recursive sorting algorithms are:

- **Selection sort**: This algorithm finds the minimum element in the unsorted part of the input array and swaps it with the first element of the unsorted part, then repeats the process until the array is sorted. The time complexity of selection sort is O(n^2) in the average and worst cases, and the space complexity is O(1) in the worst case.
- **Bubble sort**: This algorithm compares adjacent elements in the input array and swaps them if they are in the wrong order, then repeats the process until the array is sorted. The time complexity of bubble sort is O(n^2) in the average and worst cases, and the space complexity is O(1) in the worst case.
- **Insertion sort**: This algorithm inserts each element in the input array into its correct position in the sorted part of the array, shifting the larger elements to the right if necessary. The time complexity of insertion sort is O(n^2) in the average and worst cases, and O(n) in the best case, and the space complexity is O(1) in the worst case.

Here are some examples of C programs for recursive sorting algorithms:

- **C Program for Recursive Merge Sort**:

```c
// A function to merge two sorted subarrays arr[l..m] and arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
    int i, j, k; 
    int n1 = m - l + 1; 
    int n2 = r - m; 
  
    // Create temp arrays 
    int L[n1], R[n2]; 
  
    // Copy data to temp arrays L[] and R[] 
    for (i = 0; i < n1; i++) 
        L[i] = arr[l + i]; 
    for (j = 0; j < n2; j++) 
        R[j] = arr[m + 1 + j]; 
  
    // Merge the temp arrays back into arr[l..r] 
    i = 0; // Initial index of first subarray 
    j = 0; // Initial index of second subarray 
    k = l; // Initial index of merged subarray 
    while (i < n1 && j < n2) { 
        if (L[i] <= R[j]) { 
            arr[k] = L[i]; 
            i++; 
        } 
        else { 
            arr[k] = R[j]; 
            j++;

```
