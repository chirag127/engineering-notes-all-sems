

## Program for Recursive Binary & Linear Search for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- A **recursive binary search** is an algorithm that searches for a target value in a sorted array by repeatedly dividing the search interval in half and comparing the target value with the middle element of the subarray.
- A **recursive linear search** is an algorithm that searches for a target value in an array by checking each element from left to right until the target value is found or the end of the array is reached.
- Both algorithms use **recursion**, which is a technique of defining a problem in terms of smaller instances of the same problem.
- The **time complexity** of recursive binary search is O(log n), where n is the size of the array, because the search interval is halved at each recursive call.
- The **time complexity** of recursive linear search is O(n), where n is the size of the array, because each element is checked once in the worst case.
- The **space complexity** of both algorithms is O(log n), where n is the size of the array, because the maximum depth of the recursive call stack is log n.
- The **advantages** of recursive binary search are that it is faster than linear search for large arrays and that it does not require extra space for storing the indices of the subarray.
- The **disadvantages** of recursive binary search are that it requires the array to be sorted and that it may cause stack overflow for very large arrays or deep recursion.
- The **advantages** of recursive linear search are that it does not require the array to be sorted and that it is simple to implement.
- The **disadvantages** of recursive linear search are that it is slower than binary search for large arrays and that it may cause stack overflow for very large arrays or deep recursion.

- The **pseudocode** for recursive binary search is:

```
function binary_search(array, low, high, target)
  if low > high
    return -1 // target not found
  mid = (low + high) / 2 // integer division
  if array[mid] == target
    return mid // target found
  else if array[mid] > target
    return binary_search(array, low, mid - 1, target) // search in left subarray
  else
    return binary_search(array, mid + 1, high, target) // search in right subarray
```

- The **pseudocode** for recursive linear search is:

```
function linear_search(array, index, target)
  if index == array.length
    return -1 // target not found
  if array[index] == target
    return index // target found
  else
    return linear_search(array, index + 1, target) // search in next element
```



## Program for Heap Sort

Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure to sort a list of elements. It works by dividing the list into two regions: a sorted region and an unsorted region. It iteratively shrinks the unsorted region by extracting the largest element from it and inserting it into the sorted region. Here are the main steps of the heap sort algorithm:

- Build a max heap from the input list. A max heap is a complete binary tree where each node is greater than or equal to its children. The root node is the largest element in the heap. This can be done in linear time by using a bottom-up approach (see Binary heap § Building a heap).
- Swap the root node (the largest element) with the last node in the heap. This moves the largest element to the end of the list, which is now part of the sorted region.
- Reduce the size of the heap by one and heapify the root node. Heapify is a process of restoring the heap property by swapping the node with its largest child until it is greater than or equal to both of its children. This can be done in logarithmic time by using a top-down approach (see Binary heap § Heapify).
- Repeat steps 2 and 3 until the heap size is one. This means that the list is fully sorted.

Here is an example of heap sort in action:

Heap sort example

The following is a pseudocode for heap sort:

```
function heap_sort(list)
  n = length(list)
  build_max_heap(list, n) // build a max heap from the list
  for i from n to 2 // iterate from the last node to the second node
    swap list[1] and list[i] // swap the root node with the last node
    n = n - 1 // reduce the heap size by one
    heapify(list, 1, n) // heapify the root node
  end for
end function

function build_max_heap(list, n)
  for i from floor(n/2) to 1 // iterate from the last parent node to the root node
    heapify(list, i, n) // heapify each node
  end for
end function

function heapify(list, i, n)
  left = 2 * i // get the index of the left child
  right = 2 * i + 1 // get the index of the right child
  largest = i // assume the current node is the largest
  if left <= n and list[left] > list[largest] // if the left child is larger
    largest = left // update the largest
  end if
  if right <= n and list[right] > list[largest] // if the right child is larger
    largest = right // update the largest
  end if
  if largest != i // if the current node is not the largest
    swap list[i] and list[largest] // swap the current node with the largest child
    heapify(list, largest, n) // heapify the largest child
  end if
end function
```

The following are some implementations of heap sort in different programming languages:

- Python:

```python
def heap_sort(lst):
  n = len(lst)
  build_max_heap(lst, n) # build a max heap from the list
  for i in range(n-1, 0, -1): # iterate from the last node to the second node
    lst[0], lst[i] = lst[i], lst[0] # swap the root node with the last node
    n = n - 1 # reduce the heap size by one
    heapify(lst, 0, n) # heapify the root node

def build_max_heap(lst, n):
  for i in range(n//2 - 1, -1, -1): # iterate from the last parent node to the root node
    heapify(lst, i, n) # heapify each node

def heapify(lst, i, n):
  left = 2 * i + 1 # get the index of the left child
  right = 2 * i + 2 # get the index of the right child
  largest = i # assume the current node is the largest
  if left < n and lst[left] > lst[largest]: # if the left child is larger
    largest

```




