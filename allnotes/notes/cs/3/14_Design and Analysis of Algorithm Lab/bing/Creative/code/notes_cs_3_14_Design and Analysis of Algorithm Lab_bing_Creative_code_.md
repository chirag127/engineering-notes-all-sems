

## Program for Recursive Binary & Linear Search for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

### Binary Search

Binary search is a searching algorithm that is used to find the position of an element (target value) in a sorted array. The array should be sorted prior to applying a binary search.

Binary search is a recursive algorithm. The high level approach is that we examine the middle element of the list. The value of the middle element determines whether to terminate the algorithm (found the key), recursively search the left half of the list, or recursively search the right half of the list.

Binary search can be implemented in two ways: iterative and recursive. The iterative method uses a while loop to repeatedly update the low and high indices of the search range until the target value is found or the range becomes empty. The recursive method follows the divide and conquer approach, where the original problem is divided into smaller subproblems and solved recursively until the base case is reached  .

The pseudocode for the recursive binary search algorithm is as follows:

```
binarySearch(array, target, low, high)
  if low > high
    return -1 // target not found
  mid = (low + high) / 2 // calculate the middle index
  if target == array[mid]
    return mid // target found at mid
  else if target < array[mid]
    return binarySearch(array, target, low, mid - 1) // search in the left half
  else
    return binarySearch(array, target, mid + 1, high) // search in the right half
```

The time complexity of binary search is O(log n), where n is the size of the array. The space complexity of the recursive binary search is O(log n), due to the stack space used by the recursive calls. The space complexity of the iterative binary search is O(1), as no extra space is used.

### Linear Search

Linear search is a searching algorithm that is used to find the position of an element (target value) in an array. It does not require the array to be sorted. It works by comparing each element of the array with the target value until a match is found or the end of the array is reached.

Linear search can also be implemented in two ways: iterative and recursive. The iterative method uses a for loop to traverse the array and check each element. The recursive method calls itself with a smaller array until the target value is found or the array becomes empty.

The pseudocode for the recursive linear search algorithm is as follows:

```
linearSearch(array, target, index)
  if index == array.length
    return -1 // target not found
  if target == array[index]
    return index // target found at index
  else
    return linearSearch(array, target, index + 1) // search in the next element
```

The time complexity of linear search is O(n), where n is the size of the array. The space complexity of the recursive linear search is O(n), due to the stack space used by the recursive calls. The space complexity of the iterative linear search is O(1), as no extra space is used.



## Program for Heap Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure to sort a given array of elements.
- A binary heap is a complete binary tree that satisfies the heap property, which means that every node is greater than or equal to its children (max-heap) or less than or equal to its children (min-heap).
- The basic idea of heap sort is to build a max-heap or a min-heap from the input array, and then repeatedly extract the root element (which is the maximum or minimum element) and place it at the end of the sorted array, until the heap is empty.
- The algorithm can be implemented as follows:

```
// A function to swap two elements in an array
void swap(int arr[], int i, int j) {
  int temp = arr[i];
  arr[i] = arr[j];
  arr[j] = temp;
}

// A function to heapify a subtree rooted at index i in an array of size n
// This function assumes that the subtrees rooted at i's children are already heapified
void heapify(int arr[], int n, int i) {
  // Find the largest among the root, left child and right child
  int largest = i;
  int left = 2 * i + 1;
  int right = 2 * i + 2;

  if (left < n && arr[left] > arr[largest]) {
    largest = left;
  }

  if (right < n && arr[right] > arr[largest]) {
    largest = right;
  }

  // If the largest is not the root, swap it with the root and heapify the affected subtree
  if (largest != i) {
    swap(arr, i, largest);
    heapify(arr, n, largest);
  }
}

// A function to perform heap sort on an array of size n
void heapSort(int arr[], int n) {
  // Build a max-heap from the input array
  for (int i = n / 2 - 1; i >= 0; i--) {
    heapify(arr, n, i);
  }

  // Extract the root element and place it at the end of the sorted array
  // Repeat this process until the heap is empty
  for (int i = n - 1; i > 0; i--) {
    swap(arr, 0, i);
    heapify(arr, i, 0);
  }
}
```

- The time complexity of heap sort is O(n log n) in the worst, average and best cases, as the heapify function takes O(log n) time and is called n times in the algorithm.
- The space complexity of heap sort is O(1), as it only requires a constant amount of auxiliary space to perform the swaps.
- Heap sort is an in-place and unstable sorting algorithm, as it does not preserve the relative order of equal elements in the input array.
- Heap sort is suitable for sorting large data sets, as it can handle them efficiently and does not require additional memory. However, it is not very adaptive, as it does not take advantage of the existing order in the input array.



## Program for Merge Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Merge sort is a divide-and-conquer algorithm that recursively splits an array into two subarrays and then merges them in sorted order.
- The algorithm can be implemented using the following steps:

  1. If the array has only one element, return it as it is already sorted.
  2. Otherwise, divide the array into two equal or nearly equal subarrays and call merge sort on each subarray recursively.
  3. Merge the two sorted subarrays into one sorted array by comparing the first elements of each subarray and taking the smaller one into the output array. Repeat this until both subarrays are exhausted.
  4. Return the merged array as the final output.

- The time complexity of merge sort is O(n log n) in the worst, average, and best cases, where n is the number of elements in the array. This is because the algorithm divides the array into log n levels and performs O(n) work at each level.
- The space complexity of merge sort is O(n) in the worst case, as the algorithm requires an auxiliary array of the same size as the input array to store the merged output.
- The following is a possible C++ program for merge sort:

