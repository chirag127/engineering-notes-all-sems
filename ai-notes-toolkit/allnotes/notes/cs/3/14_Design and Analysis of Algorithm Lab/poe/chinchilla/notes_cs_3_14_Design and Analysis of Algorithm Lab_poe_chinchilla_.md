

## Program for Recursive Binary & Linear Search

In this section, we will discuss the program for Recursive Binary & Linear Search. These search algorithms are widely used in computer science to find a specific element in a sorted array.

### Linear Search
Linear search is a simple algorithm that searches for an element in an array by sequentially checking each element of the array until a match is found or the end of the array is reached. The time complexity of linear search is O(n).

Here is the program for linear search in C++:

```c++
int linearSearch(int arr[], int n, int x) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == x)
            return i;
    }
    return -1;
}
```

### Recursive Binary Search
Binary search is a more efficient algorithm that searches for an element in a sorted array by repeatedly dividing the search interval in half. The time complexity of binary search is O(log n).

Here is the program for recursive binary search in C++:

```c++
int binarySearch(int arr[], int low, int high, int x) {
    if (low > high)
        return -1;
    int mid = (low + high) / 2;
    if (arr[mid] == x)
        return mid;
    else if (arr[mid] > x)
        return binarySearch(arr, low, mid - 1, x);
    else
        return binarySearch(arr, mid + 1, high, x);
}
```

In the above program, we first check if the search interval is empty (i.e., low > high). If it is, we return -1 to indicate that the element was not found. Otherwise, we calculate the middle index of the interval and compare the middle element with the search element. If they are equal, we return the middle index. Otherwise, we recursively search the left or right half of the interval depending on whether the middle element is greater or less than the search element.

### Conclusion
In this section, we discussed the programs for Recursive Binary & Linear Search. These algorithms are widely used in computer science to search for a specific element in a sorted array. The binary search algorithm is more efficient than the linear search algorithm, but it requires the array to be sorted.



## Program for Heap Sort

Heap Sort is a popular sorting algorithm that uses a binary heap data structure to sort an array. It has a time complexity of O(n log n) and is often used when the input size is large. Here is a program for Heap Sort:

1. Begin by creating a binary heap from the given array. This can be done by repeatedly inserting elements into the heap.

2. Once the heap is created, we can start sorting the array. The first step is to swap the root node with the last leaf node in the heap.

3. After the swap, we remove the last leaf node from the heap and decrement the size of the heap by one.

4. Next, we need to maintain the heap property. This is done by comparing the new root node with its children and swapping them if necessary.

5. We repeat steps 2-4 until the heap is empty. At each iteration, the largest element in the heap is moved to the end of the array.

6. Finally, we have a sorted array.

Here is the complete program for Heap Sort in C++:

```
void heapify(int arr[], int n, int i) {
    int largest = i;
    int l = 2*i + 1;
    int r = 2*i + 2;
 
    if (l < n && arr[l] > arr[largest])
        largest = l;
 
    if (r < n && arr[r] > arr[largest])
        largest = r;
 
    if (largest != i) {
        swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}
 
void heapSort(int arr[], int n) {
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);
 
    for (int i = n-1; i >= 0; i--) {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}
```

In conclusion, Heap Sort is a powerful sorting algorithm that can be used to sort large arrays quickly. By understanding how it works and implementing it in code, we can gain a deeper understanding of algorithms and data structures.



## Program for Merge Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

In this lab session, we will learn about the Merge Sort algorithm, which is a sorting algorithm used to sort elements in a list or an array. Merge Sort is an efficient algorithm with a time complexity of O(nlogn). Here is a program in Python for implementing the Merge Sort algorithm:

