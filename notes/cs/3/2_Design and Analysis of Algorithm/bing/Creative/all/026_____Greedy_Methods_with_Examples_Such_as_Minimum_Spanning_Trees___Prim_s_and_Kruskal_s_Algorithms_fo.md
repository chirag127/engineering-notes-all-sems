# Greedy Methods with Examples Such as Minimum Spanning Trees – Prim’s and Kruskal’s Algorithms

- Greedy methods are a class of algorithms that make locally optimal choices at each step, hoping to find a global optimum.
- Greedy methods are often simple, fast, and easy to implement, but they may not always yield the best solution.
- Greedy methods are suitable for problems that have the following properties:
  - Optimal substructure: An optimal solution to the problem contains optimal solutions to the subproblems.
  - Greedy choice property: A locally optimal choice is always part of an optimal solution.
- One example of a problem that can be solved by greedy methods is the minimum spanning tree (MST) problem.
  - A spanning tree of a graph G is a subset of the edges of G that form a tree and include all vertices of G.
  - A minimum spanning tree of a graph G is a spanning tree of G that has the minimum total weight among all spanning trees of G.
  - The MST problem has both optimal substructure and greedy choice property, as proved by the cut property and the cycle property.
- There are several greedy algorithms for finding MSTs, such as Prim's algorithm and Kruskal's algorithm.
  - Prim's algorithm starts with a single node and keeps adding the cheapest edge that connects a node in the tree to a node outside the tree, until all nodes are included.
  - Kruskal's algorithm starts with an empty set of edges and keeps adding the cheapest edge that does not create a cycle, until all nodes are connected.
  - Both algorithms have a time complexity of O(E log V), where E is the number of edges and V is the number of vertices in the graph.
  - Both algorithms can be implemented using a priority queue and a disjoint-set data structure.