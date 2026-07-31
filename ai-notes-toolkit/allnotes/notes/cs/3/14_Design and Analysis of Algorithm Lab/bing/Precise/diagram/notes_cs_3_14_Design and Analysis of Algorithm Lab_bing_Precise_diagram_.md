

## Program for Recursive Binary & Linear Search for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

### Linear Search
Linear search is a simple search algorithm that involves iterating through an array or list of elements, comparing each element to the target value until a match is found or the end of the array is reached.

Here is an example of a recursive linear search function in C++:
```c++
int linearSearch(int arr[], int l, int r, int x)
{
    if (r < l)
        return -1;
    if (arr[l] == x)
        return l;
    if (arr[r] == x)
        return r;
    return linearSearch(arr, l + 1, r - 1, x);
}
```

### Binary Search
Binary search is a more efficient search algorithm that involves repeatedly dividing the search interval in half until the target value is found or the search interval is empty. This algorithm requires that the array or list being searched is sorted.

Here is an example of a recursive binary search function in C++:
```c++
int binarySearch(int arr[], int l, int r, int x)
{
    if (r >= l) {
        int mid = l + (r - l) / 2;
        if (arr[mid] == x)
            return mid;
        if (arr[mid] > x)
            return binarySearch(arr, l, mid - 1, x);
        return binarySearch(arr, mid + 1, r, x);
    }
    return -1;
}
```



## Program for Heap Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure. It works by dividing the input into a sorted and an unsorted region, and iteratively shrinking the unsorted region by extracting the largest element and moving that to the sorted region. The improvement consists of the use of a heap data structure rather than a linear-time search to find the maximum.

Here is an example of a heap sort algorithm in C++:

```c++
#include <iostream>
using namespace std;
  
void heapify(int arr[], int n, int i)
{
    int largest = i; 
    int l = 2*i + 1; 
    int r = 2*i + 2; 
  
    if (l < n && arr[l] > arr[largest])
        largest = l;
  
    if (r < n && arr[r] > arr[largest])
        largest = r;
  
    if (largest != i)
    {
        swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}
  
void heapSort(int arr[], int n)
{
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);
  
    for (int i=n-1; i>0; i--)
    {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}
  
void printArray(int arr[], int n)
{
    for (int i=0; i<n; ++i)
        cout << arr[i] << " ";
    cout << "\n";
}
  
int main()
{
    int arr[] = {12, 11, 13, 5, 6, 7};
    int n = sizeof(arr)/sizeof(arr[0]);
  
    heapSort(arr, n);
  
    cout << "Sorted array is \n";
    printArray(arr, n);
}
```

This program first defines a `heapify` function, which is used to maintain the heap property of the array. The `heapSort` function uses this `heapify` function to sort the array. Finally, the `printArray` function is used to print the sorted array.

The time complexity of heap sort is O(n log n) in the worst, average, and best cases. This makes it an efficient sorting algorithm for large data sets.



## Program for Merge Sort

Merge sort is a sorting algorithm that uses the divide and conquer approach to sort a list of elements. It works by dividing the unsorted list into n sub-lists, each containing one element, and then repeatedly merging sub-lists to produce new sorted sub-lists until there is only one sub-list remaining, which will be the sorted list.

Here is the algorithm for merge sort:

1. If the list is of length 0 or 1, return the list.
2. Divide the list into two smaller sub-lists by splitting it in half.
3. Recursively sort each of the two sub-lists by calling merge sort on them.
4. Merge the two sub-lists back into one sorted list.

Here is an example implementation of merge sort in C:

```c
#include <stdio.h>

void merge(int arr[], int l, int m, int r)
{
    int i, j, k;
    int n1 = m - l + 1;
    int n2 =  r - m;

    int L[n1], R[n2];

    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1+ j];

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
        int m = l+(r-l)/2;

        mergeSort(arr, l, m);
        mergeSort(arr, m+1, r);

        merge(arr, l, m, r);
    }
}

int main()
{
    int arr[] = {12, 11, 13, 5, 6, 7};
    int arr_size = sizeof(arr)/sizeof(arr[0]);

    printf("Given array is \n");
    printArray(arr, arr_size);

    mergeSort(arr, 0, arr_size - 1);

    printf("\nSorted array is \n");
    printArray(arr, arr_size);
    return 0;
}
```

