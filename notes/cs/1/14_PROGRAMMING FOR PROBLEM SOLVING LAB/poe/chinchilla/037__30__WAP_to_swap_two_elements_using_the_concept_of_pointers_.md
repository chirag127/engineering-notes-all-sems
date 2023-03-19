## 30. WAP to swap two elements using the concept of pointers.

Swapping two elements in an array is a common operation in programming. In order to swap two elements, we need to access their memory addresses. This is where pointers come in handy.

Here is a program that demonstrates how to swap two elements in an array using pointers:

```c
#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);

    int *ptr1 = &arr[1]; // Pointer to the second element
    int *ptr2 = &arr[3]; // Pointer to the fourth element

    swap(ptr1, ptr2);

    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}
```

Explanation:

1. We declare an integer array `arr` with five elements and a variable `n` to store its size.
2. We create two pointers `ptr1` and `ptr2` to point to the second and fourth elements respectively.
3. We call the `swap` function, passing the two pointers as arguments.
4. In the `swap` function, we use a temporary variable `temp` to store the value at the memory location pointed to by `a`.
5. We assign the value at the memory location pointed to by `b` to the memory location pointed to by `a`.
6. We assign the value in the temporary variable `temp` to the memory location pointed to by `b`.
7. We use a `for` loop to print the elements of the array after swapping.

Note: This program can be modified to swap elements in any array by changing the values of `ptr1` and `ptr2` to point to the desired elements.