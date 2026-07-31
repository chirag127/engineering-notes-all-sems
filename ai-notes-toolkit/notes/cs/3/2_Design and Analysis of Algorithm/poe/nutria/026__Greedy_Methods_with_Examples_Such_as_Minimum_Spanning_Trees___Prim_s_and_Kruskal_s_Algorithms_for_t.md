
### Greedy Methods with Examples 

Greedy methods are algorithms that make decisions based on the current state of the problem and the current best solution at the time. Greedy algorithms are used to solve optimization problems, such as finding the shortest path between two points, or the most efficient way to allocate resources. 

#### Minimum Spanning Trees - Prim's and Kruskal's Algorithms

Prim's algorithm is used to find the minimum spanning tree of a graph. It works by starting with an empty tree and adding edges one at a time, ensuring that the edge added does not create a cycle in the graph. Kruskal's algorithm works by sorting the edges in the graph by weight, then adding them one at a time to the tree, ensuring that the edge added does not create a cycle in the graph.

#### Optimal Reliability Allocation

Optimal reliability allocation is an algorithm used to maximize the reliability of a system by allocating resources in an optimal way. It works by constructing a reliability graph, where each node represents a component of the system, and each edge represents a possible connection between components. The algorithm then finds a set of paths between each pair of nodes such that the total reliability of the system is maximized. 

#### Knapsack

Knapsack is an optimization problem where a set of items must be placed into a knapsack in order to maximize the total value of the items. This can be solved using a greedy algorithm, which works by sorting the items by their value-to-weight ratio, then adding them to the knapsack one at a time until the knapsack is full. 

#### Single Source Shortest Paths - Dijkstra's and Bellman Ford Algorithms

Dijkstra's algorithm is used to find the shortest path between two points in a graph. It works by constructing a tree of shortest paths from the source node to all other nodes in the graph. Bellman-Ford is an algorithm used to find the shortest path between two points in a graph. It works by constructing a table of shortest paths from the source node to all other nodes in the graph.