## Program for Merge Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Merge sort is a divide-and-conquer algorithm that splits an array into two halves and recursively sorts each half, then merges the sorted halves into one sorted array.
- The algorithm can be implemented using the following steps:

  - Base case: If the array has zero or one element, it is already sorted and no further action is needed.
  - Recursive case: If the array has more than one element, divide it into two subarrays of equal or nearly equal size and sort each subarray recursively using merge sort.
  - Merge step: Combine the two sorted subarrays into one sorted array by comparing the first elements of each subarray and taking the smaller one into the output array, then repeating until one subarray is exhausted and appending the remaining elements of the other subarray to the output array.

- The time complexity of merge sort is O(n log n) in the average and worst cases, where n is the number of elements in the array. The space complexity is O(n) as the algorithm requires an auxiliary array of the same size as the input array.
- The following is a possible pseudocode implementation of merge sort:

  ```
  function merge_sort(array)
    // Base case
    if length(array) <= 1 then
      return array
    // Recursive case
    else
      // Divide the array into two subarrays
      mid = floor(length(array) / 2)
      left = array[0 ... mid - 1]
      right = array[mid ... length(array) - 1]
      // Sort each subarray recursively
      left = merge_sort(left)
      right = merge_sort(right)
      // Merge the sorted subarrays
      return merge(left, right)
    end if
  end function

  function merge(left, right)
    // Initialize an empty output array
    output = []
    // Initialize indices for left and right subarrays
    i = 0
    j = 0
    // Loop until one subarray is exhausted
    while i < length(left) and j < length(right) do
      // Compare the first elements of each subarray and take the smaller one into the output array
      if left[i] <= right[j] then
        output.append(left[i])
        i = i + 1
      else
        output.append(right[j])
        j = j + 1
      end if
    end while
    // Append the remaining elements of the non-exhausted subarray to the output array
    if i < length(left) then
      output.extend(left[i ... length(left) - 1])
    else
      output.extend(right[j ... length(right) - 1])
    end if
    // Return the output array
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

- A diagram for selection sort is given below:

Selection sort diagram

- A C program for selection sort is given below:

```
#include <stdio.h>

// A function to swap two elements
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
    if (min_index != i) {
      swap(&arr[i], &arr[min_index]);
    }
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



## Program for Insertion Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Insertion sort is a simple sorting algorithm that works by comparing each element of an array with the previous elements and inserting it in the correct position.
- The algorithm starts from the second element of the array and iterates until the last element.
- For each element, it compares it with the elements on its left and shifts them to the right until it finds the correct position to insert the element.
- The algorithm maintains a sorted subarray on the left of the current element and an unsorted subarray on the right of the current element.
- The algorithm has a time complexity of O(n^2) in the worst case and O(n) in the best case, where n is the number of elements in the array.
- The algorithm is stable, meaning that it preserves the relative order of equal elements in the array.
- The algorithm is adaptive, meaning that it performs better on partially sorted arrays than on random arrays.
- The algorithm is in-place, meaning that it does not require extra space to sort the array.
- The algorithm is suitable for small arrays or arrays that are nearly sorted.

- The following is a pseudocode for insertion sort:

```
insertion_sort(array)
  for i = 1 to length(array) - 1
    key = array[i]
    j = i - 1
    while j >= 0 and array[j] > key
      array[j + 1] = array[j]
      j = j - 1
    array[j + 1] = key
  return array
```

- The following is a C program for insertion sort:

```
#include <stdio.h>

void insertion_sort(int array[], int n)
{
  int i, j, key;
  for (i = 1; i < n; i++)
  {
    key = array[i];
    j = i - 1;
    while (j >= 0 && array[j] > key)
    {
      array[j + 1] = array[j];
      j = j - 1;
    }
    array[j + 1] = key;
  }
}

void print_array(int array[], int n)
{
  int i;
  for (i = 0; i < n; i++)
  {
    printf("%d ", array[i]);
  }
  printf("\n");
}

int main()
{
  int array[] = {5, 2, 4, 6, 1, 3};
  int n = sizeof(array) / sizeof(array[0]);
  printf("Unsorted array: ");
  print_array(array, n);
  insertion_sort(array, n);
  printf("Sorted array: ");
  print_array(array, n);
  return 0;
}
```

- The following is the output of the C program:

```
Unsorted array: 5 2 4 6 1 3
Sorted array: 1 2 3 4 5 6
```



## Program for Quick Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Quick sort is a divide-and-conquer algorithm that sorts an array of elements by recursively partitioning it into smaller subarrays and sorting them independently.
- The algorithm works as follows:
  - Choose a pivot element from the array, typically the first or the last element.
  - Rearrange the array such that all the elements smaller than the pivot are on the left side of the pivot, and all the elements larger than the pivot are on the right side of the pivot. This is called partitioning the array.
  - Recursively apply the same algorithm to the left and right subarrays, excluding the pivot element, until the subarrays are of size one or zero.
- The average time complexity of quick sort is O(n log n), where n is the number of elements in the array. The worst-case time complexity is O(n^2), which occurs when the array is already sorted or nearly sorted, and the pivot is chosen as the first or the last element.
- The space complexity of quick sort is O(log n), which is the maximum depth of the recursion stack.
- Quick sort is an in-place algorithm, which means it does not require additional memory to store the sorted array. However, it is not a stable algorithm, which means it does not preserve the relative order of equal elements in the array.
- Here is an example of a C program that implements quick sort:

```c
// A function to swap two elements in an array
void swap(int* a, int* b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

// A function to partition an array around a pivot element
int partition(int arr[], int low, int high) {
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
      swap(&arr[i], &arr[j]);
    }
  }
  // Swap the pivot element with the element at i + 1
  swap(&arr[i + 1], &arr[high]);
  // Return the index of the pivot element
  return i + 1;
}

// A function to sort an array using quick sort
void quickSort(int arr[], int low, int high) {
  // If the low index is smaller than the high index
  if (low < high) {
    // Partition the array and get the index of the pivot element
    int pi = partition(arr, low, high);
    // Recursively sort the left subarray
    quickSort(arr, low, pi - 1);
    // Recursively sort the right subarray
    quickSort(arr, pi + 1, high);
  }
}

// A function to print an array
void printArray(int arr[], int size) {
  for (int i = 0; i < size; i++) {
    printf("%d ", arr[i]);
  }
  printf("\n");
}

// A main function to test the program
int main() {
  // An example array
  int arr[] = {10, 7, 8, 9, 1, 5};
  // The size of the array
  int n = sizeof(arr) / sizeof(arr[0]);
  // Print the original array
  printf("Original array: \n");
  printArray(arr, n);
  // Sort the array using quick sort
  quickSort(arr, 0, n - 1);
  // Print the sorted array
  printf("Sorted array: \n");
  printArray(arr, n);
  // Return 0 to indicate success
  return 0;
}
```



## Knapsack Problem using Greedy Solution

- The knapsack problem is a problem of finding the optimal way to fill a knapsack with a given capacity and a set of items, each with a value and a weight.
- The fractional knapsack problem is a variant of the knapsack problem, where the items can be divided into smaller pieces and the knapsack can be filled with fractions of items.
- The greedy solution for the fractional knapsack problem is an efficient and optimal method, where the items are sorted by their value-to-weight ratio in descending order and the knapsack is filled with the highest ratio items first, until it is full or no more items are left.
- The algorithm for the greedy solution is as follows   :

  - Sort the items by their value-to-weight ratio in descending order.
  - Initialize the total value of the knapsack to zero and the remaining capacity of the knapsack to the given capacity.
  - For each item in the sorted list, do the following:
    - If the item's weight is less than or equal to the remaining capacity, then add the whole item to the knapsack, update the total value by adding the item's value, and update the remaining capacity by subtracting the item's weight.
    - If the item's weight is greater than the remaining capacity, then add a fraction of the item to the knapsack, such that the knapsack is filled to its capacity, update the total value by adding the fraction of the item's value, and update the remaining capacity to zero.
    - If the remaining capacity is zero, then stop the loop and return the total value of the knapsack.

- The time complexity of the greedy solution is O(n log n), where n is the number of items, since the sorting step takes O(n log n) time and the loop takes O(n) time.
- The greedy solution is optimal for the fractional knapsack problem, since it always chooses the item with the highest marginal value per unit weight, and thus maximizes the total value of the knapsack.
- The greedy solution is not optimal for the 0-1 knapsack problem, where the items cannot be divided and the knapsack can only be filled with whole items. In this case, the greedy solution may miss some better combinations of items that have lower value-to-weight ratios but higher total value.
- An example of the greedy solution for the fractional knapsack problem is shown below:

  - Given a knapsack with capacity 15 kg and four items with the following values and weights:

    | Item | Value | Weight | Value-to-weight ratio |
    |------|-------|--------|-----------------------|
    | A    | 10    | 2      | 5                     |
    | B    | 5     | 3      | 1.67                  |
    | C    | 15    | 5      | 3                     |
    | D    | 7     | 7      | 1                     |

  - Sort the items by their value-to-weight ratio in descending order:

    | Item | Value | Weight | Value-to-weight ratio |
    |------|-------|--------|-----------------------|
    | A    | 10    | 2      | 5                     |
    | C    | 15    | 5      | 3                     |
    | B    | 5     | 3      | 1.67                  |
    | D    | 7     | 7      | 1                     |

  - Initialize the total value of the knapsack to zero and the remaining capacity of the knapsack to 15 kg.
  - For each item in the sorted list, do the following:
    - For item A, the weight is 2 kg, which is less than the remaining capacity of 15 kg, so add the whole item to the knapsack, update the total value to 10, and update the remaining capacity to 13 kg.
    - For item C, the weight is 5 kg, which is less than the remaining capacity of 13 kg, so add the whole item to the knapsack, update the total value to 25, and update the remaining capacity to 8 kg.
    - For item B, the weight is 3 kg, which is less than the remaining capacity of 8 kg, so add the whole item to the knapsack, update the total



## Perform Travelling Salesman Problem for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- The Travelling Salesman Problem (TSP) is a classic optimization problem that asks for the shortest possible route that visits each city exactly once and returns to the starting point.
- The TSP is NP-hard, meaning that there is no known efficient algorithm that can solve it in polynomial time for any number of cities.
- The TSP has many applications in real time systems, such as scheduling, routing, logistics, and network design.
- To perform the TSP for the notes of the Design and Analysis of Algorithm Lab, one possible approach is as follows:

  - Represent the notes as nodes in a graph, where the distance between two nodes is the time required to study them.
  - Use a heuristic algorithm, such as nearest neighbor, to find an initial solution that visits all the nodes and returns to the starting point.
  - Use a local search algorithm, such as 2-opt, to improve the solution by swapping pairs of edges and checking if the total distance decreases.
  - Repeat the local search until no further improvement is possible or a time limit is reached.
  - Evaluate the quality of the solution by comparing it with the optimal solution (if known) or a lower bound (such as the minimum spanning tree).
  - Report the solution and its length, as well as the algorithm used and its performance.