### Program for Merge Sort

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
```

### Explanation of the Program

In the above program, we have defined a function called `merge_sort()` that takes an array as an input. The function recursively divides the array into two halves until each sub-array has only one element. Then, the function merges the two sub-arrays in a sorted order.

The `merge()` function takes two sub-arrays, `left_half` and `right_half`, and merges them into a single array `arr`. The `i`, `j`, and `k` variables are used to keep track of the elements in the left, right, and merged arrays, respectively.

The program first checks if the length of the array is greater than 1. If it is, the program finds the middle index of the array and divides the array into two halves. The `merge_sort()` function is called recursively on the left and right halves until the length of the sub-arrays becomes 1.

Then, the `merge()` function is called to merge the two sub-arrays. The elements from the left and right sub-arrays are compared, and the smallest element is added to the `arr` array. This process continues until all the elements from both sub-arrays are added to the `arr` array.

Finally, the sorted array is returned.

### Conclusion

In this lab session, we learned about the Merge Sort algorithm and implemented it in Python. The Merge Sort algorithm is an efficient sorting algorithm with a time complexity of O(nlogn). We hope this program will help you understand the Merge Sort algorithm better and prepare you for your exams.



## Program for Selection Sort

Selection Sort is an algorithm for sorting a list of elements in increasing or decreasing order. It is a simple and easy-to-understand sorting algorithm, but it is not very efficient for large lists. In this lab, we will learn how to implement Selection Sort in a program.

### Steps for Selection Sort

The Selection Sort algorithm involves the following steps:

1. Set the first element of the list as the minimum value.
2. Compare the minimum value with the next element in the list.
3. If the next element is smaller than the minimum value, set the next element as the new minimum value.
4. Continue comparing the minimum value with each element in the list until the end of the list is reached.
5. Swap the minimum value with the first element of the list.
6. Repeat steps 2-5 for the remaining unsorted elements in the list.

### Implementation of Selection Sort

Here is a sample program in C++ for implementing Selection Sort:

```
#include<iostream>
using namespace std;
void selectionSort(int arr[], int n)
{
    int i, j, min_idx;
    for (i = 0; i < n-1; i++)
    {
        min_idx = i;
        for (j = i+1; j < n; j++)
            if (arr[j] < arr[min_idx])
                min_idx = j;
        swap(arr[min_idx], arr[i]);
    }
}
int main()
{
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr)/sizeof(arr[0]);
    selectionSort(arr, n);
    cout << "Sorted array: \n";
    for (int i=0; i < n; i++)
        cout << arr[i] << " ";
    return 0;
}
```

The above program sorts an array of integers using Selection Sort. Here's how it works:

1. The `selectionSort` function takes an array and its size as input.
2. Two variables `i` and `j` are used for iterating over the array.
3. The `min_idx` variable is used to keep track of the index of the minimum value in the array.
4. The outer loop iterates over the unsorted elements in the array.
5. The inner loop finds the minimum value in the unsorted portion of the array.
6. The `swap` function is used to swap the minimum value with the first element of the unsorted portion of the array.
7. The sorted array is printed using a `for` loop in the `main` function.

### Time Complexity of Selection Sort

The time complexity of Selection Sort is O(n^2), where n is the number of elements in the list. This means that the algorithm takes quadratic time to sort the list. Selection Sort is not very efficient for large lists, and other sorting algorithms such as Merge Sort and Quick Sort are preferred for large datasets.

In conclusion, Selection Sort is a simple and easy-to-understand sorting algorithm that can be easily implemented in a program. However, it is not very efficient for large lists, and other sorting algorithms should be used for large datasets.



## Program for Insertion Sort

Insertion Sort is a simple sorting algorithm that works by iteratively building a sorted sublist from an unsorted list. It is an efficient algorithm for small data sets or lists that are almost sorted. In this lab, we will learn how to implement the Insertion Sort algorithm using a program.

### Steps for implementing Insertion Sort

1. Start by defining a function called `insertion_sort` that takes an array of integers as input.

2. The first step in the Insertion Sort algorithm is to iterate through the unsorted list, starting from the second element. For each element, we need to compare it with the elements before it and insert it in the correct position in the sorted sublist.

3. To do this, we need to define a variable called `key` that will hold the value of the current element being sorted.

4. We then iterate through the sorted sublist, starting from the last element and moving towards the beginning. For each element, we compare it with the `key`. If the element is greater than the `key`, we move the element one position to the right.

5. We continue this process until we find an element that is less than or equal to the `key`. We then insert the `key` at the position immediately after this element.

6. Once we have sorted the entire list in this manner, we return the sorted array.

### Sample implementation of Insertion Sort in Python

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

### Conclusion

Insertion Sort is a simple yet effective sorting algorithm that can be implemented easily using a program. By iterating through the unsorted list and building a sorted sublist, we can quickly sort small data sets or lists that are almost sorted.



## Program for Quick Sort

Quick Sort is an efficient sorting algorithm that is widely used for sorting large sets of data. It uses the divide-and-conquer approach to sort the elements in an array. The algorithm works by partitioning the array into two sub-arrays, one containing elements smaller than a chosen pivot and the other containing elements larger than the pivot. The pivot is then placed in its correct position and the algorithm recursively applies the same process to the two sub-arrays.

Here is a program for implementing Quick Sort in C++:

### Algorithm

1. Select a pivot element from the array.
2. Partition the array into two sub-arrays, one containing elements smaller than the pivot and the other containing elements larger than the pivot.
3. Recursively apply the same process to the two sub-arrays until the entire array is sorted.

### Program

```cpp
#include<iostream>
using namespace std;

void swap(int* a, int* b) {
    int t = *a;
    *a = *b;
    *b = t;
}

int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = (low - 1);

    for(int j=low; j<=high-1; j++) {
        if(arr[j] < pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i+1], &arr[high]);
    return (i+1);
}

void quickSort(int arr[], int low, int high) {
    if(low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi-1);
        quickSort(arr, pi+1, high);
    }
}