This program first defines the `merge` function, which takes in an array, the left index, the middle index, and the right index, and merges the two sub-arrays defined by these indices. The `mergeSort` function then uses this `merge` function to recursively sort the array by dividing it in half and sorting each half, then merging the two halves back together. The `main` function demonstrates how to use the `mergeSort` function to sort an array of integers.

This is the basic idea behind the merge sort algorithm and an example implementation in C. It is an efficient sorting algorithm with a time complexity of O(n log n) in the worst case. It is commonly used in the Design and Analysis of Algorithm Lab in the subject of Real Time System.



## Program for Selection Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

Selection sort is an in-place comparison-based sorting algorithm. Here is a step-by-step guide on how the algorithm works:

1. The algorithm divides the input list into two parts: the sublist of items already sorted, which is built up from left to right at the front (left) of the list, and the sublist of items remaining to be sorted that occupy the rest of the list.
2. Initially, the sorted sublist is empty and the unsorted sublist is the entire input list.
3. The algorithm proceeds by finding the smallest (or largest, depending on the sorting order) element in the unsorted sublist, exchanging (swapping) it with the leftmost unsorted element (putting it in sorted order), and moving the sublist boundaries one element to the right.

Here is an example of a selection sort program in C:

```c
#include <stdio.h>

void swap(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

void selectionSort(int arr[], int n)
{
    int i, j, min_idx;

    for (i = 0; i < n-1; i++)
    {
        min_idx = i;
        for (j = i+1; j < n; j++)
          if (arr[j] < arr[min_idx])
            min_idx = j;

        swap(&arr[min_idx], &arr[i]);
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
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr)/sizeof(arr[0]);
    selectionSort(arr, n);
    printf("Sorted array: \n");
    printArray(arr, n);
    return 0;
}
```

This program sorts an array of integers using the selection sort algorithm. The `swap` function is used to exchange the values of two variables. The `selectionSort` function implements the selection sort algorithm, and the `printArray` function is used to print the sorted array.

Selection sort has a time complexity of O(n^2) in the worst, average, and best cases, where n is the number of elements in the input list. This makes it inefficient on large lists and generally performs worse than the similar insertion sort. Selection sort is noted for its simplicity and has performance advantages over more complicated algorithms in certain situations, particularly where auxiliary memory is limited.



## Program for Insertion Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

Insertion sort is a simple sorting algorithm that works by building the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

Here is the algorithm for insertion sort:

1. Start from the second element of the array (element at index 1).
2. Compare the current element with the element before it.
3. If the current element is smaller than the element before it, swap them.
4. Continue comparing the current element with the elements before it and swapping them until the current element is in its correct position.
5. Move to the next element and repeat the process until the last element is reached.

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

This program sorts an array of integers using the insertion sort algorithm. The `insertionSort` function takes an array and its size as arguments and sorts the array in ascending order. The `printArray` function is used to print the sorted array.



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

This program first includes the necessary libraries and defines a `swap` function to swap two elements. The `partition` function takes the array, the starting index, and the ending index as arguments and partitions the array around the pivot element. The `quickSort` function recursively sorts the sub-arrays and the `printArray` function prints the sorted array.

The `main` function initializes the array to be sorted and calls the `quickSort` function. The sorted array is then printed using the `printArray` function.

Quick Sort has an average-case time complexity of O(n log n) and a worst-case time complexity of O(n^2). It is an efficient sorting algorithm for large datasets. However, its performance can degrade if the pivot element is not chosen wisely. It is also not a stable sorting algorithm, meaning that the relative order of equal elements may not be preserved.



## Knapsack Problem using Greedy Solution

The Knapsack Problem is a combinatorial optimization problem where the goal is to select a subset of items with the maximum total value, subject to a constraint on the total weight of the selected items.

A greedy solution to the Knapsack Problem involves sorting the items by their value-to-weight ratio and then selecting the items with the highest ratios until the weight constraint is reached.

1. Sort the items in decreasing order of their value-to-weight ratio.
2. Initialize the total weight and total value to 0.
3. For each item in the sorted list:
    - If the total weight plus the weight of the item is less than or equal to the weight constraint, add the item to the knapsack, update the total weight and total value.
    - Otherwise, break the loop.
4. Return the total value.

This greedy solution does not always produce the optimal solution, but it can provide a good approximation in many cases. It has a time complexity of O(n log n) due to the sorting step.

