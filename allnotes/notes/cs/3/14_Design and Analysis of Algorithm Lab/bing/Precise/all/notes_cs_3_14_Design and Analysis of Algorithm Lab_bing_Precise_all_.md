

## Program for Recursive Binary & Linear Search for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

### Linear Search
Linear search is a simple search algorithm that checks each element of a list or array sequentially until the desired element is found. Here is an example of a recursive linear search program in C++:

```c++
#include <iostream>
using namespace std;

int recursiveLinearSearch(int arr[], int l, int r, int x)
{
    if (r < l)
        return -1;
    if (arr[l] == x)
        return l;
    if (arr[r] == x)
        return r;
    return recursiveLinearSearch(arr, l + 1, r - 1, x);
}

int main()
{
    int arr[] = { 2, 3, 4, 10, 40 };
    int n = sizeof(arr) / sizeof(arr[0]);
    int x = 10;
    int index = recursiveLinearSearch(arr, 0, n - 1, x);
    if (index != -1)
        cout << "Element " << x << " is present at index " << index;
    else
        cout << "Element " << x << " is not present in the array";
    return 0;
}
```

### Binary Search
Binary search is an efficient search algorithm that works by repeatedly dividing the search interval in half. It requires the input list or array to be sorted. Here is an example of a recursive binary search program in C++:

```c++
#include <iostream>
using namespace std;

int recursiveBinarySearch(int arr[], int l, int r, int x)
{
    if (r >= l) {
        int mid = l + (r - l) / 2;
        if (arr[mid] == x)
            return mid;
        if (arr[mid] > x)
            return recursiveBinarySearch(arr, l, mid - 1, x);
        return recursiveBinarySearch(arr, mid + 1, r, x);
    }
    return -1;
}

int main()
{
    int arr[] = { 2, 3, 4, 10, 40 };
    int n = sizeof(arr) / sizeof(arr[0]);
    int x = 10;
    int result = recursiveBinarySearch(arr, 0, n - 1, x);
    (result == -1) ? cout << "Element is not present in array"
                   : cout << "Element is present at index " << result;
    return 0;
}
```

Both linear and binary search algorithms can be implemented recursively. The recursive approach can make the code more readable and easier to understand, but it may not always be the most efficient solution. It is important to analyze the time and space complexity of the algorithm and choose the appropriate approach for the specific problem at hand.



## Program for Heap Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure. It works by dividing the input into a sorted and an unsorted region, and iteratively shrinking the unsorted region by extracting the largest element and moving that to the sorted region. The following are the steps involved in the heap sort algorithm:

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
    int l = 2 * i + 1;
    int r = 2 * i + 2;

    if (l < n && arr[l] > arr[largest])
        largest = l;

    if (r < n && arr[r] > arr[largest])
        largest = r;

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

This program first defines a `swap` function to swap two elements, and a `heapify` function to maintain the max heap property. The `heapSort` function first builds a max heap from the input array, and then repeatedly extracts the maximum element from the heap and moves it to the end of the array. The `main` function demonstrates how to use the `heapSort` function to sort an array of integers.

Heap sort has a time complexity of O(n log n) for both the best and worst cases, making it an efficient sorting algorithm for large data sets. It is also an in-place sorting algorithm, meaning it only requires a constant amount of additional memory to sort the data.



## Program for Merge Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

Merge sort is a sorting algorithm that uses the divide and conquer approach. It works by dividing the unsorted list into n sub-lists, each containing one element, and then repeatedly merging sub-lists to produce new sorted sub-lists until there is only one sub-list remaining, which is the sorted list.

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

This program first defines a function `merge` that takes an array, the left index, the middle index, and the right index as arguments. It then creates two temporary arrays `L` and `R` to store the left and right halves of the array. The function then merges the two halves back into the original array in sorted order.

The `mergeSort` function takes an array, the left index, and the right index as arguments. It recursively divides the array into two halves until the base case is reached, where the sub-array has only one element. It then calls the `merge` function to merge the two halves back into the original array in sorted order.

The `main` function initializes an array and calls the `mergeSort` function to sort the array. It then prints the sorted array.

This is an example of how merge sort can be implemented in C. It is an efficient sorting algorithm with a time complexity of O(n log n) in the worst case. It is also a stable sorting algorithm, meaning that the relative order of equal elements is preserved. It is commonly used in computer science and can be applied to a wide range of problems.



