

## Program for Recursive Binary & Linear Search for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- A recursive binary search is an algorithm that searches for a target value in a sorted array by repeatedly dividing the array into two halves and comparing the middle element with the target.
- A recursive linear search is an algorithm that searches for a target value in an array by checking each element from left to right until the target is found or the end of the array is reached.
- Both algorithms use recursion, which is a technique of defining a problem in terms of smaller instances of the same problem.
- The pseudocode for recursive binary search is:

```
function binary_search(array, low, high, target)
  if low > high then
    return -1 // target not found
  end if
  mid = (low + high) / 2 // integer division
  if array[mid] == target then
    return mid // target found
  else if array[mid] < target then
    return binary_search(array, mid + 1, high, target) // search in right half
  else
    return binary_search(array, low, mid - 1, target) // search in left half
  end if
end function
```

- The pseudocode for recursive linear search is:

```
function linear_search(array, index, target)
  if index >= array.length then
    return -1 // target not found
  end if
  if array[index] == target then
    return index // target found
  else
    return linear_search(array, index + 1, target) // search in next element
  end if
end function
```

- The time complexity of recursive binary search is O(log n), where n is the size of the array, because it halves the search space in each recursive call.
- The time complexity of recursive linear search is O(n), where n is the size of the array, because it checks each element in the array once.
- The space complexity of recursive binary search is O(log n), where n is the size of the array, because it uses a call stack to store the recursive calls.
- The space complexity of recursive linear search is O(n), where n is the size of the array, because it uses a call stack to store the recursive calls.



## Program for Heap Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure to sort a given array of elements.
- A binary heap is a complete binary tree that satisfies the heap property, which means that every node is greater than or equal to its children (max-heap) or less than or equal to its children (min-heap).
- Heap sort works by first building a max-heap or a min-heap from the input array, then repeatedly extracting the root element (which is the maximum or minimum element) and placing it at the end of the sorted array, and then restoring the heap property by adjusting the remaining heap.
- The time complexity of heap sort is O(n log n) in the worst, average, and best cases, where n is the number of elements in the array. The space complexity of heap sort is O(1), as it only requires a constant amount of auxiliary space.
- The following is a pseudocode for heap sort using a max-heap:

```
heap_sort(array):
  n = length(array)
  # Build a max-heap from the array
  for i from n/2 down to 1:
    heapify(array, i, n)
  # Extract the root element and place it at the end of the sorted array
  for i from n down to 2:
    swap(array[1], array[i])
    n = n - 1
    # Restore the heap property by adjusting the remaining heap
    heapify(array, 1, n)
  return array

heapify(array, i, n):
  # Assume that the node at index i is the root of a subtree
  # and its left and right children are at index 2i and 2i+1
  largest = i
  left = 2i
  right = 2i + 1
  # Compare the root with its left and right children and find the largest element
  if left <= n and array[left] > array[largest]:
    largest = left
  if right <= n and array[right] > array[largest]:
    largest = right
  # If the root is not the largest element, swap it with the largest child and recursively heapify the affected subtree
  if largest != i:
    swap(array[i], array[largest])
    heapify(array, largest, n)
```



## Program for Merge Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Merge sort is a divide-and-conquer algorithm that recursively splits an array into two subarrays and then merges them in sorted order.
- The algorithm can be implemented using the following steps:

  1. If the array has only one element, return it as it is already sorted.
  2. Otherwise, divide the array into two equal or nearly equal subarrays and call merge sort on each subarray recursively.
  3. Merge the two sorted subarrays into one sorted array by comparing the first elements of each subarray and taking the smaller one into the output array. Repeat this until both subarrays are exhausted.
  4. Return the merged array as the final output.

- The time complexity of merge sort is O(n log n) in the worst, average and best cases, where n is the number of elements in the array. This is because the algorithm divides the array into log n levels and performs O(n) work at each level.
- The space complexity of merge sort is O(n) in the worst case, as the algorithm requires an auxiliary array of the same size as the input array to store the merged output.
- The following is a pseudocode for merge sort:

  ```
  function merge_sort(array)
    if length(array) <= 1 then
      return array
    end if
    mid = floor(length(array) / 2)
    left = merge_sort(array[0..mid-1])
    right = merge_sort(array[mid..length(array)-1])
    return merge(left, right)
  end function

  function merge(left, right)
    output = empty array
    i = 0
    j = 0
    while i < length(left) and j < length(right) do
      if left[i] <= right[j] then
        append left[i] to output
        i = i + 1
      else
        append right[j] to output
        j = j + 1
      end if
    end while
    append the remaining elements of left or right to output
    return output
  end function
  ```



## Program for Selection Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Selection sort is a simple sorting algorithm that repeatedly finds the minimum element from the unsorted part of the array and places it at the beginning.
- The algorithm maintains two subarrays in a given array: one that is already sorted and one that is unsorted.
- The algorithm iterates over the unsorted subarray, finds the smallest element, and swaps it with the leftmost element of the unsorted subarray, moving the boundary of the sorted subarray by one element to the right.
- The algorithm repeats this process until the entire array is sorted.
- The time complexity of selection sort is O(n^2), where n is the number of elements in the array, as it performs n-1 comparisons for each of the n elements.
- The space complexity of selection sort is O(1), as it only requires a constant amount of auxiliary space to store the index of the minimum element.
- Selection sort is not a stable sorting algorithm, as it may change the relative order of elements with equal values.
- Selection sort is not an adaptive sorting algorithm, as it does not take advantage of the existing order in the input array.
- Selection sort is suitable for small arrays or arrays that are nearly sorted, as it performs fewer swaps than other sorting algorithms.
- Selection sort is easy to implement and understand, but it is inefficient for large or random arrays, as it performs many unnecessary comparisons.