This solution can be used as a heuristic for solving the Knapsack Problem in the Design and Analysis of Algorithm Lab in the subject of Real Time System. It is important to note that this is just one approach to solving the problem and other algorithms may provide better results in certain cases.



## Travelling Salesman Problem

The Travelling Salesman Problem (TSP) is a problem in the field of computer science and operations research. It is defined as follows: Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?

The TSP is an NP-hard problem, meaning that there is no known polynomial-time algorithm to solve it. However, there are several heuristics and approximation algorithms that can be used to find near-optimal solutions.

Some common approaches to solving the TSP include:
1. Nearest Neighbor: Starting from a random city, the algorithm repeatedly visits the nearest unvisited city until all cities have been visited.
2. Greedy: The algorithm repeatedly selects the shortest edge that does not create a cycle with fewer than n-1 edges or increase the degree of any node to more than 2.
3. 2-opt: The algorithm repeatedly swaps pairs of edges to improve the tour until no more improvements can be made.
4. Ant Colony Optimization: The algorithm simulates the behavior of ants in finding the shortest path between their nest and a food source.

These are just a few of the many approaches to solving the TSP. The choice of algorithm will depend on the specific requirements of the problem, such as the number of cities, the accuracy of the solution, and the time available to find a solution. It is important to carefully analyze the problem and choose the most appropriate algorithm for the situation.



## Find Minimum Spanning Tree using Kruskal’s Algorithm

Kruskal's algorithm is a greedy algorithm in graph theory that finds a minimum spanning tree for a connected weighted graph. This means it finds a subset of the edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is minimized.

Here are the steps to find the minimum spanning tree using Kruskal's algorithm:

1. Sort all the edges in non-decreasing order of their weight.
2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
3. Repeat step 2 until there are (V-1) edges in the spanning tree, where V is the number of vertices in the given graph.

This algorithm can be used in the Design and Analysis of Algorithm Lab in the subject of Real Time System to find the minimum spanning tree of a given graph. It is an efficient and widely used algorithm for this purpose.



## Implement N Queen Problem using Backtracking

The N Queen problem is a classic problem in computer science and is often used to illustrate the concept of backtracking. The problem is to place N queens on an NxN chessboard such that no two queens attack each other. A queen can attack any piece in the same row, column, or diagonal.

Backtracking is a general algorithm for finding all (or some) solutions to a problem by incrementally building a solution and trying different possibilities. If the current solution is found to be unworkable, the algorithm backtracks to a previous state and tries a different possibility.

Here are the steps to implement the N Queen problem using backtracking:

1. Start with an empty NxN chessboard.
2. Place the first queen in the first column of the first row.
3. Move to the next column and try to place a queen in a row where it is not attacked by any other queen.
4. If a queen can be placed, move to the next column and repeat step 3.
5. If a queen cannot be placed in any row of the current column, backtrack to the previous column and move the queen to the next possible row.
6. Repeat steps 3-5 until all queens are placed or it is determined that no solution exists.
7. If all queens are placed, a solution has been found. Otherwise, no solution exists.

This algorithm can be implemented using recursion, where each recursive call represents the placement of a queen in a column. The base case is when all queens have been placed, and the recursive case is when a queen is placed in a column and the algorithm moves to the next column.

This is a brief overview of how to implement the N Queen problem using backtracking. For a more detailed explanation and example code, please refer to a textbook or online resource on the subject.



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

This implementation of Quick Sort uses the last element as the pivot. The partition function takes the pivot element and places it in its correct position in the sorted array, and places all smaller elements to the left of the pivot and all greater elements to the right of the pivot.

The time complexity of Quick Sort can be analyzed as follows:
- Worst case: The worst case occurs when the partition process always picks the greatest or smallest element as the pivot. This would result in an unbalanced partition and the time complexity would be O(n^2).
- Average case: The average case occurs when the partition process picks the median element as the pivot. This would result in a balanced partition and the time complexity would be O(n log n).
- Best case: The best case occurs when the partition process always picks the median element as the pivot. This would result in a balanced partition and the time complexity would be O(n log n).

In conclusion, Quick Sort is an efficient sorting algorithm that uses the divide-and-conquer approach. Its time complexity can vary depending on the selection of the pivot element, but on average it has a time complexity of O(n log n).



## Merge Sort

Merge Sort is an efficient, general-purpose, comparison-based sorting algorithm. It is a divide and conquer algorithm that was invented by John von Neumann in 1945.

