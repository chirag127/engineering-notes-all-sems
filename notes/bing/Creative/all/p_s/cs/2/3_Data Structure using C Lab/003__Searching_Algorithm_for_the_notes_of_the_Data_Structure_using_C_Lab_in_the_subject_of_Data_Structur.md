### Searching Algorithm for the notes of the Data Structure using C Lab in the subject of Data Structure using C

- A searching algorithm is a method of finding an element or retrieving an element from any data structure where it is stored.
- Searching algorithms are generally classified into two categories: sequential search and interval search .
- Sequential search: In this, the list or array is traversed sequentially and every element is checked. For example, linear search and sentinel search are sequential search algorithms.
- Interval search: In this, the list or array is divided into smaller subarrays based on some condition and the subarray containing the element is searched. For example, binary search and interpolation search are interval search algorithms.
- The choice of searching algorithm depends on the type of data structure, the size of the data, the distribution of the data, and the complexity of the algorithm.
- Some of the advantages of searching algorithms are:
  - They can help to find an element quickly and efficiently.
  - They can help to sort the data based on some criteria.
  - They can help to perform other operations on the data such as insertion, deletion, or modification.
- Some of the disadvantages of searching algorithms are:
  - They may require extra space or time to perform the search.
  - They may not work well for large or unsorted data.
  - They may not guarantee to find the element if it does not exist in the data structure.

#### Linear Search in C
- Linear search in C is a sequential search algorithm that is used to search for an element in an array in sequential order.
- The algorithm works as follows:
  - Start from the leftmost element of the array and compare it with the element to be searched.
  - If the element matches, return the index of the element.
  - If the element does not match, move to the next element and repeat the process until the end of the array is reached or the element is found.
  - If the element is not found, return -1 or some other indicator of failure.
- The time complexity of linear search in C is O(n), where n is the number of elements in the array.
- The space complexity of linear search in C is O(1), as no extra space is required.
- The advantages of linear search in C are:
  - It is simple and easy to implement.
  - It does not require the array to be sorted or have any specific order.
  - It can handle dynamic data, as new elements can be added or deleted without affecting the search.
- The disadvantages of linear search in C are:
  - It is slow and inefficient for large or sorted arrays, as it has to scan the entire array in the worst case.
  - It does not take advantage of any information about the distribution or range of the data.
- The following is an example of linear search in C:

```c
// A function to perform linear search in C
int linear_search(int arr[], int n, int x)
{
  // Loop through the array from left to right
  for (int i = 0; i < n; i++)
  {
    // If the element matches, return the index
    if (arr[i] == x)
    {
      return i;
    }
  }
  // If the element is not found, return -1
  return -1;
}
```

#### Binary Search in C
- Binary search in C is an interval search algorithm that is used to search for an element in a sorted array by repeatedly dividing the array into two halves.
- The algorithm works as follows:
  - Initialize two variables, low and high, to point to the first and last element of the array respectively.
  - Calculate the middle index, mid, by adding low and high and dividing by two.
  - Compare the element at mid with the element to be searched, x.
  - If the element matches, return the index of the element.
  - If the element is smaller than x, set low to mid + 1 and repeat the process for the right subarray.
  - If the element is larger than x, set high to mid - 1 and repeat the process for the left subarray.
  - If low is greater than high, return -1 or some other indicator of failure.
- The time complexity of binary search in C is O(log n), where n is the number of elements in the array.
- The space complexity of binary search in C is

O(1), as no extra space is required.
- The advantages of binary search in C are:
  - It is fast and efficient for large and sorted arrays, as it reduces the search space by half in each iteration.
  - It can be implemented recursively or iteratively.
  - It can be used to find the first or last occurrence of an element, or the position to insert an element in a sorted array.
- The disadvantages of binary search in C are:
  - It requires the array to be sorted in ascending or descending order before performing the search.
  - It does not work well for dynamic data, as any insertion or deletion can affect the order of the array.
  - It may cause overflow errors if the low and high values are not calculated properly.
- The following is an example of binary search in C:

```c
// A function to perform binary search in C
int binary_search(int arr[], int low, int high, int x)
{
  // Base case: if low is greater than high, the element is not found
  if (low > high)
  {
    return -1;
  }
  // Calculate the middle index
  int mid = (low + high) / 2;
  // Compare the element at mid with x
  if (arr[mid] == x)
  {
    // If the element matches, return the index
    return mid;
  }
  else if (arr[mid] < x)
  {
    // If the element is smaller than x, search in the right subarray
    return binary_search(arr, mid + 1, high, x);
  }
  else
  {
    // If the element is larger than x, search in the left subarray
    return binary_search(arr, low, mid - 1, x);
  }
}
```

#### Mnemonics and Learning Tricks for Searching Algorithms
- Some of the mnemonics and learning tricks for searching algorithms are:
  - To remember the difference between linear and binary search, think of a phone book. If you want to find a name in a phone book, you can either scan the pages one by one (linear search) or flip to the middle and compare the name with the one you are looking for (binary search).
  - To remember the formula for calculating the middle index in binary search, think of the average of low and high. The average of two numbers is the sum of the numbers divided by two. So, mid = (low + high) / 2.
  - To remember the time complexity of linear and binary search, think of the number of comparisons they make. Linear search makes n comparisons in the worst case, where n is the number of elements in the array. Binary search makes log n comparisons in the worst case, where n is the number of elements in the array. So, the time complexity of linear search is O(n) and the time complexity of binary search is O(log n).
  - To remember the space complexity of linear and binary search, think of the extra space they use. Linear search does not use any extra space, so the space complexity is O(1). Binary search can use extra space if it is implemented recursively, as it uses the call stack to store the recursive calls. The maximum depth of the call stack is log n, where n is the number of elements in the array. So, the space complexity of binary search is O(log n) if it is recursive, and O(1) if it is iterative.