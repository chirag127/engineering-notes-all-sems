


## Program for Recursive Binary & Linear Search

Recursive binary and linear search algorithms are used to search for items in a collection of data. They are commonly used in the design and analysis of algorithms lab in the subject of real-time systems.

* Binary Search: Binary search is a technique for quickly finding a particular item in a sorted list. It works by repeatedly dividing the list in half and checking if the item is in the middle. If it is not, the search continues in the appropriate half.

* Linear Search: Linear search is a technique for finding a particular item in an unsorted list. It works by sequentially checking each item in the list until either the item is found or the end of the list is reached.

* Recursive Search: Recursive search is a technique for finding a particular item in a data structure by recursively calling the same search algorithm on smaller and smaller subsets of the data. This technique is often used when searching a tree or graph data structure.




## Program for Heap Sort 

1. Heap sort is an efficient sorting algorithm that works by organizing data into a binary tree structure, also known as a heap. 
2. The algorithm begins by building a heap from the input data. 
3. It then repeatedly swaps the root node of the heap with the last element in the heap, reducing the size of the heap by one, and then maintaining the heap property. 
4. This process is repeated until the heap is of size one, at which point the sorted list is obtained.
5. Heap sort is an example of an in-place sorting algorithm, as no additional memory is required for the sorting process. 
6. Heap sort is also an example of a comparison-based sorting algorithm, as it relies on comparisons between elements to sort the data. 
7. The time complexity of heap sort is O(n log n), making it an efficient sorting algorithm.




## Program for Merge Sort 

Merge sort is an efficient, general-purpose sorting algorithm. It is a comparison-based algorithm that divides an array into two subarrays and then merges them in a sorted order. The algorithm has a time complexity of O (n log n).

This algorithm is used in the Design and Analysis of Algorithm Lab in the subject of Real Time System.

1. Divide the unsorted array into n subarrays, each containing one element.
2. Repeatedly merge subarrays to produce new sorted subarrays until there is only one subarray remaining.
3. The remaining subarray is the sorted array.

The following is a pseudocode for the Merge Sort algorithm:

```
MergeSort(A, p, r)
  if p < r
    q = (p + r)/2
    MergeSort(A, p, q)
    MergeSort(A, q + 1, r)
    Merge(A, p, q, r)

Merge(A, p, q, r)
  n1 = q - p + 1
  n2 = r - q
  let L[1..n1 + 1] and R[1..n2 + 1] be new arrays
  for i = 1 to n1
    L[i] = A[p + i - 1]
  for j = 1 to n2
    R[j] = A[q + j]
  L[n1 + 1] = ∞
  R[n2 + 1] = ∞
  i = 1
  j = 1
  for k = p to r
    if L[i] ≤ R[j]
      A[k] = L[i]
      i = i + 1
    else A[k] = R[j]
      j = j + 1
```




## Program for Selection Sort 

1. Selection sort is an algorithm for sorting an array of elements. It works by selecting the smallest element from the array and swapping it with the first element, then selecting the second smallest element and swapping it with the second element, and so on. 

2. The algorithm can be implemented using a loop, which iterates over each element in the array and finds the smallest element. Once the smallest element is found, it is swapped with the current element. 

3. The time complexity of selection sort is O(n^2), where n is the number of elements in the array. This is because the algorithm needs to iterate over each element in the array and then find the smallest element. 

4. Selection sort is not a stable sorting algorithm, meaning that the relative order of elements with the same value is not preserved. 

5. Selection sort is often used in the Design and Analysis of Algorithm Lab in the subject of Real Time System, as it is a simple algorithm to implement and understand.




## Program for Insertion Sort

* Insertion sort is an algorithm for sorting a collection of elements, one at a time, in either ascending or descending order.
* It is a simple sorting algorithm that works by taking elements from the input collection one by one and inserting them in the correct position into a new sorted collection.
* The algorithm maintains two subarrays in a given array.
  * The subarray which is already sorted.
  * Remaining subarray which is unsorted.
* In every iteration of insertion sort, an element is picked from the unsorted subarray and is placed at its correct position in the sorted subarray.
* The time complexity of Insertion Sort is O(n2) in the worst case and O(n) in the best case.
* Insertion Sort is used in the Design and Analysis of Algorithm Lab in the subject of Real Time System.




## Program for Quick Sort

Quick sort is an efficient sorting algorithm that can be used in a real-time system. It is based on the divide-and-conquer approach and works by partitioning the array into two parts and then sorting each part recursively.

