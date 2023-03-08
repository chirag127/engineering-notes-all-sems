 Here are the notes for the given topics in Markdown format:

### Divide and Conquer with Examples Such as Sorting, Matrix Multiplication, Convex Hull and Searching

- Divide and conquer is an algorithm design paradigm which divides the problem into smaller subproblems, solves them recursively and then combines their solutions to get the solution of the original problem.
- Some examples of divide and conquer algorithms are:
- Sorting: Merge sort, quicksort
- Matrix multiplication: Strassen's algorithm
- Convex hull: Graham scan algorithm
- Searching: Binary search

Advantages:
- Efficient (due to decomposing into smaller subproblems and recursion)
- Naturally parallelizable (subproblems can be solved independently)

Disadvantages:
- Extra overhead for recursion and combining subproblem solutions
- Not suitable for small input sizes (due to overhead)

### Greedy Methods with Examples Such as Optimal Reliability Allocation, Knapsack, Minimum Spanning Trees – Prim’s and Kruskal’s Algorithms, Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms.

Greedy algorithms make locally optimal choices at each stage in the hope of finding a global optimum.

Some examples:

- Optimal reliability allocation: Allocate budget to components with highest reliability-cost ratios
- Knapsack: Choose items with highest value-weight ratios until knapsack is full
- Minimum spanning trees:
 - Prim's: Grow tree from starting vertex by always choosing minimum cost edge
 - Kruskal's: Sort edges by cost and add if doesn't create cycle
- Shortest paths:
 - Dijkstra's: Greedily choose unvisited vertex with minimum distance and update neighbors
 - Bellman-Ford: Repeatedly relax all edges - useful for detecting negative weight cycles

Advantages:
- Simple and efficient
- Often gives good solutions/approximations

Disadvantages:
- Does not always find optimal solution
- Hard to prove guarantees on solution quality