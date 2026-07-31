## 23.WAP to find the minimum and maximum element of the array.

- An array is a collection of elements of the same data type, stored in contiguous memory locations.
- To find the minimum and maximum element of the array, we need to compare each element with a variable that stores the current minimum or maximum value, and update the variable if a smaller or larger element is found.
- The algorithm for finding the minimum and maximum element of the array is as follows:

  - Initialize two variables min and max to the first element of the array.
  - Loop through the array from the second element to the last element.
  - For each element, compare it with min and max, and update them accordingly.
  - After the loop, min and max will store the minimum and maximum element of the array respectively.

- The pseudocode for finding the minimum and maximum element of the array is as follows:

  ```
  min = max = array[0]
  for i = 1 to array.length - 1
    if array[i] < min
      min = array[i]
    if array[i] > max
      max = array[i]
  end for
  print min, max
  ```

- The C program for finding the minimum and maximum element of the array is as follows:

  ```c
  #include <stdio.h>
  int main()
  {
    int array[10], min, max, i;
    // Input the array elements
    printf("Enter 10 elements of the array: \n");
    for (i = 0; i < 10; i++)
    {
      scanf("%d", &array[i]);
    }
    // Initialize min and max to the first element
    min = max = array[0];
    // Loop through the array and compare each element with min and max
    for (i = 1; i < 10; i++)
    {
      if (array[i] < min)
      {
        min = array[i];
      }
      if (array[i] > max)
      {
        max = array[i];
      }
    }
    // Print the minimum and maximum element
    printf("The minimum element is %d\n", min);
    printf("The maximum element is %d\n", max);
    return 0;
  }
  ```