## 24. WAP to search an element in an array using Linear Search

Linear search is a simple search algorithm that can be used to find an element in an array. Here is an example of how to implement linear search in C:

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

This code defines a function `linearSearch` that takes an array `arr`, the size of the array `n`, and the element to search for `x` as input. The function then iterates over the array and returns the index of the first occurrence of `x` in the array. If `x` is not found in the array, the function returns `-1`.

In the `main` function, we define an array `arr` and its size `n`, and the element to search for `x`. We then call the `linearSearch` function and store the result in the variable `result`. If `result` is `-1`, we print that the element is not present in the array. Otherwise, we print the index at which the element is present.

This is a simple example of how to implement linear search in C. You can modify the code to suit your needs.