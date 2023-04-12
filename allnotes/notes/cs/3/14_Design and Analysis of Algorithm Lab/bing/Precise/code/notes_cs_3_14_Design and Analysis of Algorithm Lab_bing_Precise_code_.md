

## Program for Recursive Binary & Linear Search for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

### Linear Search
Linear search is a simple search algorithm that checks each element of a list or array until the desired element is found or the end of the list is reached. Here is an example of a recursive linear search function in Python:

```python
def recursive_linear_search(arr, l, r, x):
    if r < l:
        return -1
    if arr[l] == x:
        return l
    if arr[r] == x:
        return r
    return recursive_linear_search(arr, l+1, r-1, x)
```

In this function, `arr` is the list or array being searched, `l` and `r` are the left and right indices of the search range, and `x` is the element being searched for. The function returns the index of the element if it is found, or -1 if it is not found.

### Binary Search
Binary search is a more efficient search algorithm that works on sorted lists or arrays. It repeatedly divides the search range in half until the desired element is found or the search range is empty. Here is an example of a recursive binary search function in Python:

```python
def recursive_binary_search(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return recursive_binary_search(arr, l, mid-1, x)
        else:
            return recursive_binary_search(arr, mid+1, r, x)
    else:
        return -1
```

In this function, `arr` is the sorted list or array being searched, `l` and `r` are the left and right indices of the search range, and `x` is the element being searched for. The function returns the index of the element if it is found, or -1 if it is not found.

Both linear and binary search can be implemented recursively, as shown in the examples above. The choice of which algorithm to use depends on the specific use case and the characteristics of the data being searched. In general, binary search is more efficient for large, sorted data sets, while linear search may be more suitable for small or unsorted data sets.



## Program for Heap Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure. Here are the steps to implement heap sort:

1. Build a max heap from the input data.
2. The largest item is stored at the root of the heap. Replace it with the last item of the heap followed by reducing the size of the heap by 1. Heapify the root of the tree.
3. Repeat step 2 while the size of the heap is greater than 1.

Here is an example of a heap sort program in C:

```c
#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void heapify(int arr[], int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && arr[left] > arr[largest])
        largest = left;

    if (right < n && arr[right] > arr[largest])
        largest = right;

    if (largest != i) {
        swap(&arr[i], &arr[largest]);
        heapify(arr, n, largest);
    }
}

void heapSort(int arr[], int n) {
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    for (int i = n - 1; i >= 0; i--) {
        swap(&arr[0], &arr[i]);
        heapify(arr, i, 0);
    }
}

int main() {
    int arr[] = {12, 11, 13, 5, 6, 7};
    int n = sizeof(arr) / sizeof(arr[0]);

    heapSort(arr, n);

    printf("Sorted array is \n");
    for (int i = 0; i < n; ++i)
        printf("%d ", arr[i]);
    printf("\n");
}
```

This program first builds a max heap from the input data. Then, it repeatedly swaps the first element of the array (which is the maximum value) with the last element, reduces the size of the heap by 1, and heapifies the root. This process is repeated until the size of the heap is 1.

Heap sort has a time complexity of O(n log n) for both the best and worst cases. It is an in-place sorting algorithm, meaning it only requires a constant amount of additional memory. However, it is not a stable sort, meaning the relative order of equal elements is not preserved.



## Program for Merge Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

Merge sort is a sorting algorithm that uses the divide-and-conquer approach. It works by dividing the unsorted list into n sub-lists, each containing one element, and then repeatedly merging sub-lists to produce new sorted sub-lists until there is only one sub-list remaining, which is the sorted list.

Here is an example of a merge sort program in C:

```c
#include <stdio.h>
void merge(int arr[], int l, int m, int r)
{
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;
    int L[n1], R[n2];
    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];
    i = 0;
    j = 0;
    k = l;
    while (i < n1 && j < n2)
    {
        if (L[i] <= R[j])
        {
            arr[k] = L[i];
            i++;
        }
        else
        {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
    while (i < n1)
    {
        arr[k] = L[i];
        i++;
        k++;
    }
    while (j < n2)
    {
        arr[k] = R[j];
        j++;
        k++;
    }
}
void mergeSort(int arr[], int l, int r)
{
    if (l < r)
    {
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}
void printArray(int A[], int size)
{
    int i;
    for (i = 0; i < size; i++)
        printf("%d ", A[i]);
    printf("\n");
}
int main()
{
    int arr[] = {12, 11, 13, 5, 6, 7};
    int arr_size = sizeof(arr) / sizeof(arr[0]);
    printf("Given array is \n");
    printArray(arr, arr_size);
    mergeSort(arr, 0, arr_size - 1);
    printf("\nSorted array is \n");
    printArray(arr, arr_size);
    return 0;
}
```

This program first defines a `merge` function that takes an array, the left index, the middle index, and the right index as arguments. This function merges two sub-arrays of the given array. The first sub-array is `arr[l..m]` and the second sub-array is `arr[m+1..r]`.

The program also defines a `mergeSort` function that takes an array, the left index, and the right index as arguments. This function recursively sorts the given array using the `merge` function.

Finally, the program defines a `printArray` function that takes an array and its size as arguments and prints the elements of the array.

In the `main` function, the program creates an array of integers, prints the given array, sorts the array using the `mergeSort` function, and then prints the sorted array.

The time complexity of the merge sort algorithm is O(nlogn) in the worst case, where n is the number of elements in the array. The space complexity of the merge sort algorithm is O(n), where n is the number of elements in the array.



## Program for Selection Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

Selection sort is a simple sorting algorithm that sorts an array by repeatedly finding the minimum element from the unsorted part of the array and swapping it with the first element of the unsorted part.

Here is the algorithm for selection sort:

1. Find the minimum element in the unsorted array.
2. Swap the minimum element with the first element of the unsorted array.
3. Repeat the above steps for the remaining unsorted part of the array.

Here is an example of a selection sort program in C:

```c
#include <stdio.h>

void selectionSort(int arr[], int n) {
    int i, j, min_idx;
    for (i = 0; i < n-1; i++) {
        min_idx = i;
        for (j = i+1; j < n; j++)
            if (arr[j] < arr[min_idx])
                min_idx = j;
        int temp = arr[min_idx];
        arr[min_idx] = arr[i];
        arr[i] = temp;
    }
}

int main() {
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr)/sizeof(arr[0]);
    selectionSort(arr, n);
    printf("Sorted array: \n");
    for (int i=0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
    return 0;
}
```

This program sorts an array of integers using the selection sort algorithm. The `selectionSort` function takes an array and its size as arguments and sorts the array in ascending order.

Selection sort has a time complexity of O(n^2) in the worst case, where n is the number of elements in the array. This makes it inefficient for large datasets. However, it is easy to understand and implement, making it a good choice for small datasets or for educational purposes.



## Program for Insertion Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

Insertion sort is a simple sorting algorithm that works by building the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

Here are the steps for implementing insertion sort:

1. Start by iterating through the array from the second element to the last element.
2. For each element, compare it with the elements before it.
3. If the current element is smaller than the previous element, swap them.
4. Continue swapping until the current element is in its correct position.
5. Repeat the process for the next element until the entire array is sorted.

Here is an example of insertion sort implemented in C:

```c
#include <stdio.h>

void insertionSort(int arr[], int n) {
    int i, key, j;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

void printArray(int arr[], int n) {
    int i;
    for (i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main() {
    int arr[] = {12, 11, 13, 5, 6};
    int n = sizeof(arr) / sizeof(arr[0]);

    insertionSort(arr, n);
    printArray(arr, n);

    return 0;
}
```

This program sorts an array of integers using the insertion sort algorithm. The `insertionSort` function takes in an array and its size as arguments and sorts the array in ascending order. The `printArray` function is used to print the sorted array.

