 Here are the notes in Markdown format:

## From a given vertex in a weighted connected graph, find shortest paths to other vertices using Dijkstra's algorithm.

### Algorithm

1. Take the starting vertex as the current vertex. Mark it as visited.
2. Find an unvisited vertex which is adjacent to the current vertex and has a minimum distance from the starting vertex. Mark it as the next current vertex.
3. Repeat step#2 until all vertices are visited.
4. The minimum distance of the current vertex gives the shortest path from the starting vertex.

### Pseudocode

dijkstra(graph, startVertex):
1. create a distance array and initialize all entries to infinity except for startVertex which is 0
2. create a visited set and add startVertex to it
3. while (visited set doesn't contain all vertices):
4. find an unvisited vertex u with a minimum distance in the distance array
5. add u to the visited set
6. update distance array values for neighbors of u (distance to neighbor = distance to u + edge weight)
7. return distance array

### Complexity

Time complexity: O((V + E)logV), where V is number of vertices and E is number of edges in the graph. This is due to the priority queue used to fetch the minimum distance vertex.
Space complexity: O(V), the size of the distance array.

The notes are formal and written in points without any emojis or external links as instructed. The content is written in Markdown format inside the header you specified. Let me know if you would like me to modify or add anything.