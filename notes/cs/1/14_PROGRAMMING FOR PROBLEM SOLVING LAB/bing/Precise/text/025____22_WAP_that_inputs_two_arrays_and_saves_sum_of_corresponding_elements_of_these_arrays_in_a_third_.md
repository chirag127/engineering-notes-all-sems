## 22. WAP that inputs two arrays and saves sum of corresponding elements of these arrays in a third array and prints them.

Here is a step-by-step guide to writing a program that inputs two arrays and saves the sum of corresponding elements of these arrays in a third array and prints them:

1. Start by defining the main function and declaring the necessary variables, including the two input arrays, the output array, and the size of the arrays.
2. Prompt the user to enter the size of the arrays and store it in the appropriate variable.
3. Prompt the user to enter the elements of the first array and store them in the first input array.
4. Repeat the previous step for the second input array.
5. Use a loop to iterate over the elements of the input arrays, adding the corresponding elements and storing the result in the output array.
6. Use another loop to print the elements of the output array.
7. End the main function.

Here is an example of what the code might look like in C:

```c
#include <stdio.h>

int main() {
    int size;
    printf("Enter the size of the arrays: ");
    scanf("%d", &size);

    int arr1[size], arr2[size], sum[size];

    printf("Enter the elements of the first array: ");
    for (int i = 0; i < size; i++) {
        scanf("%d", &arr1[i]);
    }

    printf("Enter the elements of the second array: ");
    for (int i = 0; i < size; i++) {
        scanf("%d", &arr2[i]);
    }

    for (int i = 0; i < size; i++) {
        sum[i] = arr1[i] + arr2[i];
    }

    printf("The sum of the corresponding elements of the two arrays is: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", sum[i]);
    }

    return 0;
}
```