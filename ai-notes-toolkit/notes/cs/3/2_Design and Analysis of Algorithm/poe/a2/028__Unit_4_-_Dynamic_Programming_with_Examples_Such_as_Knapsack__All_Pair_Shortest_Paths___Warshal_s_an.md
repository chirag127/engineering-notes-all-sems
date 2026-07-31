 Here is the content in markdown format:

## Unit 4 - Dynamic Programming with Examples Such as Knapsack. All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms, Resource Allocation Problem. Backtracking, Branch and Bound with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

-   **Knapsack Problem**: Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
    -   **Recursive Solution**: Generate all subsets of items and recursively calculate the maximum value for each subset. The overall maximum is the required answer. The time complexity is exponential.
    -   **Dynamic Programming Solution**: Build a table K[][] in bottom-up manner and return K[n][W] where K[i][w] is the maximum value with first i items and knapsack capacity w. The time complexity is O(nw)
-   **Shortest Path**: Find the shortest path between a source vertex s and every other vertex t in a given graph.
    -   **Warshall's algorithm**: It calculates distances between every pair of vertices and modifies the given graph by including transitive edges to produce the transitive closure of the graph. The time complexity is O(V3) where V is the number of vertices.
    -   **Floyd's algorithm**: It calculates the shortest distances between every pair of vertices and detects negative weight cycles. The time complexity is O(V3).
-   **Resource Allocation Problem**: Allocate scarce resources to competing tasks to maximize the total reward earned or minimize the total cost incurred.
-   **Backtracking**: A recursive algorithm that tries to generate all possible solutions to a computational problem, each time removing candidates to focus on finding correct solutions. It abandons each partial solution as soon as it determines that it cannot lead to a valid full solution. Popular examples include Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.