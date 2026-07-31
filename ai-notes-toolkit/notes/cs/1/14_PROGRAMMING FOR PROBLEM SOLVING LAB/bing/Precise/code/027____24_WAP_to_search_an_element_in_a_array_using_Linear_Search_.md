## 24.WAP to search an element in a array using Linear Search.

Linear search is a simple search algorithm that is used to search for an element in an array. It works by iterating through the array from the first element to the last element, comparing each element with the value being searched for. If a match is found, the index of the element is returned. If no match is found, the search returns -1.

Here is an example of a program that uses linear search to search for an element in an array:

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

In this example, the `linearSearch` function takes as input an array `arr`, the size of the array `n`, and the value being searched for `x`. It returns the index of the element if it is found, or -1 if it is not found.

The `main` function initializes an array `arr` and its size `n`, as well as the value being searched for `x`. It then calls the `linearSearch` function and prints the result.

Linear search has a time complexity of O(n), where n is the size of the array. This means that in the worst case, the algorithm will have to iterate through the entire array to find the element, making it inefficient for large arrays. However, it is a simple and easy-to-implement algorithm that can be useful in certain situations.