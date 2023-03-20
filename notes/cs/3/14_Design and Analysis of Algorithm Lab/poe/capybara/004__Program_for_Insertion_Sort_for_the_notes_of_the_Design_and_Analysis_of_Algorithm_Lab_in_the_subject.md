## Program for Insertion Sort

Insertion Sort is a simple sorting algorithm that works by repeatedly inserting the elements of an array into a sorted subarray. Here is a program for implementing Insertion Sort:

1. Start the program by defining an array that needs to be sorted.
2. Determine the length of the array.
3. Begin the loop for traversing the array. The loop counter starts from 1 and goes up to the length of the array.
4. Store the current element in a temporary variable.
5. Set a variable for the index of the previous element.
6. Begin the loop for comparing the current element with the elements before it. The loop counter starts from the index of the current element and goes down to 0.
7. Compare the current element with the element at the previous index. If the current element is smaller than the previous element, then swap their positions in the array.
8. Decrement the index of the previous element.
9. Repeat steps 7-8 until the current element is in its correct position in the sorted subarray.
10. Move on to the next element in the outer loop and repeat steps 4-9 until all elements have been sorted.

```c
void insertionSort(int arr[], int n) {
    int i, key, j;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;
 
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}
```

This program takes an array `arr` and its length `n` as input, and sorts the array using the Insertion Sort algorithm. It does this by iterating through the array and comparing each element with the elements before it, swapping their positions if necessary.

Insertion Sort has a time complexity of O(n^2), which means that it is not suitable for sorting large arrays. However, it is a simple algorithm that is easy to implement and works well for small arrays or partially sorted arrays.

In conclusion, Insertion Sort is a simple sorting algorithm that can be easily implemented in a program. It works by repeatedly inserting elements into a sorted subarray and has a time complexity of O(n^2).