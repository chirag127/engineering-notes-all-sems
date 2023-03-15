# Arrays: Array Notation and Representation, Manipulating Array Elements, using Multi Dimensional Arrays. Character Arrays and Strings, Structure, union, Enumerated Data types, Array of Structures, Passing Arrays to Functions.

## Array Notation and Representation
- An array is a collection of elements of the same data type that are stored in contiguous memory locations  .
- To declare an array in C, the syntax is: `dataType arrayName[arraySize];`  .
- For example, to declare an array of 10 integers, we can write: `int numbers[10];`.
- The array name is a constant pointer to the first element of the array.
- To access an array element, we use the index notation: `arrayName[index]`  .
- The index starts from 0 and goes till arraySize - 1. For example, to access the first element of the numbers array, we write: `numbers[0]`.
- To initialize an array, we can assign values to the elements at the time of declaration or later  .
- For example, to initialize the numbers array with 10 values, we can write: `int numbers[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};` or `int numbers[10]; numbers[0] = 1; numbers[1] = 2; ... numbers[9] = 10;`.

## Manipulating Array Elements
- We can perform various operations on array elements, such as reading, writing, sorting, searching, etc.
- To read an array element, we can use the scanf function with the address of the element as the argument .
- For example, to read the first element of the numbers array, we can write: `scanf("%d", &numbers[0]);`.
- To write an array element, we can use the printf function with the value of the element as the argument .
- For example, to write the first element of the numbers array, we can write: `printf("%d", numbers[0]);`.
- To sort an array, we can use various algorithms, such as bubble sort, selection sort, insertion sort, etc.
- For example, to sort the numbers array in ascending order using bubble sort, we can write:

```c
// Bubble sort algorithm
void bubbleSort(int arr[], int n) {
  int i, j, temp;
  for (i = 0; i < n - 1; i++) {
    for (j = 0; j < n - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        // Swap the elements
        temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
}

// Calling the function
bubbleSort(numbers, 10);
```

- To search an array, we can use various algorithms, such as linear search, binary search, etc.
- For example, to search for the value 5 in the numbers array using linear search, we can write:

```c
// Linear search algorithm
int linearSearch(int arr[], int n, int x) {
  int i;
  for (i = 0; i < n; i++) {
    if (arr[i] == x) {
      // Element found, return the index
      return i;
    }
  }
  // Element not found, return -1
  return -1;
}

// Calling the function
int index = linearSearch(numbers, 10, 5);
```

## Using Multi Dimensional Arrays
- A multi dimensional array is an array of arrays  .
- To declare a multi dimensional array in C, the syntax is: `dataType arrayName[size1][size2]...[sizeN];`  .
- For example, to declare a two dimensional array of 3 rows and 4 columns, we can write: `int matrix[3][4];`.
- The array