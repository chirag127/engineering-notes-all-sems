## 23.WAP to find the minimum and maximum element of the array.

- An array is a collection of elements of the same data type, stored in contiguous memory locations.
- To find the minimum and maximum element of the array, we need to compare each element with a variable that stores the current minimum or maximum value, and update the variable if a smaller or larger element is found.
- There are different ways to implement this algorithm, such as using loops, recursion, or built-in functions.
- Here is one possible way to write a program in C language to find the minimum and maximum element of the array using loops:

```c
#include <stdio.h>
#define SIZE 10 //define the size of the array

int main()
{
    int arr[SIZE]; //declare an array of size 10
    int i, min, max; //declare variables for loop index, minimum and maximum element

    printf("Enter %d elements of the array: \n", SIZE); //prompt the user to enter the elements of the array
    for(i = 0; i < SIZE; i++) //loop from 0 to SIZE-1
    {
        scanf("%d", &arr[i]); //read the element from the user and store it in the array
    }

    min = max = arr[0]; //initialize the minimum and maximum element to the first element of the array

    for(i = 1; i < SIZE; i++) //loop from 1 to SIZE-1
    {
        if(arr[i] < min) //if the current element is smaller than the minimum element
        {
            min = arr[i]; //update the minimum element to the current element
        }
        if(arr[i] > max) //if the current element is larger than the maximum element
        {
            max = arr[i]; //update the maximum element to the current element
        }
    }

    printf("The minimum element of the array is %d\n", min); //print the minimum element of the array
    printf("The maximum element of the array is %d\n", max); //print the maximum element of the array

    return 0; //return 0 to indicate successful termination of the program
}
```