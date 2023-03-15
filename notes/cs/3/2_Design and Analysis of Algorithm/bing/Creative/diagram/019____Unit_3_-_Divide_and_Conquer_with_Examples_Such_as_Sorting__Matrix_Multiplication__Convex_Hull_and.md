## Unit 3 - Divide and Conquer with Examples Such as Sorting, Matrix Multiplication, Convex Hull and Searching. Greedy Methods with Examples Such as Optimal Reliability Allocation, Knapsack, Minimum Spanning Trees – Prim’s and Kruskal’s Algorithms, Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms.

### Divide and Conquer

- Divide and conquer is a paradigm for designing algorithms that solve a problem by breaking it into smaller subproblems, solving them recursively, and combining their solutions to get the final answer  .
- Divide and conquer algorithms have three steps:
  - Divide: Split the problem into smaller and simpler subproblems of the same type.
  - Conquer: Solve the subproblems recursively, either directly or by applying divide and conquer again.
  - Combine: Merge the solutions of the subproblems to obtain the solution of the original problem.
- Divide and conquer algorithms are often efficient and elegant, as they reduce the complexity of the problem by exploiting its structure and properties .
- Some examples of divide and conquer algorithms are:
  - Merge sort: A sorting algorithm that divides the array into two halves, sorts them recursively, and merges the sorted halves .
  - Quick sort: A sorting algorithm that partitions the array around a pivot element, and sorts the two subarrays recursively .
  - Binary search: A searching algorithm that finds an element in a sorted array by repeatedly halving the search space and comparing the middle element with the target .
  - Strassen's algorithm: A matrix multiplication algorithm that divides each matrix into four submatrices, and computes the product using seven recursive multiplications and some additions and subtractions .
  - Convex hull: A geometric problem that finds the smallest convex polygon that contains a set of points, by dividing the points into two subsets, finding their convex hulls recursively, and merging them using a linear scan.

### Greedy Methods

- Greedy methods are a paradigm for designing algorithms that make a sequence of choices, each of which is the best available option at the moment, without considering the future consequences  .
- Greedy algorithms have the following characteristics:
  - They are iterative, meaning they make one choice at a time until the problem is solved.
  - They are local, meaning they choose the best option based on the current situation, without looking ahead or back.
  - They are myopic, meaning they do not guarantee the optimal solution, as they may miss a better choice later.
- Greedy algorithms are often simple and fast, but they may not always work for every problem, as they may get stuck in a suboptimal solution  .
- Some examples of greedy algorithms are:
  - Optimal reliability allocation: A problem that allocates a given budget to improve the reliability of a system, by choosing the component with the highest improvement per unit cost at each step.
  - Knapsack: A problem that fills a knapsack with items of different weights and values, by choosing the item with the highest value per unit weight at each step  .
  - Minimum spanning tree: A problem that finds a subset of edges in a weighted graph that connects all the vertices with the minimum total weight, by choosing the edge with the lowest weight that does not form a cycle at each step  . Two common algorithms for this problem are Prim's algorithm and Kruskal's algorithm.
  - Single source shortest paths: A problem that finds the shortest paths from a given source vertex to all other vertices in a weighted graph, by choosing the vertex with the smallest distance from the source that has not been visited yet at each step  . Two common algorithms for this problem are Dijkstra's algorithm and Bellman Ford algorithm.