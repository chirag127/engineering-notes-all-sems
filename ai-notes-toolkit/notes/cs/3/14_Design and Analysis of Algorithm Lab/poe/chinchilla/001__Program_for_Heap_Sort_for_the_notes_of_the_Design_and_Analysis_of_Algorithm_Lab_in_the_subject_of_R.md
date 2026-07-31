## Program for Heap Sort

Heap Sort is a popular sorting algorithm that uses a binary heap data structure to sort an array. It has a time complexity of O(n log n) and is often used when the input size is large. Here is a program for Heap Sort:

1. Begin by creating a binary heap from the given array. This can be done by repeatedly inserting elements into the heap.

2. Once the heap is created, we can start sorting the array. The first step is to swap the root node with the last leaf node in the heap.

3. After the swap, we remove the last leaf node from the heap and decrement the size of the heap by one.

4. Next, we need to maintain the heap property. This is done by comparing the new root node with its children and swapping them if necessary.

5. We repeat steps 2-4 until the heap is empty. At each iteration, the largest element in the heap is moved to the end of the array.

6. Finally, we have a sorted array.

Here is the complete program for Heap Sort in C++:

```
void heapify(int arr[], int n, int i) {
    int largest = i;
    int l = 2*i + 1;
    int r = 2*i + 2;
 
    if (l < n && arr[l] > arr[largest])
        largest = l;
 
    if (r < n && arr[r] > arr[largest])
        largest = r;
 
    if (largest != i) {
        swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}
 
void heapSort(int arr[], int n) {
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);
 
    for (int i = n-1; i >= 0; i--) {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}
```

In conclusion, Heap Sort is a powerful sorting algorithm that can be used to sort large arrays quickly. By understanding how it works and implementing it in code, we can gain a deeper understanding of algorithms and data structures.