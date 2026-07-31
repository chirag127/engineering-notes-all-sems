

## Program for Recursive Binary & Linear Search for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Binary search is a searching algorithm that finds the position of a target value in a sorted array. It is also called a half-interval search or logarithmic search .
- Binary search works by comparing the target value with the middle element of the array. If they are equal, the search is successful and the position is returned. If the target value is smaller than the middle element, the search continues in the left half of the array. If the target value is larger than the middle element, the search continues in the right half of the array  .
- Binary search can be implemented in two ways: iterative and recursive. The iterative method uses a while loop to repeatedly update the low and high indices of the search range. The recursive method uses a function that calls itself with the new low and high indices until the base case is reached  .
- The pseudocode for the iterative binary search is:

```
binarySearch(array, target):
  low = 0
  high = array.length - 1
  while low <= high:
    mid = (low + high) / 2
    if target == array[mid]:
      return mid
    else if target < array[mid]:
      high = mid - 1
    else:
      low = mid + 1
  return -1
```

- The pseudocode for the recursive binary search is:

```
binarySearch(array, target, low, high):
  if low > high:
    return -1
  mid = (low + high) / 2
  if target == array[mid]:
    return mid
  else if target < array[mid]:
    return binarySearch(array, target, low, mid - 1)
  else:
    return binarySearch(array, target, mid + 1, high)
```

- The time complexity of binary search is O(log n), where n is the number of elements in the array. The space complexity of binary search is O(1) for the iterative method and O(log n) for the recursive method, due to the stack space used by the recursive calls  .
- Linear search is a searching algorithm that finds the position of a target value in an array by checking each element from left to right. It is also called a sequential search.
- Linear search works by comparing the target value with each element of the array. If they are equal, the search is successful and the position is returned. If the target value is not found in the array, the search is unsuccessful and -1 is returned .
- Linear search can be implemented in two ways: iterative and recursive. The iterative method uses a for loop to iterate over the array elements. The recursive method uses a function that calls itself with the next index until the base case is reached .
- The pseudocode for the iterative linear search is:

```
linearSearch(array, target):
  for i = 0 to array.length - 1:
    if target == array[i]:
      return i
  return -1
```

- The pseudocode for the recursive linear search is:

```
linearSearch(array, target, index):
  if index >= array.length:
    return -1
  if target == array[index]:
    return index
  else:
    return linearSearch(array, target, index + 1)
```

- The time complexity of linear search is O(n), where n is the number of elements in the array. The space complexity of linear search is O(1) for the iterative method and O(n) for the recursive method, due to the stack space used by the recursive calls .
- Binary search is faster and more efficient than linear search, but it requires the array to be sorted. Linear search is simpler and more flexible, but it requires more comparisons and iterations .



## Program for Heap Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure to sort a given array of elements.
- A binary heap is a complete binary tree that satisfies the heap property, which means that every node is greater than or equal to its children (max-heap) or less than or equal to its children (min-heap).
- The basic idea of heap sort is to build a max-heap or a min-heap from the input array, and then repeatedly extract the root element (which is the maximum or minimum element) and place it at the end of the sorted output array.
- The algorithm can be implemented as follows:

  - Build a max-heap or a min-heap from the input array by using a bottom-up approach, starting from the last non-leaf node and moving upwards. This can be done in O(n) time, where n is the number of elements in the array.
  - Repeat the following steps until the heap size is reduced to one:
    - Swap the root element (which is the maximum or minimum element) with the last element in the heap.
    - Reduce the heap size by one and adjust the heap to maintain the heap property by using a top-down approach, starting from the root node and moving downwards. This can be done in O(log n) time, where n is the current heap size.
    - The extracted element is placed at the end of the sorted output array.

- The overall time complexity of heap sort is O(n log n), where n is the number of elements in the array. The space complexity is O(1), as no extra space is required apart from the input array.
- Heap sort is an in-place and unstable sorting algorithm, which means that it does not require extra space to store the sorted output and it does not preserve the relative order of equal elements.
- Heap sort is suitable for sorting large data sets, as it has a good asymptotic performance and it can be easily parallelized. However, it is not very efficient for sorting small data sets, as it has a high constant factor and it does not take advantage of the existing order in the input array.
- The following is an example of a C program that implements heap sort:

```c
// A function to swap two elements
void swap(int *a, int *b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

// A function to heapify a subtree rooted at index i
// n is the size of the heap
void heapify(int arr[], int n, int i) {
  // Find the largest among the root, left child and right child
  int largest = i;
  int left = 2 * i + 1;
  int right = 2 * i + 2;

  if (left < n && arr[left] > arr[largest])
    largest = left;

  if (right < n && arr[right] > arr[largest])
    largest = right;

  // Swap and continue heapifying if the root is not the largest
  if (largest != i) {
    swap(&arr[i], &arr[largest]);
    heapify(arr, n, largest);
  }
}

// A function to perform heap sort
void heapSort(int arr[], int n) {
  // Build a max-heap from the input array
  for (int i = n / 2 - 1; i >= 0; i--)
    heapify(arr, n, i);

  // Extract the root element and place it at the end of the sorted output array
  for (int i = n - 1; i > 0; i--) {
    swap(&arr[0], &arr[i]);
    // Heapify the reduced heap
    heapify(arr, i, 0);
  }
}

// A function to print an array
void printArray(int arr[], int n) {
  for (int i = 0; i < n; i++)
    printf("%d ", arr[i]);
  printf("\n");
}

// A main function to test the program
int main() {
  int arr[] = {12, 11, 13, 5, 6, 7};
  int n = sizeof(arr) / sizeof(arr[0]);

  printf("Input array: \n");
  printArray(arr, n);

  heapSort(arr, n);

  printf("Sorted array: \n");
  printArray(arr, n);

  return 0;
}
```