int main() {
    int arr[] = {10, 7, 8, 9, 1, 5};
    int n = sizeof(arr)/sizeof(arr[0]);

    quickSort(arr, 0, n-1);

    cout<<"Sorted array: ";
    for(int i=0; i<n; i++) {
        cout<<arr[i]<<" ";
    }
    return 0;
}
```

### Explanation

1. The `swap` function is used to swap two elements in the array.
2. The `partition` function takes the last element of the array as the pivot and partitions the array into two sub-arrays.
3. The `quickSort` function recursively applies the same process to the two sub-arrays until the entire array is sorted.
4. The main function initializes the array and calls the `quickSort` function to sort the array.
5. The sorted array is printed using a for loop.

### Time Complexity

The time complexity of Quick Sort is O(nlogn) in the average case and O(n^2) in the worst case. However, the worst case can be avoided by choosing the pivot element carefully, such as by selecting the median of the array as the pivot.

### Conclusion

Quick Sort is a fast and efficient sorting algorithm that is widely used in various applications. It has a time complexity of O(nlogn) in the average case and can be optimized to avoid the worst case scenario.



## Knapsack Problem using Greedy Solution

The Knapsack Problem is a classic optimization problem in computer science, where given a set of items with weight and value, we need to find the subset of items that can be packed into a knapsack of limited capacity to maximize the total value.

### Greedy Solution

The Greedy Solution for the Knapsack Problem involves choosing the items with the highest value-to-weight ratio first and packing them into the knapsack until it is full. This algorithm works well when the items have similar weights and values, and the knapsack capacity is significantly larger than the total weight of all items.

### Steps for Greedy Solution

The following are the steps involved in the Greedy Solution for the Knapsack Problem:

1. Compute the value-to-weight ratio for each item by dividing the value by the weight.
2. Sort the items in descending order based on their value-to-weight ratio.
3. Start packing items into the knapsack in order of the sorted list until the knapsack is full.
4. If an item cannot be fully packed into the knapsack, pack a fraction of it that fits, and move on to the next item.

### Example

Suppose we have a knapsack with a capacity of 50 and the following items:

| Item | Weight | Value |
|------|--------|-------|
| 1    | 10     | 60    |
| 2    | 20     | 100   |
| 3    | 30     | 120   |

Using the Greedy Solution, we can compute the value-to-weight ratio for each item as follows:

| Item | Weight | Value | Ratio |
|------|--------|-------|-------|
| 1    | 10     | 60    | 6     |
| 2    | 20     | 100   | 5     |
| 3    | 30     | 120   | 4     |

Sorting the items in descending order based on their value-to-weight ratio, we get the following list:

| Item | Weight | Value | Ratio |
|------|--------|-------|-------|
| 1    | 10     | 60    | 6     |
| 2    | 20     | 100   | 5     |
| 3    | 30     | 120   | 4     |

We start packing the items into the knapsack in order of the sorted list:

1. Pack item 1 (10 weight, 60 value) fully into the knapsack.
2. Pack item 2 (20 weight, 100 value) fully into the knapsack.
3. Pack a fraction of item 3 (30 weight, 120 value) that fits into the knapsack, which is 20 weight, and add it to the total value.

The total weight packed into the knapsack is 50, and the total value is 180. Thus, the Greedy Solution yields an optimal solution for this problem.

### Conclusion

The Greedy Solution for the Knapsack Problem is a simple and efficient algorithm that works well for certain types of instances. However, it may not always yield an optimal solution, especially when the items have significantly different weights and values or when the knapsack capacity is small. Therefore, more advanced algorithms, such as dynamic programming, may be required to solve more complex instances of the Knapsack Problem.



## Perform Travelling Salesman Problem for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

The Travelling Salesman Problem (TSP) is a classic problem in computer science that involves finding the shortest possible route that visits a set of cities and returns to the starting point. In the Design and Analysis of Algorithm Lab of Real Time System, performing TSP is an important exercise that helps students understand various algorithms used for solving optimization problems. Here are the steps to perform TSP:

1. Define the problem: The first step in solving any problem is to define it clearly. In the case of TSP, the problem is to find the shortest possible route that visits a set of cities and returns to the starting point.

2. Choose an algorithm: There are several algorithms that can be used to solve TSP, including brute force, nearest neighbor, and genetic algorithms. Choose an algorithm that suits the problem at hand and the available resources.

3. Implement the algorithm: Once the algorithm has been chosen, it needs to be implemented in a programming language. Write code to perform TSP using the chosen algorithm.

4. Test the algorithm: Testing is an important part of algorithm development. Test the TSP algorithm using different input data sets to ensure that it works correctly and produces accurate results.

5. Optimize the algorithm: After testing, the TSP algorithm may need to be optimized for performance. This can involve tweaking the algorithm or using a different data structure to improve efficiency.

6. Document the algorithm: Documenting the TSP algorithm is important for future reference and understanding. Write a detailed report that describes the algorithm, its implementation, and the results obtained.

Performing TSP is an important exercise for students of Real Time System. It helps them understand various algorithms used for solving optimization problems and the importance of testing and optimization in algorithm development. By following these steps, students can successfully perform TSP and gain valuable experience in algorithm development.



## Find Minimum Spanning Tree using Kruskal’s Algorithm

Kruskal’s algorithm is a greedy algorithm used to find the minimum spanning tree (MST) of a given graph. The MST is a subgraph of the original graph that connects all the vertices with minimum total edge weight.

### Steps for finding MST using Kruskal’s Algorithm:

1. Sort all the edges of the graph in non-decreasing order of their weight.
2. Create an empty MST and initialize it with an empty set of edges.
3. Iterate over all the edges in the sorted order. For each edge, check if adding it to the MST forms a cycle. If not, add it to the MST.
4. Repeat step 3 until all the edges have been processed or the MST contains n-1 edges, where n is the number of vertices in the graph.

### Pseudo Code for Kruskal’s Algorithm:

```
KruskalMST(G):
  sort all the edges of G in non-decreasing order of their weight
  initialize an empty set of edges as MST
  for each vertex v in G:
    makeSet(v)
  for each edge (u, v) in G:
    if findSet(u) != findSet(v):
      add (u, v) to MST
      union(u, v)
  return MST
