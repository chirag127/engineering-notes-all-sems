## Program for Recursive Binary & Linear Search for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

### Linear Search
Linear search is a simple search algorithm that checks each element of a list or array sequentially until the desired element is found. Here is an example of a recursive linear search program in C++:

```c++
#include <iostream>
using namespace std;

int recursiveLinearSearch(int arr[], int l, int r, int x)
{
    if (r < l)
        return -1;
    if (arr[l] == x)
        return l;
    if (arr[r] == x)
        return r;
    return recursiveLinearSearch(arr, l + 1, r - 1, x);
}

int main()
{
    int arr[] = { 2, 3, 4, 10, 40 };
    int n = sizeof(arr) / sizeof(arr[0]);
    int x = 10;
    int index = recursiveLinearSearch(arr, 0, n - 1, x);
    if (index != -1)
        cout << "Element " << x << " is present at index " << index;
    else
        cout << "Element " << x << " is not present in the array";
    return 0;
}
```

### Binary Search
Binary search is an efficient search algorithm that works by repeatedly dividing the search interval in half. It requires the input list or array to be sorted. Here is an example of a recursive binary search program in C++:

```c++
#include <iostream>
using namespace std;

int recursiveBinarySearch(int arr[], int l, int r, int x)
{
    if (r >= l) {
        int mid = l + (r - l) / 2;
        if (arr[mid] == x)
            return mid;
        if (arr[mid] > x)
            return recursiveBinarySearch(arr, l, mid - 1, x);
        return recursiveBinarySearch(arr, mid + 1, r, x);
    }
    return -1;
}

int main()
{
    int arr[] = { 2, 3, 4, 10, 40 };
    int n = sizeof(arr) / sizeof(arr[0]);
    int x = 10;
    int result = recursiveBinarySearch(arr, 0, n - 1, x);
    (result == -1) ? cout << "Element is not present in array"
                   : cout << "Element is present at index " << result;
    return 0;
}
```

Both linear and binary search algorithms can be implemented recursively. The recursive approach can make the code more readable and easier to understand, but it may not always be the most efficient solution. It is important to analyze the time and space complexity of the algorithm and choose the appropriate approach for the specific problem at hand.