- Some possible advantages and disadvantages of this approach are:

  - Advantages: It is relatively simple and fast to implement and can find good solutions for small to medium sized problems.
  - Disadvantages: It is not guaranteed to find the optimal solution and can get stuck in local optima. It may also perform poorly for large or complex problems.



## Find Minimum Spanning Tree using Kruskal’s Algorithm

- A **minimum spanning tree (MST)** of a weighted, connected and undirected graph is a subset of the edges that connects all the vertices together, without any cycles and with the minimum possible total edge weight.
- **Kruskal's algorithm** is a greedy algorithm that finds a MST for a graph.
- The algorithm works as follows     :
  - Sort all the edges in non-decreasing order of their weight.
  - Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
  - Repeat step 2 until there are (V-1) edges in the spanning tree, where V is the number of vertices in the graph.
- To detect if an edge forms a cycle with the spanning tree, we can use a **union-find** data structure that keeps track of the connected components of the graph.
- The time complexity of Kruskal's algorithm is O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices, since the most time consuming operation is sorting the edges .
- The space complexity of Kruskal's algorithm is O(E + V), since we need to store the edges, the spanning tree and the union-find data structure .
- An example of applying Kruskal's algorithm to a graph is shown below:

Kruskal's algorithm example

- The edges are sorted by weight as follows: (7, 6), (8, 2), (6, 5), (0, 1), (2, 5), (8, 6), (2, 3), (7, 8), (0, 7), (1, 2), (3, 4), (4, 5), (1, 7), (3, 5).
- The MST is initially empty. We pick the smallest edge (7, 6) and add it to the MST.
- We pick the next smallest edge (8, 2) and check if it forms a cycle with the MST. Since it does not, we add it to the MST.
- We repeat this process for the remaining edges, skipping those that form cycles, until we have 8 edges in the MST (the graph has 9 vertices).
- The final MST is shown below, with a total weight of 37:

Kruskal's algorithm MST



## Implement N Queen Problem using Backtracking for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- The N Queen problem is a classic example of backtracking, a technique for solving problems recursively by trying to build a solution incrementally, removing those solutions that fail to satisfy the constraints of the problem at any point of time.
- The N Queen problem is to place N queens on an N x N chessboard such that no two queens attack each other. A queen can attack another queen if they are on the same row, column, or diagonal.
- The backtracking algorithm for the N Queen problem works as follows:

  - Start from the first row and place a queen on the first column.
  - Move to the next row and try to place a queen on each column, checking if it is safe to do so. A position is safe if no other queen can attack it from the previous rows.
  - If a safe position is found, place the queen and recursively try to place the rest of the queens on the remaining rows.
  - If no safe position is found on the current row, backtrack to the previous row and move the queen to the next column. Repeat this process until all the queens are placed or all the columns are exhausted.
  - If all the queens are placed, print the solution. Otherwise, report that no solution exists.

- The pseudocode for the backtracking algorithm is given below:

  ```
  function solveNQueen(board, row, n):
    if row == n: // all queens are placed
      print board
      return true
    for col in 0 to n-1: // try each column
      if isSafe(board, row, col, n): // check if the position is safe
        board[row][col] = 1 // place the queen
        if solveNQueen(board, row+1, n): // recursively try the next row
          return true
        board[row][col] = 0 // backtrack and remove the queen
    return false // no solution on this row
  ```

- The function isSafe checks if a queen can be placed on board[row][col] by iterating over the previous rows and checking if there is a queen on the same column, the left diagonal, or the right diagonal. The pseudocode for the function is given below:

  ```
  function isSafe(board, row, col, n):
    for i in 0 to row-1: // check the same column
      if board[i][col] == 1:
        return false
    for i, j in row-1, col-1 to 0, 0: // check the left diagonal
      if board[i][j] == 1:
        return false
    for i, j in row-1, col+1 to 0, n-1: // check the right diagonal
      if board[i][j] == 1:
        return false
    return true // the position is safe
  ```

- The time complexity of the backtracking algorithm is O(N!), where N is the number of queens. This is because there are N possible choices for the first queen, N-1 for the second, N-2 for the third, and so on, resulting in N! permutations. The space complexity is O(N^2), where N is the number of queens. This is because we need to store the board of size N x N and the recursive call stack of depth N.



## Sort a given set of n integer elements using Quick Sort method and compute its time complexity. Run the program for varied values of n> 5000 and record the time taken to sort. Plot a graph of the time taken versus non graph sheet. The elements can be read from a file or can be generated using the random number generator. Demonstrate using Java how the divide and- conquer method works along with its time complexity analysis: worst case, average case and best case.

