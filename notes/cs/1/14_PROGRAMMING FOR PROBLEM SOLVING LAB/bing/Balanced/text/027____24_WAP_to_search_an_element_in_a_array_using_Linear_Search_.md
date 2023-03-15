## 24.WAP to search an element in a array using Linear Search.

Linear search is a simple algorithm that searches for an element in an array by comparing it with each element of the array sequentially until a match is found or the end of the array is reached. The algorithm can be written as follows:

- Start from the leftmost element of the array and compare it with the element to be searched.
- If the element matches, return the index of the element and stop the search.
- If the element does not match, move to the next element of the array and repeat step 2.
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

The code for linear search in C is:

```
#include <stdio.h>

int linear_search(int array[], int size, int element)
{
  int i;
  for (i = 0; i < size; i++)
  {
    if (array[i] == element)
    {
      return i;
    }
  }
  return -1;
}

int main()
{
  int array[] = {10, 20, 30, 40, 50};
  int size = sizeof(array) / sizeof(array[0]);
  int element = 30;
  int result = linear_search(array, size, element);
  if (result == -1)
  {
    printf("Element not found in the array.\n");
  }
  else
  {
    printf("Element found at index %d.\n", result);
  }
  return 0;
}
```

The output of the code is:

```
Element found at index 2.
```