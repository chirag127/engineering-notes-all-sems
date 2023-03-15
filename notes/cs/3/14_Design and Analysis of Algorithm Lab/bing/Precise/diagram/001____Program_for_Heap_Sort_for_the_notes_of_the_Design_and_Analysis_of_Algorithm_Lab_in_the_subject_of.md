## Program for Heap Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure. It works by dividing the input into a sorted and an unsorted region, and iteratively shrinking the unsorted region by extracting the largest element and moving that to the sorted region. The improvement consists of the use of a heap data structure rather than a linear-time search to find the maximum.

Here is an example of a heap sort algorithm in C++:

```c++
#include <iostream>
using namespace std;
  
void heapify(int arr[], int n, int i)
{
    int largest = i; 
    int l = 2*i + 1; 
    int r = 2*i + 2; 
  
    if (l < n && arr[l] > arr[largest])
        largest = l;
  
    if (r < n && arr[r] > arr[largest])
        largest = r;
  
    if (largest != i)
    {
        swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}
  
void heapSort(int arr[], int n)
{
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);
  
    for (int i=n-1; i>0; i--)
    {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}
  
void printArray(int arr[], int n)
{
    for (int i=0; i<n; ++i)
        cout << arr[i] << " ";
    cout << "\n";
}
  
int main()
{
    int arr[] = {12, 11, 13, 5, 6, 7};
    int n = sizeof(arr)/sizeof(arr[0]);
  
    heapSort(arr, n);
  
    cout << "Sorted array is \n";
    printArray(arr, n);
}
```

This program first defines a `heapify` function, which is used to maintain the heap property of the array. The `heapSort` function uses this `heapify` function to sort the array. Finally, the `printArray` function is used to print the sorted array.

The time complexity of heap sort is O(n log n) in the worst, average, and best cases. This makes it an efficient sorting algorithm for large data sets.