- Quick Sort is a sorting algorithm that uses the divide and conquer method to partition the array into two subarrays based on a pivot element, such that the elements in the left subarray are smaller than or equal to the pivot and the elements in the right subarray are larger than or equal to the pivot. Then, the algorithm recursively sorts the subarrays until the array is sorted.
- The time complexity of Quick Sort depends on the choice of the pivot element and the distribution of the elements in the array. The best case occurs when the pivot is the median of the array, which results in a balanced partition and a time complexity of O(n log n). The average case also has a time complexity of O(n log n), assuming that the pivot is chosen randomly or by using some heuristic. The worst case occurs when the pivot is the smallest or the largest element of the array, which results in an unbalanced partition and a time complexity of O(n^2).
- To implement Quick Sort in Java, we need to define a method that takes an array, a low index and a high index as parameters, and returns the index of the pivot after partitioning the array. The method can use any strategy to choose the pivot, such as the first element, the last element, the middle element, or a random element. The method can also use a swap method to exchange the elements in the array. The pseudocode of the partition method is as follows:

```
partition(array, low, high):
  pivot = array[low] // choose the first element as the pivot
  i = low + 1 // initialize the index of the first element larger than the pivot
  j = high // initialize the index of the last element smaller than the pivot
  while i <= j: // loop until the indices cross
    while i <= high and array[i] <= pivot: // find the first element larger than the pivot
      i = i + 1
    while j >= low and array[j] > pivot: // find the last element smaller than the pivot
      j = j - 1
    if i < j: // swap the elements if they are out of order
      swap(array, i, j)
  swap(array, low, j) // swap the pivot with the element at j
  return j // return the index of the pivot
```

- To sort the array using Quick Sort, we need to define another method that takes an array, a low index and a high index as parameters, and recursively calls the partition method and itself until the array is sorted. The pseudocode of the quickSort method is as follows:

```
quickSort(array, low, high):
  if low < high: // check if the array has more than one element
    pivot = partition(array, low, high) // partition the array and get the index of the pivot
    quickSort(array, low, pivot - 1) // sort the left subarray
    quickSort(array, pivot + 1, high) // sort the right subarray
```

- To measure the time taken to sort the array using Quick Sort, we need to use the System.nanoTime() method to get the current time in nanoseconds before and after calling the quickSort method, and calculate the difference. We also need to generate an array of n random integers using the Random class or read the elements from a file. The pseudocode of the main method is as follows:

```
main():
  n = input("Enter the size of the array: ") // get the size of the array from the user
  array = new int[n] // create an array of n integers
  random = new Random() // create a random number generator
  for i = 0 to n - 1: // loop through the array
    array[i] = random.nextInt(10000) // generate a random integer between 0 and 9999 and assign it to the array
  // alternatively, read the elements from a file using a Scanner or a BufferedReader
  startTime = System.nanoTime() // get the current time in nanoseconds
  quickSort(array, 0, n - 1) // sort the array using Quick Sort
  endTime = System.nanoTime() // get the current time in nanoseconds

```




## Merge Sort

- Merge sort is a divide-and-conquer algorithm that recursively splits a given array of n elements into two halves, sorts each half, and then merges them back together in sorted order.
- The algorithm can be described as follows:

  - If the array has only one element, return it as it is already sorted.
  - Otherwise, divide the array into two subarrays of equal or nearly equal size.
  - Recursively sort each subarray using merge sort.
  - Merge the two sorted subarrays into one sorted array by comparing the first elements of each subarray and taking the smaller one into the output array, until one of the subarrays is empty, then copy the remaining elements of the other subarray.
- The time complexity of merge sort is O(n log n) in the worst case, average case, and best case, where n is the number of elements in the array. This is because the algorithm always divides the array into two halves, which takes O(log n) steps, and then merges them in O(n) time at each step.
- The following pseudocode illustrates the merge sort algorithm:

  ```
  function merge_sort(array)
    if length(array) <= 1
      return array
    else
      mid = floor(length(array) / 2)
      left = merge_sort(array[0..mid-1])
      right = merge_sort(array[mid..length(array)-1])
      return merge(left, right)
  end function

  function merge(left, right)
    result = empty array
    while left and right are not empty
      if left[0] <= right[0]
        append left[0] to result
        remove left[0] from left
      else
        append right[0] to result
        remove right[0] from right
      end if
    end while
    if left is not empty
      append left to result
    else if right is not empty
      append right to result
    end if
    return result
  end function
  ```

- To run the program for varied values of n > 5000, and record the time taken to sort, one can use a loop to generate random arrays of different sizes, and measure the execution time of the merge sort function using a timer. For example, in Python, one can use the following code:

  ```
  import random
  import time

  # generate a random array of size n
  def generate_array(n):
    array = []
    for i in range(n):
      array.append(random.randint(0, 1000000))
    return array

  # run merge sort on a random array of size n and record the time taken
  def run_merge_sort(n):
    array = generate_array(n)
    start = time.time()
    sorted_array = merge_sort(array)
    end = time.time()
    return end - start

  # run the experiment for different values of n and plot the results
  n_values = [5000, 10000, 20000, 40000, 80000, 160000]
  time_values = []
  for n in n_values:
    time_values.append(run_merge_sort(n))

  # plot the graph of time taken versus n using matplotlib
  import matplotlib.pyplot as plt
  plt.plot(n_values, time_values)
  plt.xlabel('n')
  plt.ylabel('time taken (seconds)')
  plt.title('Merge Sort Time Complexity')
  plt.show()
  ```

