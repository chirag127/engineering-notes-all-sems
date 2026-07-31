## 24.WAP to search an element in a array using Linear Search.

Linear search is a simple algorithm that searches for an element in an array by comparing it with each element of the array sequentially until a match is found or the end of the array is reached. The algorithm can be written in pseudocode as follows:

- Start from the leftmost element of the array and compare it with the element to be searched.
- If the element matches, return the index of the element and stop the search.
- If the element does not match, move to the next element of the array and repeat step 2.
- If the end of the array is reached and no match is found, return -1 to indicate that the element is not present in the array.

The algorithm can be implemented in any programming language using a loop. For example, in C, the code can be written as:

```c
// Function to perform linear search on an array
// arr is the array, n is the size of the array, x is the element to be searched
// The function returns the index of the element if found, or -1 otherwise
int linear_search(int arr[], int n, int x) {
  // Loop through the array from left to right
  for (int i = 0; i < n; i++) {
    // Compare the current element with x
    if (arr[i] == x) {
      // Return the index of the element if found
      return i;
    }
  }
  // Return -1 if the element is not found
  return -1;
}
```

The time complexity of linear search is O(n), where n is the size of the array, because in the worst case, the algorithm has to scan the entire array to find the element. The space complexity is O(1), because no extra space is required for the search. Linear search is suitable for small or unsorted arrays, but inefficient for large or sorted arrays.