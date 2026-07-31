Hello, I am Sydney, your AI assistant. I can help you with any topic. You have asked me to write a program to find the minimum and maximum element of the array. Here is the content in markdown format:

## 23. WAP to find the minimum and maximum element of the array.

An array is a collection of elements of the same data type, stored in contiguous memory locations. To find the minimum and maximum element of the array, we can use the following algorithm:

- Initialize two variables, min and max, to store the minimum and maximum element respectively.
- Assign the first element of the array to both min and max.
- Loop through the remaining elements of the array, starting from the second element.
- For each element, compare it with min and max, and update them accordingly.
- If the element is smaller than min, assign it to min.
- If the element is larger than max, assign it to max.
- After the loop, min and max will contain the minimum and maximum element of the array respectively.

Here is an example of the program in C language:

```c
#include <stdio.h>
#define SIZE 10 // size of the array

int main()
{
    int arr[SIZE] = {12, 34, 56, 78, 90, 11, 43, 65, 87, 9}; // sample array
    int min, max, i;

    // initialize min and max to the first element
    min = max = arr[0];

    // loop through the remaining elements
    for (i = 1; i < SIZE; i++)
    {
        // compare each element with min and max
        if (arr[i] < min)
            min = arr[i]; // update min
        if (arr[i] > max)
            max = arr[i]; // update max
    }

    // print the result
    printf("The minimum element is %d\n", min);
    printf("The maximum element is %d\n", max);

    return 0;
}
```

The output of the program is:

```
The minimum element is 9
The maximum element is 90
```