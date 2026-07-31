

## Program for Recursive Binary & Linear Search for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Binary search is a searching algorithm that finds the position of a target value in a sorted array. It is also called a half-interval search or logarithmic search  .
- Binary search works by comparing the target value with the middle element of the array. If they are equal, the search is successful and the position is returned. If they are not equal, the search continues in either the left or the right half of the array, depending on whether the target value is smaller or larger than the middle element  .
- Binary search can be implemented in two ways: iterative and recursive. The iterative method uses a loop to repeat the comparison and narrowing of the search range until the target value is found or the array is exhausted. The recursive method uses a function that calls itself with a smaller subarray as an argument until the base case is reached   .
- The pseudocode for the recursive binary search algorithm is as follows  :

```
binarySearch(array, target, low, high)
  // base case: the search range is empty
  if low > high
    return -1 // not found
  // find the middle index of the search range
  mid = (low + high) / 2
  // compare the target value with the middle element
  if target == array[mid]
    return mid // found
  else if target < array[mid]
    // search in the left half of the array
    return binarySearch(array, target, low, mid - 1)
  else
    // search in the right half of the array
    return binarySearch(array, target, mid + 1, high)
```

- The time complexity of binary search is O(log n), where n is the number of elements in the array. The space complexity of binary search is O(1) for the iterative method and O(log n) for the recursive method, due to the stack space used by the recursive calls     .
- Linear search is a searching algorithm that finds the position of a target value in an array by checking each element in order. It is also called a sequential search or a brute-force search  .
- Linear search works by comparing the target value with each element of the array until it is found or the array is exhausted. If the target value is found, the search is successful and the position is returned. If the target value is not found, the search is unsuccessful and -1 is returned  .
- Linear search can also be implemented in two ways: iterative and recursive. The iterative method uses a loop to repeat the comparison until the target value is found or the array is exhausted. The recursive method uses a function that calls itself with the next element as an argument until the base case is reached  .
- The pseudocode for the recursive linear search algorithm is as follows :

```
linearSearch(array, target, index)
  // base case: the array is exhausted
  if index == array.length
    return -1 // not found
  // compare the target value with the current element
  if target == array[index]
    return index // found
  else
    // search in the next element of the array
    return linearSearch(array, target, index + 1)
```

