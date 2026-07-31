## From a given vertex in a weighted connected graph, find shortest paths to other vertices using Dijkstra's algorithm.

Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph. It was conceived by computer scientist Edsger W. Dijkstra in 1956. The algorithm exists in many variants; Dijkstra's original variant found the shortest path between two nodes, but a more common variant fixes a single node as the "source" node and finds shortest paths from the source to all other nodes in the graph, producing a shortest-path tree.

Here are the steps to find the shortest paths from a given vertex in a weighted connected graph using Dijkstra's algorithm:

1. Create a set of all the unvisited vertices called the unvisited set.
2. Assign to every vertex a tentative distance value: set it to zero for our initial vertex and to infinity for all other vertices. Set the initial vertex as current.
3. For the current vertex, consider all of its unvisited neighbors and calculate their tentative distances through the current vertex. Compare the newly calculated tentative distance to the current assigned value and assign the new value if it is less than the current assigned value.
4. When we are done considering all of the unvisited neighbors of the current vertex, mark the current vertex as visited and remove it from the unvisited set. A visited vertex will never be checked again.
5. If the destination vertex has been marked visited (when planning a route between two specific vertices) or if the smallest tentative distance among the vertices in the unvisited set is infinity (when planning a complete traversal; occurs when there is no connection between the initial vertex and remaining unvisited vertices), then the algorithm has finished.
6. Otherwise, select the unvisited vertex that is marked with the smallest tentative distance, set it as the new current vertex, and go back to step 3.