```

### Example:

Consider the following undirected graph with 6 vertices and 9 edges:

graph

The edges are sorted in non-decreasing order of their weight as follows:

```
(B, C) -> weight: 2
(E, F) -> weight: 2
(A, B) -> weight: 3
(C, D) -> weight: 4
(B, D) -> weight: 5
(D, F) -> weight: 5
(A, D) -> weight: 6
(C, E) -> weight: 6
(B, E) -> weight: 7
```

The MST of the graph can be found using Kruskal’s Algorithm as follows:

1. Create an empty MST: `MST = {}`
2. Initialize disjoint sets for each vertex: `{A}, {B}, {C}, {D}, {E}, {F}`
3. Process the edges in the sorted order:
   - Add edge (B, C) to the MST as it does not form a cycle: `MST = {(B, C)}`
   - Add edge (E, F) to the MST as it does not form a cycle: `MST = {(B, C), (E, F)}`
   - Add edge (A, B) to the MST as it does not form a cycle: `MST = {(B, C), (E, F), (A, B)}`
   - Add edge (C, D) to the MST as it does not form a cycle: `MST = {(B, C), (E, F), (A, B), (C, D)}`
   - Add edge (B, D) to the MST as it does not form a cycle: `MST = {(B, C), (E, F), (A, B), (C, D), (B, D)}`
   - Skip edge (D, F) as it forms a cycle with the MST: `MST = {(B, C), (E, F), (A, B), (C, D), (B, D)}`
   - Add edge (A, D) to the MST as it does not form a cycle: `MST = {(B, C), (E, F), (A, B), (C, D), (B, D), (A, D)}`
   - Skip edge (C, E) as it forms a cycle with the MST: `MST = {(B, C), (E, F), (A, B), (C, D), (B, D), (A, D)}`
   - Skip edge (B, E) as it forms a cycle with the MST: `MST = {(B, C), (E, F), (A, B), (C, D), (B, D), (A, D)}`
4. The MST of the graph is: `MST = {(B, C), (E, F), (A, B), (C, D), (B, D), (A, D)}`

### Time Complexity:

The time complexity of Kruskal’s Algorithm is O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices in the graph. The sorting step takes O(E log E) time and the disjoint set operations take O(E log V) time. Since E is at most V^2, the time complexity is O(V^2 log V) in the worst case.



## Implement N Queen Problem using Backtracking

The N Queen Problem is a classic problem of placing N chess queens on an N×N chessboard such that no two queens threaten each other. This means that no two queens can share the same row, column, or diagonal. In this lab, we will implement the N Queen Problem using Backtracking.

### Backtracking

Backtracking is a technique used to solve problems by attempting to build a solution incrementally, one piece at a time, while removing solutions that fail to satisfy the constraints of the problem at any point of time. Backtracking is a depth-first search (DFS) with added constraints on the search space.

### Steps to implement N Queen Problem using Backtracking

1. Create an empty chess board of size N×N.
2. Place the first queen in the first row and first column.
3. Move to the next row and check if placing a queen in any of the columns of that row violates the constraints of the problem (i.e., no two queens can share the same row, column, or diagonal).
4. If a column is found that does not violate the constraints, place a queen in that column and move to the next row.
5. If no such column is found, backtrack to the previous row and try a different column in that row.
6. Repeat steps 3 to 5 until all queens are placed on the chessboard.

### Pseudocode

The following is the pseudocode for implementing the N Queen Problem using Backtracking:

```
procedure n_queen(board, row):
   if row = N:
      return true
   for each column in row:
      if is_safe(board, row, column):
         board[row][column] = 1
         if n_queen(board, row+1) = true:
            return true
         board[row][column] = 0
   return false

function is_safe(board, row, column):
   for i = 0 to row-1:
      if board[i][column] = 1:
         return false
   for i = row-1, j = column-1; i >= 0 and j >= 0; i--, j--:
      if board[i][j] = 1:
         return false
   for i = row-1, j = column+1; i >= 0 and j < N; i--, j++:
      if board[i][j] = 1:
         return false
   return true
```

### Complexity Analysis

The time complexity of the N Queen Problem using Backtracking is O(N!), where N is the size of the chessboard. This is because the number of possible solutions to the problem is factorial in nature.

The space complexity of the algorithm is O(N^2), where N is the size of the chessboard. This is because we are using a 2D array to represent the chessboard.

### Conclusion

In this lab, we have learned how to implement the N Queen Problem using Backtracking. Backtracking is a powerful technique that can be used to solve a wide variety of problems. The N Queen Problem is just one example of a problem that can be solved using Backtracking.



## Quick Sort Algorithm

Quick Sort is a commonly used sorting algorithm that follows the divide-and-conquer approach. It is an efficient algorithm for sorting large datasets. The algorithm works by selecting a pivot element from the dataset, partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot, and recursively applying the algorithm to each sub-array.

### Algorithm Steps

1. Choose an element in the array to be the pivot element.
2. Partition the array into two sub-arrays based on the pivot element. One sub-array contains elements smaller than the pivot element, and the other sub-array contains elements greater than the pivot element.
3. Recursively apply the algorithm to each sub-array.
4. Combine the sorted sub-arrays to obtain the final sorted array.

### Time Complexity

The time complexity of Quick Sort algorithm is as follows:

- Worst Case: O(n^2)
- Average Case: O(n log n)
- Best Case: O(n log n)

The worst case occurs when the pivot element is always the smallest or largest element in the array, resulting in unbalanced partitions. The average and best cases occur when the pivot element is chosen randomly or is the median element, resulting in balanced partitions.

### Demonstration using Java

Here is a sample implementation of Quick Sort algorithm using Java:

```java
public static void quickSort(int[] arr, int low, int high) {
    if (low < high) {
        int partitionIndex = partition(arr, low, high);
        quickSort(arr, low, partitionIndex - 1);
        quickSort(arr, partitionIndex + 1, high);
    }
}

