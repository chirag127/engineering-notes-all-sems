## 24.WAP to search an element in a array using Linear Search.

Linear search is a simple algorithm that searches for an element in an array by comparing it with each element of the array sequentially until a match is found or the end of the array is reached.

The steps to perform linear search are:

- Start from the leftmost element of the array and compare it with the element to be searched.
- If the element matches, return the index of the element and stop the search.
- If the element does not match, move to the next element and repeat the comparison.
- If the end of the array is reached and no match is found, return -1 to indicate that the element is not present in the array.

The pseudocode for linear search is:

```
function linear_search(array, element)
  for i = 0 to array.length - 1
    if array[i] == element
      return i
    end if
  end for
  return -1
end function
```

The C program for linear search is:

```
#include <stdio.h>

// Function to perform linear search
int linear_search(int array[], int size, int element)
{
  // Loop through the array
  for (int i = 0; i < size; i++)
  {
    // Compare the current element with the element to be searched
    if (array[i] == element)
    {
      // Return the index of the element if found
      return i;
    }
  }
  // Return -1 if the element is not found
  return -1;
}

// Driver code
int main()
{
  // Declare an array of 10 elements
  int array[10] = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
  // Declare an element to be searched
  int element = 50;
  // Call the linear search function and store the result
  int result = linear_search(array, 10, element);
  // Print the result
  if (result == -1)
  {
    printf("Element %d is not present in the array.\n", element);
  }
  else
  {
    printf("Element %d is present at index %d in the array.\n", element, result);
  }
  return 0;
}
```

The output of the program is:

```
Element 50 is present at index 4 in the array.
```