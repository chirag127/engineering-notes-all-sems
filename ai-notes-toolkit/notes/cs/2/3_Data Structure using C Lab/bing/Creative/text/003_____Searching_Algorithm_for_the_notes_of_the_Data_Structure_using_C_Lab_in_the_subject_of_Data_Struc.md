### Searching Algorithm for the notes of the Data Structure using C Lab in the subject of Data Structure using C

- A searching algorithm is a method of finding an element or a value in a data structure, such as an array or a list.
- There are different types of searching algorithms, depending on the order and the structure of the data, and the way of comparing the elements.
- The two basic searching algorithms are linear search and binary search.

#### Linear Search
- Linear search is a simple algorithm that checks every element of the data structure sequentially until a match is found or the end is reached.
- Linear search can be used for any type of data, whether it is sorted or not.
- Linear search has a time complexity of O(n), where n is the number of elements in the data structure.
- Linear search can be implemented using a loop or a recursion in C.
- The pseudocode of linear search is:

```
linear_search(data, value)
  for i from 0 to length of data - 1
    if data[i] is equal to value
      return i // index of the matching element
  return -1 // value not found
```

- The C code of linear search using a loop is:

```
int linear_search(int data[], int n, int value) {
  // data is the array, n is the size, value is the element to search
  int i; // loop variable
  for (i = 0; i < n; i++) {
    if (data[i] == value) {
      return i; // return the index of the matching element
    }
  }
  return -1; // return -1 if value not found
}
```

- The C code of linear search using recursion is:

```
int linear_search(int data[], int n, int value, int i) {
  // data is the array, n is the size, value is the element to search, i is the current index
  if (i == n) {
    return -1; // base case: reached the end of the array, value not found
  }
  if (data[i] == value) {
    return i; // base case: found the matching element, return the index
  }
  return linear_search(data, n, value, i + 1); // recursive case: check the next element
}
```

#### Binary Search
- Binary search is a more efficient algorithm that works on sorted data by repeatedly dividing the data into two halves and comparing the middle element with the value to search.
- Binary search can only be used for data that is sorted in ascending or descending order.
- Binary search has a time complexity of O(log n), where n is the number of elements in the data structure.
- Binary search can be implemented using a loop or a recursion in C.
- The pseudocode of binary search is:

```
binary_search(data, value)
  low = 0 // lower bound of the search range
  high = length of data - 1 // upper bound of the search range
  while low is less than or equal to high
    mid = (low + high) / 2 // middle index of the search range
    if data[mid] is equal to value
      return mid // index of the matching element
    else if data[mid] is greater than value
      high = mid - 1 // narrow the search range to the left half
    else
      low = mid + 1 // narrow the search range to the right half
  return -1 // value not found
```

- The C code of binary search using a loop is:

```
int binary_search(int data[], int n, int value) {
  // data is the sorted array, n is the size, value is the element to search
  int low, high, mid; // variables for the search range and the middle index
  low = 0; // initialize the lower bound to 0
  high = n - 1; // initialize the upper bound to the last index
  while (low <= high) {
    mid = (low + high) / 2; // calculate the middle index
    if (data[mid] == value) {
      return mid; // return the index of the matching element
    }
    else if (data[mid] > value) {
      high = mid - 1; // narrow the search range to the left half
    }
    else {
      low = mid + 1; // narrow the search range to the right half
    }

```