## Program for Selection Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

Selection sort is a simple sorting algorithm that sorts an array by repeatedly finding the minimum element from the unsorted part of the array and swapping it with the first element of the unsorted part. Here is the algorithm for selection sort:

1. Find the minimum element in the unsorted array.
2. Swap the found minimum element with the first element of the unsorted part.
3. Move the boundary of the unsorted part one element to the right.
4. Repeat steps 1-3 until the entire array is sorted.

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

This program sorts an array of integers using the selection sort algorithm. The `selectionSort` function takes as input the array to be sorted and its size, and sorts the array in place. The `main` function initializes an array of integers, calls the `selectionSort` function to sort the array, and then prints the sorted array.

Selection sort has a time complexity of O(n^2), where n is the number of elements in the array. This makes it inefficient for large datasets. However, it has the advantage of being easy to understand and implement.



## Program for Insertion Sort

Insertion sort is a simple sorting algorithm that works by building the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

Here is an example of a program for insertion sort in C:

```c
#include <stdio.h>

void insertionSort(int arr[], int n)
{
    int i, key, j;
    for (i = 1; i < n; i++)
    {
        key = arr[i];
        j = i - 1;

        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

void printArray(int arr[], int n)
{
    int i;
    for (i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main()
{
    int arr[] = {12, 11, 13, 5, 6};
    int n = sizeof(arr) / sizeof(arr[0]);

    insertionSort(arr, n);
    printArray(arr, n);

    return 0;
}
```

This program sorts an array of integers using the insertion sort algorithm. The function `insertionSort` takes as input an array of integers and its size, and sorts the array in ascending order. The function `printArray` is used to print the sorted array.

The time complexity of insertion sort is O(n^2) in the worst case, where n is the number of elements in the array. This makes it inefficient for large datasets. However, it has the advantage of being simple to implement and understand, and it can be efficient for small datasets or partially sorted data.

This program can be used as a reference for the Design and Analysis of Algorithm Lab in the subject of Real Time System. It is important to understand the working of the insertion sort algorithm and its time complexity in order to analyze its performance and compare it with other sorting algorithms.



## Program for Quick Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

Quick Sort is a sorting algorithm that uses the divide and conquer approach. It works by selecting a pivot element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The function then recursively sorts the sub-arrays.

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

This program first includes the necessary libraries and defines a `swap` function to swap two elements. The `partition` function takes the array, the starting index, and the ending index as arguments and returns the partition index. The `quickSort` function takes the array, the starting index, and the ending index as arguments and recursively sorts the sub-arrays. The `printArray` function takes the array and its size as arguments and prints the array. The `main` function defines an array, calculates its size, calls the `quickSort` function to sort the array, and then calls the `printArray` function to print the sorted array.

Quick Sort has an average-case time complexity of O(n log n) and a worst-case time complexity of O(n^2). It is an in-place sorting algorithm, meaning it only requires a constant amount of additional memory. It is also a comparison-based sorting algorithm, meaning it only needs to know the order of elements, not their actual values. Quick Sort is not a stable sorting algorithm, meaning the relative order of equal elements is not preserved. However, it can be made stable with some modifications.

Quick Sort is widely used in practice due to its efficiency and simplicity. It is often used as the default sorting algorithm in many programming languages and libraries. However, it is not always the best choice for all situations, and other sorting algorithms may be more suitable depending on the specific use case. It is important to understand the trade-offs and choose the appropriate sorting algorithm for the task at hand.



## Knapsack Problem using Greedy Solution

The Knapsack Problem is a combinatorial optimization problem where the goal is to select a subset of items with maximum total value, subject to a constraint on the total weight of the selected items. The problem can be solved using a greedy approach, where items are selected based on their value-to-weight ratio.

Here are the steps to solve the Knapsack Problem using a greedy solution:

1. Sort the items in decreasing order of their value-to-weight ratio.
2. Initialize the total weight of the selected items to 0.
3. For each item in the sorted list:
    - If the total weight of the selected items plus the weight of the current item is less than or equal to the weight constraint, add the current item to the selected items and update the total weight of the selected items.
    - Otherwise, continue to the next item.
4. Return the selected items.

This greedy approach does not always produce an optimal solution, but it can provide a good approximation in many cases. It is also relatively simple to implement and has a time complexity of O(n log n), where n is the number of items.