## Program for Merge Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Merge sort is a divide-and-conquer algorithm that splits an array into two halves and recursively sorts each half, then merges the sorted halves into one sorted array.
- The algorithm can be implemented using the following steps:

  - If the array has only one element, return the array as it is already sorted.
  - Otherwise, divide the array into two equal or nearly equal parts, called the left and right subarrays.
  - Recursively sort the left and right subarrays using merge sort.
  - Merge the sorted left and right subarrays into one sorted array using a helper function that takes two sorted arrays and returns a new sorted array that contains all the elements from both arrays in ascending order.
  - Return the merged array as the final sorted array.

- The time complexity of merge sort is O(n log n) in the average and worst cases, where n is the number of elements in the array. This is because the algorithm divides the array into log n levels, and each level takes O(n) time to merge the subarrays.
- The space complexity of merge sort is O(n), as the algorithm requires an auxiliary array of the same size as the original array to store the merged subarrays.
- The following is a possible pseudocode implementation of merge sort in C:

```c
// A function that merges two sorted subarrays into one sorted array
// Input: arr - the original array, l - the starting index of the left subarray, m - the ending index of the left subarray, r - the ending index of the right subarray
// Output: none, but the original array is modified to contain the sorted elements from l to r
void merge(int arr[], int l, int m, int r) {
  // Create an auxiliary array of size r - l + 1
  int n = r - l + 1;
  int aux[n];

  // Initialize two pointers i and j to point to the start of the left and right subarrays respectively
  int i = l;
  int j = m + 1;

  // Initialize a pointer k to point to the start of the auxiliary array
  int k = 0;

  // Loop until either i or j reaches the end of their subarray
  while (i <= m && j <= r) {
    // Compare the elements at i and j and copy the smaller one to the auxiliary array
    if (arr[i] <= arr[j]) {
      aux[k] = arr[i];
      i++;
    } else {
      aux[k] = arr[j];
      j++;
    }
    // Increment k to point to the next position in the auxiliary array
    k++;
  }

  // Copy the remaining elements from the left subarray to the auxiliary array if any
  while (i <= m) {
    aux[k] = arr[i];
    i++;
    k++;
  }

  // Copy the remaining elements from the right subarray to the auxiliary array if any
  while (j <= r) {
    aux[k] = arr[j];
    j++;
    k++;
  }

  // Copy the elements from the auxiliary array back to the original array from l to r
  for (i = l; i <= r; i++) {
    arr[i] = aux[i - l];
  }
}

// A function that implements merge sort on an array
// Input: arr - the array to be sorted, l - the starting index of the array, r - the ending index of the array
// Output: none, but the array is modified to be sorted in ascending order
void mergeSort(int arr[], int l, int r) {
  // Base case: if the array has only one element, return
  if (l == r) {
    return;
  }

  // Find the middle index of the array
  int m = (l + r) / 2;

  // Recursively sort the left and right subarrays
  mergeSort(arr, l, m);
  mergeSort(arr, m + 1, r);

  // Merge the sorted subarrays
  merge(arr, l, m, r);
}
```



# Program for Selection Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Selection sort is a simple and easy-to-understand sorting algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list.
- Selection sort is an in-place sorting algorithm, which means it does not require any additional memory to sort the list.
- Selection sort has a best-case and average-case time complexity of O(n^2), making it efficient for small data sets. It is easy to modify to sort in ascending or descending order.
- Selection sort is described as an in-place comparison-based algorithm that divides the list into two parts, the sorted part on the left and the unsorted part on the right.
- Selection sort loops over indices in the array; for each index, selection sort calls indexOfMinimum and swap. If the length of the array is n, there are n indices in the array.
- Selection sort requires scanning n elements (taking n-1 comparisons) and then swapping it into the first position. Finding the minimum requires n-1 comparisons. Then sorting the rest of the list requires n-2 comparisons. In general, finding the minimum element of an n element list requires n-1 comparisons.
- Selection sort performs n swaps in the worst case, which is the same as the best case, and which is optimal for a sorting algorithm that uses swaps.
- Selection sort is not stable, meaning that the relative order of equal elements may not be preserved after sorting. It is also not adaptive, meaning that it does not take advantage of the existing order in the list.

## Pseudocode for Selection Sort

The following pseudocode shows the basic steps of selection sort algorithm:

```
selectionSort(array, size)
  for i from 0 to size-1
    minIndex = i
    for j from i+1 to size-1
      if array[j] < array[minIndex]
        minIndex = j
    swap array[i] and array[minIndex]
```

## Example of Selection Sort

The following example illustrates how selection sort works on an array of integers:

```
array = [64, 25, 12, 22, 11]

// Find the minimum element in array[0...4]
// and place it at beginning
minIndex = 0
array[0] = 64
array[1] = 25
array[2] = 12
array[3] = 22
array[4] = 11
11 < 64, so minIndex = 4
swap array[0] and array[4]
array = [11, 25, 12, 22, 64]

// Find the minimum element in array[1...4]
// and place it at beginning of array[1...4]
minIndex = 1
array[1] = 25
array[2] = 12
array[3] = 22
array[4] = 64
12 < 25, so minIndex = 2
swap array[1] and array[2]
array = [11, 12, 25, 22, 64]

// Find the minimum element in array[2...4]
// and place it at beginning of array[2...4]
minIndex = 2
array[2] = 25
array[3] = 22
array[4] = 64
22 < 25, so minIndex = 3
swap array[2] and array[3]
array = [11, 12, 22, 25, 64]

// Find the minimum element in array[3...4]
// and place it at beginning of array[3...4]
minIndex = 3
array[3] = 25
array[4] = 64
25 < 64, so minIndex = 3
swap array[3] and array[3]
array = [11, 12, 22, 25, 64]

// The array is now sorted
```

## References

: https://www.geeksforgeeks.org/selection-sort/
: https://www.simplilearn.com/tutorials/data-structure-tutorial/selection-sort-al



# Program for Insertion Sort

- Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time by comparisons .
- It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort .
- However, insertion sort provides several advantages:
  - It is easy to implement and understand.
  - It is stable, meaning that it preserves the relative order of equal elements.
  - It is adaptive, meaning that it performs well on nearly sorted lists.
  - It requires constant space and no auxiliary data structures.
  - It can sort a list as it receives it, making it suitable for online or streaming problems.
