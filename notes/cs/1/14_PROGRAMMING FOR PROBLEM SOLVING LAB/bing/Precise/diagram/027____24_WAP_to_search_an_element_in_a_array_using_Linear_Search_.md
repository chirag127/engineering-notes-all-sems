## 24. WAP to search an element in an array using Linear Search

Linear search is a simple search algorithm that is used to search for an element in an array. It works by iterating through the array from the first element to the last element, comparing each element with the value being searched for. If a match is found, the index of the element is returned. If no match is found, the search returns -1.

Here is an example of a program that implements linear search in C:

```c
#include <stdio.h>

int linearSearch(int arr[], int n, int x) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == x) {
            return i;
        }
    }
    return -1;
}

int main() {
    int arr[] = {1, 3, 5, 7, 9};
    int n = sizeof(arr) / sizeof(arr[0]);
    int x = 5;
    int result = linearSearch(arr, n, x);
    if (result == -1) {
        printf("Element is not present in array");
    } else {
        printf("Element is present at index %d", result);
    }
    return 0;
}
```

This program defines a function `linearSearch` that takes an array, the size of the array, and the value to search for as arguments. The function iterates through the array using a for loop and compares each element with the value being searched for. If a match is found, the index of the element is returned. If no match is found, the function returns -1.

In the `main` function, an array is defined and its size is calculated. The value to search for is also defined. The `linearSearch` function is called with the array, its size, and the value to search for as arguments. The result of the search is stored in the `result` variable. If the result is -1, a message is printed indicating that the element is not present in the array. Otherwise, a message is printed indicating the index at which the element was found.

This is an example of how linear search can be implemented in C to search for an element in an array. It is a simple and straightforward algorithm, but it can be inefficient for large arrays as it requires iterating through the entire array to find the element. For large arrays, more efficient search algorithms such as binary search can be used.