Insertion sort has a time complexity of O(n^2) in the worst case, where n is the number of elements in the array. This makes it inefficient for large datasets. However, it has the advantage of being simple to implement and can be useful for small datasets or partially sorted data. It is also a stable sorting algorithm, meaning that it maintains the relative order of equal elements in the sorted output.



## Program for Quick Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

Quick Sort is a sorting algorithm that uses the divide-and-conquer approach. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The function then recursively sorts the sub-arrays.

Here is an example of a Quick Sort program in C:

```c
#include <stdio.h>

void swap(int* a, int* b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

int partition (int arr[], int low, int high)
{
    int pivot = arr[high];
    int i = (low - 1);

    for (int j = low; j <= high- 1; j++)
    {
        if (arr[j] <= pivot)
        {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}

void quickSort(int arr[], int low, int high)
{
    if (low < high)
    {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

void printArray(int arr[], int size)
{
    int i;
    for (i=0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main()
{
    int arr[] = {10, 7, 8, 9, 1, 5};
    int n = sizeof(arr)/sizeof(arr[0]);
    quickSort(arr, 0, n-1);
    printf("Sorted array: \n");
    printArray(arr, n);
    return 0;
}
```

This program first includes the necessary libraries and defines a `swap` function to swap two elements. The `partition` function takes the array, the starting index, and the ending index as arguments and partitions the array around the pivot element. The `quickSort` function recursively sorts the sub-arrays, and the `printArray` function prints the sorted array.

The `main` function initializes the array to be sorted, calls the `quickSort` function, and then prints the sorted array using the `printArray` function.

This is a basic example of a Quick Sort program. It can be further optimized and modified according to specific needs.



## Knapsack Problem using Greedy Solution

The knapsack problem is a problem in combinatorial optimization. Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.

The greedy solution to the knapsack problem is a heuristic algorithm that does not always produce the optimal solution. However, it is simple to implement and can provide a good approximation to the optimal solution in many cases.

The greedy solution to the knapsack problem works as follows:
1. Sort the items in decreasing order of value per unit weight.
2. Starting with the item with the highest value per unit weight, add as many of that item as possible to the knapsack without exceeding the weight limit.
3. Move on to the next item in the sorted list and repeat the process until the knapsack is full or there are no more items to add.

This approach is called a greedy algorithm because it makes the locally optimal choice at each step, without considering the overall problem. In some cases, this can lead to suboptimal solutions. However, the greedy solution to the knapsack problem can provide a good approximation to the optimal solution, especially when the items have similar weights.

It is important to note that the greedy solution to the knapsack problem is not guaranteed to produce the optimal solution. In some cases, it may be necessary to use a more sophisticated algorithm, such as dynamic programming, to find the optimal solution to the knapsack problem. However, the greedy solution can be a useful starting point for solving the knapsack problem, especially when a quick, approximate solution is sufficient.



## Perform Travelling Salesman Problem for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

The Travelling Salesman Problem (TSP) is a problem in the field of computer science and operations research. It is defined as follows: Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?

1. The TSP is an NP-hard problem, meaning that there is no known polynomial-time algorithm to solve it.
2. There are several approaches to solving the TSP, including exact algorithms, heuristic algorithms, and approximation algorithms.
3. Exact algorithms, such as the Held-Karp algorithm, guarantee to find the optimal solution but can take a long time to run for large instances of the problem.
4. Heuristic algorithms, such as the nearest neighbor algorithm, do not guarantee to find the optimal solution but can find good solutions quickly for large instances of the problem.
5. Approximation algorithms, such as the Christofides algorithm, guarantee to find a solution within a certain factor of the optimal solution and can also be used for large instances of the problem.

In the Design and Analysis of Algorithm Lab, students can implement and compare the performance of different algorithms for solving the TSP. This can help them understand the trade-offs between different approaches and the importance of algorithm design and analysis in real-time systems.



