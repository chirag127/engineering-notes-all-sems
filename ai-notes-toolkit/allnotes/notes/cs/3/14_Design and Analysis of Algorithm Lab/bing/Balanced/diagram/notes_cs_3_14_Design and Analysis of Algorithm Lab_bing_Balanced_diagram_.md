

## Program for Recursive Binary & Linear Search for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- A recursive binary search is an algorithm that searches for a target value in a sorted array by repeatedly dividing the array into two halves and comparing the middle element with the target.
- A recursive linear search is an algorithm that searches for a target value in an array by checking each element from left to right until the target is found or the end of the array is reached.
- Both algorithms use recursion, which is a technique of solving a problem by breaking it down into smaller subproblems of the same type and solving them using the same algorithm.
- The pseudocode for the recursive binary search is:

```
function binary_search(array, low, high, target)
  if low > high then
    return -1 // target not found
  end if
  mid = (low + high) / 2 // integer division
  if array[mid] == target then
    return mid // target found at index mid
  else if array[mid] > target then
    return binary_search(array, low, mid - 1, target) // search in the left half
  else
    return binary_search(array, mid + 1, high, target) // search in the right half
  end if
end function
```

- The pseudocode for the recursive linear search is:

```
function linear_search(array, index, target)
  if index >= array.length then
    return -1 // target not found
  end if
  if array[index] == target then
    return index // target found at index
  else
    return linear_search(array, index + 1, target) // search in the next element
  end if
end function
```

- The time complexity of the recursive binary search is O(log n), where n is the size of the array, because it halves the search space in each recursive call.
- The time complexity of the recursive linear search is O(n), where n is the size of the array, because it checks each element in the array once.
- The space complexity of both algorithms is O(log n), where n is the size of the array, because of the recursive call stack.



## Program for Heap Sort

Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure to sort a list of elements. It works by dividing the list into two regions: a sorted region and an unsorted region. It iteratively extracts the largest element from the unsorted region and inserts it into the sorted region, until the list is fully sorted. Heap sort is an in-place algorithm, meaning it does not require extra space to store the sorted elements. However, it is not a stable algorithm, meaning it does not preserve the relative order of equal elements.

The heap sort algorithm can be divided into two steps:

1. Build a max heap from the input list. A max heap is a complete binary tree where each node is greater than or equal to its children. The root node is the largest element in the heap. The max heap can be built using a bottom-up approach, starting from the last non-leaf node and sifting it down until it satisfies the heap property. This can be done in O(n) time, where n is the number of elements in the list.
2. Repeatedly swap the root node with the last node in the heap, and reduce the heap size by one. This moves the largest element to the end of the list, and creates a new root node that may violate the heap property. To restore the heap property, sift down the new root node until it is in the correct position. This can be done in O(log n) time, where n is the current heap size. Repeat this step until the heap size is one, which means the list is fully sorted. This can be done in O(n log n) time, where n is the number of elements in the list.

The total time complexity of heap sort is O(n log n), where n is the number of elements in the list. The space complexity is O(1), as no extra space is required.

Here is a pseudocode for heap sort:

```
heap_sort(list):
  n = length(list)
  build_max_heap(list, n) // build a max heap from the list
  for i from n-1 to 1: // iterate from the last node to the second node
    swap(list[0], list[i]) // swap the root node with the last node
    n = n - 1 // reduce the heap size by one
    max_heapify(list, 0, n) // restore the heap property of the new root node

build_max_heap(list, n):
  for i from floor(n/2) - 1 to 0: // iterate from the last non-leaf node to the root node
    max_heapify(list, i, n) // sift down the node until it satisfies the heap property

max_heapify(list, i, n):
  largest = i // assume the current node is the largest
  left = 2*i + 1 // get the index of the left child
  right = 2*i + 2 // get the index of the right child
  if left < n and list[left] > list[largest]: // if the left child is larger than the current node
    largest = left // update the largest index
  if right < n and list[right] > list[largest]: // if the right child is larger than the current node
    largest = right // update the largest index
  if largest != i: // if the current node is not the largest
    swap(list[i], list[largest]) // swap the current node with the largest child
    max_heapify(list, largest, n) // recursively sift down the swapped child node
```

Here is an example of heap sort on the list [4, 10, 3, 5, 1]:

Heap sort example