### Algorithm

1. Divide the unsorted list into n sublists, each containing one element (a list of one element is considered sorted).
2. Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted list.

### Time Complexity

The time complexity of Merge Sort is O(n log n) in the worst, average, and best cases. This is because the algorithm always divides the array into two halves and takes linear time to merge the two halves.

### Experiment

To demonstrate the time complexity of Merge Sort, an experiment can be conducted by sorting a given set of n integer elements using the Merge Sort method and computing its time complexity. The program can be run for varied values of n> 5000, and the time taken to sort can be recorded. A graph of the time taken versus n can be plotted on a graph sheet. The elements can be read from a file or can be generated using the random number generator.

### Divide and Conquer

Merge Sort is an example of the divide and conquer method. The algorithm works by dividing the unsorted list into n sublists, each containing one element, and then repeatedly merging sublists to produce new sorted sublists until there is only one sublist remaining. The time complexity analysis of the divide and conquer method shows that it has a worst case, average case, and best case time complexity of O(n log n).

### Conclusion

In conclusion, Merge Sort is an efficient sorting algorithm that uses the divide and conquer method. Its time complexity is O(n log n) in the worst, average, and best cases. An experiment can be conducted to demonstrate its time complexity by sorting a given set of n integer elements using the Merge Sort method and computing its time complexity. The results can be plotted on a graph to show the relationship between the time taken to sort and the number of elements being sorted.



## Implementing the 0/1 Knapsack problem using (a) Dynamic Programming method (b) Greedy method

The 0/1 Knapsack problem is a combinatorial optimization problem where the goal is to maximize the total value of items that can be placed into a knapsack of limited capacity. Each item has a weight and a value, and only one of each item is available. The problem is called 0/1 because each item can either be included (1) or not included (0) in the knapsack.

There are two common methods to solve the 0/1 Knapsack problem: the Dynamic Programming method and the Greedy method.

### (a) Dynamic Programming method

The Dynamic Programming method is an efficient approach to solve the 0/1 Knapsack problem. It is based on the principle of optimality, which states that an optimal solution to a problem can be constructed from optimal solutions to its subproblems.

The idea is to use a two-dimensional table to store the maximum value that can be obtained by using the first i items and a knapsack of capacity j. The table is filled in a bottom-up manner, starting from the smallest subproblems and building up to the final solution.

The time complexity of the Dynamic Programming method is O(nW), where n is the number of items and W is the capacity of the knapsack.

### (b) Greedy method

The Greedy method is a heuristic approach to solve the 0/1 Knapsack problem. It is based on the idea of making the locally optimal choice at each stage with the hope of finding a global optimum.

The idea is to sort the items in decreasing order of their value-to-weight ratio and then to select the items one by one, starting from the item with the highest ratio. If the current item fits into the remaining capacity of the knapsack, it is included; otherwise, it is skipped.

The time complexity of the Greedy method is O(n log n), where n is the number of items.

It is important to note that the Greedy method does not always produce an optimal solution to the 0/1 Knapsack problem. However, it can provide a good approximation in many cases and is much faster than the Dynamic Programming method.

In conclusion, the Dynamic Programming method is an efficient and exact approach to solve the 0/1 Knapsack problem, while the Greedy method is a fast and approximate approach. The choice of method depends on the requirements of the specific problem at hand.



## From a given vertex in a weighted connected graph, find shortest paths to other vertices using Dijkstra's algorithm.

Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph. It was conceived by computer scientist Edsger W. Dijkstra in 1956. The algorithm exists in many variants; Dijkstra's original variant found the shortest path between two nodes, but a more common variant fixes a single node as the "source" node and finds shortest paths from the source to all other nodes in the graph, producing a shortest-path tree.

Here are the steps to find the shortest paths from a given vertex in a weighted connected graph using Dijkstra's algorithm:

1. Assign to every vertex a tentative distance value: set it to zero for our initial vertex and to infinity for all other vertices. Set the initial vertex as current.
2. For the current vertex, consider all of its neighbors that are still in the set of unvisited vertices and calculate their tentative distances. Compare the newly calculated tentative distance to the current assigned value and assign the new value if it is less than the current assigned value.
3. When we are done considering all of the neighbors of the current vertex, mark the current vertex as visited. A visited vertex will never be checked again.
4. Select the unvisited vertex with the smallest tentative distance, set it as the new current vertex, and go back to step 2. If all the vertices have been visited, the algorithm has finished.
5. The algorithm will terminate when we have a shortest-path tree, i.e., when we have a set of edges that connect the source vertex to all other vertices in the graph such that the total weight of the edges in the tree is minimized.