## Find Minimum Spanning Tree using Kruskal’s Algorithm for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Kruskal's algorithm is a greedy algorithm that finds a minimum spanning tree for a connected weighted graph.
- The algorithm operates by adding edges to the spanning tree in increasing order of their weight, as long as the edge does not create a cycle.
- The algorithm can be implemented using a disjoint-set data structure to keep track of the connected components of the graph.
- The time complexity of Kruskal's algorithm is O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices in the graph.
- The algorithm can be used to find the minimum spanning tree of a graph in real-time systems, where efficiency and speed are important.



## Implement N Queen Problem using Backtracking for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

The N Queen problem is a classic problem in computer science. The goal is to place N queens on an NxN chessboard such that no two queens threaten each other. This means that no two queens can share the same row, column, or diagonal.

Backtracking is a general algorithm for finding all (or some) solutions to a problem. It incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution.

Here are the steps to implement the N Queen problem using backtracking:

1. Start in the leftmost column.
2. If all queens are placed, return true.
3. Try all rows in the current column. For each row, do the following:
    a. If the queen can be placed safely in this row, mark this [row, column] as part of the solution and recursively check if placing the queen here leads to a solution.
    b. If placing the queen in [row, column] leads to a solution, return true.
    c. If placing the queen doesn't lead to a solution, unmark this [row, column] (backtrack) and go to step 3 to try other rows.
4. If all rows have been tried and nothing worked, return false to trigger backtracking.

This algorithm can be implemented using recursion. The base case is when all queens are placed (i.e., when the column index is equal to N). The recursive case is when we try to place a queen in a given row and column, and then recursively try to place the rest of the queens.

The time complexity of this algorithm is O(N!) because there are N! permutations of rows to place the queens. However, the backtracking algorithm prunes the search space significantly, so it is much faster in practice than generating all permutations. The space complexity is O(N) because we need to store the column index of the queen in each row.



## Quick Sort

Quick Sort is a sorting algorithm that uses the divide-and-conquer approach. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The function then recursively sorts the sub-arrays.

The time complexity of Quick Sort depends on the implementation. In the worst case, the time complexity is O(n^2), where n is the number of elements in the array. This occurs when the pivot element is the smallest or largest element in the array, causing one of the partitions to be empty. In the average case, the time complexity is O(n log n).

To demonstrate the time complexity of Quick Sort, we can run the algorithm on varied values of n > 5000 and record the time taken to sort. We can then plot a graph of the time taken versus n on a graph sheet.

The elements to be sorted can be read from a file or generated using a random number generator. Here is an example implementation of Quick Sort in Java:

```java
public class QuickSort {
    public static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }

    public static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = (low - 1);
        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
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
}
```

This implementation of Quick Sort uses the last element as the pivot. The `partition` function takes the array, the starting index, and the ending index as arguments, and returns the index of the pivot element. The `quickSort` function recursively sorts the sub-arrays on either side of the pivot.

The worst-case time complexity of this implementation is O(n^2), while the average-case time complexity is O(n log n). The best-case time complexity is also O(n log n), which occurs when the pivot element is the median of the array, causing the partitions to be of equal size.



## Merge Sort

Merge Sort is a popular sorting algorithm that uses the divide-and-conquer approach to sort a given set of n integer elements. The algorithm works by dividing the input into two halves, recursively sorting each half, and then merging the two sorted halves together to form the final sorted output.

The time complexity of Merge Sort can be computed as follows:

- **Worst Case:** The worst case time complexity of Merge Sort is O(n log n). This occurs when the input array is already sorted in reverse order, as the algorithm has to perform the maximum number of comparisons and swaps.

- **Average Case:** The average case time complexity of Merge Sort is also O(n log n), as the algorithm performs a similar number of operations on average.

- **Best Case:** The best case time complexity of Merge Sort is O(n log n), as the algorithm still has to divide the input into two halves and recursively sort each half, even if the input is already sorted.

To demonstrate the time complexity of Merge Sort, the algorithm can be run on varied values of n > 5000 and the time taken to sort can be recorded. A graph can be plotted of the time taken versus n on a graph sheet. The elements to be sorted can be read from a file or generated using a random number generator.

