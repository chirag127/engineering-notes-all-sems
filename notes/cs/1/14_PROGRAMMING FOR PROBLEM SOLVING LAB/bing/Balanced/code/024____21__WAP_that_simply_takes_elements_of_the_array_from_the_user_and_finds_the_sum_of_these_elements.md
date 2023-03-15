## 21. WAP that simply takes elements of the array from the user and finds the sum of these elements.

- WAP stands for Write A Program, which is a common abbreviation used in computer science and programming courses.
- An array is a data structure that stores a collection of values of the same type, such as integers, characters, or strings.
- To take elements of the array from the user, we need to use some input method, such as scanf, cin, or input, depending on the programming language we are using.
- To find the sum of these elements, we need to use a loop, such as for, while, or do-while, to iterate over the array and add each element to a variable that stores the sum.
- Here is an example of a C program that implements this task:

```c
#include <stdio.h>
#define SIZE 10 // define the size of the array as a constant

int main()
{
    int array[SIZE]; // declare an array of integers with size 10
    int sum = 0; // declare and initialize a variable to store the sum
    int i; // declare a loop variable

    printf("Enter %d elements of the array:\n", SIZE); // prompt the user to enter the elements
    for (i = 0; i < SIZE; i++) // loop from 0 to SIZE-1
    {
        scanf("%d", &array[i]); // read an integer from the user and store it in the array
    }

    for (i = 0; i < SIZE; i++) // loop from 0 to SIZE-1
    {
        sum = sum + array[i]; // add the current element to the sum
    }

    printf("The sum of the elements is %d\n", sum); // print the sum
    return 0; // return 0 to indicate successful termination
}
```