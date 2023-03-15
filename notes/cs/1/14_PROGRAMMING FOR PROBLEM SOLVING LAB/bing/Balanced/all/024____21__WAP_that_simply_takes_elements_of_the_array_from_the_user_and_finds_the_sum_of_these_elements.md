## 21. WAP that simply takes elements of the array from the user and finds the sum of these elements.

- WAP stands for Write A Program, which is a common abbreviation used in programming assignments or exercises.
- An array is a data structure that can store multiple values of the same type in a contiguous memory location.
- To take elements of the array from the user, we need to use some input method, such as `scanf` in C, `input` in Python, or `Scanner` in Java.
- To find the sum of these elements, we need to use a loop, such as `for` or `while`, to iterate over the array and add each element to a variable that stores the sum.
- Here is an example of WAP that simply takes elements of the array from the user and finds the sum of these elements in C:

```c
#include <stdio.h>
int main()
{
    int n, i, sum = 0; // declare variables
    printf("Enter the size of the array: "); // prompt the user for the size of the array
    scanf("%d", &n); // read the size from the user and store it in n
    int arr[n]; // declare an array of size n
    printf("Enter the elements of the array: "); // prompt the user for the elements of the array
    for (i = 0; i < n; i++) // loop from 0 to n-1
    {
        scanf("%d", &arr[i]); // read each element from the user and store it in the array
    }
    for (i = 0; i < n; i++) // loop from 0 to n-1
    {
        sum = sum + arr[i]; // add each element to the sum
    }
    printf("The sum of the elements of the array is %d\n", sum); // print the sum
    return 0;
}
```