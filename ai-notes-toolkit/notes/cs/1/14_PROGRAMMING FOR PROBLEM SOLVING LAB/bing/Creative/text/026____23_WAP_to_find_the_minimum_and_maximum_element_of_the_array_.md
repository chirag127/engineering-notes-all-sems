## 23.WAP to find the minimum and maximum element of the array.

- An array is a collection of elements of the same data type, stored in contiguous memory locations.
- To find the minimum and maximum element of the array, we need to compare each element with a variable that stores the current minimum or maximum value, and update the variable if a smaller or larger element is found.
- The algorithm for finding the minimum and maximum element of the array is as follows:

  - Initialize two variables, min and max, with the first element of the array.
  - Loop through the array from the second element to the last element.
  - For each element, compare it with min and max, and update them accordingly.
  - After the loop, min and max will contain the minimum and maximum element of the array, respectively.

- The pseudocode for finding the minimum and maximum element of the array is as follows:

  ```
  min = max = array[0]
  for i = 1 to array.length - 1
    if array[i] < min
      min = array[i]
    else if array[i] > max
      max = array[i]
  end for
  print "The minimum element is", min
  print "The maximum element is", max
  ```

- The code for finding the minimum and maximum element of the array in C language is as follows:

  ```c
  #include <stdio.h>
  int main()
  {
    int array[10] = {12, 45, 67, 23, 89, 10, 34, 76, 54, 11}; // sample array
    int min, max, i;
    min = max = array[0]; // initialize min and max with the first element
    for (i = 1; i < 10; i++) // loop through the array from the second element
    {
      if (array[i] < min) // compare each element with min
        min = array[i]; // update min if a smaller element is found
      else if (array[i] > max) // compare each element with max
        max = array[i]; // update max if a larger element is found
    }
    printf("The minimum element is %d\n", min); // print the minimum element
    printf("The maximum element is %d\n", max); // print the maximum element
    return 0;
  }
  ```