In summary, Merge Sort is an efficient sorting algorithm that uses the divide-and-conquer approach to sort a given set of n integer elements. Its time complexity is O(n log n) in the worst, average, and best cases. The algorithm can be demonstrated by running it on varied values of n and plotting a graph of the time taken to sort versus n.



## Implementing the 0/1 Knapsack problem using (a) Dynamic Programming method (b) Greedy method

The 0/1 Knapsack problem is a combinatorial optimization problem where the goal is to maximize the total value of items that can be placed into a knapsack of limited capacity. Each item has a weight and a value, and only one of each item can be selected. There are two common methods to solve this problem: the Dynamic Programming method and the Greedy method.

### (a) Dynamic Programming method

The Dynamic Programming method is an efficient approach to solve the 0/1 Knapsack problem. It is based on the principle of optimality, which states that an optimal solution to a problem can be constructed from optimal solutions to its subproblems.

1. Create a 2D array `K[n+1][W+1]` where `n` is the number of items and `W` is the maximum capacity of the knapsack.
2. Initialize the first row and the first column of the array to 0.
3. For each item `i` from 1 to `n`, and for each capacity `w` from 1 to `W`, do the following:
    - If the weight of the item `i` is less than or equal to `w`, then set `K[i][w]` to the maximum of `K[i-1][w]` and `K[i-1][w-wt[i-1]] + val[i-1]`.
    - Otherwise, set `K[i][w]` to `K[i-1][w]`.
4. The maximum value that can be placed into the knapsack is `K[n][W]`.

### (b) Greedy method

The Greedy method is a simple approach to solve the 0/1 Knapsack problem. It is based on the idea of selecting the most valuable items first, until the knapsack is full or there are no more items to select.

1. Calculate the value per unit weight for each item, and sort the items in decreasing order of this value.
2. Initialize the total value of the knapsack to 0 and the remaining capacity of the knapsack to `W`.
3. For each item `i` from 1 to `n`, do the following:
    - If the weight of the item `i` is less than or equal to the remaining capacity of the knapsack, then add the item to the knapsack, update the total value of the knapsack, and decrease the remaining capacity of the knapsack by the weight of the item.
    - Otherwise, break the loop.
4. The maximum value that can be placed into the knapsack is the total value of the knapsack.

It is important to note that the Greedy method does not always produce an optimal solution to the 0/1 Knapsack problem. However, it is a simple and fast approach that can provide a good approximation to the optimal solution in many cases. In contrast, the Dynamic Programming method always produces an optimal solution, but it can be more time-consuming to implement and execute. The choice of method depends on the specific requirements of the problem at hand.



## From a given vertex in a weighted connected graph, find shortest paths to other vertices using Dijkstra's algorithm.

Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph. It was conceived by computer scientist Edsger W. Dijkstra in 1956. The algorithm exists in many variants; Dijkstra's original variant found the shortest path between two nodes, but a more common variant fixes a single node as the "source" node and finds shortest paths from the source to all other nodes in the graph, producing a shortest-path tree.

Here are the steps to find the shortest paths from a given vertex in a weighted connected graph using Dijkstra's algorithm:

1. Create a set of all the unvisited vertices called the unvisited set.
2. Assign to every vertex a tentative distance value: set it to zero for our initial vertex and to infinity for all other vertices. Set the initial vertex as current.
3. For the current vertex, consider all of its unvisited neighbors and calculate their tentative distances through the current vertex. Compare the newly calculated tentative distance to the current assigned value and assign the new value if it is less than the current assigned value.
4. When we are done considering all of the unvisited neighbors of the current vertex, mark the current vertex as visited and remove it from the unvisited set. A visited vertex will never be checked again.
5. If the destination vertex has been marked visited (when planning a route between two specific vertices) or if the smallest tentative distance among the vertices in the unvisited set is infinity (when planning a complete traversal; occurs when there is no connection between the initial vertex and remaining unvisited vertices), then the algorithm has finished.
6. Otherwise, select the unvisited vertex that is marked with the smallest tentative distance, set it as the new current vertex, and go back to step 3.




