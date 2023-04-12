### Searching Algorithm for the notes of the Data Structure using C Lab in the subject of Data Structure using C

- A searching algorithm is a method of finding an element or a value in a data structure, such as an array or a list.
- There are two main types of searching algorithms: linear search and binary search .
- Linear search is a simple technique that checks each element of the data structure sequentially until a match is found or the end is reached .
- Binary search is a more efficient technique that works only on sorted data structures and divides the search space into half at each step until a match is found or the search space is empty .
- The following are some points to compare linear search and binary search:

| Linear Search | Binary Search |
|---------------|---------------|
| Works on any data structure, sorted or unsorted | Works only on sorted data structures |
| Time complexity is O(n), where n is the number of elements in the data structure | Time complexity is O(log n), where n is the number of elements in the data structure |
| Does not require any extra space | Requires extra space to store the subarrays |
| Easy to implement and understand | More complex to implement and understand |
| Less efficient and slower | More efficient and faster |

- The following are some examples of linear search and binary search algorithms in C:

```c
// Linear search algorithm in C
#include <stdio.h>

// Function to perform linear search on an array
int linear_search(int arr[], int n, int x)
{
    // Loop through the array from index 0 to n-1
    for (int i = 0; i < n; i++)
    {
        // If the current element is equal to x, return its index
        if (arr[i] == x)
        {
            return i;
        }
    }
    // If x is not found in the array, return -1
    return -1;
}

// Driver code to test the function
int main()
{
    // Declare an array of 8 elements
    int arr[] = {8, 7, 2, 6, 4, 5, 4, 0};
    // Declare the size and the search element
    int n = sizeof(arr) / sizeof(arr[0]);
    int x = 4;
    // Call the linear search function and print the result
    int result = linear_search(arr, n, x);
    if (result == -1)
    {
        printf("%d is not present in the array.\n", x);
    }
    else
    {
        printf("%d is present at index %d in the array.\n", x, result);
    }
    return 0;
}
```

```c
// Binary search algorithm in C
#include <stdio.h>

// Function to perform binary search on a sorted array
int binary_search(int arr[], int low, int high, int x)
{
    // Check if the search space is valid
    if (low <= high)
    {
        // Find the middle index of the search space
        int mid = (low + high) / 2;
        // If the middle element is equal to x, return its index
        if (arr[mid] == x)
        {
            return mid;
        }
        // If the middle element is greater than x, search in the left subarray
        else if (arr[mid] > x)
        {
            return binary_search(arr, low, mid - 1, x);
        }
        // If the middle element is less than x, search in the right subarray
        else
        {
            return binary_search(arr, mid + 1, high, x);
        }
    }
    // If x is not found in the array, return -1
    return -1;
}

// Driver code to test the function
int main()
{
    // Declare a sorted array of 8 elements
    int arr[] = {0, 2, 4, 4, 5, 6, 7, 8};
    // Declare the size and the search element
    int n = sizeof(arr) / sizeof(arr[0]);
    int x = 4;
    // Call the binary search function and print the result
    int result = binary_search(arr, 0, n - 1, x);
    if (result == -1)
    {
        printf("%d is not present in the

```
