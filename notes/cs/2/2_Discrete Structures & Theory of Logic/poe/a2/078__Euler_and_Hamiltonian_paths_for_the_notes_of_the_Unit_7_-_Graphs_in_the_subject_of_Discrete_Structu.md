 Here are the notes on Euler and Hamiltonian paths for Unit 7 - Graphs in Discrete Structures & Theory of Logic:

### Euler Paths

1. An Euler path is a path in a graph that traverses every edge exactly once.
2. A graph has an Euler path if it is connected and has zero or two vertices of odd degree.
3. To find an Euler path:
  - Find all vertices of odd degree (if any)
  - Start at one of the vertices of odd degree (if any)
  - Traverse edges greedily, avoiding vertices of odd degree until you return to the starting vertex

### Hamiltonian Paths

1. A Hamiltonian path is a path in a graph that visits every vertex exactly once.
2. A graph has a Hamiltonian path if it is connected and every vertex has a degree of at most n/2, where n is the number of vertices.
3. To find a Hamiltonian path (if one exists):
  - Try iterating through vertices as a potential next vertex in the path
  - For each vertex, check if a path exists from the current vertex to the new vertex
  - Backtrack if no path can be found

The content is written in a formal tone with bullet points and Markdown format as requested. No emojis or external links have been included. Let me know if you would like me to modify or expand the notes in any way.