1. Choose a pivot element from the array.
2. Rearrange the elements in the array such that all elements smaller than the pivot element come before it and all elements larger than the pivot element come after it.
3. Recursively sort the two parts of the array.
4. The array is now sorted.

Quick sort is an in-place algorithm, meaning that it does not require additional memory and is therefore suitable for real-time systems. It is also a stable algorithm, meaning that the relative order of elements with the same key is preserved. Quick sort has an average time complexity of O(n log n) and is therefore one of the fastest sorting algorithms.




## Knapsack Problem using Greedy Solution

The Knapsack Problem is a classic problem in the field of algorithm design and analysis. It involves selecting a subset of items from a given set of items such that the total weight of the selected items does not exceed the capacity of the knapsack and the total value of the selected items is maximized.

The Greedy Solution to the Knapsack Problem involves selecting the item with the highest value per unit weight and adding it to the knapsack until the capacity of the knapsack is reached. This approach is simple and intuitive, but it does not always yield the optimal solution.

The Design and Analysis of Algorithm Lab in the subject of Real Time System explores the various algorithms and techniques used to solve the Knapsack Problem. These include the Greedy Solution, Dynamic Programming, Branch and Bound, and Integer Programming. Each of these techniques has its own advantages and disadvantages, which are discussed in the lab.




## Perform Travelling Salesman Problem 

The Travelling Salesman Problem (TSP) is an optimization problem which requires finding the shortest path between a set of cities. The goal is to find the shortest path that visits each city exactly once and returns to the starting point. 

TSP is an NP-hard problem and is commonly used to demonstrate the power of algorithms in solving complex problems. It is used in many real-world applications such as route planning, logistics, and scheduling. 

In the Design and Analysis of Algorithms Lab in the subject of Real Time System, students will learn how to solve TSP using various algorithms such as brute force, dynamic programming, branch and bound, and heuristics. 

Brute force algorithms are used to generate all possible paths and compare them to find the shortest path. Dynamic programming algorithms are used to find the shortest path by breaking the problem down into subproblems. Branch and bound algorithms use a tree-like structure to search for the optimal solution. Heuristics are used to quickly find a near-optimal solution. 

The TSP can also be solved using various metaheuristics such as simulated annealing, genetic algorithms, and ant colony optimization. These algorithms are used to find near-optimal solutions in reasonable time. 

Students will also learn about the applications of TSP in various fields such as logistics, route planning, and scheduling. They will also learn how to use TSP to solve real-world problems.




## Find Minimum Spanning Tree using Kruskal’s Algorithm 

Kruskal’s algorithm is an algorithm used to find the minimum spanning tree in a graph. It is a greedy algorithm that finds the minimum spanning tree by selecting the edges with the lowest weight and adding them to the tree until all the vertices in the graph are connected. 

The algorithm works as follows: 
1. Sort the edges in the graph by weight. 
2. Starting with the edge with the lowest weight, add it to the minimum spanning tree. 
3. Check if the edge creates a cycle. If it does, discard it. Otherwise, add it to the tree. 
4. Repeat steps 2 and 3 until all the vertices in the graph are connected. 

The algorithm is useful for finding the minimum cost of connecting all the vertices in a graph. It is used in network design, transportation, and other applications of graph theory.




## Implement N Queen Problem using Backtracking 

1. N Queen Problem is an example of a combinatorial optimization problem. It involves placing N number of queens on an NxN chessboard in such a way that no two queens can attack each other.
2. The problem can be solved using a technique known as backtracking. Backtracking is a general algorithmic technique that considers searching every possible combination in order to solve a problem.
3. In the case of the N Queen Problem, the algorithm starts by placing a queen in the first row and then moves on to the next row. In each row, the algorithm places a queen in each column and then checks if the current configuration is valid.
4. If the current configuration is valid, the algorithm moves on to the next row and repeats the process. If the current configuration is not valid, the algorithm backtracks to the previous row and tries a different configuration.
5. This process is repeated until a valid solution is found or all configurations have been checked. The time complexity of the backtracking algorithm is O(N!).
6. The Design and Analysis of Algorithm Lab in the subject of Real Time System focuses on the implementation of the backtracking algorithm to solve the N Queen Problem. The lab also covers topics such as time complexity analysis, memory management, and optimization techniques.




## Sort a given set of n integer elements using Quick Sort method 

Quick Sort is an efficient sorting algorithm that uses the divide-and-conquer approach. It works by partitioning an array into two parts, and then sorting each part recursively.

The time complexity of Quick Sort depends on the partitioning strategy used. The worst case time complexity is O(n^2) and the best case time complexity is O(n log n).

