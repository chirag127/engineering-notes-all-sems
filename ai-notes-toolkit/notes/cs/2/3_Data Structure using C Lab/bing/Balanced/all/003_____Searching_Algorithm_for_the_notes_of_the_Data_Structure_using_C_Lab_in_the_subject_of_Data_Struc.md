# Searching Algorithm for the notes of the Data Structure using C Lab in the subject of Data Structure using C

- A searching algorithm is a method of finding a specific element in a data structure, such as an array, a list, a tree, or a graph.
- A searching algorithm can be classified into two types: linear search and binary search.
- Linear search is a simple technique that scans the data structure from the beginning to the end, comparing each element with the target value until a match is found or the end is reached.
- Linear search has a time complexity of O(n), where n is the number of elements in the data structure.
- Binary search is a more efficient technique that works on sorted data structures. It divides the data structure into two halves and compares the target value with the middle element. If they are equal, the search is successful. If the target value is smaller than the middle element, the search continues in the left half. If the target value is larger than the middle element, the search continues in the right half.
- Binary search has a time complexity of O(log n), where n is the number of elements in the data structure.
- To implement a searching algorithm in C, we need to define a data structure, such as an array, and a function that takes the target value and the data structure as parameters and returns the index of the target value if found, or -1 if not found.
- For example, the following code shows a linear search function for an array of integers:

```c
// Linear search function for an array of integers
int linear_search(int target, int arr[], int size) {
  // Loop through the array from the beginning to the end
  for (int i = 0; i < size; i++) {
    // Compare each element with the target value
    if (arr[i] == target) {
      // If a match is found, return the index
      return i;
    }
  }
  // If no match is found, return -1
  return -1;
}
```

- Similarly, the following code shows a binary search function for a sorted array of integers:

```c
// Binary search function for a sorted array of integers
int binary_search(int target, int arr[], int size) {
  // Define the left and right boundaries of the search
  int left = 0;
  int right = size - 1;
  // Loop until the left and right boundaries cross
  while (left <= right) {
    // Find the middle index
    int mid = (left + right) / 2;
    // Compare the target value with the middle element
    if (arr[mid] == target) {
      // If they are equal, return the index
      return mid;
    } else if (arr[mid] < target) {
      // If the target value is larger, move the left boundary to the right of the middle
      left = mid + 1;
    } else {
      // If the target value is smaller, move the right boundary to the left of the middle
      right = mid - 1;
    }
  }
  // If no match is found, return -1
  return -1;
}
```