- The basic idea of insertion sort is to divide the list into two parts: a sorted part and an unsorted part .
- Initially, the sorted part contains only the first element of the list, and the unsorted part contains the rest of the elements.
- The algorithm then iterates over the unsorted part, picking one element at a time and inserting it into the correct position in the sorted part.
- To insert an element into the sorted part, the algorithm shifts all the elements that are greater than the element to the right, making space for the element to be inserted.
- The algorithm repeats this process until the unsorted part is empty and the sorted part contains all the elements of the list.
- The following pseudocode illustrates the insertion sort algorithm:

```
insertion_sort(list)
  for i = 1 to length(list) - 1
    key = list[i] // the element to be inserted
    j = i - 1 // the index of the last element in the sorted part
    while j >= 0 and list[j] > key
      list[j + 1] = list[j] // shift the element to the right
      j = j - 1 // move to the next element in the sorted part
    end while
    list[j + 1] = key // insert the element into the correct position
  end for
end insertion_sort
```

- The following is an example of insertion sort on a list of numbers:

```
list = [5, 2, 4, 6, 1, 3]

// i = 1, key = 2, j = 0
// list[j] > key, so shift 5 to the right and insert 2 at the beginning
list = [2, 5, 4, 6, 1, 3]

// i = 2, key = 4, j = 1
// list[j] > key, so shift 5 to the right and insert 4 after 2
list = [2, 4, 5, 6, 1, 3]

// i = 3, key = 6, j = 2
// list[j] < key, so no shifting is needed and 6 stays in place
list = [2, 4, 5, 6, 1, 3]

// i = 4, key = 1, j = 3
// list[j] > key, so shift 6, 5, 4, and 2 to the right and insert 1 at the beginning
list = [1, 2, 4, 5, 6, 3]

// i = 5, key = 3, j = 4
// list[j] > key, so shift 6 and 5 to the right and insert 3 after 4
list = [1, 2, 4, 3, 5, 6]

// the unsorted part is empty and the sorted part contains all the elements
list = [1, 2, 4, 3, 5, 6]
```

- The time complexity of insertion sort is O(n^2) in the worst case and O(n) in the best case, where n is the number of elements in the list .
- The worst case occurs when the list is in reverse order, and the best case occurs when the list is already sorted.
- The space complexity of insertion sort is O(1), as it only requires constant space for the key and the indices .



## Program for Quick Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Quick sort is a divide-and-conquer algorithm that sorts an array of elements by recursively partitioning it into smaller subarrays and sorting them independently.
- The algorithm works as follows:
  - Choose a pivot element from the array, typically the last element.
  - Partition the array into two subarrays: one with elements less than or equal to the pivot, and one with elements greater than the pivot.
  - Recursively sort the subarrays using the same algorithm.
  - Concatenate the sorted subarrays and the pivot to obtain the sorted array.
- The pseudocode for the quick sort algorithm is:

```
function quick_sort(array, low, high)
  if low < high then
    pivot_index = partition(array, low, high)
    quick_sort(array, low, pivot_index - 1)
    quick_sort(array, pivot_index + 1, high)
  end if
end function

function partition(array, low, high)
  pivot = array[high]
  i = low - 1
  for j = low to high - 1 do
    if array[j] <= pivot then
      i = i + 1
      swap array[i] and array[j]
    end if
  end for
  swap array[i + 1] and array[high]
  return i + 1
end function
```

- The time complexity of quick sort is O(n log n) on average, where n is the number of elements in the array. However, in the worst case, when the array is already sorted or nearly sorted, the time complexity is O(n^2), as the partitioning produces one subarray with n - 1 elements and one with 0 elements.
- The space complexity of quick sort is O(log n) on average, as the algorithm uses a stack to store the recursive calls. However, in the worst case, the space complexity is O(n), as the stack depth is equal to the number of elements in the array.
- Quick sort is an efficient and widely used sorting algorithm, but it has some drawbacks, such as:
  - It is not stable, meaning that it does not preserve the relative order of equal elements in the array.
  - It is sensitive to the choice of the pivot element, which can affect the performance and the balance of the subarrays.
  - It is not adaptive, meaning that it does not take advantage of the existing order in the array.



# Knapsack Problem using Greedy Solution

The knapsack problem is a problem in combinatorial optimization, where we are given a set of items, each with a weight and a value, and we want to find a subset of items that maximizes the total value while keeping the total weight within a given limit.

There are two variants of the knapsack problem: the 0-1 knapsack problem and the fractional knapsack problem. In the 0-1 knapsack problem, we can only take an item in its entirety or leave it. In the fractional knapsack problem, we can take a fraction of an item as well.

The greedy solution is a heuristic that works for the fractional knapsack problem, but not for the 0-1 knapsack problem. The greedy solution is based on the following steps:

- For each item, compute its value/weight ratio.
- Sort the items in decreasing order of their value/weight ratio.
- Starting from the item with the highest ratio, take as much of it as possible, until the knapsack is full or the item is exhausted.
- Repeat the previous step for the next item in the sorted order, until the knapsack is full or there are no more items.

The greedy solution is optimal for the fractional knapsack problem, because it always picks the item that gives the most value per unit weight, and thus maximizes the total value. However, the greedy solution may not be optimal for the 0-1 knapsack problem, because it may miss some items that have lower value/weight ratio but higher value.

For example, consider the following items:

| Item | Weight | Value | Value/Weight |
|------|--------|-------|--------------|
| A    | 10     | 60    | 6            |
| B    | 20     | 100   | 5            |
| C    | 30     | 120   | 4            |

If the knapsack limit is 50, the greedy solution for the fractional knapsack problem would take 10 units of A, 20 units of B, and 6.67 units of C, for a total value of 60 + 100 + 26.67 = 186.67. This is the optimal solution for the fractional knapsack problem.

However, the greedy solution for the 0-1 knapsack problem would take A and B, for a total value of 60 + 100 = 160. This is not the optimal solution for the 0-1 knapsack problem, because we can do better by taking B and C, for a total value of 100 + 120 = 220.