- A pseudocode for selection sort is given below:

```
procedure selection_sort(A : array of items)
   n := length(A)
   for i := 0 to n - 2 do
      min_index := i
      for j := i + 1 to n - 1 do
         if A[j] < A[min_index] then
            min_index := j
         end if
      end for
      if min_index != i then
         swap A[i] and A[min_index]
      end if
   end for
end procedure
```

- A C program for selection sort is given below:

```
#include <stdio.h>

// Function to swap two elements in an array
void swap(int *a, int *b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

// Function to perform selection sort on an array
void selection_sort(int arr[], int n) {
  int i, j, min_index;
  // Iterate over the unsorted subarray
  for (i = 0; i < n - 1; i++) {
    // Find the minimum element in the unsorted subarray
    min_index = i;
    for (j = i + 1; j < n; j++) {
      if (arr[j] < arr[min_index]) {
        min_index = j;
      }
    }
    // Swap the minimum element with the leftmost element of the unsorted subarray
    if (min_index != i) {
      swap(&arr[i], &arr[min_index]);
    }
  }
}

// Function to print an array
void print_array(int arr[], int n) {
  int i;
  for (i = 0; i < n; i++) {
    printf("%d ", arr[i]);
  }
  printf("\n");
}

// Driver code
int main() {
  int arr[] = {64, 25, 12, 22, 11};
  int n = sizeof(arr) / sizeof(arr[0]);
  printf("Unsorted array: \n");
  print_array(arr, n);
  selection_sort(arr, n);
  printf("Sorted array: \n");
  print_array(arr, n);
  return 0;
}
```

- The output of the C program is:

```
Unsorted array: 
64 25 12 22 11 
Sorted array: 
11 12 22 25 64 
```



## Program for Insertion Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Insertion sort is a simple sorting algorithm that works by comparing each element of an array with the previous elements and inserting it in the correct position.
- The algorithm starts from the second element of the array and iterates until the last element, assuming that the first element is already sorted.
- At each iteration, the current element is compared with the previous elements in the sorted part of the array and shifted to the right until it finds its correct position.
- The algorithm has a time complexity of O(n^2) in the worst case, when the array is in reverse order, and O(n) in the best case, when the array is already sorted.
- The algorithm is stable, meaning that it preserves the relative order of equal elements, and in-place, meaning that it does not use extra space.
- The algorithm is suitable for small arrays or arrays that are nearly sorted, as it has a low overhead and a fast best case.
- The algorithm can be implemented in any programming language that supports arrays and comparison operators. Here is an example of the algorithm in C:

```c
// A function to sort an array using insertion sort
void insertionSort(int arr[], int n) {
  // Loop from the second element to the last element
  for (int i = 1; i < n; i++) {
    // Store the current element in a temporary variable
    int key = arr[i];
    // Initialize a variable to store the index of the previous element
    int j = i - 1;
    // Loop through the sorted part of the array and compare the key with each element
    while (j >= 0 && arr[j] > key) {
      // Shift the element to the right if it is greater than the key
      arr[j + 1] = arr[j];
      // Decrement the index of the previous element
      j--;
    }
    // Insert the key in the correct position
    arr[j + 1] = key;
  }
}
```



## Program for Quick Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Quick sort is a sorting algorithm that uses the divide and conquer strategy to sort a list of elements.
- The basic idea of quick sort is to choose a pivot element from the list, and partition the list into two sublists: one with elements smaller than the pivot, and one with elements larger than the pivot.
- The pivot element is then placed in its correct position in the sorted list, and the sublists are recursively sorted using the same procedure.
- The algorithm can be implemented using the following steps:

  1. Choose a pivot element from the list, usually the first or the last element.
  2. Compare each element in the list with the pivot, and swap it with another element if necessary, such that all elements smaller than the pivot are on the left of the pivot, and all elements larger than the pivot are on the right of the pivot.
  3. Place the pivot in its correct position in the sorted list, and divide the list into two sublists: one with elements on the left of the pivot, and one with elements on the right of the pivot.
  4. Recursively apply the same procedure to the sublists, until the sublists are of size one or zero.

- The following is a pseudocode for quick sort:

  ```
  function quick_sort(list, low, high)
    if low < high
      pivot_index = partition(list, low, high) // partition the list and return the pivot index
      quick_sort(list, low, pivot_index - 1) // sort the left sublist
      quick_sort(list, pivot_index + 1, high) // sort the right sublist
    end if
  end function

  function partition(list, low, high)
    pivot = list[high] // choose the last element as the pivot
    i = low - 1 // initialize the index of the smaller element
    for j = low to high - 1 // loop through the list
      if list[j] < pivot // if the current element is smaller than the pivot
        i = i + 1 // increment the index of the smaller element
        swap list[i] and list[j] // swap the current element with the smaller element
      end if
    end for
    swap list[i + 1] and list[high] // swap the pivot with the element next to the smaller element
    return i + 1 // return the pivot index
  end function
  ```