- The time complexity of linear search is O(n), where n is the number of elements in the array. The space complexity of linear search is O(1) for the iterative method and O(n) for the recursive method, due to the stack space used by the recursive calls  .
- Binary search is more efficient than linear search for large and sorted arrays, as it reduces the search range by half at each step. Linear search is simpler and more suitable for small and unsorted arrays, as it does not require any sorting or extra space   [^7



## Program for Heap Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure to sort a given array of elements.
- A binary heap is a complete binary tree that satisfies the heap property, which means that every node is greater than or equal to its children (max-heap) or less than or equal to its children (min-heap).
- The basic idea of heap sort is to build a max-heap or a min-heap from the input array, and then repeatedly extract the root element (which is the maximum or minimum element) and place it at the end of the sorted array, until the heap is empty.
- The algorithm can be divided into two phases: heapify and extract.
- Heapify is the process of converting an array into a heap by adjusting the positions of the elements such that the heap property is maintained.
- Extract is the process of removing the root element from the heap and placing it at the end of the sorted array, and then restoring the heap property by swapping the last element of the heap with the new root and sifting it down the heap.
- The time complexity of heap sort is O(n log n) in the worst, average, and best cases, where n is the number of elements in the array.
- The space complexity of heap sort is O(1) in the worst, average, and best cases, as it only requires a constant amount of auxiliary space to perform the swaps.
- Heap sort is an in-place and unstable sorting algorithm, which means that it does not require extra space to store the sorted array, and it does not preserve the relative order of equal elements.
- Heap sort is suitable for sorting large data sets, as it can handle them efficiently and does not depend on the initial order of the elements.
- Heap sort is not suitable for sorting small data sets, as it has a high overhead of building and maintaining the heap structure, and it does not take advantage of the existing order of the elements.

Here is a pseudocode for heap sort:

```
procedure heap_sort(array A)
  n = length(A)
  // build a max-heap from the array
  for i = n/2 downto 1
    heapify(A, i, n)
  end for
  // extract the root element and place it at the end of the sorted array
  for i = n downto 2
    swap(A[1], A[i]) // move the maximum element to the end
    n = n - 1 // reduce the size of the heap by one
    heapify(A, 1, n) // restore the heap property
  end for
end procedure

procedure heapify(array A, index i, size n)
  // assume that the subtrees rooted at i's left and right children are heaps
  // adjust the position of A[i] such that the subtree rooted at i is a heap
  largest = i // initialize the largest element as the root
  left = 2 * i // get the index of the left child
  right = 2 * i + 1 // get the index of the right child
  // compare the root with its left child
  if left <= n and A[left] > A[largest]
    largest = left
  end if
  // compare the root with its right child
  if right <= n and A[right] > A[largest]
    largest = right
  end if
  // if the root is not the largest element, swap it with the largest child and recurse
  if largest != i
    swap(A[i], A[largest])
    heapify(A, largest, n)
  end if
end procedure
```



## Program for Merge Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Merge sort is a divide-and-conquer algorithm that splits an array into two halves and recursively sorts each half, then merges the sorted halves into a single sorted array.
- The algorithm can be implemented using the following steps:

  1. If the array has only one element, return the array as it is already sorted.
  2. Otherwise, divide the array into two equal or nearly equal parts, called the left and right subarrays.
  3. Recursively apply merge sort to the left and right subarrays, and obtain the sorted left and right subarrays.
  4. Merge the sorted left and right subarrays using a helper function that takes two sorted arrays and returns a single sorted array.
  5. Return the merged array as the final sorted array.

- The time complexity of merge sort is O(n log n) in the average and worst cases, where n is the number of elements in the array. The space complexity is O(n) as the algorithm requires an auxiliary array to store the merged subarrays.
- The following is a possible pseudocode implementation of merge sort in C:

```c
// A helper function that merges two sorted arrays into one sorted array
void merge(int arr[], int left, int mid, int right) {
  // Create a temporary array to store the merged array
  int temp[right - left + 1];

  // Initialize the indices for the left, right, and merged subarrays
  int i = left; // index for the left subarray
  int j = mid + 1; // index for the right subarray
  int k = 0; // index for the merged subarray

  // Loop until either the left or the right subarray is exhausted
  while (i <= mid && j <= right) {
    // Compare the current elements of the left and right subarrays
    // and copy the smaller one to the merged subarray
    if (arr[i] <= arr[j]) {
      temp[k] = arr[i];
      i++;
    } else {
      temp[k] = arr[j];
      j++;
    }
    k++;
  }

  // Copy the remaining elements of the left subarray, if any
  while (i <= mid) {
    temp[k] = arr[i];
    i++;
    k++;
  }

  // Copy the remaining elements of the right subarray, if any
  while (j <= right) {
    temp[k] = arr[j];
    j++;
    k++;
  }

  // Copy the merged subarray back to the original array
  for (i = left; i <= right; i++) {
    arr[i] = temp[i - left];
  }
}

// A recursive function that implements merge sort
void merge_sort(int arr[], int left, int right) {
  // Base case: if the array has only one element, return
  if (left == right) {
    return;
  }

  // Otherwise, find the middle point of the array
  int mid = (left + right) / 2;

  // Recursively sort the left and right subarrays
  merge_sort(arr, left, mid);
  merge_sort(arr, mid + 1, right);

  // Merge the sorted subarrays
  merge(arr, left, mid, right);
}
```



## Program for Selection Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Selection sort is a simple sorting algorithm that repeatedly finds the minimum element from the unsorted part of the array and puts it at the beginning.
- The algorithm maintains two subarrays in a given array: one that is already sorted and one that is unsorted.
- The algorithm repeatedly selects the smallest element from the unsorted subarray and swaps it with the leftmost element, and moves the subarray boundaries one element to the right.
- The algorithm has a time complexity of O(n^2), where n is the number of elements in the array.
- The algorithm is not stable, meaning that it does not preserve the relative order of equal elements.
- The algorithm is in-place, meaning that it does not require extra space to sort the array.

- The following is a pseudocode for selection sort:

```
selection_sort(array)
  for i from 0 to n-1
    min_index = i
    for j from i+1 to n
      if array[j] < array[min_index]
        min_index = j
    swap array[i] and array[min_index]
```

- The following is a C program for selection sort:

```c
#include <stdio.h>

// A function to swap two elements
void swap(int *a, int *b)
{
  int temp = *a;
  *a = *b;
  *b = temp;
}

// A function to perform selection sort on an array
void selection_sort(int array[], int n)
{
  int i, j, min_index;

  // One by one move boundary of unsorted subarray
  for (i = 0; i < n-1; i++)
  {
    // Find the minimum element in unsorted array
    min_index = i;
    for (j = i+1; j < n; j++)
      if (array[j] < array[min_index])
        min_index = j;

    // Swap the found minimum element with the first element
    swap(&array[min_index], &array[i]);
  }
}

// A function to print an array
void print_array(int array[], int n)
{
  int i;
  for (i = 0; i < n; i++)
    printf("%d ", array[i]);
  printf("\n");
}

// A main function to test the program
int main()
{
  int array[] = {64, 25, 12, 22, 11};
  int n = sizeof(array)/sizeof(array[0]);
  printf("Unsorted array: \n");
  print_array(array, n);
  selection_sort(array, n);
  printf("Sorted array: \n");
  print_array(array, n);
  return 0;
}
```

- The output of the program is:

```
Unsorted array: 
64 25 12 22 11 
Sorted array: 
11 12 22 25 64 
```



## Program for Insertion Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time by comparisons .
- It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort .
- However, insertion sort provides several advantages:
  - It is easy to implement and understand.
  - It is stable, meaning that it preserves the relative order of equal elements.
  - It is adaptive, meaning that it performs well on partially sorted arrays.
  - It requires constant space and no auxiliary data structures.
  - It can sort the array as it receives it, making it suitable for online or streaming data.
- The basic idea of insertion sort is to divide the array into two parts: a sorted part and an unsorted part .
- Initially, the sorted part consists of only the first element, and the unsorted part consists of the rest of the elements.
- The algorithm then picks an element from the unsorted part and inserts it into the correct position in the sorted part, shifting the larger elements to the right if necessary.
- This process is repeated until the unsorted part is empty and the array is sorted.
- The pseudocode for insertion sort is as follows:

```
insertionSort(array)
  for i = 1 to length(array)
    key = array[i]
    j = i - 1
    while j >= 0 and array[j] > key
      array[j + 1] = array[j]
      j = j - 1
    array[j + 1] = key
```

- The time complexity of insertion sort is O(n^2) in the worst case and average case, and O(n) in the best case, where n is the number of elements in the array .
- The worst case occurs when the array is in reverse order, and the best case occurs when the array is already sorted.
- The space complexity of insertion sort is O(1), as it only requires constant extra space for the key variable .



## Program for Quick Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Quick sort is a sorting algorithm that uses the divide-and-conquer strategy to sort a list of elements.
- The basic idea of quick sort is to choose a pivot element from the list, and partition the list into two sublists: one with elements smaller than the pivot, and one with elements larger than the pivot.
- The pivot element is then placed in its correct position in the sorted list, and the sublists are recursively sorted using the same procedure.
- The algorithm can be implemented using the following steps:

  1. Choose a pivot element from the list, usually the first or the last element.
  2. Compare each element in the list with the pivot, and swap it with another element if necessary, such that all elements smaller than the pivot are on its left, and all elements larger than the pivot are on its right.
  3. Place the pivot in its correct position in the sorted list, and divide the list into two sublists: one with elements on the left of the pivot, and one with elements on the right of the pivot.
  4. Recursively apply the same procedure to the sublists, until the list is sorted.

- The following is a pseudocode for quick sort:

  ```pseudocode
  procedure quick_sort(list, low, high)
    if low < high then
      pivot_index = partition(list, low, high) // partition the list and return the pivot index
      quick_sort(list, low, pivot_index - 1) // sort the left sublist
      quick_sort(list, pivot_index + 1, high) // sort the right sublist
    end if
  end procedure

  procedure partition(list, low, high)
    pivot = list[high] // choose the last element as the pivot
    i = low - 1 // initialize the index of the smaller element
    for j = low to high - 1 do // loop through the list
      if list[j] <= pivot then // if the current element is smaller than or equal to the pivot
        i = i + 1 // increment the index of the smaller element
        swap list[i] and list[j] // swap the current element with the smaller element
      end if
    end for
    swap list[i + 1] and list[high] // swap the pivot with the element next to the smaller element
    return i + 1 // return the pivot index
  end procedure
  ```

- The following is a sample C program for quick sort:

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
      if (arr[j] <= pivot) { // if the current element is smaller than or equal to the pivot
        i++; // increment the index of the smaller element
        swap(&arr[i], &arr[j]); // swap the current element with the smaller element
      }
    }
    swap(&arr[i + 1], &arr[high]); // swap the pivot with the element next to the smaller element
    return i + 1; // return the pivot index
  }

  // function to sort an array using quick sort
  void quick_sort(int arr[], int low, int high) {
    if (low < high) { // if the array is not empty
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
    int arr[] = {10, 7, 8, 9, 1, 5

```




## Knapsack Problem using Greedy Solution

- The knapsack problem is a combinatorial optimization problem that asks: Given a set of items, each with a weight and a value, determine which items to include in the collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.
- The fractional knapsack problem is a variation of the knapsack problem, where the items can be broken into smaller pieces and the thief can take any fraction of an item.
- The greedy solution for the fractional knapsack problem is an efficient method that works as follows   :
  - For each item, compute its value/weight ratio.
  - Sort the items in decreasing order of their value/weight ratio.
  - Initialize the total value and the total weight of the knapsack to zero.
  - For each item in the sorted order, do the following:
    - If the item's weight is less than or equal to the remaining capacity of the knapsack, then take the whole item and add its value and weight to the knapsack.
    - If the item's weight is more than the remaining capacity of the knapsack, then take a fraction of the item that fills the knapsack and add its proportional value and weight to the knapsack.
    - Break the loop if the knapsack is full.
  - Return the total value and the total weight of the knapsack as the optimal solution.
- The greedy solution for the fractional knapsack problem has a time complexity of O(n log n), where n is the number of items, because the main operation is sorting the items by their value/weight ratio.
- The greedy solution for the fractional knapsack problem is optimal, meaning that it always gives the maximum possible value for the knapsack, because it satisfies the greedy choice property and the optimal substructure property:
  - The greedy choice property states that a globally optimal solution can be obtained by making a locally optimal (greedy) choice at each step. In this case, the greedy choice is to take the item with the highest value/weight ratio that fits in the knapsack.
  - The optimal substructure property states that an optimal solution to a problem can be constructed from optimal solutions to its subproblems. In this case, the subproblems are the remaining items and the remaining capacity of the knapsack after each greedy choice.



## Perform Travelling Salesman Problem for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- The Travelling Salesman Problem (TSP) is a classic optimization problem that asks for the shortest possible route that visits each city exactly once and returns to the starting point.
- The TSP can be modeled as a graph, where the cities are the nodes and the distances between them are the edges. The goal is to find a Hamiltonian cycle (a cycle that visits each node exactly once) with the minimum total edge weight.
- The TSP is an NP-hard problem, meaning that there is no known efficient algorithm that can solve it in polynomial time. However, there are some approximation algorithms and heuristics that can find near-optimal solutions in reasonable time.
- One of the approximation algorithms for the TSP is the nearest neighbor algorithm, which starts from a random city and repeatedly visits the closest unvisited city until all cities are visited. This algorithm has a worst-case performance ratio of 2, meaning that the length of the tour it produces can be at most twice as long as the optimal tour.
- Another approximation algorithm for the TSP is the 2-opt algorithm, which starts from any initial tour and repeatedly swaps two edges if it improves the tour length. This algorithm can improve the solution obtained by the nearest neighbor algorithm, but it is not guaranteed to find the optimal tour. The 2-opt algorithm can be combined with other heuristics, such as the farthest insertion algorithm, which inserts the farthest unvisited city into the current tour at the best possible position.
- The notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System can be organized as follows:

  - Introduction to the TSP and its applications in real time systems, such as scheduling, routing, and resource allocation.
  - Implementation and analysis of the nearest neighbor algorithm and the 2-opt algorithm in a programming language of choice, such as C, C++, Java, or Python.
  - Comparison of the performance and quality of the two algorithms on different datasets, such as random graphs, Euclidean graphs, and real-world graphs.
  - Discussion of the advantages and disadvantages of the approximation algorithms and the challenges of finding optimal solutions for the TSP.
  - Exploration of other possible algorithms and heuristics for the TSP, such as the Christofides algorithm, the simulated annealing algorithm, and the genetic algorithm.



## Find Minimum Spanning Tree using Kruskal’s Algorithm

- A **minimum spanning tree (MST)** of a weighted, undirected graph is a subgraph that connects all the vertices with the minimum possible total edge weight.
- **Kruskal's algorithm** is a greedy algorithm that finds a MST by selecting the edges with the lowest weight that do not form a cycle  .
- The algorithm works as follows  :
  - Sort all the edges in non-decreasing order of their weight.
  - Initialize a forest of disjoint sets, where each set contains one vertex of the graph.
  - Initialize an empty queue to store the MST edges.
  - Repeat until the queue has V-1 edges, where V is the number of vertices in the graph:
    - Pick the smallest edge from the sorted edge list and remove it.
    - If the edge connects two different sets in the forest, then add it to the queue and union the two sets.
    - Otherwise, discard the edge.
  - Return the queue as the MST.
- The algorithm can be implemented using a priority queue to store the sorted edges, a union-find data structure to maintain the forest of disjoint sets, and a queue to collect the MST edges.
- The time complexity of the algorithm is O(E log E), where E is the number of edges in the graph, since the sorting step dominates the other operations.
- The algorithm can handle graphs that are not connected, in which case it will find a **minimum spanning forest**, which is a collection of MSTs for each connected component.
- The algorithm is optimal, meaning that it always finds a MST with the minimum possible weight.



## Implement N Queen Problem using Backtracking for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- The N Queen Problem is to find an arrangement of N queens on a chess board of dimension N x N, such that no two queens can attack each other. A queen can attack horizontally, vertically, or diagonally.
- Backtracking is a technique to solve problems that involve searching for a solution among a large number of possibilities. It involves trying a possible solution, and if it does not work, undoing it and trying another one, until a solution is found or all possibilities are exhausted.
- The steps to implement the N Queen Problem using Backtracking are:

  1. Start from the leftmost column of the chess board.
  2. Try placing a queen in each row of the current column, and check if it is safe to do so. A queen is safe if there is no other queen in the same row, column, or diagonal.
  3. If a safe position is found, mark it as part of the solution and move to the next column. Recursively repeat steps 2 and 3 for the remaining columns.
  4. If no safe position is found in the current column, backtrack to the previous column and remove the queen from the marked position. Try placing the queen in a different row of the same column and repeat steps 2 and 3.
  5. If all columns are filled with queens, the solution is complete and can be printed or returned.
  6. If all possible positions are tried and no solution is found, the problem has no solution and can be reported.

- The following is a possible pseudocode for the N Queen Problem using Backtracking:

  ```
  function NQueen(n):
    // create an empty n x n chess board
    board = create a 2D array of size n x n and fill it with 0
    // try placing queens starting from the first column
    if NQueenHelper(board, 0, n) == false:
      // no solution exists
      print "No solution"
    else:
      // print the solution
      print board

  function NQueenHelper(board, col, n):
    // base case: all columns are filled
    if col == n:
      // solution found
      return true
    // try each row in the current column
    for row in 0 to n-1:
      // check if the queen can be placed safely
      if isSafe(board, row, col, n) == true:
        // place the queen
        board[row][col] = 1
        // try placing queens in the next column
        if NQueenHelper(board, col+1, n) == true:
          // solution found
          return true
        // if not, backtrack and remove the queen
        board[row][col] = 0
    // if no row works, no solution exists in this branch
    return false

  function isSafe(board, row, col, n):
    // check the row
    for i in 0 to col-1:
      if board[row][i] == 1:
        return false
    // check the upper left diagonal
    for i, j in row-1, col-1 to 0, 0 by -1, -1:
      if board[i][j] == 1:
        return false
    // check the lower left diagonal
    for i, j in row+1, col-1 to n-1, 0 by 1, -1:
      if board[i][j] == 1:
        return false
    // if none of the above cases are true, the position is safe
    return true
  ```



## Sort a given set of n integer elements using Quick Sort method and compute its time complexity. Run the program for varied values of n> 5000 and record the time taken to sort. Plot a graph of the time taken versus non graph sheet. The elements can be read from a file or can be generated using the random number generator. Demonstrate using Java how the divide and- conquer method works along with its time complexity analysis: worst case, average case and best case. for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Quick Sort is a sorting algorithm that uses the divide and conquer technique to sort a given array of integers.
- The basic idea of Quick Sort is to choose a pivot element from the array, such as the first or the last element, and partition the array into two subarrays: one with elements smaller than the pivot and one with elements larger than the pivot.
- The pivot element is then placed in its correct position in the sorted array, and the subarrays are recursively sorted using the same procedure.
- The time complexity of Quick Sort depends on the choice of the pivot element and the distribution of the elements in the array.
- The worst case time complexity of Quick Sort is O(n^2), which occurs when the pivot element is the smallest or the largest element in the array, or when the array is already sorted or reverse sorted. In this case, the partitioning step does not divide the array evenly, and one subarray has n-1 elements while the other has 0 elements. This leads to n-1 recursive calls, each taking O(n) time to partition the array.
- The average case time complexity of Quick Sort is O(n log n), which occurs when the pivot element is chosen randomly or by using some heuristic, such as the median of three elements. In this case, the partitioning step divides the array into two subarrays of roughly equal size, and the recursive calls take O(log n) time to sort each subarray. The total time taken is O(n log n) + O(n) = O(n log n), where O(n) is the time taken to partition the array.
- The best case time complexity of Quick Sort is also O(n log n), which occurs when the pivot element is the median of the array. In this case, the partitioning step divides the array into two subarrays of exactly equal size, and the recursive calls take O(log n) time to sort each subarray. The total time taken is O(n log n) + O(n) = O(n log n), where O(n) is the time taken to partition the array.
- To implement Quick Sort in Java, we can use the following code:

```java
// A utility function to swap two elements in an array
public static void swap(int[] arr, int i, int j) {
  int temp = arr[i];
  arr[i] = arr[j];
  arr[j] = temp;
}

// A function to partition the array around a pivot element
public static int partition(int[] arr, int low, int high) {
  // Choose the last element as the pivot
  int pivot = arr[high];
  // Initialize the index of the smaller element
  int i = low - 1;
  // Loop through the elements from low to high - 1
  for (int j = low; j < high; j++) {
    // If the current element is smaller than or equal to the pivot
    if (arr[j] <= pivot) {
      // Increment the index of the smaller element
      i++;
      // Swap the current element with the smaller element
      swap(arr, i, j);
    }
  }
  // Swap the pivot element with the element at i + 1
  swap(arr, i + 1, high);
  // Return the index of the pivot element
  return i + 1;
}

// A function to sort the array using Quick Sort
public static void quickSort(int[] arr, int low, int high) {
  // Base case: if the array has one or zero elements, it is already sorted
  if (low >= high) {
    return;
  }
  // Partition the array around a pivot element and get its index
  int pi = partition(arr, low, high);
  // Recursively sort the left subarray
  quickSort(arr, low, pi - 1);
  // Recursively sort the right subarray
  quickSort(arr, pi + 1, high);
}

// A function to generate an array of n random integers
public static int[] generateRandomArray(int n) {
  // Create a new array of size n
  int[] arr = new int

```




## Merge Sort

- Merge sort is a divide-and-conquer algorithm that recursively splits a given array of n elements into two halves, sorts each half, and then merges them back into a single sorted array.
- The algorithm can be described as follows:

  - Base case: If the array has zero or one element, it is already sorted. Return the array as it is.
  - Recursive case: Otherwise, divide the array into two subarrays of equal or nearly equal size. Call merge sort on each subarray and store the results in two sorted arrays. Then, merge the two sorted arrays into one sorted array by comparing the first elements of each array and taking the smaller one until both arrays are exhausted. Return the merged array as the result.

- The time complexity of merge sort is O(n log n) in the worst case, average case, and best case scenarios, where n is the number of elements in the array. This is because the algorithm always divides the array into two halves, which takes O(log n) steps, and then merges them back in O(n) time per step. Therefore, the total time is O(n log n) for any input.
- The following pseudocode illustrates the merge sort algorithm:

  ```
  function merge_sort(array)
    // Base case: array has zero or one element
    if length(array) <= 1 then
      return array
    // Recursive case: divide array into two halves
    mid = floor(length(array) / 2)
    left = array[0 ... mid-1] // first half of array
    right = array[mid ... length(array)-1] // second half of array
    // Sort each half recursively
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    // Merge the two sorted halves
    return merge(sorted_left, sorted_right)
  end function

  function merge(left, right)
    // Initialize an empty result array
    result = []
    // Initialize indices for left and right arrays
    i = 0
    j = 0
    // Loop until one of the arrays is exhausted
    while i < length(left) and j < length(right) do
      // Compare the first elements of left and right
      if left[i] <= right[j] then
        // Append the smaller element to the result
        append left[i] to result
        // Increment the index for left
        i = i + 1
      else
        // Append the smaller element to the result
        append right[j] to result
        // Increment the index for right
        j = j + 1
      end if
    end while
    // Append the remaining elements of the non-empty array to the result
    if i < length(left) then
      append left[i ... length(left)-1] to result
    else
      append right[j ... length(right)-1] to result
    end if
    // Return the result array
    return result
  end function
  ```

- To run the program for varied values of n > 5000, and record the time taken to sort, we can use a loop to generate random arrays of different sizes and measure the execution time of the merge sort function using a timer. For example, in Python, we can use the following code:

  ```
  import random
  import time

  # Define the merge sort function as above
  def merge_sort(array):
    ...

  def merge(left, right):
    ...

  # Initialize an empty list to store the time taken for different values of n
  time_list = []

  # Loop from n = 5000 to n = 10000 with a step of 500
  for n in range(5000, 10001, 500):
    # Generate a random array of size n
    array = [random.randint(0, 100) for _ in range(n)]
    # Start the timer
    start = time.time()
    # Sort the array using merge sort
    sorted_array = merge_sort(array)
    # Stop the timer
    end = time.time()
    # Calculate the time taken in seconds
    time_taken = end - start
    # Append the time taken to the time list
    time_list.append(time_taken)
    # Print the value of n and the time taken
    print(f"n = {n}, time = {time_taken} seconds")
  ```

- To plot a graph of the time taken versus n on a graph sheet, we can use a scatter plot or a line plot to show the relationship between the two variables. We can label the x-axis as "n" and the y-axis as "time (seconds)". We



## Implement the 0/1 Knapsack problem using (a) Dynamic Programming method (b) Greedy method.

The 0/1 Knapsack problem is a classic optimization problem where we have a set of items, each with a weight and a value, and we need to determine the subset of items that maximizes the total value while keeping the total weight within a given limit. The name 0/1 comes from the fact that we can either take an item or leave it, but not take a fraction of it.

### (a) Dynamic Programming method

Dynamic programming is a technique for solving problems that have overlapping subproblems and optimal substructure. The idea is to break down the problem into smaller subproblems, solve them once and store their solutions, and then use them to solve the original problem.

The dynamic programming method for the 0/1 Knapsack problem works as follows:

- Define a 2D array `dp[n+1][W+1]`, where `n` is the number of items and `W` is the knapsack capacity. Each cell `dp[i][j]` will store the maximum value that can be obtained by using the first `i` items and a knapsack of capacity `j`.
- Initialize the first row and the first column of `dp` to zero, since no value can be obtained with zero items or zero capacity.
- For each item `i` from `1` to `n`, and for each capacity `j` from `1` to `W`, do the following:
  - If the weight of the item `i` is less than or equal to `j`, then we have two options: either take the item or leave it. The maximum value in this case is the maximum of these two options:
    - Take the item: the value is `dp[i-1][j-w[i]] + v[i]`, where `w[i]` and `v[i]` are the weight and value of the item `i`, and `dp[i-1][j-w[i]]` is the maximum value that can be obtained by using the first `i-1` items and a knapsack of capacity `j-w[i]`.
    - Leave the item: the value is `dp[i-1][j]`, which is the maximum value that can be obtained by using the first `i-1` items and a knapsack of capacity `j`.
  - If the weight of the item `i` is greater than `j`, then we cannot take the item, and the maximum value is `dp[i-1][j]`.
  - Update `dp[i][j]` with the maximum value obtained from the above cases.
- The final answer is `dp[n][W]`, which is the maximum value that can be obtained by using all the items and a knapsack of capacity `W`.

The pseudocode for the dynamic programming method is:

```
function knapsack_dp(w, v, n, W):
  // w: array of item weights
  // v: array of item values
  // n: number of items
  // W: knapsack capacity
  // returns: maximum value that can be obtained

  // create a 2D array of size (n+1) x (W+1)
  dp = array[n+1][W+1]

  // initialize the first row and column to zero
  for i = 0 to n:
    dp[i][0] = 0
  for j = 0 to W:
    dp[0][j] = 0

  // fill the rest of the array using the recurrence relation
  for i = 1 to n:
    for j = 1 to W:
      if w[i] <= j:
        // either take the item or leave it
        dp[i][j] = max(dp[i-1][j-w[i]] + v[i], dp[i-1][j])
      else:
        // cannot take the item
        dp[i][j] = dp[i-1][j]

  // return the final answer
  return dp[n][W]
```

The time complexity of the dynamic programming method is `O(nW)`, where `n` is the number of items and `W` is the knapsack capacity. The space complexity is also `O(nW)`, since we need to store the `dp` array.

### (b) Greedy method

The greedy method for the 0/1 Knaps



## From a given vertex in a weighted connected graph, find shortest paths to other vertices using Dijkstra's algorithm.

- Dijkstra's algorithm is a greedy algorithm that finds the shortest path from a given vertex to all other vertices in a weighted graph, where the weights represent the distances or costs of the edges.
- The algorithm maintains a set of visited vertices, initially empty, and a priority queue of unvisited vertices, initially containing all the vertices with their distances from the source vertex.
- The algorithm repeatedly extracts the vertex with the minimum distance from the priority queue, adds it to the visited set, and updates the distances of its adjacent vertices in the priority queue.
- The algorithm terminates when the priority queue is empty or when the destination vertex is extracted.
- The algorithm can be implemented using an array, a binary heap, or a Fibonacci heap as the data structure for the priority queue.
- The algorithm has a time complexity of O(V^2) using an array, O(E log V) using a binary heap, or O(E + V log V) using a Fibonacci heap, where V is the number of vertices and E is the number of edges in the graph.
- The algorithm can be used to solve various problems such as finding the shortest path between two cities, routing packets in a network, or finding the optimal sequence of tasks in a project.

Here is an example of how the algorithm works on a graph with six vertices and nine edges:

Graph

- The source vertex is A and the destination vertex is F.
- The algorithm starts with the priority queue containing all the vertices with their distances from A: {A:0, B:∞, C:∞, D:∞, E:∞, F:∞}.
- The algorithm extracts A from the priority queue, adds it to the visited set, and updates the distances of its adjacent vertices B and C: {B:7, C:9, D:∞, E:∞, F:∞}.
- The algorithm extracts B from the priority queue, adds it to the visited set, and updates the distances of its adjacent vertices D and E: {C:9, D:15, E:10, F:∞}.
- The algorithm extracts E from the priority queue, adds it to the visited set, and updates the distances of its adjacent vertices D and F: {C:9, D:11, F:13}.
- The algorithm extracts C from the priority queue, adds it to the visited set, and updates the distance of its adjacent vertex D: {D:11, F:13}.
- The algorithm extracts D from the priority queue, adds it to the visited set, and updates the distance of its adjacent vertex F: {F:13}.
- The algorithm extracts F from the priority queue, adds it to the visited set, and terminates.
- The shortest path from A to F is A-B-E-F with a distance of 13.



## Find Minimum Cost Spanning Tree of a given connected undirected graph using Kruskal's algorithm. Use Union-Find algorithms in your program.

- A **spanning tree** of a graph is a subgraph that contains all the vertices and is a tree (i.e., has no cycles).
- A **minimum cost spanning tree** (MST) of a graph is a spanning tree that has the minimum possible sum of edge weights among all the spanning trees of the graph.
- **Kruskal's algorithm** is a greedy algorithm that finds a MST of a given connected undirected graph using the following steps:
  - Sort all the edges in non-decreasing order of their weights.
  - Initialize a forest of disjoint sets, where each set contains one vertex of the graph.
  - Repeat until there are (V-1) edges in the spanning tree, where V is the number of vertices in the graph:
    - Pick the smallest edge from the sorted list that does not create a cycle in the current spanning tree.
    - Add this edge to the spanning tree and merge the two sets that contain the end vertices of this edge.
- **Union-Find** algorithms are data structures that support two operations on disjoint sets:
  - **Find**: Given an element, find the set that contains it.
  - **Union**: Given two sets, merge them into one set.
- Union-Find algorithms can be implemented using arrays, linked lists, or trees. A common and efficient implementation is using **union by rank** and **path compression**:
  - **Union by rank**: When merging two sets, attach the smaller set (by number of elements or by height of the tree) to the root of the larger set. This keeps the height of the tree balanced and reduces the time complexity of the find operation.
  - **Path compression**: When finding the set that contains an element, make every node on the path from the element to the root point directly to the root. This flattens the tree and reduces the time complexity of the find operation.



## Find Minimum Cost Spanning Tree of a given undirected graph using Prim’s algorithm.

- A **spanning tree** of a graph is a subgraph that contains all the vertices and is a tree (i.e., has no cycles).
- A **minimum cost spanning tree (MCST)** of a graph is a spanning tree that has the minimum possible total edge weight among all the spanning trees of the graph.
- **Prim's algorithm** is a greedy algorithm that finds a MCST of a given undirected graph.
- The algorithm works as follows:

  - Start with an arbitrary vertex as the root of the MCST.
  - Maintain a set of vertices that are already included in the MCST, and a set of edges that connect the included vertices to the rest of the graph.
  - Repeat until all the vertices are included in the MCST:
    - Find the edge with the minimum weight among the edges that connect the included vertices to the rest of the graph.
    - Add this edge and the corresponding vertex to the MCST, and update the set of edges accordingly.
  - Return the MCST.

- The algorithm can be implemented using a priority queue or a heap to store the edges and their weights, and to find the minimum weight edge in each iteration.
- The time complexity of the algorithm is O(E log V), where E is the number of edges and V is the number of vertices in the graph.
- The space complexity of the algorithm is O(E + V), where E is the number of edges and V is the number of vertices in the graph.
- An example of applying Prim's algorithm to a given undirected graph is shown below:

Prim's algorithm example

- The MCST of the graph has a total weight of 16, and consists of the edges AB, BC, CD, DE, and EF.



## Write programs to (a) Implement All-Pairs Shortest Paths problem using Floyd's algorithm. (b) Implement Travelling Sales Person problem using Dynamic programming. for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

### (a) Implement All-Pairs Shortest Paths problem using Floyd's algorithm.

- The All-Pairs Shortest Paths problem is to find the shortest distance between every pair of vertices in a weighted graph.
- Floyd's algorithm is a dynamic programming approach that solves this problem in O(n^3) time, where n is the number of vertices in the graph.
- The algorithm works by iteratively updating a matrix D that stores the shortest distances between all pairs of vertices, using the following formula:

```
D[i][j][k] = min(D[i][j][k-1], D[i][k][k-1] + D[k][j][k-1])
```

- This means that the shortest distance between vertices i and j using only the first k vertices as intermediate nodes is either the same as the shortest distance using only the first k-1 vertices, or it is the sum of the shortest distances from i to k and from k to j using only the first k-1 vertices.
- The algorithm starts with D[i][j][0] = w(i,j), where w(i,j) is the weight of the edge from i to j, or infinity if there is no such edge.
- The algorithm ends with D[i][j][n] = d(i,j), where d(i,j) is the shortest distance from i to j in the graph.
- The pseudocode of the algorithm is as follows:

```
// Input: A weighted graph G with n vertices
// Output: A matrix D of shortest distances between all pairs of vertices
Floyd(G):
  // Initialize D with edge weights or infinity
  for i = 1 to n:
    for j = 1 to n:
      if i == j:
        D[i][j][0] = 0
      else if (i,j) is an edge in G:
        D[i][j][0] = w(i,j)
      else:
        D[i][j][0] = infinity
  // Update D using the formula
  for k = 1 to n:
    for i = 1 to n:
      for j = 1 to n:
        D[i][j][k] = min(D[i][j][k-1], D[i][k][k-1] + D[k][j][k-1])
  // Return the final matrix
  return D
```

### (b) Implement Travelling Sales Person problem using Dynamic programming.

- The Travelling Sales Person problem is to find the shortest tour that visits every vertex in a weighted graph exactly once and returns to the starting vertex.
- This problem is NP-hard, meaning that there is no known polynomial-time algorithm that can solve it optimally.
- However, using dynamic programming, we can find an optimal solution in O(n^2 * 2^n) time, where n is the number of vertices in the graph.
- The idea is to use a matrix C that stores the minimum cost of a tour that starts at vertex 1, visits a subset of vertices S, and ends at vertex i, for every i and S.
- The algorithm works by iteratively updating C using the following formula:

```
C[i][S] = min(C[j][S-{i}] + w(j,i)) for every j in S-{i}
```

- This means that the minimum cost of a tour that starts at 1, visits S, and ends at i is the minimum of the cost of a tour that starts at 1, visits S-{i}, and ends at j, plus the cost of the edge from j to i, for every j in S-{i}.
- The algorithm starts with C[1][{1}] = 0, and C[i][{1}] = infinity for every i > 1.
- The algorithm ends with C[1][{1,2,...,n}], which is the minimum cost of a tour that visits every vertex exactly once and returns to 1.
- The pseudocode of the algorithm is as follows:

```
// Input: A weighted graph G with n vertices
// Output: The minimum cost of a TSP tour
TSP(G):
  // Initialize C with 0 or infinity
  for i = 1 to n:
    for S = {1} to {1,2,...,n}:
      if i == 1 and S == {1}:
        C[i][S] = 0

```




## Design and implement to find a subset of a given set S = {Sl, S2,.....,Sn} of n positive integers whose SUM is equal to a given positive integer d. For example, if S ={1, 2, 5, 6, 8} and d= 9, there are two solutions {1,2,6}and {1,8}. Display a suitable message, if the given problem instance doesn't have a solution. for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- This problem is an example of the **subset sum problem**, which is a special case of the **knapsack problem**. The subset sum problem is to find a subset of a given set of numbers that adds up to a given target number. The knapsack problem is to find a subset of items with given weights and values that maximizes the total value without exceeding the capacity of the knapsack.
- The subset sum problem is **NP-complete**, which means that there is no known efficient algorithm that can solve it in polynomial time for any input size. However, there are some algorithms that can solve it in **exponential time**, or in **polynomial time** for some special cases or approximations.
- One possible algorithm to solve the subset sum problem is to use **backtracking**, which is a technique that explores all possible solutions by recursively choosing and unchoosing elements from the set. The algorithm works as follows:

  - Start with an empty subset and a remaining sum equal to the target sum.
  - For each element in the set, do the following:
    - If the element is equal to the remaining sum, then add it to the subset and return the subset as a solution.
    - If the element is smaller than the remaining sum, then add it to the subset and recursively try to find a solution with the remaining elements and the reduced sum.
    - If the element is larger than the remaining sum, then skip it and continue with the next element.
  - If no element is left, then return an empty subset as a failure.

- The pseudocode for the backtracking algorithm is given below:

  ```
  function subsetSum(set, target):
    return subsetSumHelper(set, target, 0, [])

  function subsetSumHelper(set, target, index, subset):
    # base case: no elements left
    if index == set.length:
      # check if the subset is a solution
      if target == 0:
        return subset
      else:
        return []
    # recursive case: try the current element
    element = set[index]
    # case 1: element is equal to the target
    if element == target:
      # add it to the subset and return it as a solution
      subset.push(element)
      return subset
    # case 2: element is smaller than the target
    if element < target:
      # add it to the subset and try to find a solution with the remaining elements and the reduced target
      subset.push(element)
      solution = subsetSumHelper(set, target - element, index + 1, subset)
      # if a solution is found, return it
      if solution.length > 0:
        return solution
      # otherwise, remove the element from the subset and continue
      subset.pop()
    # case 3: element is larger than the target
    # skip it and continue with the next element
    return subsetSumHelper(set, target, index + 1, subset)
  ```

- The time complexity of the backtracking algorithm is **O(2^n)**, where n is the size of the set. This is because the algorithm explores all possible subsets of the set, which are 2^n in number. The space complexity is **O(n)**, where n is the size of the set. This is because the algorithm uses a recursive call stack and a subset array that can store at most n elements.
- Another possible algorithm to solve the subset sum problem is to use **dynamic programming**, which is a technique that breaks down a complex problem into smaller subproblems and stores the results of the subproblems in a table to avoid recomputation. The algorithm works as follows:

  - Create a boolean table of size (n+1) x (target+1), where n is the size of the set and target is the target sum. The table[i][j] entry indicates whether there is a subset of the first i elements of the set that adds up to j.
  - Initialize the first row of the table to false, except for the table[0][0] entry, which is true. This means that there is no subset of the empty set that adds up to



## Design and implement to find all Hamiltonian Cycles in a connected undirected Graph G of n vertices using backtracking principle.

- A Hamiltonian cycle is a cycle in a graph that visits every vertex exactly once and returns to the starting vertex.
- A graph is connected if there is a path between any two vertices.
- A graph is undirected if the edges have no direction, meaning that (u, v) and (v, u) are the same edge.
- Backtracking is a general algorithmic technique that tries different solutions recursively until a desired goal is reached or no more solutions are possible.
- To find all Hamiltonian cycles in a connected undirected graph G of n vertices using backtracking, we can use the following steps:

  1. Create an array path of size n to store the vertices of the current cycle. Initialize path[0] to any vertex in G.
  2. Create a boolean matrix visited of size n x n to keep track of the edges that have been used in the current cycle. Initialize all entries to false.
  3. Define a recursive function hamCycle(G, path, pos) that takes the graph G, the path array, and the current position pos as parameters and returns true if a Hamiltonian cycle is found, and false otherwise.
  4. In the function hamCycle, if pos is equal to n, check if there is an edge from path[n-1] to path[0] in G. If yes, print the path array as a Hamiltonian cycle and return true. If no, return false.
  5. For each vertex v in G that is adjacent to path[pos-1] and not visited, do the following:
    - Mark the edge (path[pos-1], v) as visited by setting visited[path[pos-1]][v] to true.
    - Add v to the path array by setting path[pos] to v.
    - Recursively call hamCycle(G, path, pos+1) and store the result in a boolean variable res.
    - If res is true, return true.
    - Otherwise, backtrack by unmarking the edge (path[pos-1], v) as visited by setting visited[path[pos-1]][v] to false and removing v from the path array by setting path[pos] to -1.
  6. If no vertex can be added to the path array, return false.
  7. Call the function hamCycle(G, path, 1) and return its result.

