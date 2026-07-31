### Greedy Methods with Examples Such as Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms

Greedy methods are a class of algorithms that make locally optimal choices in the hope of finding a global optimum. In this section, we will discuss greedy methods with examples such as Single Source Shortest Paths - Dijkstra's and Bellman Ford Algorithms.

1. Single Source Shortest Paths - Dijkstra's Algorithm
- Dijkstra's algorithm is a greedy algorithm for finding the shortest path between nodes in a graph.
- It starts at the source node and iteratively adds the node with the lowest distance to the visited set.
- The algorithm terminates when the destination node has been reached or all reachable nodes have been visited.
- Dijkstra's algorithm is often used in routing and as a subroutine in other graph algorithms.

2. Single Source Shortest Paths - Bellman Ford Algorithm
- Bellman Ford algorithm is another greedy algorithm used to find the shortest path between nodes in a graph.
- It can handle graphs with negative edge weights unlike Dijkstra's algorithm.
- The algorithm iterates over all edges |V|-1 times and relaxes the edges to find the shortest path.
- The algorithm returns a negative cycle if it exists in the graph.

3. Optimal Reliability Allocation
- Optimal reliability allocation is a problem of allocating reliability to components in a system to maximize the total reliability of the system.
- Greedy methods can be used to solve this problem.
- One such example is the proportional allocation method where the reliability is allocated to components proportional to their costs.

4. Knapsack Problem
- The knapsack problem is a combinatorial optimization problem where a set of items is to be packed into a knapsack of a given capacity.
- The objective is to maximize the value of the items in the knapsack without exceeding its capacity.
- Greedy methods can be used to solve this problem such as the fractional knapsack algorithm.

5. Minimum Spanning Trees - Prim's Algorithm
- Prim's algorithm is a greedy algorithm used to find the minimum spanning tree of a graph.
- The algorithm starts at a node and iteratively adds the edge with the lowest weight to the tree.
- The algorithm terminates when all nodes have been visited.

6. Minimum Spanning Trees - Kruskal's Algorithm
- Kruskal's algorithm is another greedy algorithm used to find the minimum spanning tree of a graph.
- The algorithm starts with a forest of nodes and iteratively adds the edge with the lowest weight to connect two components of the forest.
- The algorithm terminates when the forest has been reduced to a single tree.

In conclusion, greedy methods are powerful tools for solving optimization problems. They make locally optimal choices with the hope of finding a global optimum. The examples discussed in this section such as Dijkstra's algorithm, Bellman Ford algorithm, optimal reliability allocation, knapsack problem, and minimum spanning trees demonstrate the wide range of applications of greedy methods.