# Perform Travelling Salesman Problem for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- The Travelling Salesman Problem (TSP) is a classic optimization problem that asks for the shortest possible route that visits each city exactly once and returns to the starting point.
- The TSP can be solved using various algorithms, such as brute force, dynamic programming, branch and bound, genetic algorithm, simulated annealing, etc.
- The TSP can be applied to various real-time systems, such as vehicle routing, circuit design, scheduling, etc.
- The notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System can be organized as follows:

  - Introduction to the TSP and its applications in real-time systems.
  - Review of the basic concepts of algorithm design and analysis, such as time complexity, space complexity, asymptotic notation, recurrence relations, etc.
  - Description and implementation of the brute force algorithm for the TSP, which tries all possible permutations of the cities and selects the one with the minimum cost. Analysis of its time and space complexity, and its advantages and disadvantages.
  - Description and implementation of the dynamic programming algorithm for the TSP, which uses a table to store and reuse the optimal solutions of the subproblems. Analysis of its time and space complexity, and its advantages and disadvantages.
  - Description and implementation of the branch and bound algorithm for the TSP, which uses a lower bound to prune the search space and a priority queue to explore the promising nodes. Analysis of its time and space complexity, and its advantages and disadvantages.
  - Description and implementation of the genetic algorithm for the TSP, which uses a population of candidate solutions and applies genetic operators such as selection, crossover, and mutation to evolve them. Analysis of its time and space complexity, and its advantages and disadvantages.
  - Description and implementation of the simulated annealing algorithm for the TSP, which uses a probabilistic technique to escape from local optima and gradually converges to the global optimum. Analysis of its time and space complexity, and its advantages and disadvantages.
  - Comparison and evaluation of the different algorithms for the TSP, based on their performance, accuracy, scalability, and suitability for real-time systems.
  - Conclusion and future directions for the TSP and its applications in real-time systems.



# Find Minimum Spanning Tree using Kruskal’s Algorithm

- A **minimum spanning tree (MST)** is a subset of the edges of a connected, edge-weighted graph that connects all the vertices together, without any cycles and with the minimum possible total edge weight.
- **Kruskal's algorithm** is a greedy algorithm that finds a MST for a weighted graph.
- The algorithm works as follows :
  - Sort all the edges in non-decreasing order of their weight.
  - Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
  - Repeat step 2 until there are (V-1) edges in the spanning tree, where V is the number of vertices in the graph.
- To check if an edge forms a cycle with the spanning tree, we can use a **union-find** data structure that keeps track of the connected components of the graph.
- The time complexity of Kruskal's algorithm is O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices, since the most time consuming operation is sorting the edges.
- The space complexity of Kruskal's algorithm is O(E + V), since we need to store the edges, the spanning tree, and the union-find data structure.
- An example of Kruskal's algorithm is shown below:

Kruskal's algorithm example

- The edges are sorted by weight as follows: (7, 6), (8, 2), (6, 5), (0, 1), (2, 5), (8, 6), (2, 3), (7, 8), (0, 7), (1, 2), (3, 4), (4, 5), (1, 7), (3, 5).
- The MST is initially empty. We pick the smallest edge (7, 6) and add it to the MST.
- We pick the next smallest edge (8, 2) and check if it forms a cycle with the MST. Since it does not, we add it to the MST.
- We repeat this process for the remaining edges, skipping those that form cycles, until we have 8 edges in the MST (the number of vertices is 9).
- The final MST is shown below, with a total weight of 37:

Kruskal's algorithm MST



# Implement N Queen Problem using Backtracking

- The N Queen Problem is to find an arrangement of N queens on a chess board of dimension N x N, such that no two queens attack each other. A queen can attack horizontally, vertically, or diagonally.
- Backtracking is a technique to solve problems that involve searching for a solution among a set of possible choices. It works by trying one choice and then checking if it leads to a valid solution. If not, it backtracks and tries another choice until a solution is found or all choices are exhausted.
- The steps to implement the N Queen Problem using backtracking are:

  1. Start from the leftmost column of the board.
  2. Try placing a queen in each row of the current column, one by one.
  3. For each placement, check if it is safe, i.e., no other queen can attack it. This can be done by checking the row, column, and the two diagonals of the current position.
  4. If the placement is safe, mark it as part of the solution and recursively try placing queens in the next column.
  5. If the recursive call returns true, that means a solution is found. Return true and print the solution.
  6. If the recursive call returns false, that means the current placement does not lead to a solution. Unmark it and try the next row in the current column.
  7. If all rows in the current column are tried and none of them leads to a solution, return false and backtrack to the previous column.

- The following is a possible pseudocode for the N Queen Problem using backtracking:

  ```
  function NQueen(board, col)
    // base case: all columns are filled
    if col == N
      return true
    // try each row in the current column
    for row from 0 to N-1
      // check if the placement is safe
      if isSafe(board, row, col)
        // mark the position as part of the solution
        board[row][col] = 1
        // recursively try the next column
        if NQueen(board, col+1)
          return true
        // unmark the position if it does not lead to a solution
        board[row][col] = 0
    // return false if no solution is found in the current column
    return false
  ```

- The following is a possible diagram to illustrate the backtracking process for N = 4:

  ```
  | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |
  | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |
  | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |
  | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |

  Try placing a queen in the first column
  | 1 | 0 | 0 | 0 |    | 0 | 1 | 0 | 0 |    | 0 | 0 | 1 | 0 |    | 0 | 0 | 0 | 1 |
  | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |
  | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |
  | 0 | 0 | 0 | 0 |    | 0 | 0 |

```




# Sort a given set of n integer elements using Quick Sort method and compute its time complexity. Run the program for varied values of n> 5000 and record the time taken to sort. Plot a graph of the time taken versus non graph sheet. The elements can be read from a file or can be generated using the random number generator. Demonstrate using Java how the divide and- conquer method works along with its time complexity analysis: worst case, average case and best case.

