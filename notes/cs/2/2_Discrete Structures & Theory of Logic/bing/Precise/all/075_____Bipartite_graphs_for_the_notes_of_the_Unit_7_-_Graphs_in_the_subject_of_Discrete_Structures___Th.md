# Unit 7 - Graphs in the subject of Discrete Structures & Theory of Logic
### Bipartite Graphs

- A bipartite graph is a type of graph in which the vertices can be divided into two disjoint sets such that every edge connects a vertex in one set to a vertex in the other set.
- In other words, a bipartite graph does not contain any odd cycles.
- A simple way to check if a graph is bipartite is to try to color its vertices using two colors, such that no two adjacent vertices share the same color. If this is possible, then the graph is bipartite.
- Bipartite graphs have many applications in modeling real-world problems, such as matching problems, scheduling problems, and network flow problems.
- Some common examples of bipartite graphs include:
  - A graph representing a group of people and their friendships, where the two sets of vertices represent men and women, and edges represent friendships between a man and a woman.
  - A graph representing a set of tasks and a set of workers, where the two sets of vertices represent tasks and workers, and edges represent the assignment of a worker to a task.
  - A graph representing a set of items and a set of bins, where the two sets of vertices represent items and bins, and edges represent the assignment of an item to a bin.
- The complete bipartite graph $K_{m,n}$ is a bipartite graph where one set of vertices has size $m$ and the other set has size $n$, and there is an edge between every pair of vertices from the two different sets.
- A bipartite graph is said to be balanced if the two sets of vertices have the same size.
- A perfect matching in a bipartite graph is a matching that matches all vertices in one set to a unique vertex in the other set.
- The maximum matching problem in bipartite graphs can be solved using the Hungarian algorithm or the Hopcroft-Karp algorithm.
- The minimum vertex cover problem in bipartite graphs can be solved using the Konig's theorem, which states that the size of the minimum vertex cover in a bipartite graph is equal to the size of the maximum matching.