## Find Minimum Cost Spanning Tree of a given connected undirected graph using Kruskal's algorithm. Use Union-Find algorithms in your program.

Kruskal's algorithm is a greedy algorithm that finds a minimum spanning tree for a connected weighted graph. This means it finds a subset of the edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is minimized.

Here are the steps for implementing Kruskal's algorithm:
1. Sort all the edges in non-decreasing order of their weight.
2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
3. Repeat step 2 until there are (V-1) edges in the spanning tree, where V is the number of vertices in the given graph.

To detect if an edge forms a cycle with the current spanning tree, we can use the Union-Find algorithm. The Union-Find algorithm is used to keep track of a partition of a set into disjoint subsets. It has two primary operations: Find and Union.

- **Find**: Determine which subset a particular element is in. This can be used to determine if two elements are in the same subset.
- **Union**: Join two subsets into a single subset.

In the context of Kruskal's algorithm, we can use the Union-Find algorithm to keep track of the connected components in the current spanning tree. When we consider adding an edge to the tree, we can use the Find operation to determine if the two vertices connected by the edge are already in the same connected component. If they are, then adding the edge would create a cycle, so we discard it. If they are not, then we can use the Union operation to merge the two connected components into one.

Here is an example of how the algorithm might work on a given connected undirected graph:

1. Sort all the edges in non-decreasing order of their weight.
2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
3. Repeat step 2 until there are (V-1) edges in the spanning tree.




## Find Minimum Cost Spanning Tree of a given undirected graph using Prim’s algorithm

Prim's algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph. This means it finds a subset of the edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is minimized.

Here are the steps to follow to implement Prim's algorithm:

1. Initialize the minimum spanning tree with a vertex chosen at random.
2. Find all the edges that connect the tree to new vertices, find the minimum and add it to the tree.
3. Keep repeating step 2 until all the vertices are in the tree.

The time complexity of Prim's algorithm depends on the data structures used for the graph and for ordering the edges by weight, which can be done using a priority queue. Using an adjacency matrix representation and a binary heap-based priority queue, Prim's algorithm can be shown to run in O(V^2) time, where V is the number of vertices in the graph.

This algorithm can be useful for solving problems in the Design and Analysis of Algorithm Lab in the subject of Real Time Systems. It is important to understand the steps and the time complexity of the algorithm in order to apply it effectively.



## Design and Analysis of Algorithm Lab: Real Time System

### Floyd's Algorithm for All-Pairs Shortest Paths Problem

Floyd's algorithm is an efficient algorithm for finding the shortest paths between all pairs of vertices in a weighted graph. The algorithm works by iteratively improving an estimate of the shortest path distances between all pairs of vertices until the estimate is accurate.

Here is the pseudocode for Floyd's algorithm:

```
let dist be a |V| × |V| array of minimum distances initialized to ∞ (infinity)
for each edge (u,v)
    dist[u][v] ← w(u,v)  // the weight of the edge (u,v)
for each vertex v
    dist[v][v] ← 0
for k from 1 to |V|
    for i from 1 to |V|
        for j from 1 to |V|
            if dist[i][j] > dist[i][k] + dist[k][j] 
                dist[i][j] ← dist[i][k] + dist[k][j]
            end if
```

### Dynamic Programming for Travelling Sales Person Problem

The Travelling Sales Person (TSP) problem is a well-known NP-hard problem in computer science. It involves finding the shortest possible route that visits a given set of cities and returns to the starting city. Dynamic programming can be used to solve the TSP problem by breaking it down into smaller subproblems and solving them recursively.

Here is the pseudocode for solving the TSP problem using dynamic programming:

```
function TSP(graph, start)
    let n = number of vertices in graph
    let C = array of size [1..n, 1..2^(n-1)] initialized to ∞
    C[start, {start}] = 0
    for s = 2 to n
        for all subsets S ⊆ {1,2,...,n} of size s and containing start
            for all j ∈ S, j ≠ start
                C[j,S] = min { C[i,S-{j}] + d(i,j) : i ∈ S, i ≠ j }
            end for
        end for
    end for
    return min { C[i,{1,2,...,n}] + d(i,start) : i ∈ {1,2,...,n}, i ≠ start }
```