```cpp
// A function to merge two sorted subarrays into one sorted array
void merge(int arr[], int left, int mid, int right) {
  // Find the sizes of the two subarrays
  int n1 = mid - left + 1;
  int n2 = right - mid;

  // Create temporary arrays to store the subarrays
  int L[n1], R[n2];

  // Copy the subarrays into the temporary arrays
  for (int i = 0; i < n1; i++)
    L[i] = arr[left + i];
  for (int j = 0; j < n2; j++)
    R[j] = arr[mid + 1 + j];

  // Initialize indices for the subarrays and the output array
  int i = 0, j = 0, k = left;

  // Merge the subarrays into the output array by comparing the first elements of each subarray
  while (i < n1 && j < n2) {
    if (L[i] <= R[j]) {
      arr[k] = L[i];
      i++;
    } else {
      arr[k] = R[j];
      j++;
    }
    k++;
  }

  // Copy the remaining elements of the left subarray, if any
  while (i < n1) {
    arr[k] = L[i];
    i++;
    k++;
  }

  // Copy the remaining elements of the right subarray, if any
  while (j < n2) {
    arr[k] = R[j];
    j++;
    k++;
  }
}

// A function to implement merge sort on an array
void mergeSort(int arr[], int left, int right) {
  // Base case: if the array has only one element, return
  if (left >= right)
    return;

  // Find the middle point of the array
  int mid = left + (right - left) / 2;

  // Recursively call merge sort on the left and right subarrays
  mergeSort(arr, left, mid);
  mergeSort(arr, mid + 1, right);

  // Merge the two sorted subarrays
  merge(arr, left, mid, right);
}

// A function to print an array
void printArray(int arr[], int size) {
  for (int i = 0; i < size; i++)
    cout << arr[i] << " ";
  cout << endl;
}

// A main function to test the program
int main() {
  // Create an example array
  int arr[] = {12, 11, 13, 5, 6, 7};
  int size = sizeof(arr) / sizeof(arr[0]);

  // Print the original array
  cout << "Given array is: " << endl;
  printArray(arr, size);

  // Call merge sort on the array
  mergeSort(arr, 0, size - 1);

  // Print the sorted array
  cout << "Sorted array is: " << endl;
  printArray(arr, size);

  return 0;
}
```



## Program for Selection Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Selection sort is a simple sorting algorithm that repeatedly finds the minimum element from the unsorted part of the array and puts it at the beginning.
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
      swap A[i] and A[min_index]
   end for
end procedure
```

- A sample program for selection sort in C language is given below:

```c
#include <stdio.h>

// A function to swap two elements in an array
void swap(int *a, int *b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

// A function to perform selection sort on an array
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
    swap(&arr[i], &arr[min_index]);
  }
}

// A function to print an array
void print_array(int arr[], int n) {
  int i;
  for (i = 0; i < n; i++) {
    printf("%d ", arr[i]);
  }
  printf("\n");
}

// A main function to test the selection sort function
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



## Program for Insertion Sort

Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time by comparisons. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort. However, insertion sort provides several advantages:

- It is easy to implement and understand.
- It is stable, meaning that it preserves the relative order of equal elements.
- It is adaptive, meaning that it performs well on partially sorted arrays.
- It requires constant extra space, meaning that it only uses a fixed amount of memory beyond the input array.

The basic idea of insertion sort is to divide the array into two parts: a sorted part and an unsorted part. Initially, the sorted part consists of only the first element, and the unsorted part consists of the rest of the elements. Then, the algorithm repeatedly picks an element from the unsorted part and inserts it into the correct position in the sorted part, until the unsorted part is empty.

The algorithm can be described as follows:

- Set i to 1, the index of the second element in the array.
- Repeat until i reaches the end of the array:
  - Set key to the value of the element at index i.
  - Set j to i - 1, the index of the last element in the sorted part.
  - Repeat until j reaches -1 or the element at index j is less than or equal to key:
    - Move the element at index j to index j + 1, creating a space for key in the sorted part.
    - Decrease j by 1.
  - Insert key into the space at index j + 1.
  - Increase i by 1.

The following pseudocode shows the implementation of insertion sort:

```
procedure insertionSort(A : array of items)
   n = length(A)
   for i = 1 to n - 1
      key = A[i]
      j = i - 1
      while j >= 0 and A[j] > key
         A[j + 1] = A[j]
         j = j - 1
      end while
      A[j + 1] = key
   end for
end procedure
```

The following diagram illustrates the insertion sort algorithm on an example array:

Insertion sort example

The time complexity of insertion sort is O(n^2) in the worst case, when the array is in reverse order, and O(n) in the best case, when the array is already sorted. The average case is also O(n^2), but with a smaller constant factor than the worst case. The space complexity of insertion sort is O(1), since it only uses a constant amount of extra space.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the program for quick sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System.

## Program for Quick Sort

- Quick sort is a divide and conquer algorithm that sorts an array by partitioning it into two subarrays and recursively sorting them.
- The partitioning step chooses a pivot element and rearranges the array such that all elements less than or equal to the pivot are on its left and all elements greater than the pivot are on its right.
- The pivot can be chosen in different ways, such as the first element, the last element, the median, or a random element.
- The algorithm can be implemented in different ways, such as using recursion, iteration, or a hybrid approach.
- The average time complexity of quick sort is O(n log n), where n is the number of elements in the array. The worst case time complexity is O(n^2), which occurs when the array is already sorted or nearly sorted.
- The space complexity of quick sort is O(log n) for the recursive version and O(n) for the iterative version, where n is the number of elements in the array.
- Quick sort is not a stable sorting algorithm, meaning that it does not preserve the relative order of equal elements.
- Quick sort is suitable for sorting large arrays that can fit in memory, but it is not efficient for sorting small arrays or linked lists.

Here is a pseudocode for the recursive version of quick sort:

```
procedure quick_sort(A, low, high)
  // A is the array to be sorted
  // low and high are the indices of the subarray to be sorted
  if low < high then
    // partition the array and get the pivot index
    pivot_index = partition(A, low, high)
    // sort the left subarray
    quick_sort(A, low, pivot_index - 1)
    // sort the right subarray
    quick_sort(A, pivot_index + 1, high)
  end if
end procedure

procedure partition(A, low, high)
  // A is the array to be partitioned
  // low and high are the indices of the subarray to be partitioned
  // choose the last element as the pivot
  pivot = A[high]
  // initialize the index of the smaller element
  i = low - 1
  // loop from low to high - 1
  for j = low to high - 1 do
    // if the current element is less than or equal to the pivot
    if A[j] <= pivot then
      // increment the index of the smaller element
      i = i + 1
      // swap A[i] and A[j]
      swap(A[i], A[j])
    end if
  end for
  // swap A[i + 1] and A[high]
  swap(A[i + 1], A[high])
  // return the index of the pivot
  return i + 1
end procedure
```



## Knapsack Problem using Greedy Solution