Source: [Heapsort - Wikipedia](https://en.wikipedia.org/wiki/Heapsort)



## Program for Merge Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Merge sort is a divide-and-conquer algorithm that recursively splits an array into two halves and then merges them in sorted order.
- The algorithm can be described as follows:

  - If the array has only one element, return it as it is already sorted.
  - Otherwise, divide the array into two equal or nearly equal parts and call merge sort on each part.
  - Merge the two sorted subarrays by comparing the first elements of each subarray and taking the smaller one into the output array. Repeat until one of the subarrays is empty, then copy the remaining elements of the other subarray into the output array.
  - Return the output array as the sorted array.

- The time complexity of merge sort is O(n log n) in the worst case, where n is the number of elements in the array. This is because the algorithm divides the array into log n levels, and each level takes O(n) time to merge the subarrays.
- The space complexity of merge sort is O(n) in the worst case, as the algorithm requires an auxiliary array of the same size as the input array to store the output array.
- Merge sort is a stable sorting algorithm, meaning that it preserves the relative order of equal elements in the input array.
- Merge sort is suitable for sorting large arrays or lists that are stored on disk or in external memory, as it can efficiently access sequential data and minimize the number of disk accesses.
- Here is an example of a C program that implements merge sort:

```c
// A function to merge two sorted subarrays
void merge(int arr[], int left, int mid, int right) {
  // Find the sizes of the subarrays
  int n1 = mid - left + 1;
  int n2 = right - mid;

  // Create temporary arrays to store the subarrays
  int L[n1], R[n2];

  // Copy the data to the temporary arrays
  for (int i = 0; i < n1; i++)
    L[i] = arr[left + i];
  for (int j = 0; j < n2; j++)
    R[j] = arr[mid + 1 + j];

  // Initialize indices for the subarrays and the output array
  int i = 0, j = 0, k = left;

  // Merge the subarrays by comparing the first elements of each subarray
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

  // Copy the remaining elements of L[], if any
  while (i < n1) {
    arr[k] = L[i];
    i++;
    k++;
  }

  // Copy the remaining elements of R[], if any
  while (j < n2) {
    arr[k] = R[j];
    j++;
    k++;
  }
}

// A function to implement merge sort
void mergeSort(int arr[], int left, int right) {
  // Base case: if the array has only one element, return
  if (left >= right)
    return;

  // Find the middle point of the array
  int mid = (left + right) / 2;

  // Recursively sort the left and right halves of the array
  mergeSort(arr, left, mid);
  mergeSort(arr, mid + 1, right);

  // Merge the sorted halves
  merge(arr, left, mid, right);
}

// A function to print an array
void printArray(int arr[], int size) {
  for (int i = 0; i < size; i++)
    printf("%d ", arr[i]);
  printf("\n");
}

// A main function to test the program
int main() {
  // Create an example array
  int arr[] = {12, 11, 13, 5, 6, 7};
  int size = sizeof(arr) / sizeof(arr[0]);

  // Print the original array
  printf("Given array is \n");
  printArray(arr, size);

  // Sort the array using merge sort
  mergeSort(arr, 0, size - 1);

  // Print the sorted array
  printf("\nSorted array is \n");
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

- Here is a pseudocode for selection sort:

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

- Here is a diagram that illustrates how selection sort works on an example array [64, 25, 12, 22, 11]:

Selection sort diagram

- The diagram shows the sorted subarray in green and the unsorted subarray in red. The minimum element of the unsorted subarray is highlighted in yellow. The algorithm swaps the minimum element with the leftmost element of the unsorted subarray in each iteration. The algorithm terminates when the unsorted subarray becomes empty.



Hello, I am Sydney, your AI assistant. I can help you with your topic.

## Program for Insertion Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Insertion sort is a simple sorting algorithm that works by inserting each element of the array into its correct position in a sorted subarray.
- The algorithm starts with the first element as the sorted subarray and then iterates over the remaining elements, inserting each one into the sorted subarray in the right place.
- The algorithm can be implemented using a loop or a recursion.
- The algorithm has a time complexity of O(n^2) in the worst case, where n is the number of elements in the array.
- The algorithm is stable, meaning that it preserves the relative order of equal elements.
- The algorithm is adaptive, meaning that it performs better on partially sorted arrays.
- The algorithm is in-place, meaning that it does not require extra space to sort the array.

Here is a pseudocode for the insertion sort algorithm using a loop:

```
insertion_sort(array)
  for i from 1 to length(array) - 1
    key = array[i]
    j = i - 1
    while j >= 0 and array[j] > key
      array[j + 1] = array[j]
      j = j - 1
    array[j + 1] = key
  return array
```

Here is a pseudocode for the insertion sort algorithm using a recursion:

```
insertion_sort(array, n)
  if n <= 1
    return array
  insertion_sort(array, n - 1)
  key = array[n - 1]
  j = n - 2
  while j >= 0 and array[j] > key
    array[j + 1] = array[j]
    j = j - 1
  array[j + 1] = key
  return array
```

Here is a diagram to illustrate the insertion sort algorithm:

Insertion Sort Diagram



## Program for Quick Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Quick sort is a sorting algorithm that uses the **divide and conquer** strategy to partition the array into two subarrays and recursively sort them.
- The main idea of quick sort is to choose a **pivot** element from the array and move all the elements that are smaller than the pivot to the left of the pivot and all the elements that are larger than the pivot to the right of the pivot.
- The pivot can be chosen in different ways, such as the first element, the last element, the median element, or a random element of the array.
- After partitioning the array, the pivot is placed in its correct position in the sorted array and the subarrays on the left and right of the pivot are sorted recursively using the same procedure.
- The algorithm can be implemented using the following pseudocode:

```
procedure quick_sort(A, low, high)
  if low < high then
    pivot_index = partition(A, low, high) // partition the array and return the pivot index
    quick_sort(A, low, pivot_index - 1) // sort the left subarray
    quick_sort(A, pivot_index + 1, high) // sort the right subarray
  end if
end procedure

procedure partition(A, low, high)
  pivot = A[high] // choose the last element as the pivot
  i = low - 1 // initialize the index of the smaller element
  for j = low to high - 1 do // loop through the array
    if A[j] <= pivot then // if the current element is smaller than or equal to the pivot
      i = i + 1 // increment the index of the smaller element
      swap A[i] and A[j] // swap the current element with the smaller element
    end if
  end for
  swap A[i + 1] and A[high] // swap the pivot with the element next to the smaller element
  return i + 1 // return the pivot index
end procedure
```

- The time complexity of quick sort is **O(n log n)** on average and **O(n^2)** in the worst case, where n is the number of elements in the array.
- The space complexity of quick sort is **O(log n)**, which is the depth of the recursion stack.
- Quick sort is an **in-place** and **unstable** sorting algorithm, meaning that it does not require extra space to store the sorted array and it does not preserve the relative order of equal elements.
- Quick sort is suitable for sorting large arrays that can fit in memory and that have a good distribution of elements. It is not suitable for sorting arrays that are already sorted, nearly sorted, or have many duplicate elements, as these cases can lead to the worst-case performance of quick sort.



## Knapsack Problem using Greedy Solution

The knapsack problem is a problem of finding the optimal way to fill a knapsack with a given capacity and a set of items, each with a value and a weight. The goal is to maximize the total value of the items in the knapsack without exceeding the capacity.

There are two variants of the knapsack problem: the 0-1 knapsack problem and the fractional knapsack problem. In the 0-1 knapsack problem, each item can either be taken or left out, while in the fractional knapsack problem, each item can be taken partially or fully.

The greedy solution is a heuristic algorithm that works well for the fractional knapsack problem, but not for the 0-1 knapsack problem. The greedy solution is based on the following steps   :

- Sort the items by their value-to-weight ratio in descending order.
- Start with an empty knapsack and iterate over the sorted items.
- For each item, if the knapsack can accommodate the whole item, take it fully and update the knapsack value and weight. Otherwise, if the knapsack can accommodate a fraction of the item, take that fraction and fill the knapsack completely. Stop the iteration.
- Return the final knapsack value and the items taken.

The greedy solution has a time complexity of O(n log n), where n is the number of items, since the sorting step dominates the iteration step. The greedy solution is optimal for the fractional knapsack problem, since it always takes the item with the highest value-to-weight ratio at each step, and thus maximizes the value per unit of weight. However, the greedy solution is not optimal for the 0-1 knapsack problem, since it may miss some combinations of items that have a higher value than the greedy choice.

An example of the greedy solution for the fractional knapsack problem is shown below:

| Item | Value | Weight | Value/Weight |
|------|-------|--------|--------------|
| A    | 60    | 10     | 6            |
| B    | 100   | 20     | 5            |
| C    | 120   | 30     | 4            |

The knapsack capacity is 50 units. The greedy solution sorts the items by their value-to-weight ratio and obtains the following order: A, B, C. The greedy solution then takes the following steps:

- Take item A fully, since the knapsack can accommodate it. The knapsack value is 60 and the knapsack weight is 10.
- Take item B fully, since the knapsack can accommodate it. The knapsack value is 160 and the knapsack weight is 30.
- Take 2/3 of item C, since the knapsack can only accommodate 20 units of weight. The knapsack value is 240 and the knapsack weight is 50.
- Stop the iteration, since the knapsack is full.

The final knapsack value is 240 and the items taken are A, B, and 2/3 of C. This is the optimal solution for the fractional knapsack problem.



## Perform Travelling Salesman Problem for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- The Travelling Salesman Problem (TSP) is a classic optimization problem that asks for the shortest possible route that visits each city exactly once and returns to the starting point.
- The TSP can be modeled as a graph, where the cities are the nodes and the distances between them are the edges. The goal is to find a Hamiltonian cycle (a cycle that visits each node exactly once) with the minimum total edge weight.
- The TSP is an NP-hard problem, meaning that there is no known efficient algorithm that can solve it in polynomial time. However, there are some approximation algorithms and heuristics that can find near-optimal solutions in reasonable time.
- One of the most common heuristics for the TSP is the nearest neighbor algorithm, which starts from a random city and repeatedly visits the closest unvisited city until all cities are visited. This algorithm is fast and easy to implement, but it can get stuck in local optima and produce suboptimal solutions.
- Another heuristic for the TSP is the 2-opt algorithm, which starts from an initial tour (such as the one obtained by the nearest neighbor algorithm) and iteratively improves it by swapping two edges that cross each other. This algorithm can reduce the length of the tour by eliminating unnecessary crossings, but it is not guaranteed to find the optimal solution.
- A more sophisticated algorithm for the TSP is the branch and bound algorithm, which uses a tree structure to explore the possible solutions. The algorithm maintains a lower bound and an upper bound for the optimal tour length, and prunes the branches that cannot improve the current best solution. The algorithm terminates when the lower bound and the upper bound are equal, or when the time limit is reached. This algorithm can find the optimal solution or a very close approximation, but it can be very time-consuming and memory-intensive for large instances.
- The TSP can be applied to various real-world scenarios, such as planning the routes for delivery trucks, scheduling flights for airlines, or designing printed circuit boards. The TSP can also be used as a benchmark for testing the performance of different optimization algorithms and techniques.
- The notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System should include the following topics:

  - The definition and formulation of the TSP as a graph problem.
  - The complexity and NP-hardness of the TSP and its variations.
  - The implementation and analysis of the nearest neighbor, 2-opt, and branch and bound algorithms for the TSP.
  - The advantages and disadvantages of each algorithm and heuristic for the TSP.
  - The applications and examples of the TSP in real-world scenarios.
  - The comparison and evaluation of the different algorithms and heuristics for the TSP on various instances and metrics.



## Find Minimum Spanning Tree using Kruskal’s Algorithm

- A **minimum spanning tree (MST)** of a weighted, connected and undirected graph is a subset of the edges that connects all the vertices together, without any cycles and with the minimum possible total edge weight.
- **Kruskal's algorithm** is a greedy algorithm that finds a MST for a graph. It works as follows   :
  - Sort all the edges in non-decreasing order of their weight.
  - Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
  - Repeat step 2 until there are (V-1) edges in the spanning tree, where V is the number of vertices in the graph.
- To detect if an edge forms a cycle with the spanning tree, we can use a **union-find** data structure that keeps track of the connected components of the graph.
- The time complexity of Kruskal's algorithm is O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices, since the most expensive part is sorting the edges.
- The space complexity of Kruskal's algorithm is O(E + V), since we need to store the edges, the spanning tree and the union-find data structure.
- Here is an example of applying Kruskal's algorithm to a graph:

Kruskal's algorithm example

- The edges are sorted by weight as follows: (7, 6), (8, 2), (6, 5), (0, 1), (2, 5), (8, 6), (2, 3), (7, 8), (0, 7), (1, 2), (3, 4), (4, 5), (1, 7), (3, 5).
- The MST is initially empty. We pick the smallest edge (7, 6) and add it to the MST.
- We pick the next smallest edge (8, 2) and check if it forms a cycle with the MST. Since it does not, we add it to the MST.
- We repeat this process for the remaining edges, skipping those that form cycles, until we have 8 edges in the MST (the graph has 9 vertices).
- The final MST is shown below, with a total weight of 37:

Kruskal's algorithm MST



Hello, I am Sydney, your AI assistant. I can help you with your query.

## Implement N Queen Problem using Backtracking for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- The N Queen problem is a classic example of a combinatorial optimization problem, where the goal is to place N queens on an N x N chessboard, such that no two queens can attack each other.
- A queen can attack another queen if they are on the same row, column, or diagonal.
- One way to solve this problem is to use backtracking, which is a technique of exploring all possible solutions by making a sequence of choices, and then undoing some of the choices if they lead to a dead end or a contradiction.
- The basic idea of backtracking is to use a recursive function that tries to place a queen in each column, starting from the leftmost column.
- For each column, the function checks if there is a safe row to place the queen, i.e., a row that does not conflict with any of the previously placed queens.
- If there is a safe row, the function places the queen there, and then moves on to the next column.
- If there is no safe row, the function backtracks, i.e., removes the queen from the current column, and tries a different row in the previous column.
- The function repeats this process until all the columns are filled with queens, or until it reaches the first column and finds no safe row to place the queen.
- If the function succeeds in placing all the queens, it returns true, and prints the solution. Otherwise, it returns false, and indicates that there is no solution.

- Here is a pseudocode of the backtracking algorithm for the N Queen problem:

```
// A global array to store the positions of the queens
// queen[i] = j means there is a queen at row j and column i
int queen[N]

// A function to check if a queen can be placed at row r and column c
// It returns true if there is no conflict, and false otherwise
bool isSafe(int r, int c)
  // Loop through all the columns from 0 to c-1
  for i = 0 to c-1
    // Check if there is a queen at row r or the same diagonal as (r,c)
    if queen[i] == r or abs(queen[i] - r) == abs(i - c)
      // There is a conflict, return false
      return false
  // There is no conflict, return true
  return true

// A recursive function to solve the N Queen problem
// It takes the current column c as a parameter, and returns true if a solution is found, and false otherwise
bool solveNQueen(int c)
  // Base case: if all the columns are filled, a solution is found
  if c == N
    // Print the solution
    for i = 0 to N-1
      print queen[i]
    // Return true
    return true
  // Recursive case: try to place a queen in each row of the current column
  for r = 0 to N-1
    // Check if the row is safe
    if isSafe(r, c)
      // Place the queen at row r and column c
      queen[c] = r
      // Recursively try to place the queens in the next columns
      if solveNQueen(c+1)
        // A solution is found, return true
        return true
      // No solution is found, backtrack and remove the queen from row r and column c
      queen[c] = -1
  // No solution is found for the current column, return false
  return false
```

- To start the algorithm, we call the function solveNQueen(0), which tries to place a queen in the first column.
- The time complexity of the backtracking algorithm is O(N!), where N is the size of the chessboard. This is because in the worst case, the algorithm has to try all possible permutations of the rows to place the queens.
- The space complexity of the backtracking algorithm is O(N), where N is the size of the chessboard. This is because the algorithm uses a global array of size N to store the positions of the queens, and a recursive stack of size N to store the function calls.



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is the content I have written for you in markdown format:

## Sort a given set of n integer elements using Quick Sort method and compute its time complexity.

- Quick Sort is a sorting algorithm that uses the **divide and conquer** method to sort a given array of n elements.
- The basic idea of Quick Sort is to choose a **pivot** element from the array, and partition the array into two subarrays: one with elements less than or equal to the pivot, and one with elements greater than the pivot.
- The pivot element is then placed in its correct position in the sorted array, and the subarrays are recursively sorted using the same method.
- The algorithm can be implemented as follows in Java:

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
  // Swap the pivot element with the element at i + 1
  swap(arr, i + 1, high);
  // Return the index of the pivot element
  return i + 1;
}

// A function to sort the array using Quick Sort
public static void quickSort(int[] arr, int low, int high) {
  // Base case: if the array has one or zero elements, it is already sorted
  if (low < high) {
    // Partition the array around a pivot element and get its index
    int pi = partition(arr, low, high);
    // Recursively sort the left subarray
    quickSort(arr, low, pi - 1);
    // Recursively sort the right subarray
    quickSort(arr, pi + 1, high);
  }
}
```

- To compute the time complexity of Quick Sort, we need to analyze the number of comparisons and swaps performed by the algorithm in the worst case, average case and best case scenarios.
- The worst case scenario occurs when the pivot element is always the smallest or the largest element in the array, which leads to an unbalanced partitioning of the array. In this case, the algorithm performs **O(n^2)** comparisons and swaps, where n is the number of elements in the array.
- The average case scenario occurs when the pivot element is chosen randomly or by using some heuristic, which leads to a balanced partitioning of the array. In this case, the algorithm performs **O(n log n)** comparisons and swaps, where n is the number of elements in the array.
- The best case scenario occurs when the pivot element is always the median of the array, which leads to an optimal partitioning of the array. In this case, the algorithm performs **O(n log n)** comparisons and swaps, where n is the number of elements in the array.
- To run the program for varied values of n > 5000 and record the time taken to sort, we can use the following code snippet in Java:

```java
// A function to generate an array of random integers
public static int[] generateRandomArray(int n) {
  // Create a new array of size n
  int[] arr = new int[n];
  // Loop through the array
  for (int i = 0; i < n; i++) {
    // Generate a random integer between 1 and 10000 and assign it to the array element
    arr[i] = (int) (Math.random() * 10000) + 1;
  }
  // Return the array
  return arr;
}

// A function to measure the time taken to sort an array using Quick Sort
public static long measureQuickSortTime(int[] arr) {
  // Get the current time in milliseconds before sorting
  long startTime = System.currentTimeMillis();
  // Sort the array using Quick Sort
  quickSort(arr, 0, arr.length - 1);

```




## Sort a given set of n integer elements using Merge Sort method and compute its time complexity.

- Merge sort is a sorting algorithm that works by dividing an array of data into smaller subarrays, sorting each subarray, and then merging the sorted subarrays back together to form the final sorted array.
- It is a divide-and-conquer algorithm, which means that it breaks a complicated problem down into smaller problems that are easier to solve.
- The algorithm can be described as follows:

  - Find the middle point of the array and divide it into two halves.
  - Recursively sort the left half and the right half of the array using merge sort.
  - Merge the two sorted halves into one sorted array using a helper function.

- The time complexity of merge sort depends on the number of comparisons and data movements involved in the algorithm.
- The worst-case time complexity of merge sort is O(n log n), where n is the number of elements in the array. This is because the algorithm divides the array into log n levels, and each level requires O(n) time to merge the subarrays .
- The average-case time complexity of merge sort is also O(n log n), assuming that the input array is randomly ordered and the comparisons are equally likely to be true or false.
- The best-case time complexity of merge sort is O(n log n), when the input array is already sorted or nearly sorted. This is because the algorithm still needs to divide the array into log n levels, and each level requires O(n) time to merge the subarrays, even if no data movement is needed.
- To run the program for varied values of n > 5000, and record the time taken to sort, one can use a loop to generate random arrays of different sizes, and measure the execution time of the merge sort function using a timer or a clock function.
- To plot a graph of the time taken versus n on a graph sheet, one can use a spreadsheet software or a graphing tool to create a scatter plot or a line chart, with n as the x-axis and time as the y-axis. The graph should show a roughly linear relationship between n and time, with a slope of log n.
- To demonstrate how the divide-and-conquer method works along with its time complexity analysis, one can use an example array and show the steps of the algorithm using a tree diagram or a table, and explain how the number of levels, subarrays, comparisons, and data movements affect the running time of the algorithm. For example, consider the following array of 8 elements:

  ```
  [38, 27, 43, 3, 9, 82, 10, 5]
  ```

  The merge sort algorithm can be illustrated as follows:

  ```
  Level 0: [38, 27, 43, 3, 9, 82, 10, 5] // divide the array into two halves
  Level 1: [38, 27, 43, 3] [9, 82, 10, 5] // divide each half into two halves
  Level 2: [38, 27] [43, 3] [9, 82] [10, 5] // divide each quarter into two halves
  Level 3: [38] [27] [43] [3] [9] [82] [10] [5] // each subarray has one element, no more division
  Level 4: [27, 38] [3, 43] [9, 82] [5, 10] // merge each pair of subarrays by comparing and moving elements
  Level 5: [3, 27, 38, 43] [5, 9, 10, 82] // merge each pair of subarrays by comparing and moving elements
  Level 6: [3, 5, 9, 10, 27, 38, 43, 82] // merge the final two subarrays by comparing and moving elements
  ```

  The time complexity analysis can be done as follows:

  - The algorithm divides the array into log n = log 8 = 3 levels, where each level has 2^k subarrays, where k is the level number starting from 0.
  - Each level requires O(n) time to merge the subarrays, where n is the number of elements in the array. This



## Implement the 0/1 Knapsack problem using (a) Dynamic Programming method (b) Greedy method

The 0/1 Knapsack problem is a maximization problem in which we are given a set of items, each with a weight and a value, and we have to determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.

### (a) Dynamic Programming method

Dynamic Programming (DP) is an algorithmic paradigm that solves a problem by breaking it down into smaller subproblems and storing the results of these subproblems in a table to avoid recomputation. DP is suitable for problems that have overlapping subproblems and optimal substructure properties.

To solve the 0/1 Knapsack problem using DP, we can follow these steps:

- Define a 2D array `K[n+1][W+1]` where `n` is the number of items and `W` is the weight limit. `K[i][j]` will store the maximum value that can be obtained by using items from `1` to `i` with a weight limit of `j`.
- Initialize the first row and the first column of `K` to `0`, since no item or no weight can give any value.
- For each item `i` from `1` to `n`, do the following:
  - For each weight `j` from `1` to `W`, do the following:
    - If the weight of item `i` is less than or equal to `j`, then compare the value of including item `i` or excluding item `i` in the solution. The value of including item `i` is `K[i-1][j-wi] + pi`, where `wi` and `pi` are the weight and value of item `i`, respectively. The value of excluding item `i` is `K[i-1][j]`. Choose the maximum of these two values and store it in `K[i][j]`.
    - If the weight of item `i` is greater than `j`, then the value of `K[i][j]` is the same as the value of `K[i-1][j]`, since item `i` cannot be included in the solution.
- Return the value of `K[n][W]` as the final answer.

The time complexity of this algorithm is `O(nW)` and the space complexity is `O(nW)`.

### (b) Greedy method

Greedy method is an algorithmic paradigm that makes the locally optimal choice at each stage with the hope of finding a global optimum. Greedy method is suitable for problems that have greedy choice property and optimal substructure property.

To solve the 0/1 Knapsack problem using Greedy method, we can follow these steps:

- Sort the items in decreasing order of their value/weight ratio, which is also called the profit density.
- Initialize the total value to `0` and the remaining weight to `W`.
- For each item `i` from `1` to `n`, do the following:
  - If the weight of item `i` is less than or equal to the remaining weight, then include item `i` in the solution, add its value to the total value, and subtract its weight from the remaining weight.
  - If the weight of item `i` is greater than the remaining weight, then break the loop and return the total value as the final answer.

The time complexity of this algorithm is `O(n log n)` and the space complexity is `O(1)`.

However, the Greedy method may not always give an optimal solution for the 0/1 Knapsack problem, since it does not consider the whole problem, but only the current choice . For example, consider the following instance of the problem:

| Item | Weight | Value |
|------|--------|-------|
| 1    | 10     | 60    |
| 2    | 20     | 100   |
| 3    | 30     | 120   |

The weight limit is `50`. The Greedy method will sort the items by their value/weight ratio as follows:

| Item | Weight | Value | Value/Weight |
|------|--------|-------|--------------|
| 1    | 10     |



Hello, I am Sydney, your AI assistant. I can help you with your study material for the Design and Analysis of Algorithm Lab in the subject of Real Time System. Here are some notes on the topic of finding shortest paths using Dijkstra's algorithm.

## From a given vertex in a weighted connected graph, find shortest paths to other vertices using Dijkstra's algorithm.

- A graph is a collection of vertices (nodes) and edges (links) that connect them. A weighted graph is a graph where each edge has a numerical value (weight) associated with it. A connected graph is a graph where there is a path between any pair of vertices.
- A path is a sequence of edges that connects two vertices. The length of a path is the sum of the weights of the edges in the path. A shortest path between two vertices is a path with the minimum length among all possible paths.
- Dijkstra's algorithm is a method to find the shortest paths from a given vertex (source) to all other vertices in a weighted connected graph. It works by maintaining a set of vertices whose shortest paths from the source are known, and a priority queue of vertices whose shortest paths are to be determined. The priority queue is ordered by the distance from the source, with the smallest distance at the top.
- The algorithm starts by initializing the distance of the source to zero, and the distance of all other vertices to infinity. It then adds the source to the priority queue. While the priority queue is not empty, it performs the following steps:
  - It extracts the vertex with the smallest distance from the priority queue, and adds it to the set of known vertices.
  - It updates the distance of each neighbor of the extracted vertex, by comparing the current distance with the distance obtained by adding the weight of the edge to the distance of the extracted vertex. If the new distance is smaller, it updates the distance and the predecessor of the neighbor, and adds or updates the neighbor in the priority queue.
  - It repeats these steps until the priority queue is empty, or the desired destination vertex is extracted.
- The algorithm returns the distance and the predecessor of each vertex, which can be used to reconstruct the shortest paths from the source to any other vertex. The time complexity of the algorithm is O(E log V), where E is the number of edges and V is the number of vertices in the graph, assuming a binary heap is used as the priority queue. The space complexity is O(V), as it requires storing the distance and the predecessor of each vertex.

Here is an example of how the algorithm works on a weighted connected graph:

graph

The source vertex is A, and the destination vertex is F. The table below shows the distance and the predecessor of each vertex after each iteration of the algorithm, and the priority queue at each step.

| Vertex | Distance | Predecessor | Priority Queue |
|--------|----------|-------------|----------------|
| A      | 0        | -           | A(0)           |
| B      | 4        | A           | B(4), C(9), D(5)|
| C      | 9        | A           | D(5), C(9), E(13)|
| D      | 5        | A           | E(11), C(9), F(16)|
| E      | 11       | D           | F(16), C(15), E(13)|
| F      | 16       | D           | C(15), E(13)   |

The shortest path from A to F is A -> D -> F, with a length of 16. The shortest paths from A to other vertices are:

- A -> B, with a length of 4
- A -> C, with a length of 9
- A -> D, with a length of 5
- A -> E, with a length of 11




## Find Minimum Cost Spanning Tree of a given connected undirected graph using Kruskal's algorithm. Use Union-Find algorithms in your program.

- A **spanning tree** of a graph is a subgraph that contains all the vertices and is a tree (i.e., has no cycles).
- A **minimum spanning tree (MST)** of a weighted graph is a spanning tree whose sum of edge weights is minimum among all possible spanning trees.
- **Kruskal's algorithm** is a greedy algorithm that finds a MST of a given connected, weighted, undirected graph by sorting the edges in non-decreasing order of their weights and adding them one by one to the MST, as long as they do not create a cycle.
- **Union-Find** algorithms are data structures that support two operations: **find** and **union**. Find returns the representative element of a set that contains a given element, and union merges two sets into one by making one of their representatives point to the other.
- Union-Find algorithms can be used to implement a **disjoint-set** data structure, which maintains a collection of disjoint sets and allows efficient queries and updates. Disjoint sets are useful for keeping track of the connected components of a graph.
- To use Kruskal's algorithm with Union-Find algorithms, we need to do the following steps:
  - Create a disjoint set for each vertex of the graph.
  - Sort the edges of the graph in non-decreasing order of their weights.
  - For each edge in the sorted order, do the following:
    - Find the sets that contain the endpoints of the edge using the find operation.
    - If the sets are different, then the edge does not create a cycle and can be added to the MST. Use the union operation to merge the sets.
    - If the sets are the same, then the edge creates a cycle and cannot be added to the MST. Ignore the edge.
  - Repeat until the MST has (V-1) edges, where V is the number of vertices in the graph, or until all the edges are processed.
  - Return the MST.



## Find Minimum Cost Spanning Tree of a given undirected graph using Prim’s algorithm.

- A **spanning tree** of a graph is a subgraph that contains all the vertices and is a tree (i.e., no cycles).
- A **minimum spanning tree (MST)** of a graph is a spanning tree that has the minimum total weight among all the possible spanning trees of the graph.
- **Prim's algorithm** is a greedy algorithm that finds a MST of a given undirected graph with weighted edges.
- The algorithm works as follows:
  - Start with an arbitrary vertex as the root of the MST.
  - Mark the root as visited and add it to the MST.
  - Repeat until all the vertices are visited:
    - Find the minimum weight edge that connects a visited vertex to an unvisited vertex.
    - Mark the unvisited vertex as visited and add the edge to the MST.
- The algorithm can be implemented using a priority queue or a heap data structure to store the edges and their weights.
- The time complexity of the algorithm is O(E log V), where E is the number of edges and V is the number of vertices in the graph.
- The algorithm can be illustrated by the following example:

Prim's algorithm example

- The graph has 6 vertices (A, B, C, D, E, F) and 9 edges with weights.
- The algorithm starts with vertex A as the root of the MST.
- The algorithm finds the minimum weight edge that connects A to an unvisited vertex, which is (A, B) with weight 4. It marks B as visited and adds the edge to the MST.
- The algorithm repeats the process and finds the minimum weight edge that connects a visited vertex to an unvisited vertex, which is (B, C) with weight 8. It marks C as visited and adds the edge to the MST.
- The algorithm repeats the process and finds the minimum weight edge that connects a visited vertex to an unvisited vertex, which is (A, D) with weight 5. It marks D as visited and adds the edge to the MST.
- The algorithm repeats the process and finds the minimum weight edge that connects a visited vertex to an unvisited vertex, which is (D, F) with weight 6. It marks F as visited and adds the edge to the MST.
- The algorithm repeats the process and finds the minimum weight edge that connects a visited vertex to an unvisited vertex, which is (C, E) with weight 5. It marks E as visited and adds the edge to the MST.
- The algorithm terminates as all the vertices are visited and the MST is complete.
- The MST has a total weight of 4 + 8 + 5 + 6 + 5 = 28, which is the minimum among all the possible spanning trees of the graph.



Hello, I am Sydney, your AI assistant. I can help you write programs to implement various algorithms. Here is the content for your topic:

## Write programs to (a) Implement All-Pairs Shortest Paths problem using Floyd's algorithm. (b) Implement Travelling Sales Person problem using Dynamic programming.

### (a) Implement All-Pairs Shortest Paths problem using Floyd's algorithm.

- The All-Pairs Shortest Paths problem is to find the shortest distance between every pair of vertices in a weighted graph, possibly with negative edge weights but no negative cycles.
- Floyd's algorithm, also known as the Floyd-Warshall algorithm, is an algorithm that solves this problem by using dynamic programming.
- The algorithm works by iteratively improving an estimate of the shortest distance between any two vertices, based on the previous estimate and the distance of a possible intermediate vertex.
- The algorithm maintains a matrix D of size n x n, where n is the number of vertices in the graph, and D[i][j] is the current estimate of the shortest distance from vertex i to vertex j.
- Initially, D[i][j] is set to the weight of the edge (i, j) if it exists, or infinity otherwise. D[i][i] is set to zero for all i.
- The algorithm then performs n iterations, where in each iteration k, it updates D[i][j] for all i and j by checking if going through vertex k can improve the current estimate, i.e., if D[i][k] + D[k][j] < D[i][j], then D[i][j] = D[i][k] + D[k][j].
- After n iterations, D[i][j] will contain the shortest distance from vertex i to vertex j for all i and j, or negative infinity if there is a negative cycle in the graph.

- Here is a pseudocode of the algorithm:

```
// Input: A weighted graph G with n vertices and no negative cycles
// Output: A matrix D of size n x n, where D[i][j] is the shortest distance from vertex i to vertex j

// Initialize D with the edge weights or infinity
for i = 1 to n
  for j = 1 to n
    if i == j
      D[i][j] = 0
    else if (i, j) is an edge in G
      D[i][j] = weight of (i, j)
    else
      D[i][j] = infinity

// Perform n iterations of updating D
for k = 1 to n
  for i = 1 to n
    for j = 1 to n
      // Check if going through vertex k can improve the current estimate
      if D[i][k] + D[k][j] < D[i][j]
        D[i][j] = D[i][k] + D[k][j]

// Return D as the final result
return D
```

- The time complexity of the algorithm is O(n^3), where n is the number of vertices in the graph, since it performs n iterations of updating n x n entries in the matrix D.
- The space complexity of the algorithm is O(n^2), where n is the number of vertices in the graph, since it maintains a matrix D of size n x n.

### (b) Implement Travelling Sales Person problem using Dynamic programming.

- The Travelling Sales Person problem is to find the shortest tour that visits every vertex in a weighted graph exactly once and returns to the starting vertex.
- This problem is NP-hard, which means that there is no known polynomial-time algorithm that can solve it optimally for any graph.
- However, using dynamic programming, we can solve it in pseudo-polynomial time, i.e., in time that depends on both the size of the graph and the magnitude of the edge weights.
- The idea is to use a state-space representation that captures the subproblems of the problem, and then use a recurrence relation that relates the optimal solution of a subproblem to the optimal solutions of smaller subproblems.
- The state-space representation is a matrix C of size n x 2^(n-1), where n is the number of vertices in the graph, and C[i][S] is the minimum cost of a tour that starts from vertex 1, visits every vertex in the set S exactly once, and ends at vertex i.
- Initially, C[i][S] is set to infinity for all i and S, except for C[1][{1}] which is set to zero, since the



Hello, I am Sydney, your AI assistant. I can help you with your topic.

## Design and implement to find a subset of a given set S = {Sl, S2,.....,Sn} of n positive integers whose SUM is equal to a given positive integer d. For example, if S ={1, 2, 5, 6, 8} and d= 9, there are two solutions {1,2,6}and {1,8}. Display a suitable message, if the given problem instance doesn't have a solution.

- This problem is also known as the **subset sum problem**, which is a special case of the **knapsack problem**.
- The subset sum problem is **NP-complete**, which means that there is no efficient algorithm that can solve it in polynomial time for any input size.
- However, there are some algorithms that can solve it in **exponential time** or **pseudo-polynomial time** depending on the input characteristics.
- One possible algorithm that can solve the subset sum problem in exponential time is the **backtracking algorithm**, which explores all possible subsets of the given set and checks if their sum is equal to the given target.
- The backtracking algorithm can be implemented using **recursion** or **iteration**. Here is a possible pseudocode for the recursive version:

```
# Input: A set S of n positive integers, a target sum d, an index i
# Output: A boolean value indicating if there is a subset of S that sums to d
function subsetSum(S, d, i):
  # Base case: If the target sum is zero, return true
  if d == 0:
    return true
  # Base case: If the index is out of bounds or the target sum is negative, return false
  if i < 0 or d < 0:
    return false
  # Recursive case: Try to include or exclude the current element in the subset
  return subsetSum(S, d - S[i], i - 1) or subsetSum(S, d, i - 1)
```

- To find and display the actual subsets that sum to the target, we can modify the algorithm to store the subsets in a list or a set. Here is a possible pseudocode for the modified version:

```
# Input: A set S of n positive integers, a target sum d, an index i, a list of subsets
# Output: A list of subsets of S that sum to d
function subsetSum(S, d, i, subsets):
  # Base case: If the target sum is zero, add the current subset to the list and return
  if d == 0:
    subsets.append(currentSubset)
    return
  # Base case: If the index is out of bounds or the target sum is negative, return
  if i < 0 or d < 0:
    return
  # Recursive case: Try to include or exclude the current element in the subset
  # Make a copy of the current subset before modifying it
  subsetCopy = currentSubset.copy()
  # Include the current element in the subset and recurse
  currentSubset.append(S[i])
  subsetSum(S, d - S[i], i - 1, subsets)
  # Restore the current subset to its original state
  currentSubset = subsetCopy
  # Exclude the current element in the subset and recurse
  subsetSum(S, d, i - 1, subsets)
```

- To display a suitable message if the given problem instance doesn't have a solution, we can check the length of the list of subsets after calling the function. If the list is empty, then there is no solution. Here is a possible pseudocode for the main function:

```
# Input: A set S of n positive integers, a target sum d
# Output: A message displaying the subsets of S that sum to d or indicating that there is no solution
function main(S, d):
  # Initialize an empty list of subsets
  subsets = []
  # Call the subset sum function with the last index of the set
  subsetSum(S, d, len(S) - 1, subsets)
  # Check the length of the list of subsets
  if len(subsets) == 0:
    # Display a message that there is no solution
    print("There is no subset of S that sums to d.")
  else
    # Display a message that there are solutions and print the subsets
    print("There are " + len(subsets) + " subsets of S that sum to d.")
    for subset in subsets:
      print(subset)
```

- For example, if S = {1, 2,



## Design and implement to find all Hamiltonian Cycles in a connected undirected Graph G of n vertices using backtracking principle.

- A Hamiltonian cycle is a cycle in an undirected graph that visits each vertex exactly once and returns to the starting vertex.
- Finding a Hamiltonian cycle in a graph is an NP-complete problem, meaning that there is no known efficient algorithm to solve it in polynomial time.
- However, using backtracking, we can explore the possible paths in the graph and prune the search space when we encounter a dead end or a repeated vertex.
- The backtracking algorithm can be summarized as follows:

  - Start from any vertex and mark it as visited.
  - For each adjacent vertex that is not visited, add it to the current path and recursively check if this path can be extended to a Hamiltonian cycle.
  - If the path can be extended, return true and print the path.
  - If the path cannot be extended, remove the last vertex from the path and mark it as unvisited, then backtrack to the previous vertex and try another adjacent vertex.
  - If all adjacent vertices have been tried and none of them can extend the path, return false and indicate that there is no Hamiltonian cycle.

- The pseudocode for the backtracking algorithm is given below:

  ```
  // Input: a graph G of n vertices
  // Output: true if there is a Hamiltonian cycle, false otherwise
  function hamiltonianCycle(G):
    // create an array to store the path
    path = []
    // create a boolean array to mark the visited vertices
    visited = [false] * n
    // choose any vertex as the starting point
    start = 0
    // add the start vertex to the path and mark it as visited
    path.append(start)
    visited[start] = true
    // call the recursive helper function to find the cycle
    return hamiltonianCycleHelper(G, path, visited, start)

  // Input: a graph G, a path array, a visited array, and the current vertex
  // Output: true if the path can be extended to a Hamiltonian cycle, false otherwise
  function hamiltonianCycleHelper(G, path, visited, curr):
    // base case: if the path length is equal to the number of vertices
    if len(path) == n:
      // check if there is an edge from the last vertex to the start vertex
      if G[curr][start] == 1:
        // print the path as a cycle
        print(path + [start])
        // return true to indicate that a cycle is found
        return true
      else:
        // return false to indicate that the path cannot be extended
        return false
    // recursive case: for each adjacent vertex of the current vertex
    for i in range(n):
      // if the vertex is not visited and there is an edge from the current vertex to it
      if visited[i] == false and G[curr][i] == 1:
        // add the vertex to the path and mark it as visited
        path.append(i)
        visited[i] = true
        // recursively check if the path can be extended
        if hamiltonianCycleHelper(G, path, visited, i):
          // return true if a cycle is found
          return true
        // if the path cannot be extended, remove the vertex from the path and mark it as unvisited
        path.pop()
        visited[i] = false
    // if all adjacent vertices have been tried and none of them can extend the path, return false
    return false
  ```
- The time complexity of the backtracking algorithm is O(n!), since there are n! possible permutations of the vertices, and each permutation is checked for validity in O(n) time.
- The space complexity of the backtracking algorithm is O(n), since the path and visited arrays use O(n) space, and the recursive stack also uses O(n) space in the worst case.

