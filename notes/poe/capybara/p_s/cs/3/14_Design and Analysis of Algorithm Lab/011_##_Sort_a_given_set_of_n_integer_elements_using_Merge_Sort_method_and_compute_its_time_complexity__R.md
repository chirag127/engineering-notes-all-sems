## From a given vertex in a weighted connected graph, find shortest paths to other vertices using Dijkstra's algorithm.

Dijkstra's algorithm is a popular algorithm for finding the shortest path between two nodes in a graph. It works by maintaining a set of unvisited nodes, and repeatedly selecting the node with the shortest distance from the start node, updating the distance to its neighbors, and adding them to the set of visited nodes.

### Steps of Dijkstra's algorithm:

1. Assign a tentative distance value to every vertex: set it to zero for the start vertex and to infinity for all other vertices.

2. Set the start vertex as current and mark it visited.

3. For each neighbor of the current vertex, calculate the tentative distance from the start vertex to that neighbor. Compare the newly calculated tentative distance to the current assigned value and assign the smaller one.

4. When we have visited all the neighbors, mark the current vertex as visited. If the destination vertex has been marked visited (when planning a route between two specific nodes) or if the smallest tentative distance among the nodes in the unvisited set is infinity (when planning a complete traversal), then stop. The algorithm has finished.

5. Select the unvisited node that is marked with the smallest tentative distance, and set it as the new current node.

6. Repeat steps 3 to 5 until all nodes have been visited.

### Advantages of Dijkstra's algorithm:

- Dijkstra's algorithm is guaranteed to find the shortest path between two nodes in a graph, provided that the graph is weighted, connected, and has no negative edge weights.
- It is relatively simple to understand and implement.
- The algorithm can be adapted to find the shortest path between a source node and all other nodes in the graph.

### Disadvantages of Dijkstra's algorithm:

- Dijkstra's algorithm does not work with negative edge weights. In such cases, other algorithms like Bellman-Ford algorithm can be used.
- The algorithm can be slow on large graphs with many edges or vertices.
- It may not be suitable for real-time systems or time-critical applications.

### Example:

Consider the following weighted graph:

```
     2        3
(A)----(B)----(C)
 |   1/ \4     |5
 |   /   \    |
 |  /     \   |
 | /2     1\  |
(D)---------(E)
      3
```

Starting at node A, we want to find the shortest path to all other nodes in the graph.

Applying Dijkstra's algorithm, we get the following table:

| Node | Distance from A | Visited? |
|------|----------------|----------|
| A    | 0              | Yes      |
| B    | 2              | Yes      |
| D    | 1              | Yes      |
| C    | 5              | No       |
| E    | 3              | No       |

The shortest paths from A to all other nodes in the graph are:

- A -> B -> E: distance = 2 + 1 = 3
- A -> D: distance = 1
- A -> B: distance = 2
- A -> C -> E: distance = 5 + 3 = 8

### Applications:

Dijkstra's algorithm has many practical applications, including:

- Finding the shortest path between two points on a map.
- Routing data packets in computer networks.
- Optimizing supply chain logistics.
- Scheduling tasks in project management.