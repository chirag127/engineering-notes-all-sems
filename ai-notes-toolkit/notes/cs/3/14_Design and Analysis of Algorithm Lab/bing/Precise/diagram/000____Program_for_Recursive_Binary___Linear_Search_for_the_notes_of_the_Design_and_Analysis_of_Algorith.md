## Program for Recursive Binary & Linear Search for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

### Linear Search
Linear search is a simple search algorithm that involves iterating through an array or list of elements, comparing each element to the target value until a match is found or the end of the array is reached.

Here is an example of a recursive linear search function in C++:
```c++
int linearSearch(int arr[], int l, int r, int x)
{
    if (r < l)
        return -1;
    if (arr[l] == x)
        return l;
    if (arr[r] == x)
        return r;
    return linearSearch(arr, l + 1, r - 1, x);
}
```

### Binary Search
Binary search is a more efficient search algorithm that involves repeatedly dividing the search interval in half until the target value is found or the search interval is empty. This algorithm requires that the array or list being searched is sorted.

Here is an example of a recursive binary search function in C++:
```c++
int binarySearch(int arr[], int l, int r, int x)
{
    if (r >= l) {
        int mid = l + (r - l) / 2;
        if (arr[mid] == x)
            return mid;
        if (arr[mid] > x)
            return binarySearch(arr, l, mid - 1, x);
        return binarySearch(arr, mid + 1, r, x);
    }
    return -1;
}
```