- The knapsack problem is a problem of finding the optimal way to fill a knapsack with a given capacity and a set of items, each with a value and a weight.
- The fractional knapsack problem is a variation of the knapsack problem, where the items can be divided into smaller pieces and the knapsack can be filled with fractions of items.
- The greedy solution for the fractional knapsack problem is an efficient and optimal method that works as follows   :
  - Sort the items by their value-to-weight ratio in descending order.
  - Start with the item with the highest ratio and take as much of it as possible, until the knapsack is full or the item is exhausted.
  - If the knapsack is not full and there are more items, move to the next item with the next highest ratio and repeat the previous step.
  - Continue this process until the knapsack is full or there are no more items.
- The greedy solution for the fractional knapsack problem has a time complexity of O(n log n), where n is the number of items, because the sorting step dominates the algorithm.
- The greedy solution for the fractional knapsack problem is optimal because at each step, it chooses the item that gives the maximum value per unit weight, which maximizes the total value of the knapsack.
- The greedy solution for the fractional knapsack problem does not work for the 0-1 knapsack problem, where the items cannot be divided and the knapsack can only be filled with whole items. In this case, the greedy solution may not find the optimal solution, because it may miss some combinations of items that have a higher total value than the greedy choice.
- An example of the fractional knapsack problem using the greedy solution is shown below:

  - Suppose we have a knapsack with a capacity of 15 kg and four items with the following values and weights:

    | Item | Value | Weight | Value/Weight |
    | ---- | ----- | ------ | ------------ |
    | A    | 10    | 2      | 5            |
    | B    | 5     | 3      | 1.67         |
    | C    | 15    | 5      | 3            |
    | D    | 7     | 7      | 1            |

  - The first step is to sort the items by their value-to-weight ratio in descending order:

    | Item | Value | Weight | Value/Weight |
    | ---- | ----- | ------ | ------------ |
    | A    | 10    | 2      | 5            |
    | C    | 15    | 5      | 3            |
    | B    | 5     | 3      | 1.67         |
    | D    | 7     | 7      | 1            |

  - The second step is to start with the item with the highest ratio, which is A, and take as much of it as possible. Since the weight of A is 2 kg and the capacity of the knapsack is 15 kg, we can take the whole item A and put it in the knapsack. The value of the knapsack is now 10 and the remaining capacity is 13 kg.

  - The third step is to move to the next item with the next highest ratio, which is C, and take as much of it as possible. Since the weight of C is 5 kg and the remaining capacity of the knapsack is 13 kg, we can also take the whole item C and put it in the knapsack. The value of the knapsack is now 25 and the remaining capacity is 8 kg.

  - The fourth step is to move to the next item with the next highest ratio, which is B, and take as much of it as possible. Since the weight of B is 3 kg and the remaining capacity of the knapsack is 8 kg, we can also take the whole item B and put it in the knapsack. The value of the knapsack is now 30 and the remaining capacity is 5 kg.

  - The fifth step is to move to the last item, which is D, and take as much of it as possible. Since the weight of D is 7 kg and



Hello, I am Sydney, your AI assistant. I can help you with your topic.

## Perform Travelling Salesman Problem for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- The Travelling Salesman Problem (TSP) is a classic optimization problem that asks for the shortest possible route that visits each city exactly once and returns to the starting point.
- The TSP is NP-hard, which means that there is no known efficient algorithm that can solve it in polynomial time for any number of cities.
- The TSP has many applications in real time systems, such as scheduling, routing, logistics, and planning.
- To perform the TSP for the notes of the Design and Analysis of Algorithm Lab, we can use the following steps:

  1. Represent the notes as nodes in a graph, and the distances between them as edges with weights. For example, if we have four notes A, B, C, and D, and the distances between them are 10, 20, 30, and 40 units, we can draw a graph like this:

  ```
  A---10---B
  |       / |
  |      /  |
  40    30  20
  |    /    |
  |   /     |
  D---10---C
  ```

  2. Choose a starting node, and mark it as visited. For example, let's choose A as the starting node.
  3. Find the nearest unvisited node to the current node, and move to it. Mark it as visited. For example, the nearest unvisited node to A is B, so we move to B and mark it as visited.
  4. Repeat step 3 until all nodes are visited. For example, after moving to B, the nearest unvisited node is C, so we move to C and mark it as visited. Then, the nearest unvisited node is D, so we move to D and mark it as visited.
  5. Return to the starting node, and complete the cycle. For example, after moving to D, we return to A and complete the cycle.
  6. Calculate the total distance of the cycle, and compare it with the best solution found so far. If it is better, update the best solution. For example, the total distance of the cycle A-B-C-D-A is 10 + 20 + 10 + 40 = 80 units, which is the best solution so far.
  7. Repeat steps 2 to 6 for each possible starting node, and find the best solution among them. For example, if we start from B, the cycle B-A-D-C-B has a total distance of 10 + 40 + 10 + 30 = 90 units, which is worse than the previous solution. If we start from C, the cycle C-B-A-D-C has a total distance of 20 + 10 + 40 + 10 = 80 units, which is equal to the previous solution. If we start from D, the cycle D-C-B-A-D has a total distance of 10 + 30 + 20 + 40 = 100 units, which is worse than the previous solution. Therefore, the best solution is A-B-C-D-A with a total distance of 80 units.

- This method is called the nearest neighbor heuristic, which is a simple and fast way to find a good solution for the TSP, but not necessarily the optimal one. There are other more sophisticated methods, such as branch and bound, dynamic programming, genetic algorithms, and simulated annealing, that can find better or optimal solutions, but they are more complex and time-consuming.



# Find Minimum Spanning Tree using Kruskal’s Algorithm

- A **minimum spanning tree (MST)** is a subset of the edges of a connected, edge-weighted graph that connects all the vertices together, without any cycles and with the minimum possible total edge weight.
- **Kruskal's algorithm** is a greedy algorithm that finds a MST for a weighted graph.
- The algorithm works as follows :
  - Sort all the edges in non-decreasing order of their weight.
  - Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
  - Repeat step 2 until there are (V-1) edges in the spanning tree, where V is the number of vertices in the graph.
- The algorithm can be implemented using a **priority queue** to store the edges by weight, a **union-find** data structure to check for cycles, and a **queue** to collect the MST edges.
- The time complexity of the algorithm is O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices, as the most expensive part is sorting the edges.
- The space complexity of the algorithm is O(E + V), as we need to store the edges, the union-find data structure, and the MST edges.
- An example of applying the algorithm to a graph is shown below:

Kruskal's algorithm example

- The edges are sorted by weight as follows: (7, 6), (8, 2), (6, 5), (0, 1), (2, 5), (8, 6), (2, 3), (7, 8), (0, 7), (1, 2), (3, 4), (4, 5), (1, 7), (3, 5).
- The algorithm picks the smallest edge (7, 6) and adds it to the MST.
- The algorithm picks the next smallest edge (8, 2) and adds it to the MST.
- The algorithm picks the next smallest edge (6, 5) and adds it to the MST.
- The algorithm picks the next smallest edge (0, 1) and adds it to the MST.
- The algorithm picks the next smallest edge (2, 5) and discards it as it forms a cycle with the MST.
- The algorithm picks the next smallest edge (8, 6) and discards it as it forms a cycle with the MST.
- The algorithm picks the next smallest edge (2, 3) and adds it to the MST.
- The algorithm picks the next smallest edge (7, 8) and discards it as it forms a cycle with the MST.
- The algorithm picks the next smallest edge (0, 7) and discards it as it forms a cycle with the MST.
- The algorithm picks the next smallest edge (1, 2) and adds it to the MST.
- The algorithm picks the next smallest edge (3, 4) and adds it to the MST.
- The algorithm picks the next smallest edge (4, 5) and discards it as it forms a cycle with the MST.
- The algorithm picks the next smallest edge (1, 7) and discards it as it forms a cycle with the MST.
- The algorithm picks the next smallest edge (3, 5) and discards it as it forms a cycle with the MST.
- The algorithm stops as there are (9-1) = 8 edges in the MST.
- The MST is shown below with the total weight of 37:

Kruskal's algorithm MST



# Implement N Queen Problem using Backtracking for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- The N Queen Problem is to find an arrangement of N queens on a chessboard of dimension N x N, such that no two queens attack each other. A queen can attack horizontally, vertically, or diagonally.
- Backtracking is a technique to solve problems that involve searching for a solution among a large number of possibilities. It involves trying a possible solution, and if it does not work, undoing it and trying another one, until a solution is found or all possibilities are exhausted.
- The algorithm for solving the N Queen Problem using backtracking is as follows:

1. Start in the leftmost column
2. If all queens are placed, return true
3. Try all rows in the current column. Do following for every tried row.
   - If the queen can be placed safely in this row, then mark this [row, column] as part of the solution and recursively check if placing queen here leads to a solution.
   - If placing the queen in [row, column] leads to a solution, then return true.
   - If placing the queen does not lead to a solution, then unmark this [row, column] (backtrack) and try another row.
4. If all rows have been tried and nothing worked, return false to trigger backtracking.

- The pseudocode for the algorithm is as follows:

```
// A utility function to check if a queen can be placed on board[row][col]
// Note that this function is called when "col" queens are already placed
// in columns from 0 to col -1. So we need to check only left side for
// attacking queens
function isSafe(board, row, col)
    // Check this row on left side
    for i = 0 to col
        if board[row][i] == 1
            return false
    // Check upper diagonal on left side
    for i = row, j = col, while i >= 0 and j >= 0
        if board[i][j] == 1
            return false
        i = i - 1
        j = j - 1
    // Check lower diagonal on left side
    for i = row, j = col, while i < N and j >= 0
        if board[i][j] == 1
            return false
        i = i + 1
        j = j - 1
    return true

// A recursive utility function to solve N Queen problem
function solveNQUtil(board, col)
    // base case: If all queens are placed then return true
    if col == N
        return true
    // Consider this column and try placing this queen in all rows one by one
    for i = 0 to N-1
        // Check if the queen can be placed on board[i][col]
        if isSafe(board, i, col)
            // Place this queen in board[i][col]
            board[i][col] = 1
            // recur to place rest of the queens
            if solveNQUtil(board, col + 1) == true
                return true
            // If placing queen in board[i][col] doesn't lead to a solution, then
            // remove queen from board[i][col]
            board[i][col] = 0 // BACKTRACK
    // If the queen can not be placed in any row in this column col, then return false
    return false

// This function solves the N Queen problem using Backtracking. It mainly uses
// solveNQUtil() to solve the problem. It returns false if queens cannot be placed,
// otherwise, return true and prints placement of queens in the form of 1s.
// Please note that there may be more than one solutions, this function prints one
// of the feasible solutions.
function solveNQ()
    board = { {0, 0, 0, 0},
              {0, 0, 0, 0},
              {0, 0, 0, 0},
              {0, 0, 0, 0} }
    if solveNQUtil(board, 0) == false
       print "Solution does not exist"
       return false
    printSolution(board)
    return true
```
- The time complexity of the algorithm is O(N!), where N is the number of queens. This is because for



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is the content in markdown format:

## Sort a given set of n integer elements using Quick Sort method and compute its time complexity. Run the program for varied values of n> 5000 and record the time taken to sort. Plot a graph of the time taken versus non graph sheet. The elements can be read from a file or can be generated using the random number generator. Demonstrate using Java how the divide and- conquer method works along with its time complexity analysis: worst case, average case and best case.

```markdown
- Quick Sort is a sorting algorithm that uses the divide and conquer method to partition the array into two subarrays based on a pivot element, such that the elements in the left subarray are smaller than the pivot and the elements in the right subarray are larger than the pivot.
- The algorithm then recursively sorts the left and right subarrays until the array is sorted.
- The time complexity of Quick Sort depends on the choice of the pivot element and the distribution of the elements in the array.
- The worst case occurs when the pivot is the smallest or the largest element in the array, resulting in an unbalanced partition. In this case, the time complexity is O(n^2), where n is the number of elements in the array.
- The average case occurs when the pivot is close to the median of the array, resulting in a balanced partition. In this case, the time complexity is O(n log n), where n is the number of elements in the array.
- The best case occurs when the pivot is the median of the array, resulting in a perfectly balanced partition. In this case, the time complexity is also O(n log n), where n is the number of elements in the array.
- To run the program for varied values of n> 5000 and record the time taken to sort, we can use a loop to generate random arrays of different sizes and measure the execution time using the System.nanoTime() method in Java.
- To plot a graph of the time taken versus non graph sheet, we can use a spreadsheet software such as Excel or Google Sheets and create a scatter plot with the x-axis as the array size and the y-axis as the time taken.
- To demonstrate using Java how the divide and conquer method works along with its time complexity analysis, we can use the following code snippet:

```java
// A utility method to swap two elements in an array
public static void swap(int[] arr, int i, int j) {
  int temp = arr[i];
  arr[i] = arr[j];
  arr[j] = temp;
}