- The following is a sample program for quick sort in C language:

  ```c
  #include <stdio.h>

  // function to swap two elements in an array
  void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
  }

  // function to partition an array using the last element as the pivot
  int partition(int arr[], int low, int high) {
    int pivot = arr[high]; // choose the last element as the pivot
    int i = low - 1; // initialize the index of the smaller element
    for (int j = low; j < high; j++) { // loop through the array
      if (arr[j] < pivot) { // if the current element is smaller than the pivot
        i++; // increment the index of the smaller element
        swap(&arr[i], &arr[j]); // swap the current element with the smaller element
      }
    }
    swap(&arr[i + 1], &arr[high]); // swap the pivot with the element next to the smaller element
    return i + 1; // return the pivot index
  }

  // function to sort an array using quick sort
  void quick_sort(int arr[], int low, int high) {
    if (low < high) {
      int pivot_index = partition(arr, low, high); // partition the array and return the pivot index
      quick_sort(arr, low, pivot_index - 1); // sort the left subarray
      quick_sort(arr, pivot_index + 1, high); // sort the right subarray
    }
  }

  // function to print an array
  void print_array(int arr[], int size) {
    for (int i = 0; i < size; i++) {
      printf("%d ", arr[i]);
    }
    printf("\n");
  }

  // main function
  int main() {
    int arr[] = {10, 7, 8, 9, 1, 5}; // sample array
    int size =

```




# Knapsack Problem using Greedy Solution

- The knapsack problem is a problem of finding the optimal way to fill a knapsack with a given capacity and a set of items, each with a value and a weight.
- The fractional knapsack problem is a variation of the knapsack problem, where the items can be divided into smaller pieces and the knapsack can be filled with fractions of items.
- The greedy solution for the fractional knapsack problem is an efficient and optimal method that works as follows:
  - Sort the items by their value-to-weight ratio in descending order.
  - Start with the item with the highest ratio and take as much of it as possible, until the knapsack is full or the item is exhausted.
  - If the knapsack is not full, move to the next item with the next highest ratio and repeat the previous step.
  - Continue this process until the knapsack is full or there are no more items left.
- The greedy solution for the fractional knapsack problem has a time complexity of O(n log n), where n is the number of items, because the sorting step dominates the algorithm.
- The greedy solution for the fractional knapsack problem is optimal because at each step, it chooses the item that gives the maximum value per unit weight, which maximizes the total value of the knapsack.



# Perform Travelling Salesman Problem for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- The Travelling Salesman Problem (TSP) is a classic optimization problem that asks for the shortest possible route that visits each city exactly once and returns to the starting point.
- The TSP is an NP-hard problem, meaning that there is no known efficient algorithm that can solve it in polynomial time for any number of cities.
- The TSP has many applications in real time systems, such as scheduling, routing, logistics, and planning.
- The TSP can be formulated as a graph problem, where the cities are the vertices and the distances between them are the edge weights.
- The TSP can be solved using various methods, such as brute force, dynamic programming, branch and bound, heuristic algorithms, and metaheuristic algorithms.
- Brute force is the simplest method that tries all possible permutations of the cities and chooses the one with the minimum total distance. It has a time complexity of O(n!), where n is the number of cities.
- Dynamic programming is a method that uses a table to store and reuse the optimal solutions of subproblems. It has a time complexity of O(n^2 * 2^n), where n is the number of cities.
- Branch and bound is a method that uses a tree to explore the search space and prune the branches that cannot lead to a better solution. It has a time complexity of O(n!), but it can be much faster in practice depending on the quality of the bounding function.
- Heuristic algorithms are methods that use some rules or intuition to find a good solution, but not necessarily the optimal one. They have a lower time complexity than the exact methods, but they have no guarantee of optimality or quality. Some examples of heuristic algorithms are nearest neighbor, greedy, and 2-opt.
- Metaheuristic algorithms are methods that use some general strategies to explore the search space and escape from local optima. They have a lower time complexity than the exact methods, but they have no guarantee of optimality or quality. Some examples of metaheuristic algorithms are simulated annealing, genetic algorithm, and ant colony optimization.



## Find Minimum Spanning Tree using Kruskal’s Algorithm

- A **minimum spanning tree (MST)** of a weighted, undirected graph is a subgraph that connects all the vertices with the minimum possible total edge weight.
- **Kruskal's algorithm** is a greedy algorithm that finds a MST by selecting the edges with the smallest weights in ascending order, as long as they do not create a cycle in the MST .
- The algorithm can be described as follows  :

  1. Sort all the edges in non-decreasing order of their weight.
  2. Pick the smallest edge and check if it forms a cycle with the MST constructed so far. If not, include it in the MST. If yes, discard it.
  3. Repeat step 2 until there are (V-1) edges in the MST, where V is the number of vertices in the graph.
  4. Return the MST.