To run the program for varied values of n > 5000, the elements can be read from a file or generated using a random number generator.

Demonstrating Quick Sort using Java requires implementing the divide-and-conquer approach. First, the array must be partitioned into two parts, then each part must be sorted recursively. The time complexity analysis of Quick Sort must be done for the worst case, average case and best case.

To plot a graph of the time taken versus non graph sheet, a chart can be created with the time taken for each value of n. This chart can then be used to compare the time taken for different values of n.





## Sort a given set of n integer elements using Merge Sort method

Merge Sort is an efficient algorithm for sorting a given set of n integer elements. It is a divide and conquer algorithm, meaning it divides the input into smaller subproblems and then solves these subproblems recursively.

The algorithm works by dividing the input array in half and then recursively sorting each half. The two sorted halves are then merged together to produce the sorted output.

The time complexity of Merge Sort is O(n log n). This means that the algorithm runs in linearithmic time, meaning it takes time proportional to the number of elements in the array multiplied by the logarithm of the same number.

## Computing the Time Complexity

In order to compute the time complexity of Merge Sort, the program must be run for varied values of n greater than 5000 and the time taken to sort must be recorded. A graph of the time taken versus n can then be plotted to demonstrate the time complexity.

The elements can be read from a file or can be generated using a random number generator.

## Demonstrating the Divide and Conquer Method

The divide and conquer method works by dividing a problem into smaller subproblems and then solving them recursively. In the case of Merge Sort, the input array is divided into two halves and each half is sorted recursively. The two sorted halves are then merged together to produce the sorted output.

## Time Complexity Analysis

The time complexity of Merge Sort can be analyzed in terms of worst case, average case and best case scenarios.

In the worst case, the time complexity is O(n log n). This is because the algorithm must divide the input array in half and sort each half recursively.

In the average case, the time complexity is also O(n log n). This is because the algorithm must still divide the input array in half and sort each half recursively.

In the best case, the time complexity is O(n log n). This is because the algorithm must still divide the input array in half and sort each half recursively.




## Implementing the 0/1 Knapsack Problem

The 0/1 Knapsack problem is a classic problem in computer science and algorithms. It can be solved using either a Dynamic Programming method or a Greedy method. 

### Dynamic Programming Method

Dynamic Programming is a method of solving problems by breaking them down into smaller, sub-problems and then solving each of those sub-problems in turn. In the 0/1 Knapsack problem, the goal is to maximize the value of items placed in a knapsack with limited capacity. The Dynamic Programming approach to solving this problem involves creating a matrix of values for each item and each capacity of the knapsack. 

To solve the 0/1 Knapsack problem using Dynamic Programming, the following steps should be followed:

1. Create a matrix of values for each item and each capacity of the knapsack.
2. For each item, calculate the maximum value that can be obtained by placing it in the knapsack.
3. Select the item with the highest value and place it in the knapsack.
4. Repeat steps 2 and 3 until the knapsack is full.

### Greedy Method

The Greedy method is an algorithm for solving the 0/1 Knapsack problem that works by selecting the item with the highest value at each step. The Greedy approach to solving the 0/1 Knapsack problem involves the following steps:

1. Select the item with the highest value.
2. Place the item in the knapsack.
3. Repeat steps 1 and 2 until the knapsack is full.

The Greedy method is a simple approach to solving the 0/1 Knapsack problem, but it does not guarantee an optimal solution.




## From a given vertex in a weighted connected graph, find shortest paths to other vertices using Dijkstra's algorithm

Dijkstra's algorithm is a graph search algorithm used to find the shortest path from one node to another in a weighted graph. It is often used in routing and as a subroutine in other graph algorithms.

The algorithm works by maintaining a set of nodes for which the shortest path from the source vertex is known. At each step, the algorithm adds the node with the lowest distance to the source to the set of known nodes and updates the distance of all its neighbors.

The algorithm works by:

1. Initializing the distance of the source vertex to 0 and all other nodes to infinity.
2. Selecting the unvisited node with the smallest distance from the source.
3. Updating the distance of all the neighbors of the selected node. 
4. Repeating steps 2 and 3 until all the nodes have been visited.

The algorithm can be used to find the shortest paths from a given vertex to all other vertices in a weighted connected graph. It can also be used to find the shortest path between two given vertices.




## Find Minimum Cost Spanning Tree of a given connected undirected graph using Kruskal's algorithm

