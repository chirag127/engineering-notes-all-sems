## From a given vertex in a weighted connected graph, find shortest paths to other vertices using Dijkstra's algorithm.

Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph. It was conceived by computer scientist Edsger W. Dijkstra in 1956. The algorithm exists in many variants; Dijkstra's original variant found the shortest path between two nodes, but a more common variant fixes a single node as the "source" node and finds shortest paths from the source to all other nodes in the graph, producing a shortest-path tree.

Here are the steps to find the shortest paths from a given vertex in a weighted connected graph using Dijkstra's algorithm:

1. Assign a tentative distance value to every vertex: set it to zero for our initial vertex and to infinity for all other vertices. Set the initial vertex as current.
2. For the current vertex, consider all of its neighbors that are still in the unvisited set. Calculate the tentative distance for each neighbor through the current vertex. Compare the newly calculated tentative distance to the current assigned value and assign the new value if it is less than the current assigned value.
3. When we are done considering all of the neighbors of the current vertex, mark the current vertex as visited. A visited vertex will never be checked again.
4. Select the unvisited vertex with the smallest tentative distance, set it as the new current vertex, and go back to step 2. If all the vertices have been visited, the algorithm has finished.
5. The algorithm will stop when it has found the shortest path to every vertex in the graph.