- The algorithm can be implemented using a **priority queue** to store the edges in sorted order, a **union-find** data structure to check for cycles, and a **queue** to store the MST edges.
- The algorithm can be illustrated with an example:

  - Input graph:

    input graph

  - Sorted edges:

    | Edge | Weight |
    |------|--------|
    | (7,6) | 1 |
    | (8,2) | 2 |
    | (6,5) | 2 |
    | (0,1) | 4 |
    | (2,5) | 4 |
    | (8,6) | 6 |
    | (2,3) | 7 |
    | (7,8) | 7 |
    | (0,7) | 8 |
    | (1,2) | 8 |
    | (3,4) | 9 |
    | (5,4) | 10 |
    | (1,7) | 11 |
    | (3,5) | 14 |

  - MST construction:

    - Pick edge (7,6) with weight 1. It does not form a cycle, so include it in the MST.

      step 1

    - Pick edge (8,2) with weight 2. It does not form a cycle, so include it in the MST.

      step 2

    - Pick edge (6,5) with weight 2. It does not form a cycle, so include it in the MST.

      step 3

    - Pick edge (0,1) with weight 4. It does not form a cycle, so include it in the MST.

      step 4

    - Pick edge (2,5) with weight 4. It forms a cycle with the MST, so discard it.

      step 5

    - Pick edge (8,6) with weight 6. It forms a cycle with the MST, so discard it.

      step 6

    - Pick edge (2,3) with weight 7. It does not form a cycle, so include it in the MST.

      step 7

    - Pick edge (7,8) with weight 7. It forms a cycle with the MST, so discard it.

      step 8

    - Pick edge (0,7) with weight 8. It forms a cycle with the MST, so discard it.

      step 9

    - Pick edge (1,2) with weight 8. It does not form a cycle, so include it in the MST.



## Implement N Queen Problem using Backtracking for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- The N Queen problem is a classic example of backtracking, a technique for solving problems recursively by trying to build a solution incrementally, removing those solutions that fail to satisfy the constraints of the problem at any point of time.
- The N Queen problem is to place N queens on an N x N chessboard such that no two queens attack each other. A queen can move horizontally, vertically, or diagonally on the board.
- The backtracking algorithm for the N Queen problem works as follows:

  - Start from the leftmost column of the board.
  - For each row in the current column, do the following:
    - Check if placing a queen in this row is safe, i.e., it does not conflict with any of the previously placed queens.
    - If it is safe, mark this row and column as part of the solution and recursively try to place the rest of the queens in the next columns.
    - If placing a queen in this row leads to a solution, return true.
    - If placing a queen in this row does not lead to a solution, unmark this row and column as part of the solution and backtrack to the previous column.
  - If all the rows in the current column have been tried and none of them leads to a solution, return false.

- The pseudocode for the backtracking algorithm is given below:

  ```
  function solveNQueen(board, col)
    // base case: all queens are placed
    if col == N
      return true
    // consider each row in the current column
    for row from 0 to N-1
      // check if placing a queen in this row is safe
      if isSafe(board, row, col)
        // mark this row and column as part of the solution
        board[row][col] = 1
        // recursively try to place the rest of the queens
        if solveNQueen(board, col + 1)
          return true
        // if placing a queen in this row does not lead to a solution, backtrack
        board[row][col] = 0
    // if no row in the current column leads to a solution, return false
    return false
  ```

- The function isSafe(board, row, col) checks if placing a queen in the given row and column is safe, i.e., it does not conflict with any of the previously placed queens. It can be implemented as follows:

  ```
  function isSafe(board, row, col)
    // check the left side of the current row
    for i from 0 to col-1
      if board[row][i] == 1
        return false
    // check the upper left diagonal
    for i, j from row-1, col-1 to 0, 0
      if board[i][j] == 1
        return false
    // check the lower left diagonal
    for i, j from row+1, col-1 to N-1, 0
      if board[i][j] == 1
        return false
    // if none of the above cases is true, return true
    return true
  ```

- The time complexity of the backtracking algorithm is O(N!), where N is the number of queens. This is because there are N possible choices for the first queen, N-1 for the second queen, and so on, until 1 for the last queen. The space complexity is O(N^2), where N is the number of queens. This is because we need to store the board of size N x N and the recursive call stack of depth N.



# Sort a given set of n integer elements using Quick Sort method and compute its time complexity. Run the program for varied values of n> 5000 and record the time taken to sort. Plot a graph of the time taken versus non graph sheet. The elements can be read from a file or can be generated using the random number generator. Demonstrate using Java how the divide and- conquer method works along with its time complexity analysis: worst case, average case and best case.

## Quick Sort
- Quick Sort is a sorting algorithm that uses the **divide and conquer** technique to sort a given array of integers.
- The basic idea is to choose a **pivot** element from the array, and partition the array into two subarrays: one with elements smaller than the pivot, and one with elements larger than the pivot.
- The pivot element is then placed in its correct position in the sorted array, and the subarrays are recursively sorted using the same procedure.
- The algorithm terminates when the array size is one or zero, which means it is already sorted.

## Time Complexity
- The time complexity of Quick Sort depends on how the pivot element is chosen, and how balanced the partitions are.
- In the **worst case**, the pivot element is always the smallest or the largest element in the array, which means one partition is empty and the other contains n-1 elements. This leads to a recursive call on an array of size n-1, which repeats until the array is sorted. The time complexity in this case is **O(n^2)**, where n is the number of elements in the array.
- In the **average case**, the pivot element is chosen randomly or by using some heuristic, which means the partitions are roughly equal in size. This leads to a recursive call on two subarrays of size n/2, which repeats until the array is sorted. The time complexity in this case is **O(n log n)**, where n is the number of elements in the array.
- In the **best case**, the pivot element is always the median of the array, which means the partitions are exactly equal in size. This leads to a recursive call on two subarrays of size n/2, which repeats until the array is sorted. The time complexity in this case is also **O(n log n)**, where n is the number of elements in the array.

## Java Implementation
- The following code snippet shows how to implement Quick Sort in Java, using a random pivot selection and a swap function to partition the array.

