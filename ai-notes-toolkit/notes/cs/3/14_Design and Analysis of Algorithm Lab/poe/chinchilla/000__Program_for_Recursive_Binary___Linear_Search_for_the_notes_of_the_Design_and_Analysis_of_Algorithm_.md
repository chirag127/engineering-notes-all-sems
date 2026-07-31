## Program for Recursive Binary & Linear Search

In this section, we will discuss the program for Recursive Binary & Linear Search. These search algorithms are widely used in computer science to find a specific element in a sorted array.

### Linear Search
Linear search is a simple algorithm that searches for an element in an array by sequentially checking each element of the array until a match is found or the end of the array is reached. The time complexity of linear search is O(n).

Here is the program for linear search in C++:

```c++
int linearSearch(int arr[], int n, int x) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == x)
            return i;
    }
    return -1;
}
```

### Recursive Binary Search
Binary search is a more efficient algorithm that searches for an element in a sorted array by repeatedly dividing the search interval in half. The time complexity of binary search is O(log n).

Here is the program for recursive binary search in C++:

```c++
int binarySearch(int arr[], int low, int high, int x) {
    if (low > high)
        return -1;
    int mid = (low + high) / 2;
    if (arr[mid] == x)
        return mid;
    else if (arr[mid] > x)
        return binarySearch(arr, low, mid - 1, x);
    else
        return binarySearch(arr, mid + 1, high, x);
}
```

In the above program, we first check if the search interval is empty (i.e., low > high). If it is, we return -1 to indicate that the element was not found. Otherwise, we calculate the middle index of the interval and compare the middle element with the search element. If they are equal, we return the middle index. Otherwise, we recursively search the left or right half of the interval depending on whether the middle element is greater or less than the search element.

### Conclusion
In this section, we discussed the programs for Recursive Binary & Linear Search. These algorithms are widely used in computer science to search for a specific element in a sorted array. The binary search algorithm is more efficient than the linear search algorithm, but it requires the array to be sorted.