This approach can be used in the Design and Analysis of Algorithm Lab in the subject of Real Time System to solve the Knapsack Problem. It is important to note that this is just one possible solution and other approaches may also be used.



## Travelling Salesman Problem

The Travelling Salesman Problem (TSP) is a problem in the field of computer science and operations research. It is defined as follows: Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?

The TSP is an NP-hard problem, meaning that there is no known polynomial-time algorithm to solve it. However, there are several heuristics and approximation algorithms that can be used to find near-optimal solutions.

Some common approaches to solving the TSP include:
1. Nearest Neighbor: Start at a city and always visit the nearest unvisited city until all cities have been visited.
2. Greedy: At each step, choose the edge with the smallest weight that does not create a cycle with fewer than n edges or increase the degree of any node to more than 2.
3. 2-opt: Start with an initial tour and iteratively improve it by swapping pairs of edges until no further improvement can be made.
4. Branch and Bound: Use a tree search to systematically explore the solution space, using bounds to prune branches that cannot lead to an optimal solution.

These are just a few of the many approaches to solving the TSP. The choice of algorithm will depend on the specific requirements of the problem, such as the number of cities, the accuracy of the solution required, and the time available to find a solution. It is important to carefully analyze the problem and choose the most appropriate algorithm for the situation.



## Find Minimum Spanning Tree using Kruskal’s Algorithm

Kruskal's algorithm is a greedy algorithm that finds a minimum spanning tree for a connected weighted graph. This means it finds a subset of the edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is minimized.

Here are the steps to find the minimum spanning tree using Kruskal's algorithm:

1. Sort all the edges in non-decreasing order of their weight.
2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
3. Repeat step 2 until there are (V-1) edges in the spanning tree, where V is the number of vertices in the graph.

Kruskal's algorithm can be implemented using a disjoint-set data structure to keep track of the subsets of vertices in the spanning tree. This allows for efficient checking of whether adding an edge will form a cycle or not.

This algorithm is commonly used in the Design and Analysis of Algorithm Lab in the subject of Real Time System to find the minimum spanning tree of a graph. It is an important concept to understand and can be useful for solving problems in various fields.



## Implement N Queen Problem using Backtracking for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

The N Queen problem is a classic problem in computer science. The goal is to place N queens on an NxN chessboard such that no two queens threaten each other. This means that no two queens can be in the same row, column, or diagonal.

Backtracking is a general algorithm for finding all (or some) solutions to a problem that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution.

Here are the steps to implement the N Queen problem using backtracking:

1. Start in the leftmost column.
2. If all queens are placed, return true.
3. Try all rows in the current column. For each row, do the following:
    a. If the queen can be placed safely in this row, mark this [row, column] as part of the solution and recursively check if placing the queen here leads to a solution.
    b. If placing the queen in [row, column] leads to a solution, return true.
    c. If placing the queen doesn't lead to a solution, unmark this [row, column] (backtrack) and go to step 3 to try other rows.
4. If all rows have been tried and nothing worked, return false to trigger backtracking.

This algorithm can be implemented using recursion and backtracking. The time complexity of this algorithm is O(N!) as there are N! permutations of the N queens on the NxN chessboard. However, the backtracking helps to prune the search space and reduce the time complexity.




## Quick Sort

Quick Sort is a sorting algorithm that uses the divide-and-conquer approach. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The function then recursively sorts the sub-arrays.

The time complexity of Quick Sort is as follows:
- Worst case: O(n^2)
- Average case: O(n log n)
- Best case: O(n log n)

To demonstrate the time complexity of Quick Sort, we can run the algorithm on varied values of n > 5000 and record the time taken to sort. The elements can be read from a file or generated using a random number generator. The time taken to sort can then be plotted on a graph versus n on a graph sheet.

Here is an example implementation of Quick Sort in Java:

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

This implementation of Quick Sort uses the last element as the pivot. The partition function takes the pivot and places it in its correct position in the sorted array, and places all smaller elements to the left of the pivot and all greater elements to the right of the pivot.

The time complexity of Quick Sort can be analyzed as follows:
- Worst case: The worst case occurs when the partition process always picks the greatest or smallest element as the pivot. This would result in an unbalanced partition and the time complexity would be O(n^2).
- Average case: The average case occurs when the partition process picks the median as the pivot. This would result in a balanced partition and the time complexity would be O(n log n).
- Best case: The best case occurs when the partition process always picks the median as the pivot. This would result in a balanced partition and the time complexity would be O(n log n).