```java
// A utility function to swap two elements in an array
public static void swap(int[] arr, int i, int j) {
  int temp = arr[i];
  arr[i] = arr[j];
  arr[j] = temp;
}

// A function to perform Quick Sort on a given array
public static void quickSort(int[] arr, int low, int high) {
  // Base case: array size is one or zero
  if (low >= high) {
    return;
  }

  // Choose a random pivot element and swap it with the last element
  int pivotIndex = (int) (Math.random() * (high - low + 1)) + low;
  swap(arr, pivotIndex, high);

  // Partition the array around the pivot element
  int i = low; // index for smaller elements
  int j = high - 1; // index for larger elements
  while (i <= j) {
    // Find the first element that is larger than or equal to the pivot
    while (i <= j && arr[i] < arr[high]) {
      i++;
    }
    // Find the last element that is smaller than or equal to the pivot
    while (i <= j && arr[j] > arr[high]) {
      j--;
    }
    // Swap the two elements if they are out of order
    if (i <= j) {
      swap(arr, i, j);
      i++;
      j--;
    }
  }
  // Swap the pivot element with the first element that is larger than it
  swap(arr, i, high);

  // Recursively sort the left and right subarrays
  quickSort(arr, low, i - 1);
  quickSort(arr, i + 1, high);
}
```

## Experiment and Graph
- To test the performance of Quick Sort, we can generate random arrays of different sizes (n > 5000) and measure the time taken to sort them using the Java implementation.
- We can use the `System.nanoTime()` method to get the current time in nanoseconds before and after the sorting, and calculate the difference as the elapsed time.
- We can repeat the experiment for different values of n



# Merge Sort

## Introduction

- Merge sort is a sorting algorithm that uses the divide and conquer technique to sort a given set of n integer elements.
- The algorithm divides the input array into two subarrays of roughly equal size, recursively sorts each subarray, and then merges the two sorted subarrays into one final sorted array.
- The algorithm can be implemented using recursion or iteration, and can be adapted to sort arrays in ascending or descending order, as well as other data structures such as linked lists.

## Algorithm

- The algorithm can be described as follows:

```
merge_sort(A, p, r):
  // A is the input array, p is the starting index, r is the ending index
  if p < r: // base case: array has at least two elements
    q = floor((p + r) / 2) // find the middle point of the array
    merge_sort(A, p, q) // recursively sort the left subarray
    merge_sort(A, q + 1, r) // recursively sort the right subarray
    merge(A, p, q, r) // merge the two sorted subarrays

merge(A, p, q, r):
  // A is the input array, p is the starting index of the left subarray, 
  // q is the ending index of the left subarray, r is the ending index of the right subarray
  n1 = q - p + 1 // compute the length of the left subarray
  n2 = r - q // compute the length of the right subarray
  create arrays L[1..n1 + 1] and R[1..n2 + 1] // create temporary arrays to store the subarrays
  for i = 1 to n1: // copy the left subarray to L
    L[i] = A[p + i - 1]
  for j = 1 to n2: // copy the right subarray to R
    R[j] = A[q + j]
  L[n1 + 1] = infinity // set a sentinel value at the end of L
  R[n2 + 1] = infinity // set a sentinel value at the end of R
  i = 1 // initialize the index for L
  j = 1 // initialize the index for R
  for k = p to r: // loop through the elements of A
    if L[i] <= R[j]: // if the current element of L is smaller or equal to the current element of R
      A[k] = L[i] // copy the element of L to A
      i = i + 1 // increment the index for L
    else: // otherwise, the current element of R is smaller than the current element of L
      A[k] = R[j] // copy the element of R to A
      j = j + 1 // increment the index for R
```

## Time Complexity Analysis

- The time complexity of merge sort depends on the number of comparisons and data movements performed by the algorithm.
- The merge function takes O(n) time to merge two subarrays of size n, where n = r - p + 1.
- The merge sort function divides the array into two subarrays of size n/2, and recursively sorts each subarray in O(n log n) time, where n = r - p + 1.
- Therefore, the overall time complexity of merge sort is O(n log n) for the worst case, average case and best case scenarios, where n is the number of elements in the input array.

## Experiment

- To demonstrate the performance of merge sort, we can run the program for varied values of n > 5000, and record the time taken to sort.
- The elements can be read from a file or can be generated using the random number generator.
- We can plot a graph of the time taken versus n on a graph sheet, and observe the shape of the curve.
- We can also compare the results with other sorting algorithms, such as insertion sort, selection sort, bubble sort, quick sort, heap sort, etc., and analyze their time complexities and advantages and disadvantages.

## Divide and Conquer Method

- Merge sort is an example of the divide and conquer method, which is a general technique for solving problems by breaking them into smaller and simpler subproblems, solving each subproblem recursively or iteratively, and combining the solutions to obtain the final solution.
- The divide and conquer method works by following three steps:

  - Divide: Divide the problem into smaller and simpler subproblems of the same type.
  - Conquer: Solve each subproblem recursively or iteratively, until they are simple



## Implement the 0/1 Knapsack problem using (a) Dynamic Programming method (b) Greedy method.

The 0/1 Knapsack problem is a classic optimization problem where we have a set of items, each with a weight and a value, and we want to choose a subset of items that maximizes the total value while keeping the total weight within a given limit. The 0/1 means that we can either take an item or leave it, but not take a fraction of it.

There are two common methods to solve this problem: dynamic programming and greedy method.

### (a) Dynamic Programming method

Dynamic programming is a technique that breaks down a complex problem into smaller and overlapping subproblems, and solves them by reusing the solutions of the subproblems. The idea is to use a table to store the optimal value for each subproblem, and then use the table to construct the final solution.