## Find Minimum Cost Spanning Tree of a given connected undirected graph using Kruskal's algorithm. Use Union-Find algorithms in your program.

Kruskal's algorithm is a greedy algorithm that finds a minimum spanning tree for a connected weighted graph. This means it finds a subset of the edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is minimized.

Here are the steps to implement Kruskal's algorithm:

1. Sort all the edges in non-decreasing order of their weight.
2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
3. Repeat step 2 until there are (V-1) edges in the spanning tree, where V is the number of vertices in the given graph.

To detect if an edge forms a cycle with the current spanning tree, we can use the Union-Find algorithm. This algorithm keeps track of the connected components in the graph and allows us to efficiently check if two vertices are in the same connected component.

Here is an example of how to implement the Union-Find algorithm:

1. Create a parent array to keep track of the parent of each vertex in the connected components.
2. Initialize all the vertices as individual sets with only one element.
3. To find the parent of a vertex, follow the parent pointers until you reach the root of the set.
4. To merge two sets, make the root of one set the parent of the root of the other set.

With the help of the Union-Find algorithm, we can efficiently implement Kruskal's algorithm to find the minimum cost spanning tree of a given connected undirected graph.



## Find Minimum Cost Spanning Tree of a given undirected graph using Prim’s algorithm

Prim's algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph. This means it finds a subset of the edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is minimized.

Here are the steps to follow to implement Prim's algorithm:

1. Initialize the minimum spanning tree with a vertex chosen at random.
2. Find all the edges that connect the tree to new vertices, find the minimum and add it to the tree.
3. Keep repeating step 2 until all the vertices are in the tree.

This algorithm can be implemented using a priority queue to select the next edge with the minimum weight. The time complexity of this algorithm is O(E log V), where E is the number of edges and V is the number of vertices in the graph.

This algorithm is useful in the Design and Analysis of Algorithm Lab in the subject of Real Time Systems, as it provides an efficient way to find the minimum cost spanning tree of a given undirected graph. It is important to understand and be able to implement this algorithm for exams in this subject.



## Design and Analysis of Algorithm Lab: Real Time System

### Floyd's Algorithm for All-Pairs Shortest Paths Problem

Floyd's algorithm is an efficient algorithm for finding the shortest paths between all pairs of vertices in a weighted graph. The algorithm works by iteratively improving an estimate of the shortest path distances between all pairs of vertices until the estimate is accurate.

Here is an example of how to implement Floyd's algorithm in C++:

```c++
#include <iostream>
#include <algorithm>
using namespace std;
#define V 4
#define INF 99999

void floydWarshall (int graph[][V])
{
    int dist[V][V], i, j, k;
    for (i = 0; i < V; i++)
        for (j = 0; j < V; j++)
            dist[i][j] = graph[i][j];
    for (k = 0; k < V; k++)
    {
        for (i = 0; i < V; i++)
        {
            for (j = 0; j < V; j++)
            {
                if (dist[i][k] + dist[k][j] < dist[i][j])
                    dist[i][j] = dist[i][k] + dist[k][j];
            }
        }
    }
    for (int i = 0; i < V; i++)
    {
        for (int j = 0; j < V; j++)
        {
            if (dist[i][j] == INF)
                cout<<"INF"<<"     ";
            else
                cout<<dist[i][j]<<"     ";
        }
        cout<<endl;
    }
}

int main()
{
    int graph[V][V] = { {0, 5, INF, 10},
                        {INF, 0, 3, INF},
                        {INF, INF, 0, 1},
                        {INF, INF, INF, 0}
                      };
    floydWarshall(graph);
    return 0;
}
```

### Dynamic Programming for Travelling Sales Person Problem

The Travelling Sales Person (TSP) problem is a well-known problem in computer science. Given a set of cities and the distances between them, the goal is to find the shortest possible route that visits each city exactly once and returns to the starting city.

One way to solve the TSP problem is to use dynamic programming. The idea is to break the problem down into smaller subproblems and solve them recursively. The solution to the original problem is then constructed from the solutions to the subproblems.