In conclusion, Quick Sort is an efficient sorting algorithm that uses the divide-and-conquer approach. Its time complexity can vary depending on the selection of the pivot, but on average it has a time complexity of O(n log n).



## Sort a given set of n integer elements using Merge Sort method and compute its time complexity

Merge Sort is a popular sorting algorithm that uses the divide-and-conquer approach to sort a given set of n integer elements. The algorithm works by dividing the input into two halves, recursively sorting each half, and then merging the two sorted halves together to form the final sorted output.

The time complexity of Merge Sort can be computed as follows:

1. The algorithm divides the input into two halves, which takes constant time O(1).
2. The algorithm recursively sorts each half, which takes O(n log n) time for each half.
3. The algorithm merges the two sorted halves together, which takes O(n) time.

Therefore, the overall time complexity of Merge Sort is O(n log n).

To demonstrate the time complexity of Merge Sort, the algorithm can be run on varied values of n > 5000, and the time taken to sort can be recorded. A graph of the time taken versus n can be plotted on a graph sheet to visualize the relationship between the input size and the time taken to sort.

The elements to be sorted can be read from a file or generated using a random number generator.

In terms of its time complexity analysis, Merge Sort has a worst-case, average-case, and best-case time complexity of O(n log n). This is because the algorithm always divides the input into two halves and recursively sorts each half, regardless of the input distribution.

In summary, Merge Sort is an efficient sorting algorithm that uses the divide-and-conquer approach to sort a given set of n integer elements. Its time complexity is O(n log n) in the worst, average, and best cases. The algorithm can be demonstrated by running it on varied values of n > 5000 and plotting a graph of the time taken versus n. The elements to be sorted can be read from a file or generated using a random number generator.



## Implementing the 0/1 Knapsack problem using (a) Dynamic Programming method (b) Greedy method

The 0/1 Knapsack problem is a combinatorial optimization problem where we are given a set of items, each with a weight and a value, and we need to determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. There are two common methods to solve this problem: the Dynamic Programming method and the Greedy method.

### (a) Dynamic Programming method

The Dynamic Programming method is an efficient way to solve the 0/1 Knapsack problem. It is based on the principle of optimality, which states that an optimal solution to a problem can be constructed from optimal solutions to its subproblems.

1. Create a 2D array `K[n+1][W+1]` where `n` is the number of items and `W` is the maximum weight the knapsack can carry.
2. Initialize the first row and the first column of the array to 0.
3. For `i` from 1 to `n`, do the following:
    1. For `w` from 1 to `W`, do the following:
        1. If the weight of the `i`-th item is less than or equal to `w`, then `K[i][w] = max(K[i-1][w], K[i-1][w-wt[i-1]] + val[i-1])`.
        2. Else, `K[i][w] = K[i-1][w]`.
4. The maximum value that can be obtained is `K[n][W]`.

### (b) Greedy method

The Greedy method is a simple and intuitive way to solve the 0/1 Knapsack problem. It is based on the idea of selecting the most valuable items first, until the knapsack is full or there are no more items to select.

1. Calculate the value per unit weight for each item and sort the items in decreasing order of their value per unit weight.
2. Initialize the total value of the knapsack to 0 and the total weight of the knapsack to 0.
3. For each item in the sorted list, do the following:
    1. If the weight of the item is less than or equal to the remaining capacity of the knapsack, add the item to the knapsack, update the total value and the total weight of the knapsack.
    2. Else, break the loop.
4. The maximum value that can be obtained is the total value of the knapsack.

It is important to note that the Greedy method does not always produce an optimal solution to the 0/1 Knapsack problem. However, it is a fast and easy-to-implement method that can provide a good approximate solution in many cases. On the other hand, the Dynamic Programming method always produces an optimal solution, but it can be more time-consuming to implement and has a higher time complexity. The choice of method depends on the specific requirements of the problem at hand.



## From a given vertex in a weighted connected graph, find shortest paths to other vertices using Dijkstra's algorithm.

Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph. It was conceived by computer scientist Edsger W. Dijkstra in 1956. The algorithm exists in many variants; Dijkstra's original variant found the shortest path between two nodes, but a more common variant fixes a single node as the "source" node and finds shortest paths from the source to all other nodes in the graph, producing a shortest-path tree.