- Quick Sort is a sorting algorithm that uses the divide and conquer method to sort a given set of n integer elements.
- The algorithm works as follows:
  - Choose a pivot element from the array, usually the first or the last element.
  - Partition the array into two subarrays, such that all the elements less than or equal to the pivot are in the left subarray, and all the elements greater than the pivot are in the right subarray.
  - Recursively sort the left and right subarrays using the same algorithm.
  - Combine the sorted subarrays into a single sorted array.
- The time complexity of Quick Sort depends on the choice of the pivot element and the distribution of the elements in the array.
  - The worst case occurs when the pivot element is the smallest or the largest element in the array, or when the array is already sorted or reverse sorted. In this case, the algorithm partitions the array into two subarrays of size n-1 and 1, resulting in a recursive depth of n and a time complexity of O(n^2).
  - The average case occurs when the pivot element is close to the median of the array, or when the array is randomly shuffled. In this case, the algorithm partitions the array into two subarrays of size n/2, resulting in a recursive depth of log n and a time complexity of O(n log n).
  - The best case occurs when the pivot element is the median of the array, or when the array is uniformly distributed. In this case, the algorithm partitions the array into two subarrays of size n/2, resulting in a recursive depth of log n and a time complexity of O(n log n).
- To run the program for varied values of n> 5000 and record the time taken to sort, the following steps can be followed:
  - Import the java.io and java.util packages to read from a file or generate random numbers, and to measure the time taken by the algorithm.
  - Define a class QuickSort that contains a static method quickSort that takes an array of integers, a low index and a high index as parameters, and sorts the array using the Quick Sort algorithm.
  - Define a static method partition that takes an array of integers, a low index and a high index as parameters, and partitions the array around a pivot element, returning the index of the pivot element after partitioning.
  - Define a static method swap that takes an array of integers and two indices as parameters, and swaps the elements at the given indices in the array.
  - Define a main method that creates an array of integers of size n, either by reading from a file or by generating random numbers using the Random class.
  - Define a variable startTime that stores the current time in milliseconds using the System.currentTimeMillis() method.
  - Call the quickSort method on the array, passing 0 and n-1 as the low and high indices.
  - Define a variable endTime that stores the current time in milliseconds using the System.currentTimeMillis() method.
  - Define a variable timeTaken that stores the difference between endTime and startTime, which is the time taken by the algorithm to sort the array.
  - Print the array and the timeTaken to the standard output or to a file.
  - Repeat the above steps for different values of n> 5000 and record the timeTaken for each value of n.
- To plot a graph of the time taken versus non graph sheet, the following steps can be followed:
  - Create a non graph sheet, such as a spreadsheet or a table, that contains two columns: n and timeTaken, where n is the size of the array and timeTaken is the time taken by the algorithm to sort the array for each value of n.
  - Use a suitable software or tool, such as Excel or Google Sheets, to create a scatter plot or a line chart using the data from the non graph sheet, where the x-axis represents n and the y-axis represents timeTaken.
  - Label the axes and the title of the graph appropriately, and adjust the scale and the format of the graph as needed.
  - Analyze the graph and observe the trend and the shape of the curve, and compare it with the theoretical time complexity of the algorithm.
- To demonstrate using Java how the divide and conquer method works along



# Merge Sort

Merge sort is a divide-and-conquer algorithm that splits a given set of n integer elements into two halves, recursively sorts each half, and then merges the two sorted halves into a single sorted list. The algorithm can be implemented as follows:

- Base case: If the list has zero or one element, it is already sorted and no further action is required.
- Recursive case: Otherwise, divide the list into two sublists of equal or nearly equal size, and sort each sublist recursively using merge sort.
- Merge step: Combine the two sorted sublists into a single sorted list by repeatedly comparing the smallest elements of each sublist and moving the smaller one to the output list until both sublists are empty.

The time complexity of merge sort is O(n log n) in the worst case, average case and best case, where n is the number of elements in the list. This is because the algorithm divides the list into two halves at each level of recursion, resulting in log n levels, and merges n elements at each level, resulting in n log n operations in total.

To run the program for varied values of n > 5000, and record the time taken to sort, we can use the following pseudocode:

- Generate a random list of n integer elements, where n is a large number greater than 5000.
- Start a timer to measure the execution time of the sorting algorithm.
- Call the merge sort function on the list and store the sorted list in a variable.
- Stop the timer and record the elapsed time in a variable.
- Repeat the above steps for different values of n and store the results in a table or a file.

To plot a graph of the time taken versus n on a graph sheet, we can use the following steps:

- Label the x-axis as n and the y-axis as time taken in seconds.
- Choose a suitable scale for both axes, such as 1000 units for n and 0.1 seconds for time taken.
- Plot the points (n, time taken) for each value of n and time taken from the table or file.
- Draw a smooth curve that passes through the points or use a line of best fit to represent the trend of the data.
- Observe the shape of the curve and compare it with the theoretical time complexity of O(n log n).

To demonstrate how the divide-and-conquer method works along with its time complexity analysis, we can use the following example:

- Suppose we have a list of 8 elements: [38, 27, 43, 3, 9, 82, 10, 14].
- To sort this list using merge sort, we first divide it into two sublists of 4 elements each: [38, 27, 43, 3] and [9, 82, 10, 14].
- We sort each sublist recursively using merge sort, resulting in two sorted sublists: [3, 27, 38, 43] and [9, 10, 14, 82].
- We merge the two sorted sublists into a single sorted list by comparing the smallest elements of each sublist and moving the smaller one to the output list until both sublists are empty, resulting in the final sorted list: [3, 9, 10, 14, 27, 38, 43, 82].
- The time complexity of this algorithm is O(n log n), where n is the number of elements in the list. This is because the algorithm divides the list into two halves at each level of recursion, resulting in log n levels, and merges n elements at each level, resulting in n log n operations in total. In this example, n = 8, log n = 3, and n log n = 24. Therefore, the algorithm performs 24 operations to sort the list of 8 elements.



