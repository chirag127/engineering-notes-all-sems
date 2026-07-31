

## Program for Recursive Binary & Linear Search for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- **Linear Search**: Linear search is a simple search algorithm that checks each element of a list or array until the desired element is found or the end of the list is reached. It can be implemented using a loop that iterates over each element of the list and checks if it is equal to the desired value. If the element is found, the loop can be terminated and the index of the element can be returned. If the element is not found, the function can return a value indicating that the element was not found.

- **Recursive Linear Search**: A recursive implementation of linear search can be achieved by dividing the list into two parts: the first element and the rest of the list. The function can then check if the first element is equal to the desired value. If it is, the function can return the index of the first element. If it is not, the function can call itself recursively on the rest of the list, incrementing the index by one each time. If the element is not found, the function can return a value indicating that the element was not found.

- **Binary Search**: Binary search is a search algorithm that works on sorted lists or arrays. It operates by repeatedly dividing the list in half and checking if the middle element is equal to the desired value. If it is, the function can return the index of the middle element. If it is not, the function can determine if the desired value is in the left or right half of the list and repeat the process on that half until the element is found or the list is empty. If the element is not found, the function can return a value indicating that the element was not found.

- **Recursive Binary Search**: A recursive implementation of binary search can be achieved by dividing the list into two parts: the left half and the right half. The function can then check if the middle element is equal to the desired value. If it is, the function can return the index of the middle element. If it is not, the function can determine if the desired value is in the left or right half of the list and call itself recursively on that half, passing the appropriate indices to indicate the new bounds of the list. If the element is not found, the function can return a value indicating that the element was not found.




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

This program first builds a max heap from the input data, then repeatedly swaps the first element (which is the largest) with the last element, reduces the heap size by 1, and heapifies the root. This continues until the heap size is reduced to 1, at which point the array is sorted.

Heap sort has a time complexity of O(n log n) for both the best and worst cases, making it an efficient sorting algorithm. It is also an in-place sorting algorithm, meaning it does not require additional memory to sort the data.



## Program for Merge Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

Merge sort is a sorting algorithm that uses the divide-and-conquer approach to sort a list of elements. The algorithm works by dividing the unsorted list into n sublists, each containing one element, and then repeatedly merging sublists to produce new sorted sublists until there is only one sublist remaining, which will be the sorted list.

Here is the algorithm for merge sort:

1. If the list is of length 0 or 1, return the list.
2. Divide the list into two smaller sublists by splitting it in half.
3. Recursively sort each of the two sublists by calling merge sort on them.
4. Merge the two sorted sublists back into one sorted list.

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

