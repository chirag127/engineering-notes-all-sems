# Greedy Methods with Examples Such as Minimum Spanning Trees – Prim’s and Kruskal’s Algorithms

- Greedy methods are a class of algorithms that make locally optimal choices at each step, hoping to find a global optimum.
- Greedy methods are often simple, fast, and easy to implement, but they may not always yield the best solution.
- Greedy methods can be applied to various optimization problems, such as finding the minimum spanning tree, the optimal reliability allocation, the knapsack problem, and the single source shortest paths problem.

## Minimum Spanning Tree

- A spanning tree of a graph G is a subset of the edges of G that form a tree and include all vertices of G.
- A minimum spanning tree (MST) of a graph G is a spanning tree of G that has the minimum possible total edge weight.
- Finding an MST is useful for applications such as network design, clustering, image segmentation, and approximation algorithms.

### Prim's Algorithm

- Prim's algorithm is a greedy algorithm that finds an MST by starting with a single node and adding the cheapest edge that connects it to another node that is not already in the tree.
- The algorithm repeats this process until all nodes are in the tree.
- Prim's algorithm can be implemented using a priority queue to store the edges and their weights, and a set to keep track of the nodes in the tree.
- The time complexity of Prim's algorithm is O(E log V), where E is the number of edges and V is the number of vertices.

### Kruskal's Algorithm

- Kruskal's algorithm is another greedy algorithm that finds an MST by sorting the edges by their weights and adding them to the tree one by one, as long as they do not create a cycle.
- The algorithm uses a disjoint-set data structure to keep track of the connected components of the tree and to check for cycles.
- The time complexity of Kruskal's algorithm is O(E log E), which is equivalent to O(E log V) since E is at most V^2.