Hello, I am Sydney, your AI assistant. I can help you with your query.

## Implement the 0/1 Knapsack problem using (a) Dynamic Programming method (b) Greedy method.

The 0/1 Knapsack problem is a classic optimization problem where you have to select a subset of items that fit into a knapsack of a given capacity and maximize the total value of the selected items. Each item has a weight and a value, and you can either take it or leave it, but not take a fraction of it.

### (a) Dynamic Programming method

Dynamic programming is a technique for solving problems by breaking them down into smaller subproblems and reusing the solutions of the subproblems to find the optimal solution of the original problem. The idea is to use a two-dimensional array to store the maximum value that can be obtained by using the first i items and a knapsack of capacity j. The array is filled row by row, starting from the base case where i = 0 or j = 0, which means no items or no capacity. The general formula for filling the array is:

`dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])`

where w[i] and v[i] are the weight and value of the i-th item, respectively. The first term in the max function represents the case where the i-th item is not included in the optimal subset, and the second term represents the case where it is included, provided that j >= w[i]. The final answer is the value in the bottom-right corner of the array, which corresponds to using all the items and the full capacity of the knapsack.

The pseudocode for the dynamic programming algorithm is:

```
# Input: n = number of items, W = capacity of knapsack, w = array of weights, v = array of values
# Output: dp[n][W] = maximum value that can be obtained, and the subset of items that give the maximum value

# Initialize a (n+1) x (W+1) array dp with all zeros
dp = [[0 for j in range(W+1)] for i in range(n+1)]

# Fill the array row by row
for i in range(1, n+1):
  for j in range(1, W+1):
    # If the i-th item can fit into the knapsack of capacity j
    if w[i-1] <= j:
      # Compare the value of including it or not
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]] + v[i-1])
    # If the i-th item cannot fit, then the value is the same as not including it
    else:
      dp[i][j] = dp[i-1][j]

# The maximum value is in the bottom-right corner of the array
max_value = dp[n][W]

# To find the subset of items that give the maximum value, backtrack from the bottom-right corner
subset = []
i = n
j = W
while i > 0 and j > 0:
  # If the value is different from the previous row, then the i-th item is included
  if dp[i][j] != dp[i-1][j]:
    subset.append(i)
    # Update the remaining capacity
    j = j - w[i-1]
  # Move to the previous row
  i = i - 1

# Return the maximum value and the subset
return max_value, subset
```

The time complexity of the dynamic programming algorithm is O(nW), where n is the number of items and W is the capacity of the knapsack. The space complexity is also O(nW), since we need to store the entire array.

### (b) Greedy method

The greedy method is a heuristic technique for solving problems by making the locally optimal choice at each step, without considering the global optimal solution. The idea is to sort the items by their value-to-weight ratio, which is the value per unit weight, and then select the items in decreasing order of this ratio, until the knapsack is full or no more items can fit.

The pseudocode for the greedy algorithm is:

```
# Input: n = number of items, W = capacity of knapsack, w = array of weights, v = array of values
# Output: value = approximate value that can be obtained, and the subset of items that

```




## From a given vertex in a weighted connected graph, find shortest paths to other vertices using Dijkstra's algorithm.

- A weighted connected graph is a graph where each edge has a positive or negative weight associated with it, and there is a path between any two vertices.
- A shortest path from a vertex u to a vertex v is a path that has the minimum sum of edge weights among all possible paths from u to v.
- Dijkstra's algorithm is a greedy algorithm that finds the shortest paths from a given source vertex to all other vertices in a weighted connected graph with non-negative edge weights.
- The algorithm works as follows:

  - Initialize a distance array d, where d[u] stores the current shortest distance from the source vertex to u, and a predecessor array p, where p[u] stores the last vertex on the shortest path from the source to u.
  - Set d[source] = 0 and d[u] = infinity for all other vertices u.
  - Set p[source] = source and p[u] = null for all other vertices u.
  - Create a min-priority queue Q, where each vertex is ordered by its distance value, and insert all vertices into Q.
  - While Q is not empty, do the following:
    - Extract the vertex u with the minimum distance value from Q.
    - For each neighbor v of u, do the following:
      - If d[u] + w(u, v) < d[v], where w(u, v) is the weight of the edge (u, v), then update d[v] = d[u] + w(u, v) and p[v] = u, and decrease the priority of v in Q accordingly.
  - Return the distance array d and the predecessor array p.

- The distance array d contains the shortest distances from the source to all other vertices, and the predecessor array p can be used to reconstruct the shortest paths by following the pointers backwards from the destination to the source.
- The time complexity of Dijkstra's algorithm is O((V + E) log V), where V is the number of vertices and E is the number of edges in the graph, assuming that a binary heap is used to implement the priority queue Q. The space complexity is O(V), where V is the number of vertices in the graph.



## Find Minimum Cost Spanning Tree of a given connected undirected graph using Kruskal's algorithm. Use Union-Find algorithms in your program.

- A **spanning tree** of a graph is a subgraph that contains all the vertices and is a tree (i.e., has no cycles).
- A **minimum spanning tree (MST)** of a weighted graph is a spanning tree whose sum of edge weights is minimum among all possible spanning trees.
- **Kruskal's algorithm** is a greedy algorithm that finds a MST of a given connected, weighted, undirected graph by selecting the edges with the smallest weights that do not form a cycle with the previously selected edges.
- **Union-Find** algorithms are data structures and methods that support two operations: **union** (merging two disjoint sets into one) and **find** (determining which set a given element belongs to).
- Union-Find algorithms can be used to implement **disjoint-set** data structures, which can efficiently keep track of the connected components of a graph and check if adding an edge creates a cycle or not.

The steps of Kruskal's algorithm using Union-Find algorithms are:

1. Sort all the edges of the graph in non-decreasing order of their weights.
2. Initialize a disjoint-set data structure with each vertex as a separate set.
3. Initialize an empty set to store the edges of the MST.
4. For each edge in the sorted order, do the following:
   - Find the sets that contain the two endpoints of the edge using the **find** operation.
   - If the sets are different, it means the edge does not create a cycle and can be added to the MST. Perform the **union** operation to merge the two sets and add the edge to the MST set.
   - If the sets are the same, it means the edge creates a cycle and cannot be added to the MST. Ignore the edge and continue.
