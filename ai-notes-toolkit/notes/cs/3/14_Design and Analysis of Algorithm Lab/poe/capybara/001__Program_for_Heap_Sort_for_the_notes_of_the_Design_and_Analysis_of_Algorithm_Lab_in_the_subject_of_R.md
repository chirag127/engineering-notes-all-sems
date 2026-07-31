## Program for Heap Sort

Heap Sort is an efficient sorting algorithm that uses a binary heap data structure to sort an array. Here is a program for Heap Sort that you can use for your Design and Analysis of Algorithm Lab in the subject of Real Time System:

1. Start by building a max heap from the given array.
    - The max heap is built by starting at the last non-leaf node of the binary tree and performing a max heapify operation on each node.
2. Swap the root node with the last element of the heap.
3. Reduce the heap size by one.
4. Perform a max heapify operation on the new root node.
5. Repeat steps 2-4 until the heap size is one.

Here is the pseudocode for the program:

```
void heapSort(int arr[], int n) {
    // Build max heap
    for (int i = n / 2 - 1; i >= 0; i--)
        maxHeapify(arr, n, i);
 
    // Extract elements from heap
    for (int i = n - 1; i >= 0; i--) {
        // Move current root to end
        swap(arr[0], arr[i]);
 
        // call max heapify on the reduced heap
        maxHeapify(arr, i, 0);
    }
}
 
void maxHeapify(int arr[], int n, int i) {
    int largest = i; // Initialize largest as root
    int l = 2 * i + 1; // left = 2*i + 1
    int r = 2 * i + 2; // right = 2*i + 2
 
    // If left child is larger than root
    if (l < n && arr[l] > arr[largest])
        largest = l;
 
    // If right child is larger than largest so far
    if (r < n && arr[r] > arr[largest])
        largest = r;
 
    // If largest is not root
    if (largest != i) {
        swap(arr[i], arr[largest]);
 
        // Recursively heapify the affected sub-tree
        maxHeapify(arr, n, largest);
    }
}
```

This program for Heap Sort has a time complexity of O(n log n) and a space complexity of O(1). It is a good choice for sorting large arrays because it is both efficient and easy to implement.