Here is an example of how to implement a dynamic programming solution to the TSP problem in C++:

```c++
#include <iostream>
#include <algorithm>
using namespace std;
#define V 4
#define INF 99999

int tsp(int graph[][V], int s) {
    int dp[1 << V][V];
    for (int i = 0; i < (1 << V); i++)
        for (int j = 0; j < V; j++)
            dp[i][j] = INF;
    dp[1 << s][s] = 0;
    for (int mask = 0; mask < (1 << V); mask++) {
        for (int i = 0; i < V; i++) {
            if (mask & (1 << i)) {
                for (int j = 0; j < V; j++) {
                    if (!(mask & (1 << j))) {
                        dp[mask | (1 << j)][j] = min(dp[mask | (1 << j)][j], dp[mask][i] + graph[i][j]);
                    }
                }
            }
        }
    }
    int ans = INF;
    for (int i = 0; i < V; i++)
        ans = min(ans, dp[(1 << V) - 1][i] + graph[i][s]);
    return ans;
}

int main() {
    int graph[][V] = { {0, 10, 15, 20},
                        {10, 0, 35, 25},
                        {15, 35, 0, 30},
                        {20, 25, 30, 0}
                      };
    int s = 0;
    cout << tsp(graph, s) << endl;
    return 0;
}
```

These are the implementations of Floyd's algorithm for the All-Pairs Shortest Paths problem and a dynamic programming solution for the Travelling Sales Person problem. These algorithms can be used in the Design and Analysis of Algorithm Lab in the subject of Real Time System.



## Design and implement to find a subset of a given set S = {Sl, S2,.....,Sn} of n positive integers whose SUM is equal to a given positive integer d.

This problem can be solved using a recursive algorithm. The idea is to consider two cases for every element: (1) the element is included in the subset, (2) the element is not included in the subset. The base case of the recursion is when the remaining sum is 0, which means a subset has been found, or when there are no remaining elements, which means no subset has been found.

Here is an example implementation in Python:

```python
def subset_sum(S, n, d, subset):
    if d == 0:
        print(subset)
        return
    if n == 0:
        return
    subset_sum(S, n-1, d, subset)
    subset.append(S[n-1])
    subset_sum(S, n-1, d-S[n-1], subset)
    subset.pop()

S = [1, 2, 5, 6, 8]
d = 9
subset = []
subset_sum(S, len(S), d, subset)
```

This algorithm will print all the subsets of the given set S whose sum is equal to the given positive integer d. In the example above, the output will be [1, 8] and [1, 2, 6].

If the given problem instance doesn't have a solution, no subsets will be printed. In this case, a suitable message can be displayed by checking if any subsets were found.

For example:

```python
S = [1, 2, 5, 6, 8]
d = 9
subset = []
found = subset_sum(S, len(S), d, subset)
if not found:
    print("No solution found")
```

This algorithm has an exponential time complexity, as it considers all the possible subsets of the given set S. However, it can be optimized using dynamic programming techniques.



## Design and implement to find all Hamiltonian Cycles in a connected undirected Graph G of n vertices using backtracking principle

A Hamiltonian cycle is a cycle in an undirected graph that visits each vertex exactly once and returns to the starting vertex. The problem of finding all Hamiltonian cycles in a graph is a well-known NP-complete problem.

One approach to finding all Hamiltonian cycles in a graph is to use the backtracking principle. This involves recursively exploring all possible paths in the graph, while keeping track of the vertices visited so far. If a path visits all vertices exactly once and returns to the starting vertex, it is a Hamiltonian cycle.

The algorithm can be implemented as follows:

1. Start with an empty path and a boolean array to keep track of visited vertices.
2. Add the starting vertex to the path and mark it as visited.
3. For each unvisited neighbor of the current vertex, add it to the path and mark it as visited. Recursively call the function with the new path and visited array.
4. If the path contains all vertices and the last vertex is a neighbor of the starting vertex, the path is a Hamiltonian cycle. Add it to the list of Hamiltonian cycles.
5. Backtrack by removing the current vertex from the path and marking it as unvisited.

This algorithm will find all Hamiltonian cycles in a connected undirected graph using the backtracking principle. It has an exponential time complexity, as it explores all possible paths in the graph. However, it can be an effective approach for small graphs or graphs with certain properties that make it easier to find Hamiltonian cycles.