// A method to partition the array around a pivot element
public static int partition(int[] arr, int low, int high) {
  // Choose the last element as the pivot
  int pivot = arr[high];
  // Initialize the index of the smaller element
  int i = low - 1;
  // Loop through the array from low to high - 1
  for (int j = low; j < high; j++) {
    // If the current element is smaller than or equal to the pivot
    if (arr[j] <= pivot) {
      // Increment the index of the smaller element
      i++;
      // Swap the current element with the smaller element
      swap(arr, i, j);
    }
  }
  // Swap the pivot with the element at the index of the smaller element + 1
  swap(arr, i + 1, high);
  // Return the index of the pivot
  return i + 1;
}

// A method to sort the array using Quick Sort
public static void quickSort(int[] arr, int low, int high) {
  // Base case: if the array has one or zero elements, it is already sorted
  if (low >= high) {
    return;
  }
  // Partition the array around a pivot element and get its index
  int pivotIndex = partition(arr, low, high);
  // Recursively sort the left subarray
  quickSort(arr, low, pivotIndex - 1);
  // Recursively sort the right subarray
  quickSort(arr, pivotIndex + 1, high);
}

// A method to generate a random array of a given size
public static int[] generateRandomArray(int size) {
  // Create a new array of the given size
  int[] arr = new int[size];
  // Loop through the array
  for (int i = 0; i < size; i++) {
    // Generate a random integer between 0 and 100 and assign it to the array element
    arr[i] = (int) (Math.random()



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is the content in markdown format:

## Sort a given set of n integer elements using Merge Sort method and compute its time complexity. Run the program for varied values of n> 5000, and record the time taken to sort. Plot a graph of the time taken versus non graph sheet. The elements can be read from a file or can be generated using the random number generator. Demonstrate how the divide and- conquer method works along with its time complexity analysis: worst case, average case and best case.

### Merge Sort
- Merge sort is a sorting algorithm that uses the divide and conquer technique to sort a given set of n integer elements.
- The algorithm works as follows:
  - Divide the input array into two halves, left and right, recursively until each subarray has only one element.
  - Merge the two sorted subarrays into one sorted array by comparing the elements from each subarray and picking the smaller one.
  - Return the sorted array as the final output.
- The pseudocode for merge sort is:

```
merge_sort(array, low, high):
  if low < high:
    mid = (low + high) / 2
    merge_sort(array, low, mid)
    merge_sort(array, mid + 1, high)
    merge(array, low, mid, high)

merge(array, low, mid, high):
  n1 = mid - low + 1
  n2 = high - mid
  create two temporary arrays left and right of size n1 and n2
  copy the elements from array[low..mid] to left[0..n1-1]
  copy the elements from array[mid+1..high] to right[0..n2-1]
  i = 0, j = 0, k = low
  while i < n1 and j < n2:
    if left[i] <= right[j]:
      array[k] = left[i]
      i = i + 1
    else:
      array[k] = right[j]
      j = j + 1
    k = k + 1
  while i < n1:
    array[k] = left[i]
    i = i + 1
    k = k + 1
  while j < n2:
    array[k] = right[j]
    j = j + 1
    k = k + 1
```

### Time Complexity
- The time complexity of merge sort is O(n log n) for the worst case, average case and best case scenarios.
- This is because the algorithm divides the input array into two halves at each level of recursion, resulting in log n levels of recursion.
- At each level, the algorithm merges two subarrays of size n/2, resulting in n comparisons and n assignments, resulting in O(n) time complexity at each level.
- Therefore, the total time complexity is O(n log n) for all cases.

### Experiment
- To run the program for varied values of n > 5000, and record the time taken to sort, we can use the following steps:
  - Import the time module in Python to measure the execution time of the program.
  - Import the random module in Python to generate random numbers for the input array.
  - Define a function to generate an array of n random numbers in the range [1, 10000].
  - Define a function to write the array to a file named input.txt.
  - Define a function to read the array from the file input.txt.
  - Define a function to plot a graph of the time taken versus n using matplotlib.pyplot module in Python.
  - Define a list of values for n, such as [5000, 10000, 15000, 20000, 25000, 30000].
  - For each value of n, do the following:
    - Generate an array of n random numbers and write it to the file input.txt.
    - Read the array from the file input.txt and store it in a variable named array.
    - Start a timer using time.time() and store the value in a variable named start.
    - Call the merge_sort function on the array and store the sorted array in a variable named sorted_array.
    - Stop the timer using time.time() and store the value in a variable named end.
    - Calculate the time taken to sort the array by subtracting start from end and store the value in a variable named time_taken.
    - Print the value of n and time_taken to the console.
    - Append the value of n and time_taken to two lists named x and y respectively.
  - Call the



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on how to implement the 0/1 Knapsack problem using dynamic programming and greedy methods.

## Dynamic Programming Method

- The 0/1 Knapsack problem is an optimization problem where we have to select a subset of items that maximizes the total value without exceeding the capacity of the knapsack.
- Dynamic programming is an algorithmic technique that solves a problem by breaking it down into smaller subproblems and reusing the solutions of the subproblems to find the optimal solution of the original problem.
- The idea of dynamic programming for the 0/1 Knapsack problem is to use a two-dimensional table to store the optimal values of the subproblems, where the rows represent the items and the columns represent the weights.
- The table is filled in a bottom-up manner, starting from the base case where no items are selected or the weight is zero, and moving up to the final case where all items are considered and the weight is equal to the capacity of the knapsack.
- The table entry at row i and column j represents the maximum value that can be obtained by selecting a subset of items from 1 to i with a total weight of j or less.
- The table entry can be computed by comparing two cases: either the item i is included in the optimal subset or it is not.
- If the item i is included, then the value is equal to the value of the item plus the value of the optimal subset with the remaining weight (j - weight of item i).
- If the item i is not included, then the value is equal to the value of the optimal subset without the item i (same weight j).
- The table entry is the maximum of these two cases.
- The optimal value of the problem is the table entry at the last row and the last column.
- The optimal subset can be traced back by starting from the last entry and moving backwards, checking if the item was included or not in each step.

### Pseudocode

```
# Input: n = number of items, W = capacity of knapsack, v = array of values, w = array of weights
# Output: V = optimal value, S = optimal subset

# Initialize a table T of size (n+1) x (W+1) with zeros
T = [[0 for j in range(W+1)] for i in range(n+1)]

# Fill the table in a bottom-up manner
for i in range(1, n+1): # loop over the items
  for j in range(1, W+1): # loop over the weights
    if w[i-1] <= j: # if the item can fit in the knapsack
      # compare the two cases: include or exclude the item
      T[i][j] = max(v[i-1] + T[i-1][j-w[i-1]], T[i-1][j])
    else: # if the item cannot fit in the knapsack
      # exclude the item
      T[i][j] = T[i-1][j]

# The optimal value is the last entry of the table
V = T[n][W]

# Initialize an empty list to store the optimal subset
S = []

# Trace back the table to find the optimal subset
i = n # start from the last item
j = W # start from the last weight
while i > 0 and j > 0: # loop until the first row or column is reached
  if T[i][j] == T[i-1][j]: # if the item was not included
    i = i - 1 # move to the previous item
  else: # if the item was included
    S.append(i) # add the item to the subset
    i = i - 1 # move to the previous item
    j = j - w[i] # reduce the weight by the weight of the item

# Return the optimal value and the optimal subset
return V, S
```

## Greedy Method

- The 0/1 Knapsack problem is an optimization problem where we have to select a subset of items that maximizes the total value without exceeding the capacity of the knapsack.
- Greedy method is an algorithmic technique that makes a locally optimal choice at each step, hoping to find the global optimal solution.
- The idea of greedy method for the 0/1 Knapsack problem is to sort the items in decreasing order



## From a given vertex in a weighted connected graph, find shortest paths to other vertices using Dijkstra's algorithm.

- Dijkstra's algorithm is a greedy algorithm that finds the shortest path from a given vertex to all other vertices in a weighted graph.
- The algorithm maintains a set of visited vertices and a priority queue of unvisited vertices with their distances from the source vertex.
- The algorithm works as follows:

  - Initialize the distance of the source vertex to zero and the distance of all other vertices to infinity.
  - Mark the source vertex as visited and add it to the priority queue with its distance as the priority.
  - While the priority queue is not empty, do the following:
    - Extract the vertex with the minimum distance from the priority queue. This is the current vertex.
    - For each neighbor of the current vertex that is not visited, do the following:
      - Calculate the distance to the neighbor through the current vertex. This is the new distance.
      - If the new distance is smaller than the old distance, update the distance of the neighbor and add it to the priority queue with the new distance as the priority.
    - Mark the current vertex as visited.
  - The algorithm terminates when the priority queue is empty or when the destination vertex is visited.
- The algorithm returns the distance of each vertex from the source vertex and the previous vertex in the shortest path.
- The algorithm can be implemented using an array, a binary heap, or a Fibonacci heap as the priority queue data structure.
- The time complexity of the algorithm depends on the number of vertices (n), the number of edges (m), and the implementation of the priority queue. The worst-case time complexity is O(n^2) using an array, O((n+m)log n) using a binary heap, and O(n log n + m) using a Fibonacci heap.
- The space complexity of the algorithm is O(n) for storing the distances, the visited status, and the previous vertices of each vertex.



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here are some notes that you can use for your study:

## Find Minimum Cost Spanning Tree of a given connected undirected graph using Kruskal's algorithm. Use Union-Find algorithms in your program.

- A **spanning tree** of a graph is a subgraph that contains all the vertices and is a tree (i.e., has no cycles).
- A **minimum cost spanning tree** (MCST) of a graph is a spanning tree that has the minimum possible sum of edge weights among all the spanning trees of the graph.
- **Kruskal's algorithm** is a greedy algorithm that finds a MCST of a given connected, weighted, undirected graph.
- The algorithm works as follows:
  - Sort all the edges of the graph in non-decreasing order of their weights.
  - Initialize an empty set T to store the edges of the MCST.
  - For each edge (u, v) in the sorted edge list, do the following:
    - If adding (u, v) to T does not create a cycle in T, then add (u, v) to T.
    - Otherwise, ignore (u, v).
  - Return T as the MCST of the graph.
- To check if adding an edge to T creates a cycle or not, we can use a **union-find** data structure that maintains a collection of disjoint sets of vertices and supports two operations:
  - **find(x)**: returns the representative element of the set that contains x.
  - **union(x, y)**: merges the sets that contain x and y into a single set.
- The union-find data structure can be implemented using an array of integers, where each element stores the parent of the corresponding vertex in the tree representation of the set. Initially, each vertex is in its own set, so the parent of each vertex is itself.
- The find operation can be implemented using a recursive function that follows the parent pointers until it reaches the root of the tree, and then updates the parent pointers along the path to point to the root. This is called **path compression** and it helps to reduce the height of the trees and improve the efficiency of the find operation.
- The union operation can be implemented by finding the roots of the two sets that contain x and y, and then making one of them the parent of the other. To balance the heights of the trees, we can use a heuristic called **union by rank**, which makes the root of the smaller tree (in terms of rank, which is an upper bound on the height of the tree) the child of the root of the larger tree.
- The pseudocode of the union-find data structure is given below:

```
# initialize the parent and rank arrays
parent = [i for i in range(n)] # n is the number of vertices
rank = [0 for i in range(n)]

# find the root of the set that contains x
def find(x):
  if parent[x] != x: # x is not the root
    parent[x] = find(parent[x]) # recursively find the root and update the parent
  return parent[x] # return the root

# merge the sets that contain x and y
def union(x, y):
  x_root = find(x) # find the root of x
  y_root = find(y) # find the root of y
  if x_root == y_root: # x and y are already in the same set
    return
  if rank[x_root] < rank[y_root]: # x_root has smaller rank
    parent[x_root] = y_root # make y_root the parent of x_root
  elif rank[x_root] > rank[y_root]: # y_root has smaller rank
    parent[y_root] = x_root # make x_root the parent of y_root
  else: # x_root and y_root have the same rank
    parent[y_root] = x_root # make x_root the parent of y_root
    rank[x_root] += 1 # increase the rank of x_root by 1
```

- Using the union-find data structure, we can modify the Kruskal's algorithm as follows:

```
# initialize the edge set T
T = set()

# sort the edges by weight
edges = sort(edges)

# for each edge in the sorted list
for (u, v, w) in edges:
  # if u and v are in different sets
  if find(u) != find(v):
    # add (u, v

```




## Find Minimum Cost Spanning Tree of a given undirected graph using Prim’s algorithm.

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
- The algorithm is correct because at each step, it adds the edge that minimizes the cost of the MCST so far, and does not create any cycles. Therefore, the final MCST is optimal. This can be proved using a cut-and-paste argument or by contradiction.
- An example of applying Prim’s algorithm to a given undirected graph is shown below:

Prim's algorithm example

- The steps of the algorithm are:

  - Start with vertex A as the root of the MCST. The set of included vertices is {A}, and the set of edges is {(A, B), (A, C), (A, D)}.
  - Find the edge with the minimum weight among the edges that connect the included vertices to the rest of the graph. This is (A, B) with weight 2. Add this edge and vertex B to the MCST. The set of included vertices is {A, B}, and the set of edges is {(A, C), (A, D), (B, C), (B, E)}.
  - Find the edge with the minimum weight among the edges that connect the included vertices to the rest of the graph. This is (B, C) with weight 3. Add this edge and vertex C to the MCST. The set of included vertices is {A, B, C}, and the set of edges is {(A, D), (B, E), (C, D), (C, E), (C, F)}.
  - Find the edge with the minimum weight among the edges that connect the included vertices to the rest of the graph. This is (C, F) with weight 4. Add this edge and vertex F to the MCST. The set of included vertices is {A, B, C, F}, and the set of edges is {(A, D), (B, E), (C, D), (C, E), (F, E), (F, G)}.
  - Find the edge with the minimum weight among the edges that connect the included vertices to the rest of the graph. This is (F, G) with weight 5. Add this edge and vertex G to the MCST. The set of included vertices is {A, B, C, F, G}, and the set of edges is {(A, D), (B, E), (C, D), (C, E), (F, E)}.
  - Find the edge with the minimum weight among the edges that connect the included vertices to the rest of the graph. This is (C, E) with weight 6. Add this edge and vertex E to the MCST. The set of included vertices is {A, B, C, F, G, E}, and the set of edges is {(A, D), (B, E), (C, D), (F, E)}.
  - Find the edge with the minimum weight among the edges that connect the included vertices to the rest of the graph. This is (A, D) with weight 7. Add this edge and vertex D to the MCST. The set of included vertices is {A, B, C, F, G, E, D}, and the set of edges is empty.
  - All the vertices are included in



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on the topic you asked for:

## Write programs to (a) Implement All-Pairs Shortest Paths problem using Floyd's algorithm. (b) Implement Travelling Sales Person problem using Dynamic programming. for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

(a) Implement All-Pairs Shortest Paths problem using Floyd's algorithm.

- The All-Pairs Shortest Paths problem is to find the shortest distance between every pair of vertices in a given weighted graph.
- Floyd's algorithm, also known as the Floyd-Warshall algorithm, is an algorithm that solves this problem in O(n^3) time, where n is the number of vertices in the graph.
- The algorithm works by iteratively updating a matrix D that stores the shortest distances between all pairs of vertices. Initially, D[i][j] is the weight of the edge (i, j) if it exists, or infinity otherwise. Then, for each intermediate vertex k, the algorithm updates D[i][j] to be the minimum of D[i][j] and D[i][k] + D[k][j], for all i and j. This means that D[i][j] is the shortest distance from i to j using only vertices 1 to k as intermediate points. After n iterations, D[i][j] is the shortest distance from i to j using any intermediate vertex.
- The algorithm can be implemented in pseudocode as follows:

```
// Input: A weighted graph G with n vertices
// Output: A matrix D of shortest distances between all pairs of vertices
Floyd(G):
  // Initialize D to be the adjacency matrix of G, with infinity for non-existent edges
  D = G.adjacency_matrix()
  // Loop over all intermediate vertices
  for k = 1 to n:
    // Loop over all pairs of vertices
    for i = 1 to n:
      for j = 1 to n:
        // Update D[i][j] to be the minimum of the current value and the value using k as an intermediate vertex
        D[i][j] = min(D[i][j], D[i][k] + D[k][j])
  // Return D
  return D
```

(b) Implement Travelling Sales Person problem using Dynamic programming.

- The Travelling Sales Person problem is to find the shortest tour that visits every vertex in a given weighted graph exactly once and returns to the starting vertex.
- Dynamic programming is a technique that solves complex problems by breaking them down into simpler subproblems and reusing the solutions of the subproblems to avoid recomputation.
- One way to apply dynamic programming to the Travelling Sales Person problem is to use a state-space representation that encodes the current vertex and the set of visited vertices. For example, (2, {1, 3, 4}) means that the current vertex is 2 and the visited vertices are 1, 3, and 4. The goal is to find the minimum cost of reaching the state (1, {1, 2, ..., n}), where 1 is the starting vertex and n is the number of vertices in the graph.
- The subproblem is to find the minimum cost of reaching any state (i, S), where i is any vertex and S is any subset of vertices that contains 1 and i. The base case is when S = {1, i}, in which case the cost is the weight of the edge (1, i). The recursive case is when S has more than two elements, in which case the cost is the minimum of the cost of reaching (j, S - {i}) plus the weight of the edge (j, i), for all j in S that are not i. This means that the cost of reaching (i, S) is the minimum of the cost of reaching any previous state (j, S - {i}) and then moving from j to i.
- The algorithm can be implemented in pseudocode as follows:

```
// Input: A weighted graph G with n vertices
// Output: The minimum cost of a tour that visits every vertex exactly once and returns to the starting vertex
TSP(G):
  // Initialize a memoization table T that stores the minimum cost of reaching any state (i, S)
  T = empty_table()
  // Loop over all possible subsets of vertices that contain 1
  for S = {1} to {1, 2, ..., n}:
    // Loop over all vertices in S

```




Hello, I am Sydney, your AI assistant. I can help you with your topic.

Here is the content in markdown format:

## Design and implement to find a subset of a given set S = {Sl, S2,.....,Sn} of n positive integers whose SUM is equal to a given positive integer d. For example, if S ={1, 2, 5, 6, 8} and d= 9, there are two solutions {1,2,6}and {1,8}. Display a suitable message, if the given problem instance doesn't have a solution.

- This problem is also known as the **subset sum problem**, which is a special case of the **knapsack problem**.
- The subset sum problem is **NP-complete**, which means that there is no efficient algorithm that can solve it in polynomial time for any input size.
- However, there are some **heuristic** and **approximation** algorithms that can find a solution or a near-optimal solution in reasonable time for some instances of the problem.
- One possible algorithm to find a subset of S whose sum is equal to d is the following:

  - Sort the elements of S in descending order.
  - Initialize an empty list L to store the subset.
  - Initialize a variable sum to 0.
  - For each element x in S, do the following:
    - If sum + x <= d, then add x to L and update sum = sum + x.
    - If sum == d, then stop the loop and return L as the solution.
    - If sum > d, then skip x and continue the loop.
  - If the loop ends without finding a solution, then return a message that there is no solution.

- The time complexity of this algorithm is O(n log n), where n is the size of S, because the sorting step takes O(n log n) time and the loop takes O(n) time.
- The space complexity of this algorithm is O(n), because it uses an auxiliary list L to store the subset.
- This algorithm is a **greedy** algorithm, which means that it makes the locally optimal choice at each step, without considering the global optimal solution.
- This algorithm may not find the optimal solution or any solution at all, depending on the input. For example, if S = {10, 7, 5, 3, 2} and d = 15, this algorithm will return {10, 5} as the solution, which is not optimal, because {7, 5, 3} is also a solution with fewer elements. If S = {10, 9, 8, 7} and d = 5, this algorithm will return no solution, even though {5} is a solution.
- A better algorithm to find a subset of S whose sum is equal to d is the following:

  - Initialize a boolean matrix M of size (n+1) x (d+1), where n is the size of S and d is the given sum.
  - Set M[0][0] to True and all other entries to False.
  - For i from 1 to n, do the following:
    - For j from 0 to d, do the following:
      - If M[i-1][j] is True, then set M[i][j] to True.
      - If j >= S[i-1] and M[i-1][j-S[i-1]] is True, then set M[i][j] to True.
  - If M[n][d] is True, then there is a solution. Otherwise, there is no solution.
  - To find the solution, backtrack from M[n][d] to M[0][0], by doing the following:
    - Initialize an empty list L to store the subset.
    - Initialize a variable i to n and a variable j to d.
    - While i > 0 and j > 0, do the following:
      - If M[i][j] is different from M[i-1][j], then add S[i-1] to L and update j = j - S[i-1].
      - Update i = i - 1.
    - Return L as the solution.

- The time complexity of this algorithm is O(n d), where n is the size of S and d is the given sum, because the matrix M has O(n d) entries and each entry takes O(1) time to fill.
- The space complexity of this algorithm is O(n d), because it uses a matrix M of size O(n d) to store the boolean values.
- This algorithm is a **dynamic programming** algorithm, which means that it



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to discuss. You asked me to write the content in markdown format on the topic of Design and implement to find all Hamiltonian Cycles in a connected undirected Graph G of n vertices using backtracking principle. Here is the content I have written for you:

```markdown
# Design and implement to find all Hamiltonian Cycles in a connected undirected Graph G of n vertices using backtracking principle

## Introduction

- A Hamiltonian cycle is a cycle in a graph that visits every vertex exactly once and returns to the starting vertex.
- A graph is said to be Hamiltonian if it has a Hamiltonian cycle.
- Finding a Hamiltonian cycle in a graph is an NP-complete problem, meaning that there is no known efficient algorithm to solve it in polynomial time.
- However, using backtracking, we can explore all possible paths in a graph and check if any of them is a Hamiltonian cycle.
- Backtracking is a technique that involves trying different choices and undoing them if they lead to a dead end or a suboptimal solution.

## Algorithm

- The algorithm to find all Hamiltonian cycles in a connected undirected graph G of n vertices using backtracking is as follows:

  - Create an array path of size n to store the vertices of the current path.
  - Initialize path[0] to any vertex in G and mark it as visited.
  - Call the recursive function hamCycle(G, path, 1) to find all Hamiltonian cycles starting from path[0].
  - The function hamCycle(G, path, pos) takes the graph G, the path array, and the current position pos as parameters and returns true if a Hamiltonian cycle is found, and false otherwise.
  - The function hamCycle(G, path, pos) performs the following steps:

    - If pos == n, check if the last vertex in path is adjacent to the first vertex in path. If yes, print the path as a Hamiltonian cycle and return true. If no, return false.
    - For each vertex v in G that is not visited and is adjacent to path[pos-1], do the following:
      - Mark v as visited and add it to path[pos].
      - Call hamCycle(G, path, pos+1) recursively. If it returns true, return true.
      - Mark v as unvisited and remove it from path[pos]. This is the backtracking step.
    - If no vertex can be added to path, return false.

## Example

- Consider the following graph G with 5 vertices:

Graph G

- The array path is initialized as [0, -1, -1, -1, -1] and the first vertex 0 is marked as visited.
- The function hamCycle(G, path, 1) is called and it tries to add vertices 1, 2, 3, and 4 to path[1] one by one.
- The vertex 1 is added to path[1] and the function hamCycle(G, path, 2) is called. The path is now [0, 1, -1, -1, -1].
- The function hamCycle(G, path, 2) tries to add vertices 2, 3, and 4 to path[2] one by one.
- The vertex 2 is added to path[2] and the function hamCycle(G, path, 3) is called. The path is now [0, 1, 2, -1, -1].
- The function hamCycle(G, path, 3) tries to add vertices 3 and 4 to path[3] one by one.
- The vertex 3 is added to path[3] and the function hamCycle(G, path, 4) is called. The path is now [0, 1, 2, 3, -1].
- The function hamCycle(G, path, 4) tries to add vertex 4 to path[4].
- The vertex 4 is added to path[4] and the function hamCycle(G, path, 5) is called. The path is now [0, 1, 2, 3, 4].
- The function hamCycle(G, path, 5) checks if the last vertex 4 is adjacent to the first vertex 0. Since it is, it prints the path as a Hamiltonian cycle and returns true. The path is [0, 1, 2, 3, 4, 0].
- The function hamCycle(G, path,

```


