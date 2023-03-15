Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the program for merge sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System.

## Program for Merge Sort

Merge sort is a divide-and-conquer algorithm that splits an array into two halves, recursively sorts each half, and then merges them back together in order. The algorithm can be implemented using the following steps:

- Define a function `merge_sort` that takes an array `arr` and two indices `low` and `high` as parameters. The function should sort the subarray `arr[low..high]` using merge sort.
- If `low` is equal to `high`, then the subarray has only one element and is already sorted. Return from the function.
- Otherwise, find the middle index `mid` by adding `low` and `high` and dividing by two.
- Recursively call `merge_sort` on the left half `arr[low..mid]` and the right half `arr[mid+1..high]`.
- Define another function `merge` that takes an array `arr` and three indices `low`, `mid`, and `high` as parameters. The function should merge the sorted subarrays `arr[low..mid]` and `arr[mid+1..high]` into a single sorted subarray `arr[low..high]`.
- Create two temporary arrays `left` and `right` to store the elements of the left and right subarrays. Copy the elements from `arr[low..mid]` to `left` and from `arr[mid+1..high]` to `right`.
- Initialize three variables `i`, `j`, and `k` to zero, zero, and `low` respectively. These variables will keep track of the indices of the `left`, `right`, and `arr` arrays.
- Use a while loop to iterate until either `i` or `j` reaches the end of their respective arrays. Compare the elements at `left[i]` and `right[j]` and copy the smaller one to `arr[k]`. Increment `i`, `j`, and `k` accordingly.
- Use another while loop to copy the remaining elements from `left` or `right` to `arr` if any.
- Return from the function `merge`.
- Call the function `merge_sort` on the entire array `arr` with `low` as zero and `high` as the length of the array minus one.

Here is an example of the program in C language:

```c
#include <stdio.h>

// Function to merge two sorted subarrays arr[low..mid] and arr[mid+1..high]
void merge(int arr[], int low, int mid, int high)
{
    // Create two temporary arrays to store the elements of the left and right subarrays
    int n1 = mid - low + 1; // Size of the left subarray
    int n2 = high - mid; // Size of the right subarray
    int left[n1], right[n2]; // Temporary arrays

    // Copy the elements from arr[low..mid] to left and from arr[mid+1..high] to right
    for (int i = 0; i < n1; i++)
        left[i] = arr[low + i];
    for (int j = 0; j < n2; j++)
        right[j] = arr[mid + 1 + j];

    // Initialize three variables to keep track of the indices of the left, right, and arr arrays
    int i = 0, j = 0, k = low;

    // Use a while loop to iterate until either i or j reaches the end of their respective arrays
    while (i < n1 && j < n2)
    {
        // Compare the elements at left[i] and right[j] and copy the smaller one to arr[k]
        if (left[i] <= right[j])
        {
            arr[k] = left[i];
            i++;
        }
        else
        {
            arr[k] = right[j];
            j++;
        }
        k++;
    }

    // Use another while loop to copy the remaining elements from left or right to arr if any
    while (i < n1)
    {
        arr[k] = left[i];
        i++;
        k++;
    }
    while (j < n2)
    {
        arr[k] = right[j];
        j++;
        k++;
    }
}

// Function to sort an array arr[low..high] using merge sort
void merge_sort(int arr[], int low, int high