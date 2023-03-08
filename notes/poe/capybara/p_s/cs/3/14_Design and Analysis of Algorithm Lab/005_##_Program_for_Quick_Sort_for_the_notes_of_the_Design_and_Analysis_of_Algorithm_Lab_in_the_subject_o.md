## Sort a given set of n integer elements using Merge Sort method and compute its time complexity

Merge Sort is a Divide and Conquer algorithm that works on a principle of breaking down the array into smaller, simpler sub-arrays until they become simple enough to sort. These sorted sub-arrays are then merged to form a sorted array. 

### Divide and Conquer Method
The Divide and Conquer algorithm works on the following principle:
- Divide: The array is divided into two sub-arrays of equal size, or as close to equal as possible.
- Conquer: Each sub-array is recursively sorted using the merge sort algorithm.
- Combine: The two sorted sub-arrays are merged to form a single, sorted array.

### Time Complexity Analysis
The time complexity of Merge Sort can be analyzed as follows:

- Best case: O(n log n)
- Average case: O(n log n)
- Worst case: O(n log n)

The algorithm has a time complexity of O(n log n) in all cases. 

### Program Execution
In order to run the program, we need to follow the following steps:
1. Generate a set of n integer elements using the random number generator or read it from a file.
2. Implement the Merge Sort algorithm to sort the elements.
3. Record the time taken to sort the elements for varied values of n > 5000.
4. Plot a graph of the time taken versus non-graph sheet.

### Advantages of Merge Sort
- It has a consistent time complexity of O(n log n) for all cases.
- It is a stable sorting algorithm.
- It can be easily implemented using recursion.

### Disadvantages of Merge Sort
- It requires additional memory space to store the sub-arrays.
- It has a slower time complexity compared to other sorting algorithms for small arrays.

### Example
Let us consider an array of size 8 with the following elements: [3, 6, 2, 7, 1, 8, 4, 5]

1. We divide the array into two sub-arrays of size 4: [3, 6, 2, 7] and [1, 8, 4, 5]
2. We recursively sort each sub-array using the merge sort algorithm:
- [3, 6, 2, 7] is divided into [3, 6] and [2, 7]
- [1, 8, 4, 5] is divided into [1, 8] and [4, 5]
3. We merge the sorted sub-arrays to form the final sorted array:
- [3, 6] and [2, 7] are merged to form [2, 3, 6, 7]
- [1, 8] and [4, 5] are merged to form [1, 4, 5, 8]
- [2, 3, 6, 7] and [1, 4, 5, 8] are merged to form [1, 2, 3, 4, 5, 6, 7, 8]

### Applications
Merge Sort is used in various applications such as:
- External sorting
- Parallel processing
- Data compression
- Database sorting