Kruskal's algorithm is an algorithm used to find the Minimum Cost Spanning Tree (MCST) of a given connected undirected graph. The algorithm works by sorting the edges of the graph by weight and then adding them to the tree one by one, ensuring that the tree remains connected. The algorithm uses the Union-Find data structure to detect cycles in the graph and prevent them from forming.

The algorithm can be used to solve various problems related to graph theory, such as finding the shortest path between two nodes, or finding the minimum cost of a network. It is also useful in real-time systems, where it can be used to find the most efficient route from one point to another in a given time frame.

### Steps of the algorithm

1. Sort all the edges of the graph in non-decreasing order of their weights.
2. Pick the smallest edge and check if it forms a cycle with the spanning tree formed so far.
  - If the edge does not form a cycle, include it in the spanning tree.
  - If the edge forms a cycle, discard it.
3. Repeat steps 2 and 3 until there are (V-1) edges in the spanning tree.

### Union-Find Algorithms

Union-Find algorithms are used to detect cycles in a graph. The algorithms work by keeping track of the components of a graph, and if two components are connected, they are merged into a single component. This process is repeated until all the components are merged into one component.

If a cycle is detected, the algorithm will not add the edge to the spanning tree as it would create a cycle.

### Time Complexity

The time complexity of Kruskal's algorithm is O(ElogE), where E is the number of edges in the graph. This is because the algorithm sorts the edges of the graph in non-decreasing order of their weights, which takes O(ElogE) time. The rest of the algorithm takes linear time, making the overall time complexity O(ElogE).




## Find Minimum Cost Spanning Tree of a given undirected graph using Prim’s algorithm

Prim's algorithm is a greedy algorithm used to find a minimum cost spanning tree of a given undirected graph. It works by building a tree one vertex at a time, always choosing the cheapest edge that connects the current tree to a new vertex.

The algorithm starts with a single vertex, and then adds the cheapest edge connecting it to the graph. It continues to add the cheapest edge connecting the tree to a new vertex until all vertices in the graph are included in the tree.

The following steps outline the algorithm:

1. Initialize a tree with a single vertex, chosen arbitrarily from the graph.
2. Find the cheapest edge from the tree to a vertex not yet in the tree.
3. Add the cheapest edge to the tree.
4. Repeat steps 2 and 3 until all vertices are in the tree.

The resulting tree is a minimum cost spanning tree of the graph.




## Write programs to (a) Implement All-Pairs Shortest Paths problem using Floyd's algorithm. (b) Implement Travelling Sales Person problem using Dynamic programming. for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

* All-Pairs Shortest Paths problem: The goal of this problem is to find the shortest paths between all pairs of vertices in a given graph. Floyd's algorithm is a well-known algorithm used to solve this problem, which works by iteratively updating the distances between all pairs of vertices.

* Travelling Sales Person problem: The goal of this problem is to find the shortest tour that visits every vertex in a given graph. Dynamic programming is a well-known algorithm used to solve this problem, which works by constructing a table of the minimum cost to visit each vertex.





## Design and Implement to Find a Subset of a Given Set

This topic is related to the Design and Analysis of Algorithm Lab in the subject of Real Time System. The goal is to design and implement an algorithm to find a subset of a given set S = {Sl, S2,.....,Sn} of n positive integers whose SUM is equal to a given positive integer d. 

For example, if S ={1, 2, 5, 6, 8} and d= 9, there are two solutions {1,2,6}and {1,8}. 

The algorithm should display a suitable message if the given problem instance doesn't have a solution.




## Design and Implementation of Hamiltonian Cycles in a Connected Undirected Graph G of n Vertices Using Backtracking Principle

1. A Hamiltonian cycle, also known as a Hamiltonian circuit, is a graph cycle that visits each vertex exactly once. 
2. In a connected undirected graph G of n vertices, there may be multiple Hamiltonian cycles. 
3. To find all Hamiltonian cycles in a connected undirected graph G, the backtracking principle can be used. 
4. The backtracking principle involves starting at a vertex, exploring all possible paths that start from that vertex, and backtracking when a vertex has no further unexplored paths. 
5. The backtracking principle can be implemented using a recursive algorithm. 
6. The recursive algorithm starts at a vertex and recursively visits each vertex in the graph, until all vertices have been visited. 
7. If all vertices have been visited, the algorithm checks if the current path forms a Hamiltonian cycle. 
8. If the path does not form a Hamiltonian cycle, the algorithm backtracks to the previous vertex and continues exploring all possible paths from that vertex. 
9. The algorithm continues exploring all possible paths until all Hamiltonian cycles have been found. 
10. The time complexity of the backtracking algorithm is O(n!), where n is the number of vertices in the graph.

