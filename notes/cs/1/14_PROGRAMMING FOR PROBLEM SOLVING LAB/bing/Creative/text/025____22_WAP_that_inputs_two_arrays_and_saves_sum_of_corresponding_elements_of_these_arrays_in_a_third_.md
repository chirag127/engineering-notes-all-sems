## 22.WAP that inputs two arrays and saves sum of corresponding elements of these arrays in a third array and prints them.

- A WAP (write a program) is a task that requires writing code in a specific programming language to achieve a desired output or functionality.
- An array is a data structure that stores a collection of elements of the same type in a contiguous memory location.
- The sum of corresponding elements of two arrays is the result of adding the elements at the same index position in both arrays.
- To input two arrays, we need to declare and initialize them with some values, or use a loop to read the values from the user.
- To save the sum of corresponding elements of two arrays in a third array, we need to declare and initialize a third array with the same size as the input arrays, and use a loop to iterate over the elements and store the sum in the third array.
- To print the third array, we need to use a loop to display the elements on the screen, or use a built-in function to print the whole array at once.

- Here is an example of a WAP that inputs two arrays and saves sum of corresponding elements of these arrays in a third array and prints them in C language:

```c
#include <stdio.h>
#define SIZE 5 //define the size of the arrays

int main()
{
    int arr1[SIZE], arr2[SIZE], arr3[SIZE]; //declare three arrays of size 5
    int i; //declare a loop variable

    //input the first array
    printf("Enter %d elements for the first array:\n", SIZE);
    for(i = 0; i < SIZE; i++)
    {
        scanf("%d", &arr1[i]); //read an element from the user and store it in the first array
    }

    //input the second array
    printf("Enter %d elements for the second array:\n", SIZE);
    for(i = 0; i < SIZE; i++)
    {
        scanf("%d", &arr2[i]); //read an element from the user and store it in the second array
    }

    //save the sum of corresponding elements of the two arrays in the third array
    for(i = 0; i < SIZE; i++)
    {
        arr3[i] = arr1[i] + arr2[i]; //add the elements at the same index position and store the result in the third array
    }

    //print the third array
    printf("The third array is:\n");
    for(i = 0; i < SIZE; i++)
    {
        printf("%d ", arr3[i]); //display an element of the third array
    }
    printf("\n"); //print a new line

    return 0; //end the program
}
```