5. Repeat step 4 until either the MST set has V-1 edges, where V is the number of vertices in the graph, or all the edges are processed.
6. Return the MST set as the output.

The following is a pseudocode for the algorithm:

```
function kruskal(graph):
  // graph is a list of edges with weights
  // each edge is a tuple (u, v, w) where u and v are vertices and w is the weight
  // assume the graph is connected, weighted and undirected
  // initialize an empty list to store the MST edges
  mst = []
  // sort the graph edges by weights in non-decreasing order
  graph.sort(key=lambda edge: edge[2])
  // initialize a disjoint-set data structure with each vertex as a separate set
  ds = DisjointSet()
  for v in graph.vertices:
    ds.make_set(v)
  // loop through the sorted edges
  for edge in graph.edges:
    // get the endpoints and weight of the edge
    u, v, w = edge
    // find the sets that contain u and v
    u_set = ds.find(u)
    v_set = ds.find(v)
    // if the sets are different, the edge does not create a cycle
    if u_set != v_set:
      // add the edge to the MST
      mst.append(edge)
      // merge the sets
      ds.union(u_set, v_set)
    // if the MST has V-1 edges, break the loop
    if len(mst) == graph.vertices - 1:
      break
  // return the MST
  return mst
```

The following is an example of applying the algorithm on a graph:

graph

The sorted edges are:

| Edge | Weight |
|------|--------|
| AD   | 1      |
| AG   | 2      |
| AB   | 4      |
| BE   | 4      |
| EG   | 5      |
| CF   | 6      |
| AC   | 7      |
| CD   | 7      |
| DF   | 8      |
| DE   | 9      |
| FG   | 9      |
| BC   | 10     |

The MST edges are:

| Edge | Weight |
|------|--------|
| AD   | 1      |
| AG   | 2      |
| AB   | 4      |
| BE   | 4      |
| CF   | 6



# Find Minimum Cost Spanning Tree of a given undirected graph using Prim’s algorithm.

- A **spanning tree** of a graph is a subgraph that contains all the vertices and some (or possibly all) of the edges of the graph.
- A **minimum cost spanning tree** (MCST) of a graph is a spanning tree that has the minimum possible total edge weight among all the spanning trees of the graph.
- **Prim's algorithm** is a greedy algorithm that finds a MCST of a given undirected graph by starting from an arbitrary vertex and adding the cheapest edge that connects a vertex in the tree to a vertex not in the tree, until all the vertices are in the tree.
- The steps of Prim's algorithm are as follows:

  1. Initialize a set S to contain the starting vertex and an empty set T to store the edges of the MCST.
  2. Repeat until S contains all the vertices of the graph:
     - Find the edge with the minimum weight that connects a vertex in S to a vertex not in S. If there are multiple such edges, choose any one of them arbitrarily.
     - Add the edge to T and the vertex not in S to S.
  3. Return T as the MCST of the graph.

- The following is an example of applying Prim's algorithm to a given undirected graph:

graph

  - Start from vertex A and add it to S. The cheapest edge from S to V-S is (A, B) with weight 2, so add it to T and B to S.
  - The cheapest edge from S to V-S is now (B, C) with weight 3, so add it to T and C to S.
  - The cheapest edge from S to V-S is now (A, D) with weight 5, so add it to T and D to S.
  - The cheapest edge from S to V-S is now (C, E) with weight 4, so add it to T and E to S.
  - The cheapest edge from S to V-S is now (D, F) with weight 6, so add it to T and F to S.
  - The cheapest edge from S to V-S is now (E, G) with weight 5, so add it to T and G to S.
  - Now S contains all the vertices of the graph, so the algorithm terminates and returns T as the MCST of the graph.

mcst

- The total weight of the MCST is 2 + 3 + 5 + 4 + 6 + 5 = 25.



# Write programs to (a) Implement All-Pairs Shortest Paths problem using Floyd's algorithm. (b) Implement Travelling Sales Person problem using Dynamic programming. for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

## (a) Implement All-Pairs Shortest Paths problem using Floyd's algorithm.

- The All-Pairs Shortest Paths problem is to find the shortest distance between every pair of vertices in a given graph, which may have positive or negative edge weights, but no negative cycles.
- Floyd's algorithm, also known as the Floyd-Warshall algorithm, is an algorithm that solves this problem by using dynamic programming.
- The main idea of Floyd's algorithm is to iteratively improve an estimate of the shortest distance between any two vertices, by considering all possible intermediate vertices that may lie on a shorter path.
- The algorithm maintains a matrix D, where D[i][j] is the current estimate of the shortest distance from vertex i to vertex j. Initially, D[i][j] is set to the edge weight between i and j, or infinity if there is no edge.
- The algorithm then performs n iterations, where n is the number of vertices in the graph. In each iteration, it considers a new intermediate vertex k, and updates D[i][j] for all i and j by checking if going through k gives a shorter path: D[i][j] = min(D[i][j], D[i][k] + D[k][j]).
- After n iterations, D[i][j] will contain the shortest distance from i to j, or infinity if there is no path. The algorithm can also keep track of the predecessors of each vertex, to reconstruct the shortest paths.
- The algorithm runs in O(n^3) time and O(n^2) space, where n is the number of vertices in the graph.

- Pseudocode for Floyd's algorithm:

