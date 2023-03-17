## 23. WAP to find the minimum and maximum element of the array

Here are the steps to find the minimum and maximum element of an array using a C program:

1. Declare an array of integers of a specific size.
2. Initialize the array with random integer values.
3. Set the minimum and maximum variables to the first element of the array.
4. Traverse through the array using a for loop.
5. Compare each element of the array with the minimum and maximum variables.
6. If an element is smaller than the minimum variable, update the minimum variable.
7. If an element is larger than the maximum variable, update the maximum variable.
8. After the loop finishes, the minimum and maximum variables will hold the minimum and maximum values of the array.
9. Print the minimum and maximum values.

Here's an example code implementation in C:

```c
#include <stdio.h>

int main() {
   int arr[] = {5, 12, 3, 8, 1, 9};
   int size = sizeof(arr)/sizeof(arr[0]);
   int min = arr[0];
   int max = arr[0];
   
   for(int i = 1; i < size; i++) {
      if(arr[i] < min) {
         min = arr[i];
      }
      if(arr[i] > max) {
         max = arr[i];
      }
   }
   
   printf("Minimum element in array: %d\n", min);
   printf("Maximum element in array: %d\n", max);
   
   return 0;
}
```

This program initializes an array of integers with random values and finds the minimum and maximum elements in the array. The minimum and maximum values are then printed on the console.