- The graph of the time taken versus n on a non graph sheet can be drawn by hand using a ruler and a pencil, or using a software tool such as Microsoft Excel or Google Sheets. The graph should look like a curve that increases gradually as n increases, as shown below:

Merge Sort Graph

- To demonstrate how the divide-and-conquer method works along with its time complexity analysis, one can use an example array and show the steps of the algorithm visually, as shown below:

Merge Sort Example

- The time complexity analysis can be explained as follows:

  - At each level of recursion, the array is divided into two subarrays of half the size, which takes O(1) time.
  - The number of levels of recursion is log n, where n is the size of the array, since the array is halved at each level until it reaches a single element.
  - At each level of recursion, the merge function takes O(n) time to merge the two sorted subarrays into one sorted array, where n is the size of the array at that level.
  - Therefore



## Implement the 0/1 Knapsack problem using (a) Dynamic Programming method (b) Greedy method.

The 0/1 Knapsack problem is a classic optimization problem where we have a set of items, each with a weight and a value, and we want to choose a subset of items that maximizes the total value while keeping the total weight within a given limit. The 0/1 means that we can either take an item or leave it, but not take a fraction of it.

There are two common methods to solve this problem: dynamic programming and greedy method.

### (a) Dynamic Programming method

Dynamic programming is a technique that breaks down a complex problem into smaller and overlapping subproblems, and solves them by reusing the solutions of the subproblems. The idea is to use a table to store the optimal value for each subproblem, and then use the table to construct the final solution.

The steps for the dynamic programming method are:

- Define the subproblems: Let `V[i][w]` be the maximum value that can be obtained by using the first `i` items and a knapsack of capacity `w`. The base case is `V[0][w] = 0` for any `w`, meaning that no items can be taken.
- Define the recurrence relation: For each `i > 0` and `w >= 0`, we have two choices: either take the `i`-th item or leave it. If we take it, we add its value to the optimal value of the subproblem with `i-1` items and `w-wi` capacity, where `wi` is the weight of the `i`-th item. If we leave it, we get the optimal value of the subproblem with `i-1` items and `w` capacity. Therefore, the recurrence relation is:

  `V[i][w] = max(V[i-1][w], vi + V[i-1][w-wi])` if `wi <= w`

  `V[i][w] = V[i-1][w]` otherwise

  where `vi` is the value of the `i`-th item.
- Fill the table: We can fill the table in a bottom-up manner, starting from the base case and following the recurrence relation. The final answer will be `V[n][W]`, where `n` is the number of items and `W` is the knapsack capacity.
- Reconstruct the solution: To find the subset of items that gives the optimal value, we can trace back the table from `V[n][W]` and check which items were taken. If `V[i][w] > V[i-1][w]`, then the `i`-th item was taken, and we reduce the problem to `V[i-1][w-wi]`. Otherwise, the `i`-th item was not taken, and we reduce the problem to `V[i-1][w]`. We repeat this process until we reach the base case.

The pseudocode for the dynamic programming method is:

```
// Input: n = number of items, W = knapsack capacity, w[] = array of item weights, v[] = array of item values
// Output: V[n][W] = maximum value, S[] = array of items taken (1 = taken, 0 = not taken)

// Initialize the table V[][] with 0
for i = 0 to n
  for j = 0 to W
    V[i][j] = 0

// Fill the table using the recurrence relation
for i = 1 to n
  for j = 0 to W
    if w[i] <= j // the item can be taken
      V[i][j] = max(V[i-1][j], v[i] + V[i-1][j-w[i]])
    else // the item cannot be taken
      V[i][j] = V[i-1][j]

// Initialize the solution array S[] with 0
for i = 0 to n
  S[i] = 0

// Trace back the table to find the items taken
i = n
j = W
while i > 0 and j > 0
  if V[i][j] > V[i-1][j] // the item was taken
    S[i] = 1 // mark the item as taken
    j = j - w[i] // reduce the capacity by the item weight
  i = i - 1 // move to the previous item

// Return the maximum value and the solution array
return V[n][W],

```




## From a given vertex in a weighted connected graph, find shortest paths to other vertices using Dijkstra's algorithm.

- Dijkstra's algorithm is a greedy algorithm that finds the shortest path from a given vertex to all other vertices in a weighted graph.
- The algorithm maintains a set of visited vertices and a priority queue of unvisited vertices, where the priority is the current distance from the source vertex.
- The algorithm works as follows:

  - Initialize the distance of the source vertex to zero and the distance of all other vertices to infinity.
  - Mark the source vertex as visited and add it to the priority queue with its distance as the priority.
  - While the priority queue is not empty, do the following:
    - Extract the vertex with the minimum priority from the queue. This is the current vertex.
    - For each neighbor of the current vertex that is not visited, do the following:
      - Calculate the distance to the neighbor by adding the edge weight to the current distance.
      - If the distance to the neighbor is smaller than the previous distance, update the distance and the predecessor of the neighbor.
      - Add the neighbor to the priority queue with its distance as the priority.
    - Mark the current vertex as visited.
  - The algorithm terminates when the priority queue is empty or when the destination vertex is visited.