Here are the steps to implement Dijkstra's algorithm:

1. Create a set of all the unvisited nodes called the unvisited set.
2. Assign to every node a tentative distance value: set it to zero for our initial node and to infinity for all other nodes. Set the initial node as current.
3. For the current node, consider all of its unvisited neighbors and calculate their tentative distances through the current node. Compare the newly calculated tentative distance to the current assigned value and assign the smaller one.
4. When we are done considering all of the unvisited neighbors of the current node, mark the current node as visited and remove it from the unvisited set. A visited node will never be checked again.
5. If the destination node has been marked visited (when planning a route between two specific nodes) or if the smallest tentative distance among the nodes in the unvisited set is infinity (when planning a complete traversal; occurs when there is no connection between the initial node and remaining unvisited nodes), then stop. The algorithm has finished.
6. Otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the new current node, and go back to step 3.

This algorithm can be used to find the shortest path from a given vertex in a weighted connected graph to other vertices. It is important to note that the weights of the edges must be non-negative for the algorithm to work correctly. If the graph contains negative edge weights, a different algorithm such as the Bellman-Ford algorithm can be used.



## Find Minimum Cost Spanning Tree of a given connected undirected graph using Kruskal's algorithm. Use Union-Find algorithms in your program.

Kruskal's algorithm is a greedy algorithm that finds a minimum spanning tree for a connected weighted graph. This means it finds a subset of the edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is minimized.

Here are the steps to implement Kruskal's algorithm:

1. Sort all the edges in non-decreasing order of their weight.
2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
3. Repeat step 2 until there are (V-1) edges in the spanning tree, where V is the number of vertices in the given graph.

To detect if an edge forms a cycle with the spanning tree formed so far, we can use the Union-Find algorithm. The Union-Find algorithm is used to keep track of a partition of a set into disjoint subsets. It has two main operations: Find and Union.

- Find: Determine which subset a particular element is in. This can be used to determine if two elements are in the same subset.
- Union: Join two subsets into a single subset.

In the context of Kruskal's algorithm, we can use the Union-Find algorithm to check if an edge forms a cycle with the spanning tree formed so far. If the two vertices of the edge are already in the same subset, then adding the edge will form a cycle. Otherwise, we can add the edge and use the Union operation to merge the two subsets.

Here is an example of how to implement Kruskal's algorithm using the Union-Find algorithm in a program:

```python
# Python program for Kruskal's algorithm to find Minimum Spanning Tree
# of a given connected, undirected and weighted graph

from collections import defaultdict

# Class to represent a graph
class Graph:

    def __init__(self, vertices):
        self.V = vertices # No. of vertices
        self.graph = [] # default dictionary to store graph

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # A utility function to find set of an element i
    # (uses path compression technique)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Attach smaller rank tree under root of high rank tree
        # (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        # If ranks are same, then make one as root and increment
        # its rank by one
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # The main function to construct MST using Kruskal's algorithm
    def KruskalMST(self):

        result = [] # This will store the resultant MST

        i = 0 # An index variable, used for sorted edges
        e = 0 # An index variable, used for result[]

        # Step 1: Sort all the edges in non-decreasing order of their
        # weight. If we are not allowed to change the given graph, we
        # can create a copy of graph
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:

            # Step 2: Pick the smallest edge and increment the index
            # for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge does't cause cycle, include it
            # in result and increment the index of result for next edge
            if x != y:
                e = e + 1

```




## Find Minimum Cost Spanning Tree of a given undirected graph using Prim’s algorithm

Prim's algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph. This means it finds a subset of the edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is minimized.

Here are the steps to follow to implement Prim's algorithm:

1. Initialize the minimum spanning tree with a vertex chosen at random.
2. Find all the edges that connect the tree to new vertices, find the minimum and add it to the tree.
3. Keep repeating step 2 until all the vertices are in the tree.

This algorithm can be implemented using a priority queue to select the next edge with the minimum weight. The time complexity of this algorithm is O(ElogV), where E is the number of edges and V is the number of vertices in the graph.

This algorithm is useful in the Design and Analysis of Algorithm Lab in the subject of Real Time Systems, as it provides an efficient way to find the minimum cost spanning tree of a given undirected graph. It is important to understand and be able to implement this algorithm for exams in this subject.



