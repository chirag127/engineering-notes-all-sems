## 24.WAP to search an element in a array using Linear Search.

Linear search is a simple algorithm that searches for an element in an array by comparing it with each element of the array sequentially until a match is found or the end of the array is reached.

The steps to write a program to search an element in an array using linear search are:

- Declare and initialize an array of integers with some values.
- Declare and initialize a variable to store the element to be searched, say `key`.
- Declare and initialize a variable to store the index of the element if found, say `pos`, to -1.
- Use a loop to iterate over the array from the first element to the last element.
- Inside the loop, compare the current element of the array with the `key`.
- If they are equal, assign the current index to `pos` and break the loop.
- After the loop, check if `pos` is not -1, which means the element was found.
- Print the value of `pos` as the index of the element in the array.
- Otherwise, print a message that the element was not found in the array.

Here is an example of a program in C language that implements the above steps:

```c
#include <stdio.h>
#define SIZE 10 //define the size of the array

int main()
{
    int arr[SIZE] = {12, 34, 56, 78, 90, 11, 22, 33, 44, 55}; //declare and initialize the array
    int key = 33; //declare and initialize the element to be searched
    int pos = -1; //declare and initialize the position variable
    int i; //declare a loop variable

    //use a loop to iterate over the array
    for(i = 0; i < SIZE; i++)
    {
        //compare the current element with the key
        if(arr[i] == key)
        {
            //assign the current index to pos and break the loop
            pos = i;
            break;
        }
    }

    //check if pos is not -1
    if(pos != -1)
    {
        //print the index of the element
        printf("Element %d found at index %d in the array.\n", key, pos);
    }
    else
    {
        //print a message that the element was not found
        printf("Element %d not found in the array.\n", key);
    }

    return 0;
}
```