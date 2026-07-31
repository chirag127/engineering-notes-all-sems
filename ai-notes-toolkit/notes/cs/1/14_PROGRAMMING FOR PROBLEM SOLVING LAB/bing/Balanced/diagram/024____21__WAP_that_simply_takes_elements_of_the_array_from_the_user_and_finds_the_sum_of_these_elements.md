## 21. WAP that simply takes elements of the array from the user and finds the sum of these elements.

- WAP stands for Write a Program.
- An array is a data structure that can store multiple values of the same type in a contiguous memory location.
- To take elements of the array from the user, we need to use some input method, such as scanf() in C, cin in C++, or input() in Python.
- To find the sum of these elements, we need to use a loop, such as for or while, to iterate over the array and add each element to a variable that stores the sum.
- Here is an example of WAP that simply takes elements of the array from the user and finds the sum of these elements in C:

```c
#include <stdio.h>
int main()
{
    int n, i, sum = 0; // declare variables
    printf("Enter the number of elements in the array: "); // prompt the user
    scanf("%d", &n); // read the input
    int arr[n]; // declare the array
    printf("Enter the elements of the array: "); // prompt the user
    for (i = 0; i < n; i++) // loop from 0 to n-1
    {
        scanf("%d", &arr[i]); // read each element
        sum += arr[i]; // add each element to the sum
    }
    printf("The sum of the elements is %d\n", sum); // print the result
    return 0;
}
```