## 24.WAP to search an element in a array using Linear Search.

Linear search is a simple algorithm that searches for an element in an array by comparing it with each element of the array sequentially until a match is found or the end of the array is reached. The algorithm can be written in pseudocode as follows:

```
LinearSearch(array, element)
  for i = 0 to array.length - 1
    if array[i] == element
      return i // element found at index i
    end if
  end for
  return -1 // element not found in array
end LinearSearch
```

The algorithm can be implemented in different programming languages, such as C, Java, Python, etc. Here is an example of C code that performs linear search on an array of integers:

```
#include <stdio.h>

// Function to perform linear search on an array
int linearSearch(int array[], int size, int element) {
  // Loop through the array from index 0 to size - 1
  for (int i = 0; i < size; i++) {
    // Compare the current element with the element to be searched
    if (array[i] == element) {
      // Return the index of the element if found
      return i;
    }
  }
  // Return -1 if the element is not found
  return -1;
}

// Main function to test the linear search function
int main() {
  // Declare and initialize an array of integers
  int array[] = {10, 20, 30, 40, 50};
  // Get the size of the array
  int size = sizeof(array) / sizeof(array[0]);
  // Declare and initialize an element to be searched
  int element = 30;
  // Call the linear search function and store the result
  int result = linearSearch(array, size, element);
  // Print the result
  if (result == -1) {
    printf("Element %d is not present in the array.\n", element);
  } else {
    printf("Element %d is present at index %d in the array.\n", element, result);
  }
  // Return 0 to indicate successful execution
  return 0;
}
```

The output of the above code is:

```
Element 30 is present at index 2 in the array.
```