The steps for the dynamic programming method are:

- Define the subproblems: Let `V[i][w]` be the maximum value that can be obtained by using the first `i` items and a knapsack of capacity `w`. The base case is `V[0][w] = 0` for any `w`, meaning that no items can be taken.
- Define the recurrence relation: For each `i > 0` and `w >= 0`, we have two options: either take the `i`-th item or leave it. If we take it, we add its value to the optimal value of the subproblem with `i-1` items and `w-wi` capacity, where `wi` is the weight of the `i`-th item. If we leave it, we keep the optimal value of the subproblem with `i-1` items and `w` capacity. Therefore, we have:

  `V[i][w] = max(V[i-1][w], vi + V[i-1][w-wi])` if `wi <= w`

  `V[i][w] = V[i-1][w]` if `wi > w`

  where `vi` is the value of the `i`-th item.
- Fill the table: We can use a nested loop to fill the table from bottom to top and left to right, following the recurrence relation.
- Construct the solution: We can use another nested loop to trace back the table from the bottom right corner to the top left corner, and check which items are included in the optimal solution. If `V[i][w] > V[i-1][w]`, it means that the `i`-th item is taken, and we reduce the capacity by `wi`. Otherwise, it means that the `i`-th item is not taken, and we move to the previous row.

The pseudocode for the dynamic programming method is:

```
// Input: n = number of items, W = knapsack capacity, w[] = array of item weights, v[] = array of item values
// Output: V[n][W] = maximum value, X[] = array of item choices (1 for taken, 0 for not taken)

// Initialize the table V[][] with 0
for i = 0 to n
  for j = 0 to W
    V[i][j] = 0

// Fill the table V[][] using the recurrence relation
for i = 1 to n
  for j = 0 to W
    if w[i] <= j // if the item can fit in the knapsack
      V[i][j] = max(V[i-1][j], v[i] + V[i-1][j-w[i]]) // choose the maximum value between taking and leaving the item
    else // if the item cannot fit in the knapsack
      V[i][j] = V[i-1][j] // leave the item

// Initialize the array X[] with 0
for i = 0 to n
  X[i] = 0

// Trace back the table V[][] to construct the solution
i = n // start from the last item
j = W // start from the full capacity
while i > 0 and j > 0
  if V[i][j] > V[i-1][j] // if the item is taken
    X[i] = 1 // mark the item as taken
    j = j - w[i] // reduce the capacity by the item weight
  i = i - 1 // move to the previous item
```

### (b) Greedy method

Greedy method is a technique that makes a locally optimal choice at each



## From a given vertex in a weighted connected graph, find shortest paths to other vertices using Dijkstra's algorithm.

- A weighted connected graph is a graph where each edge has a positive or negative weight associated with it, and there is a path between any two vertices.
- A shortest path from a vertex u to a vertex v is a path that has the minimum total weight among all possible paths from u to v.
- Dijkstra's algorithm is a greedy algorithm that finds the shortest paths from a given source vertex to all other vertices in a weighted connected graph with non-negative edge weights.
- The algorithm works as follows:

  - Initialize a distance array dist, where dist[v] is the distance from the source to v, and a predecessor array pred, where pred[v] is the previous vertex on the shortest path from the source to v.
  - Set dist[source] to 0 and dist[v] to infinity for all other vertices v.
  - Set pred[source] to null and pred[v] to undefined for all vertices v.
  - Create a priority queue Q of vertices, where the priority of a vertex is its distance from the source, and insert the source into Q.
  - While Q is not empty, do the following:
    - Dequeue the vertex u with the minimum priority from Q.
    - For each neighbor v of u, do the following:
      - If dist[v] > dist[u] + weight(u, v), then
        - Update dist[v] to dist[u] + weight(u, v).
        - Update pred[v] to u.
        - If v is not in Q, then insert v into Q with priority dist[v].
        - Else, update the priority of v in Q to dist[v].
  - Return the distance array dist and the predecessor array pred.

- The time complexity of Dijkstra's algorithm is O((V + E) log V), where V is the number of vertices and E is the number of edges in the graph, assuming that the priority queue is implemented using a binary heap.
- The space complexity of Dijkstra's algorithm is O(V), where V is the number of vertices in the graph.
- An example of Dijkstra's algorithm is shown below:

Dijkstra's algorithm example

- In this example, the source vertex is A, and the graph has 6 vertices and 9 edges. The algorithm finds the shortest paths from A to all other vertices, as shown by the colors and the numbers on the edges. The final distance and predecessor arrays are:

| Vertex | Distance | Predecessor |
|--------|----------|-------------|
| A      | 0        | null        |
| B      | 7        | A           |
| C      | 9        | A           |
| D      | 20       | B           |
| E      | 20       | C           |
| F      | 11       | C           |



# Find Minimum Cost Spanning Tree of a given connected undirected graph using Kruskal's algorithm. Use Union-Find algorithms in your program.