public static int partition(int[] arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;
    return i + 1;
}
```

### Time Complexity Analysis

We can analyze the time complexity of Quick Sort algorithm using the following scenarios:

1. Worst Case: When the pivot element is always the smallest or largest element in the array, resulting in unbalanced partitions. This leads to the worst case time complexity of O(n^2).
2. Best Case: When the pivot element is the median element, resulting in balanced partitions. This leads to the best case time complexity of O(n log n).
3. Average Case: When the pivot element is chosen randomly, resulting in balanced partitions on average. This leads to the average case time complexity of O(n log n).

### Running the Program

To run the program for varied values of n>5000 and record the time taken to sort, we can use the following steps:

1. Generate an array of n random integers using the random number generator.
2. Call the quickSort() function with the array as input.
3. Record the time taken to sort the array using the System.currentTimeMillis() function.
4. Plot a graph of the time taken versus n using a graph sheet.

### Conclusion

Quick Sort is an efficient sorting algorithm that can be used for large datasets. The algorithm follows the divide-and-conquer approach and has a worst case time complexity of O(n^2), an average case time complexity of O(n log n), and a best case time complexity of O(n log n). By generating arrays of random integers with varied values of n>5000 and recording the time taken to sort, we can plot a graph of the time taken versus n to analyze the performance of the algorithm.



## Sort a Given Set of n Integer Elements using Merge Sort Method and Compute its Time Complexity

Merge sort is a popular sorting algorithm that follows the "Divide and Conquer" approach. It divides the array into two halves, sorts them separately, and then merges them to obtain a sorted array. In this way, it solves the problem of sorting a large array by breaking it down into smaller sub-problems. 

### Merge Sort Algorithm

1. Divide the given array into two halves.
2. Recursively sort the left and right halves of the array.
3. Merge the two sorted halves to obtain the final sorted array.

### Pseudo Code

```
mergesort(arr, left, right)
    if left < right
        middle = (left + right) / 2
        mergesort(arr, left, middle)
        mergesort(arr, middle+1, right)
        merge(arr, left, middle, right)