- The algorithm returns the distance and the predecessor of each vertex, which can be used to reconstruct the shortest path from the source to any other vertex.
- The time complexity of the algorithm is O(E log V), where E is the number of edges and V is the number of vertices, assuming a binary heap is used as the priority queue.
- The space complexity of the algorithm is O(V), where V is the number of vertices, as it requires an array of distances and an array of predecessors for each vertex.



## Find Minimum Cost Spanning Tree of a given connected undirected graph using Kruskal's algorithm. Use Union-Find algorithms in your program.

- A **spanning tree** of a graph is a subgraph that contains all the vertices and is a tree (i.e., has no cycles).
- A **minimum cost spanning tree (MST)** of a graph is a spanning tree that has the minimum possible total edge weight among all the spanning trees of the graph.
- **Kruskal's algorithm** is a greedy algorithm that finds a MST of a given connected undirected graph by sorting the edges in non-decreasing order of their weight and adding them one by one to the spanning tree, as long as they do not create a cycle.
- **Union-Find algorithms** are data structures and algorithms that support two operations: **union** and **find**. Union merges two disjoint sets into one, while find returns the representative element of the set that contains a given element.
- Union-Find algorithms can be used to implement **disjoint-set data structures**, which are collections of disjoint sets that support efficient union and find operations. Disjoint-set data structures can be used to keep track of the connected components of a graph and to detect cycles.
- The pseudocode of Kruskal's algorithm using Union-Find algorithms is as follows:

```
Kruskal(G):
  Input: A connected undirected graph G = (V, E) with edge weights
  Output: A MST of G

  Initialize an empty set T to store the edges of the MST
  Initialize a disjoint-set data structure S with each vertex in V as a singleton set
  Sort the edges in E in non-decreasing order of their weight
  For each edge (u, v) in E, in sorted order:
    If S.find(u) != S.find(v): # u and v belong to different sets, so adding (u, v) will not create a cycle
      Add (u, v) to T
      S.union(u, v) # merge the sets containing u and v
  Return T
```
- The time complexity of Kruskal's algorithm using Union-Find algorithms is O(E log E + E log V), where E is the number of edges and V is the number of vertices in the graph. The first term is for sorting the edges, and the second term is for performing the union and find operations.



## Find Minimum Cost Spanning Tree of a given undirected graph using Prim’s algorithm.

- A **spanning tree** of a graph is a subgraph that contains all the vertices and is a tree (i.e., no cycles).
- A **minimum cost spanning tree (MCST)** of a graph is a spanning tree that has the minimum possible total edge weight among all the spanning trees of the graph.
- **Prim's algorithm** is a greedy algorithm that finds a MCST of a given undirected graph.
- The algorithm works as follows:
  - Start with an arbitrary vertex as the root of the tree.
  - Repeat until all the vertices are in the tree:
    - Find the minimum weight edge that connects a vertex in the tree to a vertex not in the tree.
    - Add that edge and the new vertex to the tree.
- The algorithm can be implemented using a priority queue to store the edges that connect the vertices in the tree to the vertices not in the tree, and extract the minimum weight edge at each step.
- The time complexity of the algorithm is O(E log V), where E is the number of edges and V is the number of vertices in the graph.
- The algorithm can be illustrated by the following example:

Example of Prim's algorithm

- The graph has 9 vertices and 14 edges, and the algorithm starts with vertex A as the root of the tree.
- The algorithm adds the edges AB, BC, CD, DE, EF, FG, GH, and HI to the tree, in that order, and the final MCST has a total weight of 37.



## Write programs to (a) Implement All-Pairs Shortest Paths problem using Floyd's algorithm. (b) Implement Travelling Sales Person problem using Dynamic programming. for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

### (a) Implement All-Pairs Shortest Paths problem using Floyd's algorithm.

- The All-Pairs Shortest Paths problem is to find the shortest distance between every pair of vertices in a weighted graph, possibly with negative edge weights but no negative cycles.
- Floyd's algorithm, also known as the Floyd-Warshall algorithm, is an algorithm that solves this problem by using dynamic programming.
- The algorithm works by iteratively improving an estimate of the shortest distance between any two vertices, based on the previous estimate and the distance of a possible intermediate vertex.
- The algorithm maintains a matrix D of size n x n, where n is the number of vertices in the graph, and D[i][j] is the current estimate of the shortest distance from vertex i to vertex j.
- Initially, D[i][j] is set to the weight of the edge (i, j) if it exists, or infinity otherwise. D[i][i] is set to zero for all i.
- The algorithm then performs n iterations, where in each iteration k, it updates D[i][j] for all i and j by checking if going through vertex k can improve the current estimate. That is, D[i][j] is set to the minimum of D[i][j] and D[i][k] + D[k][j].
- After n iterations, D[i][j] will contain the shortest distance from i to j, or infinity if there is no path from i to j.
- The algorithm can also be used to find the transitive closure of a graph, by replacing the minimum operation with a logical OR, and the addition operation with a logical AND.
- The algorithm has a time complexity of O(n^3), where n is the number of vertices in the graph, and a space complexity of O(n^2), where n is the number of vertices in the graph.

