Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write a program that inputs two arrays and saves sum of corresponding elements of these arrays in a third array and prints them. Here is the content in markdown format:

## 22.WAP that inputs two arrays and saves sum of corresponding elements of these arrays in a third array and prints them.

- An array is a collection of elements of the same data type that are stored in contiguous memory locations.
- To input two arrays, we need to declare two variables of array type and specify their size. For example, `int arr1[5];` and `int arr2[5];` declare two arrays of integers with five elements each.
- To input the elements of the arrays, we can use a loop and the `scanf` function. For example, `for(int i = 0; i < 5; i++) { scanf("%d", &arr1[i]); }` inputs the elements of the first array from the user.
- To save the sum of corresponding elements of the two arrays in a third array, we need to declare another variable of array type and specify its size. For example, `int arr3[5];` declares a third array of integers with five elements.
- To calculate the sum of corresponding elements of the two arrays, we can use another loop and the `+` operator. For example, `for(int i = 0; i < 5; i++) { arr3[i] = arr1[i] + arr2[i]; }` assigns the sum of the ith elements of the first and second arrays to the ith element of the third array.
- To print the elements of the third array, we can use another loop and the `printf` function. For example, `for(int i = 0; i < 5; i++) { printf("%d ", arr3[i]); }` prints the elements of the third array separated by spaces.

- Here is the complete program in C language:

```c
#include <stdio.h>
int main()
{
    //declare and initialize two arrays of size 5
    int arr1[5], arr2[5];
    //declare a third array of size 5
    int arr3[5];
    //input the elements of the first array
    printf("Enter the elements of the first array:\n");
    for(int i = 0; i < 5; i++)
    {
        scanf("%d", &arr1[i]);
    }
    //input the elements of the second array
    printf("Enter the elements of the second array:\n");
    for(int i = 0; i < 5; i++)
    {
        scanf("%d", &arr2[i]);
    }
    //calculate the sum of corresponding elements of the two arrays and store in the third array
    for(int i = 0; i < 5; i++)
    {
        arr3[i] = arr1[i] + arr2[i];
    }
    //print the elements of the third array
    printf("The elements of the third array are:\n");
    for(int i = 0; i < 5; i++)
    {
        printf("%d ", arr3[i]);
    }
    return 0;
}
```