merge(arr, left, middle, right)
    n1 = middle - left + 1
    n2 = right - middle
    
    L = [0] * n1
    R = [0] * n2
    
    for i in range(n1):
        L[i] = arr[left+i]
    
    for j in range(n2):
        R[j] = arr[middle+j+1]
        
    i = 0
    j = 0
    k = left
    
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
        
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
        
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
```

### Time Complexity Analysis

The time complexity of Merge Sort can be analyzed using the "Master Theorem." The theorem states that if a problem of size n is divided into a sub-problems of size n/b, each solved recursively in time T(n/b), and the combine step takes time O(n), then the overall time complexity can be expressed as:

T(n) = aT(n/b) + O(n)

where a is the number of sub-problems and b is the size of each sub-problem.

#### Worst Case Time Complexity

In the worst case, Merge Sort takes O(n log n) time. This occurs when the array is in reverse sorted order, and each level of recursion requires the merging of two sub-arrays of size n/2.

#### Average Case Time Complexity

The average case time complexity of Merge Sort is also O(n log n). This is because it divides the array into two halves and sorts them separately, which takes O(log n) time. The merging step takes O(n) time. Therefore, the overall time complexity is O(n log n).

#### Best Case Time Complexity

The best case time complexity of Merge Sort is also O(n log n). This occurs when the array is already sorted. In this case, the algorithm still divides the array into two halves and merges them, but each level of recursion requires only O(n) time.

### Running Time Analysis

To measure the running time of Merge Sort, we can run the algorithm on different input sizes and record the time taken to sort each list. We can use a random number generator to generate the input lists or read them from a file. We can then plot a graph of the time taken versus the input size.

### Steps to Run the Program

1. Generate or read a list of integers of size n > 5000.
2. Implement the Merge Sort algorithm as shown above.
3. Measure the time taken to sort the list using a timer function.
4. Plot a graph of the time taken versus the input size.

### Conclusion

Merge Sort is a popular sorting algorithm that uses the "Divide and Conquer" approach to sort large arrays efficiently. It has a worst-case time complexity of O(n log n) and is widely used in practice. By measuring the running time of the algorithm for different input sizes, we can analyze its performance and compare it with other sorting algorithms.



## Implementing the 0/1 Knapsack Problem

The 0/1 Knapsack problem is a well-known optimization problem in computer science that involves selecting items of certain values and weights to maximize the value of items that can be carried in a knapsack of limited capacity. The problem is often encountered in real-world applications such as resource allocation, financial portfolio optimization, and scheduling.

In this article, we will discuss two methods of solving the 0/1 Knapsack problem: Dynamic Programming and Greedy methods. These methods will be implemented using C++ programming language for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System.

### Dynamic Programming Method

1. Define a 2D array `dp[][]` of size `(n+1) x (W+1)`, where `n` is the number of items and `W` is the maximum weight that the knapsack can carry.

2. Initialize the first row and column of the `dp` array with 0.

3. Create a loop that iterates through each item `i` and weight `j`. For each (i, j) pair, calculate the maximum value that can be obtained by either including or excluding the `ith` item in the knapsack.

4. If the weight of the `ith` item is less than or equal to the current weight `j`, then calculate the maximum value that can be obtained by either including or excluding the `ith` item using the following formula:

    `dp[i][j] = max(value[i] + dp[i-1][j-weight[i]], dp[i-1][j])`

   where `value[i]` is the value of the `ith` item, and `weight[i]` is the weight of the `ith` item.

5. If the weight of the `ith` item is greater than the current weight `j`, then the `ith` item cannot be included in the knapsack. In such cases, the `dp` value for the current (i, j) pair will be equal to the `dp` value obtained for the previous item `i-1`.

6. The final answer will be stored in `dp[n][W]`.

### Greedy Method

1. Create a vector `v` of pairs, where each pair consists of the value and weight of an item.

2. Sort the vector `v` in non-increasing order of value per unit weight.

3. Initialize the total value `ans` and the remaining weight `W` as 0 and the maximum capacity of the knapsack `w` respectively.

4. Create a loop that iterates through each item in the sorted vector `v`. For each item, if the weight of the item is less than or equal to the remaining weight `W`, add the entire value of the item to `ans` and subtract the weight of the item from `W`. Otherwise, add a fraction of the value of the item to `ans` proportional to the remaining capacity of the knapsack.

5. The final answer will be stored in `ans`.

In conclusion, the Dynamic Programming method guarantees an optimal solution to the 0/1 Knapsack problem, but has a higher time and space complexity compared to the Greedy method. The Greedy method on the other hand, provides a suboptimal solution but has a lower time and space complexity. The choice of which method to use will depend on the specific problem constraints and requirements.



## From a given vertex in a weighted connected graph, find shortest paths to other vertices using Dijkstra's algorithm.

Dijkstra's algorithm is a popular algorithm for finding the shortest path between a source vertex and all other vertices in a weighted graph. This algorithm is widely used in real-world applications such as GPS navigation and network routing.

### Algorithm Steps:

1. Initialize the distance of all vertices to infinity and the distance of the source vertex to 0.
2. Create a priority queue and insert the source vertex with distance 0.
3. While the priority queue is not empty, do the following:
   1. Extract the vertex with the minimum distance from the priority queue.
   2. For each adjacent vertex v, calculate the distance from the source vertex to v through the extracted vertex u. If this distance is less than the current distance of v, update the distance of v to this new distance and add v to the priority queue.
4. The final distances of all vertices from the source vertex will be the shortest paths.

### Example:

Consider the following weighted graph:

Graph Example

Let the source vertex be vertex A. We can use Dijkstra's algorithm to find the shortest paths to all other vertices.

1. Initialize the distance of all vertices to infinity and the distance of vertex A to 0.
   - Distance[A] = 0
   - Distance[B] = Distance[C] = Distance[D] = Distance[E] = Infinity
2. Insert vertex A with distance 0 into the priority queue.
3. While the priority queue is not empty, do the following:
   - Extract vertex A from the priority queue.
   - For each adjacent vertex v, calculate the distance from vertex A to v through vertex u. If this distance is less than the current distance of v, update the distance of v to this new distance and add v to the priority queue.
     - Distance[B] = min(Distance[B], Distance[A] + Weight[A,B]) = min(Infinity, 2) = 2
     - Distance[C] = min(Distance[C], Distance[A] + Weight[A,C]) = min(Infinity, 4) = 4
   - Vertex B is now the vertex with the minimum distance, so extract it from the priority queue.
     - Distance[D] = min(Distance[D], Distance[B] + Weight[B,D]) = min(Infinity, 1) = 1
     - Distance[E] = min(Distance[E], Distance[B] + Weight[B,E]) = min(Infinity, 3) = 3
   - Vertex D is now the vertex with the minimum distance, so extract it from the priority queue.
     - Vertex C is already visited, so no update is necessary.
     - Vertex E is already visited, so no update is necessary.
4. The final distances from vertex A to all other vertices are:
   - Distance[A] = 0
   - Distance[B] = 2
   - Distance[C] = 4
   - Distance[D] = 3
   - Distance[E] = 5

### Time Complexity:

The time complexity of Dijkstra's algorithm depends on the data structure used for the priority queue. Using a binary heap, the time complexity is O(VlogV + E), where V is the number of vertices and E is the number of edges in the graph. However, using a Fibonacci heap can reduce the time complexity to O(VlogV + E).



## Find Minimum Cost Spanning Tree of a given connected undirected graph using Kruskal's algorithm. Use Union-Find algorithms in your program.

In this topic, we will discuss how to find the minimum cost spanning tree of a given connected undirected graph using Kruskal's algorithm and Union-Find algorithms.

### Kruskal's Algorithm

Kruskal's algorithm is a greedy algorithm used to find the minimum cost spanning tree of a connected undirected graph. The algorithm works by sorting the edges of the graph in non-decreasing order of their weights and then adding them to the spanning tree one by one, as long as they do not form a cycle.

The steps involved in Kruskal's algorithm are as follows:

1. Sort the edges of the graph in non-decreasing order of their weights.
2. Initialize an empty set to represent the minimum cost spanning tree.
3. For each edge in the sorted list of edges, add it to the spanning tree if it does not form a cycle with the edges already in the tree.
4. Stop when all the vertices of the graph are included in the spanning tree.

### Union-Find Algorithms

Union-Find algorithms are used to maintain a collection of disjoint sets. They support two operations: union and find. The union operation merges two sets, and the find operation determines the set containing a given element.

The two most common Union-Find algorithms are:

1. Union-by-rank: In this algorithm, the smaller tree is always attached to the root of the larger tree to keep the height of the tree as small as possible. The rank of a tree is the height of its root node.
2. Path compression: In this algorithm, the find operation is optimized by flattening the tree so that all nodes in the path from the root to the given element point directly to the root.

### Kruskal's Algorithm with Union-Find Algorithms

To implement Kruskal's algorithm using Union-Find algorithms, we can use the following steps:

1. Create a disjoint set for each vertex of the graph.
2. Sort the edges of the graph in non-decreasing order of their weights.
3. For each edge in the sorted list of edges, find the sets containing the two vertices of the edge using the find operation.
4. If the sets are not the same, merge them using the union operation and add the edge to the minimum cost spanning tree.
5. Stop when all the vertices of the graph are included in the spanning tree.

### Complexity Analysis

The time complexity of Kruskal's algorithm with Union-Find algorithms is O(E log E), where E is the number of edges in the graph. The space complexity is O(V), where V is the number of vertices in the graph.

### Conclusion

In this topic, we have discussed how to find the minimum cost spanning tree of a given connected undirected graph using Kruskal's algorithm and Union-Find algorithms. By implementing these algorithms, we can efficiently find the minimum cost spanning tree of large graphs, which can be useful in various applications.



## Find Minimum Cost Spanning Tree of a given undirected graph using Prim’s algorithm

Prim's algorithm is a popular algorithm for finding the minimum cost spanning tree of a given undirected graph. It is an example of a greedy algorithm that works by selecting the minimum weight edge that connects any two trees in the graph at each iteration, until all the vertices are included in the tree. The algorithm has a time complexity of O(ElogV), where E is the number of edges and V is the number of vertices in the graph.

Here are the steps to implement Prim's algorithm:

1. Initialize a set of visited vertices to an empty set and a set of unvisited vertices to all vertices in the graph.

2. Choose any vertex from the unvisited set as the starting vertex, and add it to the visited set.

3. For each adjacent vertex to the starting vertex, create a new edge with the weight of the edge connecting the two vertices.

4. Add these new edges to a priority queue or a heap, sorted by their weight.

5. While the priority queue or heap is not empty, remove the edge with the smallest weight from the queue.

6. If the vertices connected by the edge are already in the visited set, discard the edge.

7. Otherwise, add the edge to the minimum spanning tree and add the new vertex to the visited set.

8. Repeat steps 3 to 7 until all vertices are in the visited set.

9. The minimum cost spanning tree is the collection of edges in the minimum spanning tree.

Here is an example implementation of Prim's algorithm in Python:

```
# Python implementation of Prim's algorithm for finding minimum cost spanning tree
import heapq

