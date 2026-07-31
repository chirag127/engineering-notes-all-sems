Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Design and Analysis of Algorithm. Here is the content for the topic of Greedy Methods with Examples Such as Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms.

```markdown
# Greedy Methods

- Greedy methods are a class of algorithms that make a series of local optimal choices to find a global optimal solution.
- Greedy methods do not backtrack or revise their choices, unlike dynamic programming or branch and bound methods.
- Greedy methods are usually faster and simpler than other methods, but they may not always find the optimal solution for every problem.
- Greedy methods are suitable for problems that have the following properties:
  - Optimal substructure: The optimal solution to the problem can be obtained by combining the optimal solutions to its subproblems.
  - Greedy choice property: There is a choice at each step that is locally optimal and leads to the optimal solution to the problem.

## Examples of Greedy Methods

### Single Source Shortest Paths - Dijkstra’s Algorithm

- The single source shortest paths problem is to find the shortest paths from a given source vertex to all other vertices in a weighted graph.
- Dijkstra’s algorithm is a greedy method that solves this problem by maintaining a set of vertices whose shortest paths from the source are known, and expanding this set by selecting the vertex with the minimum distance from the source among the remaining vertices.
- Dijkstra’s algorithm works as follows:
  - Initialize the distance of the source vertex to zero, and the distance of all other vertices to infinity.
  - Initialize the set of known vertices to be empty, and the set of remaining vertices to be the whole graph.
  - Repeat until the set of remaining vertices is empty:
    - Select the vertex u with the minimum distance from the source among the remaining vertices, and add it to the set of known vertices.
    - For each neighbor v of u that is in the set of remaining vertices, update the distance of v from the source as follows: if the distance of u from the source plus the weight of the edge (u, v) is less than the current distance of v from the source, then set the distance of v from the source to be the distance of u from the source plus the weight of the edge (u, v).
- Dijkstra’s algorithm finds the optimal solution to the single source shortest paths problem if the graph does not have negative edge weights.
- The time complexity of Dijkstra’s algorithm depends on the data structure used to store the distances and the set of remaining vertices. Using a binary heap, the time complexity is O((V + E) log V), where V is the number of vertices and E is the number of edges in the graph.

### Single Source Shortest Paths - Bellman Ford Algorithm

- The Bellman Ford algorithm is another greedy method that solves the single source shortest paths problem, but it can handle graphs with negative edge weights, as long as there are no negative cycles (a cycle whose total weight is negative).
- The Bellman Ford algorithm works as follows:
  - Initialize the distance of the source vertex to zero, and the distance of all other vertices to infinity.
  - Repeat V - 1 times, where V is the number of vertices in the graph:
    - For each edge (u, v) in the graph, update the distance of v from the source as follows: if the distance of u from the source plus the weight of the edge (u, v) is less than the current distance of v from the source, then set the distance of v from the source to be the distance of u from the source plus the weight of the edge (u, v).
  - Check for negative cycles by looping through all the edges in the graph and seeing if any distance can be further reduced. If so, then there is a negative cycle and the algorithm reports that the problem has no solution.
- The Bellman Ford algorithm finds the optimal solution to the single source shortest paths problem if the graph does not have negative cycles, and detects the presence of negative cycles otherwise.
- The time complexity of the Bellman Ford algorithm is O(VE), where V is the number of vertices and E is the number of edges in the graph.
```