void printArray(int A[], int size)
{
    int i;
    for (i=0; i < size; i++)
        printf("%d ", A[i]);
    printf("\n");
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

This program first defines a `merge` function that takes in an array, the left index, the middle index, and the right index, and merges the two subarrays `arr[l..m]` and `arr[m+1..r]` into one sorted array. The `mergeSort` function takes in an array, the left index, and the right index, and recursively sorts the array by dividing it into two subarrays, sorting each subarray, and then merging the two sorted subarrays back into one sorted array. The `main` function defines an array, prints the given array, calls the `mergeSort` function to sort the array, and then prints the sorted array.

This is an example of how merge sort can be implemented in C. The time complexity of merge sort is O(nlogn) in the worst case, which makes it an efficient sorting algorithm for large datasets. It is also a stable sorting algorithm, meaning that it maintains the relative order of equal elements in the sorted list. However, it requires additional space to store the subarrays during the merging process, which can make it less space-efficient than other sorting algorithms.



## Program for Selection Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

Selection sort is a simple sorting algorithm that sorts an array by repeatedly finding the minimum element from the unsorted part of the array and swapping it with the first element of the unsorted part. Here are the steps to implement selection sort:

1. Start from the first element of the array and find the minimum element in the unsorted part of the array.
2. Swap the minimum element with the first element of the unsorted part.
3. Move the boundary of the unsorted part one element to the right.
4. Repeat the above steps until the entire array is sorted.

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

This program first defines a `swap` function that swaps the values of two variables. The `selectionSort` function takes an array and its size as arguments and sorts the array using the selection sort algorithm. The `printArray` function prints the elements of the array. In the `main` function, we define an array, call the `selectionSort` function to sort it, and then print the sorted array using the `printArray` function.

Selection sort has a time complexity of O(n^2) in the worst case, where n is the number of elements in the array. This makes it inefficient for large datasets. However, it is easy to understand and implement, and can be useful for small datasets or as a part of more complex algorithms.



## Program for Insertion Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

Here is an example of how the insertion sort algorithm works:

1. Start by iterating over the array, starting from the second element (index 1).
2. Compare the current element with the previous element.
3. If the current element is smaller than the previous element, swap the two elements.
4. Continue comparing the current element with the previous elements until it is no longer smaller than the previous element or until the first element is reached.
5. Repeat the process for the next element in the array until the entire array is sorted.

Here is an example of a program that implements the insertion sort algorithm in C:

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

int main() {
    int arr[] = {12, 11, 13, 5, 6};
    int n = sizeof(arr) / sizeof(arr[0]);

    insertionSort(arr, n);

    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");

    return 0;
}
```

This program sorts an array of integers using the insertion sort algorithm. The `insertionSort` function takes an array and its length as arguments and sorts the array in place.



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

This program first includes the necessary libraries and defines a swap function to swap two elements. The partition function takes the array, the low and high indices as input and returns the partition index. The quickSort function recursively sorts the sub-arrays and the printArray function prints the sorted array.

The time complexity of Quick Sort is O(n^2) in the worst case and O(nlogn) in the average and best cases. The space complexity is O(logn).



## Knapsack Problem using Greedy Solution

The Knapsack Problem is a well-known optimization problem in the field of computer science and operations research. It involves selecting a subset of items, each with a weight and a value, such that the total weight is less than or equal to a given capacity and the total value is maximized.

One approach to solving the Knapsack Problem is to use a greedy algorithm. A greedy algorithm makes a locally optimal choice at each step, with the hope of finding a global optimum.

In the context of the Knapsack Problem, a greedy solution would involve sorting the items by their value-to-weight ratio, and then selecting the items with the highest ratios until the capacity is reached.

While this approach can provide a good solution, it is not guaranteed to find the optimal solution. In some cases, the greedy solution may be far from optimal.

Despite its limitations, the greedy approach to the Knapsack Problem is commonly used due to its simplicity and efficiency. It can provide a good approximation to the optimal solution in many cases, and is often used as a starting point for more advanced algorithms.

In summary, the Knapsack Problem can be solved using a greedy algorithm by sorting the items by their value-to-weight ratio and selecting the items with the highest ratios until the capacity is reached. While this approach is not guaranteed to find the optimal solution, it is simple and efficient, and can provide a good approximation in many cases.



## Perform Travelling Salesman Problem for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- The Travelling Salesman Problem (TSP) is a problem in the field of computer science and operations research.
- The problem is to find the shortest possible route that visits a given set of cities and returns to the starting city.
- The TSP is an NP-hard problem, meaning that there is no known efficient algorithm to solve it in polynomial time.
- There are several approaches to solving the TSP, including exact algorithms, heuristics, and approximation algorithms.
- Exact algorithms, such as the Held-Karp algorithm, can find the optimal solution to the TSP, but they are not practical for large instances due to their high computational complexity.
- Heuristics, such as the nearest neighbor algorithm and the 2-opt algorithm, can find good solutions to the TSP quickly, but they do not guarantee an optimal solution.
- Approximation algorithms, such as the Christofides algorithm, can find solutions to the TSP that are guaranteed to be within a certain factor of the optimal solution.
- The choice of algorithm to use for solving the TSP depends on the size of the instance and the desired trade-off between solution quality and computational time.



## Find Minimum Spanning Tree using Kruskal’s Algorithm for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Kruskal's algorithm is a greedy algorithm that finds a minimum spanning tree for a connected weighted graph.
- The algorithm operates by adding edges to the spanning tree in increasing order of their weight, as long as the edge does not create a cycle.
- The algorithm can be implemented using a disjoint-set data structure to keep track of the connected components of the graph.
- The time complexity of Kruskal's algorithm is O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices in the graph.
- The algorithm can be used to find the minimum spanning tree of a graph in real-time systems, where efficiency and speed are important.



## Implement N Queen Problem using Backtracking for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

The N Queen problem is a classic problem in computer science, where the goal is to place N queens on an NxN chessboard such that no two queens threaten each other. This means that no two queens can share the same row, column, or diagonal.

One way to solve the N Queen problem is by using backtracking. Backtracking is a general algorithm for finding all (or some) solutions to a problem by incrementally building a solution and trying different possibilities. If a partial solution is found to be invalid, the algorithm backtracks to a previous state and tries a different possibility.

Here are the steps to implement the N Queen problem using backtracking:

1. Start with an empty NxN chessboard.
2. Place the first queen in the first column of the first row.
3. Move to the next column and try to place a queen in a row where it is not threatened by any previously placed queen.
4. If a valid position is found, place the queen and move to the next column.
5. If no valid position is found, backtrack to the previous column and move the queen to a different row.
6. Repeat steps 3-5 until all queens are placed or it is determined that no solution exists.

This algorithm can be implemented using recursion, where each recursive call represents the placement of a queen in a column. The base case is when all queens have been placed, and the recursive case is when a queen is placed in a column and the algorithm moves to the next column.

The time complexity of this algorithm is O(N!), where N is the number of queens. This is because, in the worst case, the algorithm must try all possible permutations of queen placements. However, in practice, the algorithm is much faster due to the pruning of invalid solutions.

In conclusion, the N Queen problem can be solved using backtracking, where the algorithm incrementally builds a solution and backtracks when an invalid partial solution is found. This algorithm can be implemented using recursion and has a time complexity of O(N!).



## Quick Sort Method

Quick Sort is a sorting algorithm that uses the divide-and-conquer approach. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The function then recursively sorts the sub-arrays.

The time complexity of Quick Sort is as follows:
- Worst case: O(n^2)
- Average case: O(n log n)
- Best case: O(n log n)

To demonstrate the time complexity of Quick Sort, the program can be run for varied values of n>5000 and the time taken to sort can be recorded. A graph of the time taken versus n can be plotted on a graph sheet.

The elements to be sorted can be read from a file or generated using a random number generator.

Here is an example of how Quick Sort can be implemented in Java:

```java
public static void quickSort(int[] arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi-1);
        quickSort(arr, pi+1, high);
    }
}