In the above pseudocode, `C[j,S]` represents the minimum cost of visiting all vertices in the set `S` and ending at vertex `j`. The function `d(i,j)` represents the distance between vertices `i` and `j`. The final result is the minimum cost of visiting all vertices and returning to the starting vertex.



## Design and implement to find a subset of a given set S = {Sl, S2,.....,Sn} of n positive integers whose SUM is equal to a given positive integer d.

This problem can be solved using a recursive approach. The idea is to consider two cases for every element. Either we include the current element in the subset or we do not include it. We recursively call the function for both cases. If the remaining sum becomes 0, we have found a subset with the given sum.

Here is the algorithm to solve the problem:

1. Create a function `subset_sum` that takes the set `S`, the remaining sum `d`, the current index `i`, and the current subset as input.
2. If the remaining sum is 0, print the current subset and return.
3. If the remaining sum is negative or the current index is greater than or equal to the length of the set, return.
4. Call the function `subset_sum` recursively with the current element included in the subset and the remaining sum reduced by the current element.
5. Call the function `subset_sum` recursively without including the current element in the subset.
6. In the main function, call the function `subset_sum` with the initial values of the remaining sum, current index, and current subset.

Here is an example implementation in Python:

```python
def subset_sum(S, d, i, subset):
    if d == 0:
        print(subset)
        return
    if d < 0 or i >= len(S):
        return
    subset_sum(S, d - S[i], i + 1, subset + [S[i]])
    subset_sum(S, d, i + 1, subset)

S = [1, 2, 5, 6, 8]
d = 9
subset_sum(S, d, 0, [])
```

This implementation will print the two solutions `{1, 2, 6}` and `{1, 8}` for the given example. If there are no solutions, no subsets will be printed. A suitable message can be displayed by checking if any subsets were printed or not.

This algorithm has an exponential time complexity as it generates all possible subsets of the given set. However, it can be optimized using dynamic programming techniques.



## Design and implement to find all Hamiltonian Cycles in a connected undirected Graph G of n vertices using backtracking principle

A Hamiltonian cycle is a cycle in an undirected graph that visits each vertex exactly once and returns to the starting vertex. The problem of finding a Hamiltonian cycle in a graph is NP-complete, meaning that there is no known efficient algorithm to solve it in all cases.

However, one approach to finding all Hamiltonian cycles in a connected undirected graph G of n vertices is to use the backtracking principle. This involves recursively exploring all possible paths in the graph, while keeping track of the vertices visited so far, and backtracking when a dead end is reached.

Here are the steps to implement this approach:

1. Start with an empty path and a boolean array visited[] of size n, initialized to false.
2. Choose a starting vertex and mark it as visited.
3. Recursively explore all unvisited neighbors of the current vertex, adding them to the path and marking them as visited.
4. If all vertices have been visited and the current vertex is adjacent to the starting vertex, a Hamiltonian cycle has been found. Print or store the cycle.
5. Backtrack by removing the current vertex from the path and marking it as unvisited.
6. Repeat steps 3-5 for all unvisited neighbors of the current vertex.

This algorithm will find all Hamiltonian cycles in the graph by systematically exploring all possible paths and backtracking when a dead end is reached. The time complexity of this algorithm is exponential, as it must explore all possible paths in the worst case. However, it can be an effective approach for small graphs or graphs with certain properties that make it easier to find Hamiltonian cycles.

This is a brief overview of how to design and implement an algorithm to find all Hamiltonian cycles in a connected undirected graph using the backtracking principle. It is important to note that this is just one approach and there may be other algorithms that can solve this problem more efficiently in certain cases. It is always a good idea to carefully analyze the properties of the graph and the requirements of the problem before choosing an algorithm to solve it.

