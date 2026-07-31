```
## 23.WAP to find the minimum and maximum element of the array.

- An array is a collection of elements of the same data type stored in contiguous memory locations.
- To find the minimum and maximum element of the array, we need to compare each element with a variable that stores the current minimum or maximum value.
- We can use a loop to iterate over the array elements and update the minimum or maximum variable accordingly.
- The algorithm for finding the minimum and maximum element of the array is as follows:

  - Initialize two variables min and max to the first element of the array.
  - Loop from the second element to the last element of the array.
  - For each element, compare it with min and max.
  - If the element is smaller than min, update min to the element.
  - If the element is larger than max, update max to the element.
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
  print min and max
  ```

- The code for finding the minimum and maximum element of the array in C language is as follows:

  ```
  #include <stdio.h>
  int main()
  {
    int array[10] = {12, 34, 56, 78, 90, 11, 43, 65, 87, 9};
    int min, max, i;
    min = max = array[0];
    for (i = 1; i < 10; i++)
    {
      if (array[i] < min)
        min = array[i];
      if (array[i] > max)
        max = array[i];
    }
    printf("The minimum element of the array is %d\n", min);
    printf("The maximum element of the array is %d\n", max);
    return 0;
  }
  ```
```