- A **spanning tree** of a graph is a subgraph that contains all the vertices and is a tree (i.e., has no cycles).
- A **minimum spanning tree (MST)** of a weighted graph is a spanning tree whose sum of edge weights is minimum among all possible spanning trees.
- **Kruskal's algorithm** is a greedy algorithm that finds a MST of a given connected, weighted, undirected graph by selecting the edges with the smallest weights that do not form a cycle with the edges already in the MST.
- **Union-Find** algorithms are data structures and methods that support two operations: **union** (merging two disjoint sets into one) and **find** (determining which set an element belongs to).
- Union-Find algorithms can be used to implement **disjoint-set** data structures, which can efficiently track the connected components of a graph and check whether adding an edge creates a cycle or not.
- The steps of Kruskal's algorithm using Union-Find are as follows:
  - Sort all the edges in non-decreasing order of their weights.
  - Initialize a MST as an empty set and a disjoint-set data structure with each vertex as a separate set.
  - Repeat until the MST has (V-1) edges or the edge list is empty:
    - Pick the edge with the smallest weight from the edge list and remove it.
    - If the edge connects two vertices that belong to different sets in the disjoint-set data structure, then add the edge to the MST and perform a union operation on the two sets.
    - Otherwise, discard the edge as it creates a cycle in the MST.
  - Return the MST or report that the graph is not connected.



# Find Minimum Cost Spanning Tree of a given undirected graph using Prim’s algorithm.

- A **spanning tree** of a graph is a subgraph that contains all the vertices and is a tree (i.e., has no cycles).
- A **minimum cost spanning tree (MCST)** of a graph is a spanning tree that has the minimum possible total edge weight among all the spanning trees of the graph.
- **Prim’s algorithm** is a greedy algorithm that finds a MCST of a given undirected graph.
- The algorithm works as follows:
  - Start with an arbitrary vertex as the root of the MCST.
  - Maintain a set of vertices that are already included in the MCST, and a set of edges that connect the included vertices to the rest of the graph.
  - Repeat until all the vertices are included in the MCST:
    - Find the edge with the minimum weight among the edges that connect the included vertices to the rest of the graph.
    - Add this edge and the corresponding vertex to the MCST, and update the set of edges accordingly.
- The algorithm can be implemented using a priority queue or a heap data structure to store the edges and find the minimum weight edge efficiently.
- The time complexity of the algorithm is O(E log V), where E is the number of edges and V is the number of vertices in the graph.



# Write programs to (a) Implement All-Pairs Shortest Paths problem using Floyd's algorithm. (b) Implement Travelling Sales Person problem using Dynamic programming.

## (a) Implement All-Pairs Shortest Paths problem using Floyd's algorithm.

- The All-Pairs Shortest Paths problem is to find the shortest distance between every pair of vertices in a weighted graph, possibly with negative edge weights but no negative cycles.
- Floyd's algorithm, also known as the Floyd-Warshall algorithm, is an algorithm that solves this problem by using dynamic programming.
- The algorithm works by iteratively improving an estimate of the shortest distance between any two vertices, based on the previous estimate and the edge weights.
- The algorithm maintains a matrix D of size n x n, where n is the number of vertices in the graph, and D[i][j] is the current estimate of the shortest distance from vertex i to vertex j.
- Initially, D[i][j] is set to the edge weight w(i, j) if there is an edge from i to j, or infinity otherwise.
- Then, for each intermediate vertex k from 1 to n, the algorithm updates D[i][j] by checking if going through vertex k can improve the current estimate, i.e., if D[i][k] + D[k][j] < D[i][j].
- If so, the algorithm sets D[i][j] to D[i][k] + D[k][j], and records k as the predecessor of j on the shortest path from i to j.
- After n iterations, the matrix D contains the final shortest distances between all pairs of vertices, and the predecessor matrix can be used to reconstruct the shortest paths.
- The algorithm runs in O(n^3) time and O(n^2) space, where n is the number of vertices in the graph.

- Here is a pseudocode implementation of Floyd's algorithm:

```
// Input: A weighted graph G with n vertices and no negative cycles
// Output: A matrix D of shortest distances and a matrix P of predecessors
function Floyd(G):
  // Initialize D and P
  for i = 1 to n:
    for j = 1 to n:
      if i == j:
        D[i][j] = 0 // The distance from a vertex to itself is zero
        P[i][j] = null // There is no predecessor for a vertex to itself
      else if there is an edge from i to j with weight w(i, j):
        D[i][j] = w(i, j) // The distance is the edge weight
        P[i][j] = i // The predecessor is the source vertex
      else:
        D[i][j] = infinity // There is no edge from i to j
        P[i][j] = null // There is no predecessor
  
  // Update D and P using intermediate vertices
  for k = 1 to n: // For each intermediate vertex k
    for i = 1 to n: // For each source vertex i
      for j = 1 to n: // For each destination vertex j
        if D[i][k] + D[k][j] < D[i][j]: // If going through k is better
          D[i][j] = D[i][k] + D[k][j] // Update the distance
          P[i][j] = P[k][j] // Update the predecessor
  
  // Return the final matrices
  return D, P
```



## Design and implement to find a subset of a given set S = {Sl, S2,.....,Sn} of n positive integers whose SUM is equal to a given positive integer d. For example, if S ={1, 2, 5, 6, 8} and d= 9, there are two solutions {1,2,6}and {1,8}. Display a suitable message, if the given problem instance doesn't have a solution.

- This problem is an example of the **subset sum problem**, which is a special case of the **knapsack problem**. The subset sum problem is to find a subset of a given set of numbers that adds up to a given target number. The knapsack problem is to find a subset of a given set of items, each with a weight and a value, that maximizes the total value while staying within a given weight limit.
- The subset sum problem is **NP-complete**, which means that there is no known efficient algorithm that can solve it in polynomial time for all instances. However, there are some algorithms that can solve it in polynomial time for some special cases, or that can find approximate solutions in polynomial time for general cases.
- One possible algorithm to solve the subset sum problem is to use **backtracking**, which is a technique that explores all possible solutions by recursively choosing and unchoosing elements from the set. The algorithm works as follows:

  - Start with an empty subset and a remaining sum equal to the target sum.
  - For each element in the set, do the following:
    - If the element is equal to the remaining sum, then add it to the subset and return the subset as a solution.
    - If the element is smaller than the remaining sum, then add it to the subset and recursively try to find a solution with the remaining elements and the reduced sum.
    - If the element is larger than the remaining sum, then skip it and continue with the next element.
  - If no element is left, then return no solution.