## Design and Analysis of Algorithm Lab in the subject of Real Time System

### All-Pairs Shortest Paths problem using Floyd's algorithm

Floyd's algorithm is an efficient algorithm for finding the shortest paths between all pairs of vertices in a weighted graph. The algorithm works by iteratively improving an estimate of the shortest path between all pairs of vertices until the estimate is optimal.

Here is an example of how to implement Floyd's algorithm in Python:

```python
def floyd_warshall(graph):
    n = len(graph)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph
```

### Travelling Sales Person problem using Dynamic programming

The Travelling Sales Person (TSP) problem is a well-known problem in computer science. Given a set of cities and the distances between them, the goal is to find the shortest possible route that visits each city exactly once and returns to the starting city.

Dynamic programming is a powerful technique that can be used to solve the TSP problem. The idea is to break the problem down into smaller subproblems and solve them recursively.

Here is an example of how to implement the TSP problem using dynamic programming in Python:

```python
from math import inf

def tsp(graph):
    n = len(graph)
    C = [[inf] * (1 << n) for _ in range(n)]
    C[0][1] = 0
    for size in range(1, n):
        for S in range(1, 1 << n):
            if bin(S).count('1') == size:
                for i in range(n):
                    if (S >> i) & 1:
                        for j in range(n):
                            if (S >> j) & 1 and i != j:
                                C[i][S] = min(C[i][S], C[j][S ^ (1 << i)] + graph[j][i])
    return min(C[i][(1 << n) - 1] + graph[i][0] for i in range(n))
```

These are the implementations of the All-Pairs Shortest Paths problem using Floyd's algorithm and the Travelling Sales Person problem using Dynamic programming. These algorithms can be used to solve problems in the Design and Analysis of Algorithm Lab in the subject of Real Time System.



## Design and implement to find a subset of a given set S = {Sl, S2,.....,Sn} of n positive integers whose SUM is equal to a given positive integer d.

This problem can be solved using a backtracking algorithm. The idea is to consider each element in the set and explore two possibilities - include the element in the subset or exclude it. We recursively explore these possibilities for all elements in the set until we either find a subset whose sum is equal to d or we have exhausted all possibilities.

Here are the steps to implement this algorithm:

1. Create a recursive function that takes the current index, the current sum, and the current subset as input arguments.
2. If the current sum is equal to d, print the current subset and return.
3. If the current index is equal to n, return.
4. Include the current element in the subset and recursively call the function with the next index, updated sum, and updated subset.
5. Exclude the current element from the subset and recursively call the function with the next index, the same sum, and the same subset.

For example, if S ={1, 2, 5, 6, 8} and d= 9, there are two solutions {1,2,6}and {1,8}. If the given problem instance doesn't have a solution, a suitable message can be displayed.

This algorithm has an exponential time complexity, as it explores all possible subsets of the given set. However, it is guaranteed to find all solutions to the problem if they exist. It is also possible to optimize the algorithm by using techniques such as pruning to reduce the search space.



## Design and implement to find all Hamiltonian Cycles in a connected undirected Graph G of n vertices using backtracking principle

A Hamiltonian cycle is a cycle in an undirected graph that visits each vertex exactly once and returns to the starting vertex. The problem of finding all Hamiltonian cycles in a graph is a well-known NP-complete problem.

One approach to finding all Hamiltonian cycles in a graph is to use the backtracking principle. This involves recursively exploring all possible paths in the graph, while keeping track of the vertices visited so far. If a path visits all vertices exactly once and returns to the starting vertex, it is a Hamiltonian cycle.

Here are the steps to implement this approach:

1. Choose a starting vertex and mark it as visited.
2. For each unvisited neighbor of the current vertex, mark it as visited and recursively explore the path starting from that neighbor.
3. If all vertices have been visited and the current vertex is adjacent to the starting vertex, a Hamiltonian cycle has been found.
4. Backtrack by unmarking the current vertex as visited and returning to the previous vertex in the path.

This approach can be implemented using a depth-first search algorithm. The time complexity of this approach is exponential, as it involves exploring all possible paths in the graph.

In summary, finding all Hamiltonian cycles in a connected undirected graph can be achieved using the backtracking principle. This involves recursively exploring all possible paths in the graph while keeping track of the vertices visited so far. This approach can be implemented using a depth-first search algorithm, but has an exponential time complexity.

