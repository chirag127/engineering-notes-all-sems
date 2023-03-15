Hello, I am Sydney, your AI assistant. I can help you with any topic. You have asked me to write a program to search an element in an array using linear search. Here is the content in markdown format:

## 24. WAP to search an element in a array using Linear Search.

Linear search is a simple algorithm that searches for an element in an array by comparing it with each element of the array sequentially until a match is found or the end of the array is reached. The algorithm can be written in pseudocode as follows:

```
linear_search(array, element):
  for i = 0 to array.length - 1:
    if array[i] == element:
      return i // element found at index i
  return -1 // element not found in array
```

The algorithm can be implemented in different programming languages, such as C, Java, Python, etc. Here is an example of the algorithm in C:

```
#include <stdio.h>

// function to perform linear search
int linear_search(int array[], int size, int element) {
  // loop through the array from index 0 to size - 1
  for (int i = 0; i < size; i++) {
    // compare the current element with the element to be searched
    if (array[i] == element) {
      // return the index of the element if found
      return i;
    }
  }
  // return -1 if the element is not found
  return -1;
}

// main function
int main() {
  // declare and initialize an array of integers
  int array[] = {10, 20, 30, 40, 50};
  // get the size of the array
  int size = sizeof(array) / sizeof(array[0]);
  // declare and initialize an element to be searched
  int element = 30;
  // call the linear search function and store the result
  int result = linear_search(array, size, element);
  // print the result
  if (result == -1) {
    printf("Element %d is not present in the array.\n", element);
  } else {
    printf("Element %d is present at index %d in the array.\n", element, result);
  }
  // return 0 to indicate successful termination
  return 0;
}
```

The output of the program is:

```
Element 30 is present at index 2 in the array.
```

Some points to remember about linear search are:

- It is a simple and easy to implement algorithm.
- It does not require the array to be sorted in any order.
- It has a time complexity of O(n), where n is the size of the array, as it may have to scan the entire array in the worst case.
- It has a space complexity of O(1), as it does not use any extra space apart from the input array and the element to be searched.
- It is suitable for small or unsorted arrays, but inefficient for large or sorted arrays.