- The pseudocode for the backtracking algorithm is given below:

  ```
  function subsetSum(set, target):
    return subsetSumHelper(set, target, [], 0)

  function subsetSumHelper(set, target, subset, index):
    # base case: no elements left
    if index == length(set):
      # check if the subset sum is equal to the target
      if sum(subset) == target:
        # return the subset as a solution
        return subset
      else:
        # return no solution
        return null
    # recursive case: try the next element
    else:
      # get the next element
      element = set[index]
      # case 1: the element is equal to the target
      if element == target:
        # add the element to the subset and return it as a solution
        subset.append(element)
        return subset
      # case 2: the element is smaller than the target
      elif element < target:
        # add the element to the subset and recursively try to find a solution
        subset.append(element)
        solution = subsetSumHelper(set, target - element, subset, index + 1)
        # if a solution is found, return it
        if solution != null:
          return solution
        # otherwise, backtrack and remove the element from the subset
        else:
          subset.pop()
      # case 3: the element is larger than the target
      else:
        # skip the element and continue with the next one
        pass
      # recursively try to find a solution without the element
      return subsetSumHelper(set, target, subset, index + 1)
  ```

- The time complexity of the backtracking algorithm is **O(2^n)**, where n is the size of the set. This is because the algorithm explores all possible subsets of the set, which are 2^n in number. The space complexity of the algorithm is **O(n)**, where n is the size of the set. This is because the algorithm uses a recursive call stack that can store at most n elements at a time.
- Another possible algorithm to solve the subset sum problem is to use **dynamic programming**, which is a technique that breaks down a complex problem into smaller subproblems and stores the results of the subproblems in a table to avoid recomputation. The algorithm works as follows:

  - Create a boolean table of size (n+1) x (target+1), where n is the size of the set and target is the target sum. The table[i][j] entry indicates whether there is a subset of the first i elements of the set that adds up to j.
  - Initialize the first row of the table



## Design and implement to find all Hamiltonian Cycles in a connected undirected Graph G of n vertices using backtracking principle.

- A Hamiltonian cycle is a cycle in a graph that visits every vertex exactly once and returns to the starting vertex.
- A graph is connected if there is a path between any two vertices.
- A graph is undirected if the edges have no direction, meaning that (u, v) and (v, u) are the same edge.
- Backtracking is a general algorithmic technique that tries different solutions recursively until a desired goal is reached or all possibilities are exhausted.
- To find all Hamiltonian cycles in a connected undirected graph G of n vertices using backtracking, we can use the following steps:

  - Start from any vertex v and mark it as visited.
  - Add v to the current path and check if the path is a Hamiltonian cycle. If yes, print or store the path and backtrack to the previous vertex.
  - For each neighbor u of v that is not visited, recursively explore the graph from u, marking u as visited and adding it to the path.
  - After exploring all neighbors of v, unmark v as visited and remove it from the path.
  - Repeat the above steps for all vertices as the starting point.

- The pseudocode for the algorithm is given below:

  ```
  // G is the adjacency matrix of the graph
  // n is the number of vertices
  // path is an array to store the current path
  // pos is the current position in the path
  // visited is a boolean array to mark the visited vertices

  // A function to check if the vertex v can be added to the path
  function isSafe(v, G, path, pos)
    // Check if v is adjacent to the last vertex in the path
    if G[path[pos - 1]][v] == 0
      return false
    // Check if v is already in the path
    for i = 0 to pos - 1
      if path[i] == v
        return false
    return true

  // A recursive function to find all Hamiltonian cycles
  function findHamiltonianCycles(G, path, pos, visited)
    // Base case: the path is a Hamiltonian cycle
    if pos == n
      // Check if the last vertex is adjacent to the first vertex
      if G[path[pos - 1]][path[0]] == 1
        // Print or store the path
        print path
      return
    // Try different vertices as the next candidate
    for v = 0 to n - 1
      // Check if v can be added to the path
      if isSafe(v, G, path, pos)
        // Mark v as visited and add it to the path
        visited[v] = true
        path[pos] = v
        // Recursively explore the graph from v
        findHamiltonianCycles(G, path, pos + 1, visited)
        // Backtrack to the previous vertex
        visited[v] = false
        path[pos] = -1

  // A function to initialize the algorithm
  function findAllHamiltonianCycles(G)
    // Initialize the path, visited and position arrays
    path = new int[n]
    visited = new boolean[n]
    pos = 0
    // Fill the path and visited arrays with -1 and false respectively
    for i = 0 to n - 1
      path[i] = -1
      visited[i] = false
    // Call the recursive function for each vertex as the starting point
    for v = 0 to n - 1
      // Mark v as visited and add it to the path
      visited[v] = true
      path[pos] = v
      // Recursively explore the graph from v
      findHamiltonianCycles(G, path, pos + 1, visited)
      // Backtrack to the previous vertex
      visited[v] = false
      path[pos] = -1
  ```