public static int partition(int[] arr, int low, int high) {
    int pivot = arr[high];
    int i = (low-1);
    for (int j=low; j<high; j++) {
        if (arr[j] < pivot) {
            i++;
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    int temp = arr[i+1];
    arr[i+1] = arr[high];
    arr[high] = temp;
    return i+1;
}
```

This is an example of how the divide-and-conquer method works in Quick Sort. The time complexity analysis shows that in the worst case, the time taken to sort is O(n^2), while in the average and best cases, the time taken is O(n log n).



## Merge Sort

Merge sort is a sorting algorithm that uses the divide and conquer approach to sort a given set of n integer elements. The algorithm works by dividing the input into two halves, recursively sorting each half, and then merging the two sorted halves together to form the final sorted output.

The time complexity of merge sort can be computed as follows:

- **Worst case:** The worst case time complexity of merge sort is O(n log n). This occurs when the input is such that each merge operation requires the maximum number of comparisons.

- **Average case:** The average case time complexity of merge sort is also O(n log n), since on average, each merge operation requires half the maximum number of comparisons.

- **Best case:** The best case time complexity of merge sort is O(n), which occurs when the input is already sorted, and no merge operations are required.

To demonstrate the time complexity of merge sort, the algorithm can be run on varied values of n > 5000, and the time taken to sort can be recorded. A graph of the time taken versus n can then be plotted on a graph sheet. The elements to be sorted can be read from a file or generated using a random number generator.

In summary, merge sort is an efficient sorting algorithm that uses the divide and conquer approach to sort a given set of n integer elements. Its time complexity is O(n log n) in the worst and average cases, and O(n) in the best case. The algorithm can be demonstrated by running it on varied values of n > 5000 and plotting a graph of the time taken versus n. This can help to illustrate how the divide and conquer method works, along with its time complexity analysis for the worst, average, and best cases. This information can be useful for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System.



## Implementing the 0/1 Knapsack problem using (a) Dynamic Programming method (b) Greedy method

The 0/1 Knapsack problem is a combinatorial optimization problem where we have a set of items, each with a weight and a value, and we need to determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.

There are two common methods to solve the 0/1 Knapsack problem: the Dynamic Programming method and the Greedy method.

### (a) Dynamic Programming method

The Dynamic Programming method is an efficient way to solve the 0/1 Knapsack problem. It is based on the principle of optimality, which states that an optimal solution to a problem can be constructed from optimal solutions to its subproblems.

The Dynamic Programming method for the 0/1 Knapsack problem involves constructing a table where the rows represent the items and the columns represent the maximum weight of the knapsack. The entry in the table at row i and column j represents the maximum value that can be obtained by considering the first i items and a knapsack of maximum weight j.

The table is filled in a bottom-up manner, starting from the first row and column. The value of each entry is calculated by considering two cases: either the item is included in the knapsack or it is not. If the item is included, the value of the entry is the sum of the value of the item and the value of the entry in the previous row and the column corresponding to the remaining weight after including the item. If the item is not included, the value of the entry is the same as the value of the entry in the previous row and the same column.

Once the table is filled, the maximum value that can be obtained is the value of the entry in the last row and the last column. The items included in the optimal solution can be determined by tracing back the table from the last row and column.

### (b) Greedy method

The Greedy method is a simple and intuitive way to solve the 0/1 Knapsack problem. It involves sorting the items in decreasing order of their value-to-weight ratio and then selecting the items in this order until the weight of the knapsack is reached.

The Greedy method is not guaranteed to find the optimal solution to the 0/1 Knapsack problem. However, it can provide a good approximation to the optimal solution in many cases.

In conclusion, the Dynamic Programming method and the Greedy method are two common methods to solve the 0/1 Knapsack problem. The Dynamic Programming method is an efficient way to find the optimal solution, while the Greedy method is a simple and intuitive way to find a good approximation to the optimal solution. Both methods have their advantages and disadvantages and can be used depending on the specific requirements of the problem.



## From a given vertex in a weighted connected graph, find shortest paths to other vertices using Dijkstra's algorithm.

Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph. It was conceived by computer scientist Edsger W. Dijkstra in 1956. The algorithm exists in many variants; Dijkstra's original variant found the shortest path between two nodes, but a more common variant fixes a single node as the "source" node and finds shortest paths from the source to all other nodes in the graph, producing a shortest-path tree.

Here are the steps to find the shortest paths from a given vertex in a weighted connected graph using Dijkstra's algorithm:

1. Assign a tentative distance value to every vertex: set it to zero for our initial vertex and to infinity for all other vertices. Set the initial vertex as current.
2. For the current vertex, consider all of its neighbors that are still in the unvisited set. Calculate the tentative distance for each neighbor through the current vertex. Compare the newly calculated tentative distance to the current assigned value and assign the new value if it is less than the current assigned value.
3. When we are done considering all of the neighbors of the current vertex, mark the current vertex as visited. A visited vertex will never be checked again.
4. Select the unvisited vertex with the smallest tentative distance, set it as the new current vertex, and go back to step 2. If all the vertices have been visited, the algorithm has finished.
5. The algorithm will stop when it has found the shortest path to every vertex in the graph.




## Find Minimum Cost Spanning Tree of a given connected undirected graph using Kruskal's algorithm. Use Union-Find algorithms in your program. for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Kruskal's algorithm is a greedy algorithm that finds a minimum spanning tree for a connected weighted graph.
- The algorithm operates by sorting all the edges in non-decreasing order of their weight.
- Then, it iterates through the sorted edges and adds the edge to the minimum spanning tree if it doesn't form a cycle with the already included edges.
- To check if an edge forms a cycle with the already included edges, we can use the Union-Find algorithm.
- The Union-Find algorithm is used to keep track of the connected components in the graph.
- It has two main operations: Find and Union.
- The Find operation determines if two vertices are in the same connected component.
- The Union operation merges two connected components into one.
- In Kruskal's algorithm, we use the Find operation to check if an edge forms a cycle with the already included edges.
- If the edge doesn't form a cycle, we use the Union operation to merge the connected components of the two vertices of the edge.
- The algorithm continues until all the vertices are in the same connected component, which means that the minimum spanning tree has been found.
- The time complexity of Kruskal's algorithm is O(ElogE) or O(ElogV), where E is the number of edges and V is the number of vertices in the graph.
- The space complexity of the algorithm is O(E+V), where E is the number of edges and V is the number of vertices in the graph.



## Find Minimum Cost Spanning Tree of a given undirected graph using Prim’s algorithm

Prim's algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph. This means it finds a subset of the edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is minimized.

Here are the steps to follow to apply Prim's algorithm:

1. Initialize the minimum spanning tree with a vertex chosen at random.
2. Find all the edges that connect the tree to new vertices, find the minimum and add it to the tree.
3. Keep repeating step 2 until all the vertices are in the tree.

This algorithm can be implemented using a priority queue to select the next edge with the minimum weight. The time complexity of this algorithm is O(E log V), where E is the number of edges and V is the number of vertices in the graph.

This algorithm is useful in the Design and Analysis of Algorithm Lab in the subject of Real Time System as it provides an efficient way to find the minimum cost spanning tree of a given undirected graph. It is an important concept to understand and can be applied in various real-world scenarios.



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

The Travelling Sales Person (TSP) problem is a well-known NP-hard problem in computer science. It involves finding the shortest possible route that visits a given set of cities and returns to the starting city. Dynamic programming is a method that can be used to solve the TSP problem.

Here is an example of how to implement a dynamic programming solution to the TSP problem in C++:

```c++
#include <iostream>
#include <algorithm>
using namespace std;
#define V 4
#define INF 99999

int tsp(int graph[][V], int s) {
    int dp[1 << V][V];
    for (int i = 0; i < (1 << V); i++) {
        for (int j = 0; j < V; j++) {
            dp[i][j] = INF;
        }
    }
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
    for (int i = 0; i < V; i++) {
        ans = min(ans, dp[(1 << V) - 1][i] + graph[i][s]);
    }
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

These are examples of how to implement Floyd's algorithm for the All-Pairs Shortest Paths problem and a dynamic programming solution to the Travelling Sales Person problem. These algorithms can be useful for solving problems in the Design and Analysis of Algorithm Lab in the subject of Real Time System.



## Design and implement to find a subset of a given set S = {Sl, S2,.....,Sn} of n positive integers whose SUM is equal to a given positive integer d.

This problem can be solved using a recursive algorithm. The basic idea is to consider all subsets of the given set S and check if the sum of elements in the subset is equal to the given positive integer d.

1. If the given set is empty, return false.
2. If the first element of the set is greater than the given positive integer d, ignore it and recur for the remaining set.
3. Else, recur for the remaining set with the given positive integer d reduced by the first element of the set.
4. If any of the above recursive calls returns true, return true.
5. Else, return false.

For example, if S ={1, 2, 5, 6, 8} and d= 9, there are two solutions {1,2,6}and {1,8}. If the given problem instance doesn't have a solution, a suitable message can be displayed.

This algorithm can be implemented using a recursive function that takes the given set S, the given positive integer d, and the current index as input arguments. The base case of the recursive function is when the current index is equal to the size of the given set S. In this case, if the given positive integer d is equal to 0, return true, else return false. The recursive function can be called twice, once by including the current element in the subset and once by excluding it. If any of the recursive calls returns true, return true, else return false.

This algorithm has an exponential time complexity as it considers all subsets of the given set S. However, it can be optimized using dynamic programming techniques. A 2D boolean array can be used to store the results of subproblems. The value of the array at index i, j represents if there is a subset of the first i elements of the given set S whose sum is equal to j. The array can be filled in a bottom-up manner using the above recursive relation. Once the array is filled, the solution can be obtained by checking the value of the array at index n, d.

This optimized algorithm has a time complexity of O(n*d) and a space complexity of O(n*d), where n is the size of the given set S and d is the given positive integer. This makes it more efficient than the recursive algorithm for large inputs. However, it still has an exponential space complexity and may not be feasible for very large inputs. In such cases, other techniques such as branch and bound or backtracking can be used to solve the problem.



## Design and implement to find all Hamiltonian Cycles in a connected undirected Graph G of n vertices using backtracking principle.

A Hamiltonian cycle is a cycle in an undirected graph that visits each vertex exactly once and returns to the starting vertex. The problem of finding a Hamiltonian cycle in a graph is NP-complete, meaning that there is no known efficient algorithm to solve it in all cases.

However, one approach to finding all Hamiltonian cycles in a connected undirected graph G of n vertices is to use the backtracking principle. Backtracking is a general algorithmic technique that involves exploring all possible solutions to a problem by incrementally building a solution and then backing up when a partial solution is found to be unworkable.

Here are the steps to design and implement a backtracking algorithm to find all Hamiltonian cycles in a connected undirected graph G of n vertices:

1. Create an empty path array and add vertex 0 as the first vertex in the path.
2. If all vertices are included in the path, and there is an edge from the last vertex in the path to the first vertex, then the path is a Hamiltonian cycle. Print the path and return.
3. For each vertex v that is not in the path and is adjacent to the last vertex in the path, add v to the path and recursively call the function to construct the rest of the path.
4. If adding vertex v doesn't lead to a solution, then remove v from the path and try another vertex.
5. If no vertex can be added to the path, then return.

This algorithm uses the backtracking principle to explore all possible paths in the graph and find all Hamiltonian cycles. The time complexity of this algorithm is exponential, as it needs to explore all possible paths in the graph. However, it can be an effective approach for small graphs or graphs with certain properties that make it easier to find Hamiltonian cycles.