def prim(graph):
    visited = set()
    unvisited = set(graph.keys())
    start = next(iter(unvisited))
    visited.add(start)
    unvisited.remove(start)
    heap = []
    for dest, weight in graph[start].items():
        heapq.heappush(heap, (weight, start, dest))
    mst = []
    while heap:
        weight, src, dest = heapq.heappop(heap)
        if dest in visited:
            continue
        visited.add(dest)
        unvisited.remove(dest)
        mst.append((src, dest, weight))
        for dest2, weight2 in graph[dest].items():
            if dest2 not in visited:
                heapq.heappush(heap, (weight2, dest, dest2))
    return mst
```

In this implementation, the graph is represented as a dictionary where the keys are the vertices and the values are another dictionary that maps adjacent vertices to the weight of the connecting edge. The function returns a list of tuples representing the edges in the minimum cost spanning tree.

In conclusion, Prim's algorithm is a simple and efficient way to find the minimum cost spanning tree of a given undirected graph. The algorithm works by greedily choosing the minimum weight edge at each iteration, and has a time complexity of O(ElogV).



## Write programs to (a) Implement All-Pairs Shortest Paths problem using Floyd's algorithm. (b) Implement Travelling Sales Person problem using Dynamic programming.

In the Design and Analysis of Algorithm Lab, we will learn about two important problems in the field of algorithms - the All-Pairs Shortest Paths problem and the Travelling Sales Person problem. We will also learn to implement them using two popular algorithms, Floyd's algorithm and Dynamic programming, respectively. Let's discuss them in detail:

### All-Pairs Shortest Paths problem

The All-Pairs Shortest Paths problem is to find the shortest path between all pairs of vertices in a given graph. Floyd's algorithm is a popular algorithm used to solve this problem. Here are the steps to implement it:

1. Create a 2D array `dist` of size `n x n` to store the shortest distances between all pairs of vertices, where `n` is the number of vertices in the graph.
2. Initialize the array `dist` with the weights of the edges in the graph. If there is no edge between two vertices, the distance between them is considered as infinity.
3. For each vertex `k`, iterate over all pairs of vertices `i` and `j` and update the value of `dist[i][j]` as `min(dist[i][j], dist[i][k] + dist[k][j])`.
4. After iterating over all vertices, the array `dist` will contain the shortest distances between all pairs of vertices in the graph.

### Travelling Sales Person problem

The Travelling Sales Person problem is to find the shortest possible route that visits every city exactly once and returns to the starting city. Dynamic programming is a popular algorithm used to solve this problem. Here are the steps to implement it:

1. Create a 2D array `dp` of size `2^n x n` to store the optimal solutions to subproblems, where `n` is the number of cities in the given graph.
2. Initialize the first row of the array `dp` with the distances between the starting city and all other cities in the graph.
3. For each subproblem `S` of size `k`, where `k` ranges from 2 to `n`, iterate over all possible sets of cities `T` of size `k` that contain the starting city and are a subset of `S`. For each set `T`, calculate the optimal route that visits all cities in `T` exactly once and returns to the starting city. Update the value of `dp[S][i]` as `min(dp[S-T][j] + dist[j][i])`, where `j` is the last city visited before returning to the starting city.
4. After iterating over all subproblems, the optimal route that visits every city exactly once and returns to the starting city can be obtained from the value of `dp[2^n-1][i]`, where `i` is the starting city.

By implementing these two algorithms, we can efficiently solve the All-Pairs Shortest Paths problem and the Travelling Sales Person problem.



## Design and implement to find a subset of a given set S = {Sl, S2,.....,Sn} of n positive integers whose SUM is equal to a given positive integer d.

Given a set of positive integers S and a target positive integer d, the problem is to find a subset of S whose sum is equal to d. If such a subset exists, the algorithm should return the subset. Otherwise, it should display a message indicating that the problem instance doesn't have a solution.

### Algorithm

The algorithm for solving this problem can be implemented using dynamic programming. The steps involved are:

1. Create a 2-D array of size (n+1) x (d+1), where n is the number of elements in the set S and d is the target sum.
2. Initialize the first column of the array to True and the first row to False.
3. For each element in the set S, iterate through the columns of the array from d to the value of the element.
4. If the previous row at the current column minus the value of the current element is True, set the current cell to True. Otherwise, set it to False.
5. If the cell at the bottom right of the array is True, backtrack through the array to find the subset that adds up to d.

### Pseudo Code

```
function find_subset(S, d):
    n = len(S)
    table = [[False] * (d+1) for _ in range(n+1)]
    
    for i in range(n+1):
        table[i][0] = True
    
    for i in range(1, n+1):
        for j in range(1, d+1):
            if j < S[i-1]:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = table[i-1][j] or table[i-1][j-S[i-1]]
    
    if not table[n][d]:
        print("No solution exists")
        return None
    
    subset = []
    i = n
    j = d
    while j > 0:
        if table[i-1][j]:
            i -= 1
        else:
            subset.append(S[i-1])
            j -= S[i-1]
            i -= 1
    
    print("Subset that adds up to d:", subset)
    return subset
