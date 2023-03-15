Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write a program that inputs two arrays and saves sum of corresponding elements of these arrays in a third array and prints them. Here is the content in markdown format:

## 22.WAP that inputs two arrays and saves sum of corresponding elements of these arrays in a third array and prints them.

- An array is a collection of data elements of the same type, stored in contiguous memory locations.
- To input two arrays, we need to declare two variables of array type, specify their size, and use a loop to read the elements from the user.
- To save the sum of corresponding elements of these arrays in a third array, we need to declare another variable of array type with the same size as the input arrays, and use another loop to add the elements at the same index from both arrays and store the result in the third array.
- To print the third array, we need to use another loop to display the elements of the third array on the screen.
- Here is an example of a program in C language that implements this logic:

```c
#include <stdio.h>
#define SIZE 5 //define the size of the arrays

int main()
{
    int a[SIZE], b[SIZE], c[SIZE]; //declare three arrays of size 5
    int i; //declare a loop variable

    //input the first array
    printf("Enter %d elements for the first array:\n", SIZE);
    for(i = 0; i < SIZE; i++)
    {
        scanf("%d", &a[i]); //read the element from the user and store it in the first array
    }

    //input the second array
    printf("Enter %d elements for the second array:\n", SIZE);
    for(i = 0; i < SIZE; i++)
    {
        scanf("%d", &b[i]); //read the element from the user and store it in the second array
    }

    //save the sum of corresponding elements in the third array
    for(i = 0; i < SIZE; i++)
    {
        c[i] = a[i] + b[i]; //add the elements at the same index from both arrays and store the result in the third array
    }

    //print the third array
    printf("The third array is:\n");
    for(i = 0; i < SIZE; i++)
    {
        printf("%d ", c[i]); //display the element of the third array on the screen
    }
    printf("\n");

    return 0;
}
```