- A possible pseudocode for the algorithm is:

```
// Input: A weighted graph G with n vertices
// Output: A matrix D of size n x n, where D[i][j] is the shortest distance from i to j in G
Floyd(G):
  // Initialize D with the edge weights or infinity
  for i = 1 to n:
    for j = 1 to n:
      if i == j:
        D[i][j] = 0
      else if (i, j) is an edge in G:
        D[i][j] = weight of (i, j)
      else:
        D[i][j] = infinity
  // Perform n iterations of updating D
  for k = 1 to n:
    for i = 1 to n:
      for j = 1 to n:
        // Check if going through k can improve the current estimate
        D[i][j] = min(D[i][j], D[i][k] + D[k][j])
  // Return D
  return D
```



## Design and implement to find a subset of a given set S = {Sl, S2,.....,Sn} of n positive integers whose SUM is equal to a given positive integer d. For example, if S ={1, 2, 5, 6, 8} and d= 9, there are two solutions {1,2,6}and {1,8}. Display a suitable message, if the given problem instance doesn't have a solution. for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- This problem is an example of the **subset sum problem**, which is a special case of the **knapsack problem**. The subset sum problem is to find a subset of a given set of numbers that adds up to a given target number. The knapsack problem is to find a subset of items with given weights and values that maximizes the total value without exceeding the capacity of the knapsack.
- The subset sum problem is **NP-complete**, which means that there is no known efficient algorithm that can solve it in polynomial time for any input size. However, there are some algorithms that can solve it in **pseudo-polynomial time**, which means that they are polynomial in the input size and the target number. One such algorithm is the **dynamic programming** approach, which uses a two-dimensional array to store the possible sums that can be obtained from the subsets of the input set.
- The dynamic programming algorithm works as follows:
  - Let S = {s1, s2, ..., sn} be the input set of n positive integers, and let d be the target sum.
  - Create a boolean array T[n+1][d+1], where T[i][j] indicates whether there is a subset of {s1, s2, ..., si} that adds up to j.
  - Initialize T[0][0] to true, and T[0][j] to false for all j > 0. This means that the empty set can only add up to zero, and no other sum.
  - For each i from 1 to n, do the following:
    - For each j from 0 to d, do the following:
      - If T[i-1][j] is true, then set T[i][j] to true. This means that if there is a subset of {s1, s2, ..., si-1} that adds up to j, then there is also a subset of {s1, s2, ..., si} that adds up to j, by simply excluding si from the subset.
      - If T[i-1][j] is false, then check if j >= si. If yes, then set T[i][j] to T[i-1][j-si]. This means that if there is a subset of {s1, s2, ..., si-1} that adds up to j-si, then there is also a subset of {s1, s2, ..., si} that adds up to j, by simply including si in the subset. If no, then set T[i][j] to false. This means that there is no subset of {s1, s2, ..., si} that adds up to j, since si is larger than j.
  - After filling the array T, check the value of T[n][d]. If it is true, then there is a solution to the problem. If it is false, then there is no solution to the problem.
  - To find the actual subsets that add up to d, we can backtrack from T[n][d] and trace the choices that were made in the array. For each i from n to 1, do the following:
    - If T[i][d] is true and T[i-1][d] is false, then si is part of the solution. Add si to the subset, and update d to d-si.
    - If T[i][d] is true and T[i-1][d] is true, then si may or may not be part of the solution. We can branch into two cases: one where we include si in the subset, and one where we exclude si from the subset. In both cases, we update d accordingly and continue the backtracking.
    - If T[i][d] is false, then si is not part of the solution. We skip si and continue the backtracking.
  - The backtracking process will generate all the possible subsets that add up to d, or display a suitable message if there is no solution.
- The time complexity of the dynamic programming algorithm is O(n*d), where n is the size of the input set and d is the target



## Design and implement to find all Hamiltonian Cycles in a connected undirected Graph G of n vertices using backtracking principle.

- A Hamiltonian cycle is a cycle in a graph that visits every vertex exactly once and returns to the starting vertex.
- A graph is connected if there is a path between any pair of vertices.
- A graph is undirected if the edges have no direction, meaning that (u, v) and (v, u) are the same edge.
- Backtracking is a general algorithmic technique that tries different solutions recursively until a valid solution is found or all possibilities are exhausted.
- To find all Hamiltonian cycles in a connected undirected graph G of n vertices using backtracking, we can use the following algorithm:

  - Create an array path of size n, where path[i] will store the i-th vertex in the cycle.
  - Initialize path[0] to any vertex in G, and mark it as visited.
  - Define a recursive function hamCycle(path, pos) that takes the current path and the position of the last vertex added to the path as parameters.
  - If pos == n, check if there is an edge from path[n-1] to path[0]. If yes, then we have found a Hamiltonian cycle and we can print or store the path. If no, then return false.
  - For each vertex v in G that is adjacent to path[pos-1] and not visited, do the following:
    - Mark v as visited and add it to path[pos].
    - Call hamCycle(path, pos+1) recursively. If it returns true, then return true.
    - Unmark v as visited and remove it from path[pos].
  - If no vertex can be added to the path, then return false.