```

### Time Complexity

The time complexity of this algorithm is O(nd), where n is the number of elements in the set S and d is the target sum. This is because we iterate through all the elements of the set S and for each element, we iterate through all the possible sums from 1 to d.

### Space Complexity

The space complexity of this algorithm is O(nd), as we need to create a 2-D array of size (n+1) x (d+1) to store the intermediate results.



## Design and implement to find all Hamiltonian Cycles in a connected undirected Graph G of n vertices using backtracking principle.

In this lab, we will discuss how to find all Hamiltonian Cycles in a connected undirected Graph G of n vertices using backtracking principle. Here are the steps to design and implement this algorithm:

1. Start by defining a Graph G with n vertices and representing it using an adjacency matrix or list.

2. Initialize an empty path array and a boolean array to keep track of visited vertices.

3. Choose a starting vertex and add it to the path array. Mark the vertex as visited.

4. Recursively explore all the unvisited neighbors of the last vertex added to the path array.

5. If a neighbor is not visited, add it to the path array and mark it as visited.

6. If a neighbor is already visited, check if it is the starting vertex. If it is, then a Hamiltonian Cycle has been found. Print the path array as the cycle.

7. If the neighbor is not the starting vertex, continue exploring its unvisited neighbors.

8. If there are no unvisited neighbors, backtrack by removing the last vertex from the path array and marking it as unvisited.

9. Repeat steps 4-8 until all possible Hamiltonian Cycles have been found.

10. To ensure that all possible cycles are found, we need to explore all possible starting vertices. Thus, we need to repeat steps 3-9 for each vertex in the Graph G.

11. Finally, print all the Hamiltonian Cycles found.

The time complexity of this algorithm is O(n!), since there can be n! possible Hamiltonian Cycles in a Graph with n vertices. However, since we are using backtracking, we can prune the search tree and reduce the actual running time.

In conclusion, finding all Hamiltonian Cycles in a connected undirected Graph G of n vertices using backtracking principle involves exploring all possible paths and checking if they form a cycle. The above steps provide a general outline for designing and implementing this algorithm.

