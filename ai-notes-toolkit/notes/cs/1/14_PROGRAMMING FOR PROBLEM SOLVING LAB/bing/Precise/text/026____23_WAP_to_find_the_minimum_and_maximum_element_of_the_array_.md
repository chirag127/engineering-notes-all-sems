## 23. WAP to find the minimum and maximum element of the array.

Here is an example of a program that finds the minimum and maximum elements of an array:

```c
#include <stdio.h>

int main() {
    int n, i;
    printf("Enter the number of elements in the array: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter the elements of the array: ");
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    int min = arr[0], max = arr[0];
    for (i = 1; i < n; i++) {
        if (arr[i] < min) {
            min = arr[i];
        }
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    printf("The minimum element of the array is %d\n", min);
    printf("The maximum element of the array is %d\n", max);
    return 0;
}
```

This program prompts the user to enter the number of elements in the array and the elements of the array. It then initializes the `min` and `max` variables to the first element of the array. The program then iterates through the rest of the elements of the array, updating the `min` and `max` variables if a smaller or larger element is found, respectively. Finally, the program prints the minimum and maximum elements of the array.

- The time complexity of this program is O(n), where n is the number of elements in the array.
- The space complexity of this program is O(1), as the program uses a constant amount of additional space.