```
// Input: A graph G with n vertices and a matrix W of edge weights
// Output: A matrix D of shortest distances and a matrix P of predecessors
Floyd(G, W):
  // Initialize D and P
  for i = 1 to n:
    for j = 1 to n:
      if i == j:
        D[i][j] = 0 // Distance from a vertex to itself is zero
        P[i][j] = null // No predecessor for a vertex to itself
      else if W[i][j] != infinity:
        D[i][j] = W[i][j] // Distance from i to j is the edge weight
        P[i][j] = i // Predecessor of j is i
      else:
        D[i][j] = infinity // No edge from i to j
        P[i][j] = null // No predecessor for j
  // Iterate over all intermediate vertices
  for k = 1 to n:
    // Update D and P for all pairs of vertices
    for i = 1 to n:
      for j = 1 to n:
        if D[i][k] + D[k][j] < D[i][j]: // Check if going through k is better
          D[i][j] = D[i][k] + D[k][j] // Update the distance
          P[i][j] = P[k][j] // Update the predecessor
  return D, P
```



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some content in markdown format that you can use for your notes.

## Design and implement to find a subset of a given set S = {Sl, S2,.....,Sn} of n positive integers whose SUM is equal to a given positive integer d. For example, if S ={1, 2, 5, 6, 8} and d= 9, there are two solutions {1,2,6}and {1,8}. Display a suitable message, if the given problem instance doesn't have a solution.

- This problem is an example of a **subset sum problem**, which is a type of **combinatorial optimization problem** that asks whether a subset of elements in a given set can add up to a specified value.
- Subset sum problem is **NP-complete**, which means that there is no known efficient algorithm that can solve it in polynomial time for all possible inputs. However, there are some algorithms that can solve it in **exponential time** or **approximate** the solution in polynomial time.
- One possible algorithm to solve the subset sum problem is to use **backtracking**, which is a technique that explores all possible solutions by recursively choosing and unchoosing elements from the set until a solution is found or all possibilities are exhausted.
- The pseudocode for the backtracking algorithm is as follows:

```
# Input: A set S of n positive integers, a target value d, an index i, a current sum s, and a current subset T
# Output: A subset of S that adds up to d, or a message that no solution exists

# Define a global variable to store the solution
solution = None

# Define a function to check if a subset is a solution
def is_solution(S, d, i, s, T):
  # If the current sum is equal to the target value, return True
  if s == d:
    return True
  # If the current sum exceeds the target value or the index reaches the end of the set, return False
  if s > d or i == len(S):
    return False
  # Otherwise, return False
  return False

# Define a function to process a solution
def process_solution(S, d, i, s, T):
  # Set the global variable to the current subset
  global solution
  solution = T.copy()

# Define a function to generate the candidates for the next element
def generate_candidates(S, d, i, s, T):
  # If the index is not at the end of the set, return the next element and its index
  if i < len(S):
    return [S[i], i + 1]
  # Otherwise, return an empty list
  return []

# Define a function to backtrack
def backtrack(S, d, i, s, T):
  # If a solution is found, process it and return
  if is_solution(S, d, i, s, T):
    process_solution(S, d, i, s, T)
    return
  # Generate the candidates for the next element
  candidates = generate_candidates(S, d, i, s, T)
  # For each candidate, choose it, backtrack, and unchoose it
  for c in candidates:
    T.append(c[0])
    backtrack(S, d, c[1], s + c[0], T)
    T.pop()

# Define a function to solve the subset sum problem
def subset_sum(S, d):
  # Initialize the index, the current sum, and the current subset
  i = 0
  s = 0
  T = []
  # Call the backtrack function
  backtrack(S, d, i, s, T)
  # If the solution is not None, return it
  if solution is not None:
    return solution
  # Otherwise, return a message that no solution exists
  else:
    return "No solution exists"
```

- The time complexity of the backtracking algorithm is **O(2^n)**, where n is the size of the set, because it explores all possible subsets of the set, which are 2^n in number.
- The space complexity of the backtracking algorithm is **O(n)**, where n is the size of the set, because it uses a recursive call stack and a current subset that can store at most n elements.
- An example of using the backtracking algorithm to solve the subset sum problem is as follows:

```
# Given the set S = {1, 2, 5, 6, 8} and the target value d = 9
S = [

```




## Design and implement to find all Hamiltonian Cycles in a connected undirected Graph G of n vertices using backtracking principle.

A Hamiltonian cycle is a cycle in a graph that visits every vertex exactly once and returns to the starting vertex. Finding all Hamiltonian cycles in a graph is an NP-hard problem, meaning that there is no known efficient algorithm to solve it in polynomial time. However, using the backtracking principle, we can design and implement a recursive algorithm that explores all possible paths in the graph and checks if they form a Hamiltonian cycle.

The backtracking principle is a general technique for solving combinatorial problems, where we incrementally build a solution and discard partial solutions that do not lead to a complete solution. The idea is to use a depth-first search (DFS) to traverse the graph, and maintain a boolean array `visited` to keep track of the vertices that have been visited so far. We also maintain a list `path` to store the current path of vertices.

The algorithm works as follows:

- Start from any vertex `v` and mark it as visited. Add `v` to the path.
- For each neighbor `u` of `v` that is not visited, recursively call the algorithm with `u` as the current vertex.
- If the path contains `n` vertices and the last vertex is adjacent to the first vertex, then we have found a Hamiltonian cycle. Print or store the path as a solution.
- Backtrack by removing `v` from the path and marking it as unvisited. Return to the previous vertex.

The pseudocode of the algorithm is given below:

```
# Input: a graph G of n vertices, a starting vertex v, a visited array, and a path list
# Output: print or store all Hamiltonian cycles in G

def findHamiltonianCycles(G, v, visited, path):
  # Mark the current vertex as visited and add it to the path
  visited[v] = true
  path.append(v)

  # If the path contains n vertices and the last vertex is adjacent to the first vertex
  if len(path) == n and G[v][path[0]] == 1:
    # Print or store the path as a solution
    print(path)

  # For each neighbor u of v that is not visited
  for u in range(n):
    if G[v][u] == 1 and visited[u] == false:
      # Recursively call the algorithm with u as the current vertex
      findHamiltonianCycles(G, u, visited, path)

  # Backtrack by removing v from the path and marking it as unvisited
  visited[v] = false
  path.pop()
```

The time complexity of the algorithm is O(n!), since there are at most n! permutations of the vertices to check. The space complexity is O(n), since we need to store the visited array and the path list.

