### Multigraphs

- A multigraph is a graph that allows multiple edges (also called parallel edges) between the same pair of vertices. A multigraph may or may not have loops, which are edges that connect a vertex to itself.  
- A multigraph can be represented by an ordered pair G = (V, E), where V is a set of vertices and E is a multiset of unordered pairs of vertices. A multiset is a collection of elements that can have repetitions.  
- A multigraph can be visualized by drawing the vertices as points and the edges as curves connecting the vertices. If there are multiple edges between two vertices, they are drawn as separate curves. If there is a loop at a vertex, it is drawn as a curve that starts and ends at the same vertex.  
- For example, the following is a multigraph with 4 vertices and 7 edges, including 2 loops and 2 parallel edges:

![multigraph example](https://i.imgur.com/0wZy7w1.png)

- A multigraph is a generalization of a simple graph, which is a graph that does not have loops or multiple edges. A simple graph can be seen as a special case of a multigraph where the multiset of edges is a set, i.e., no repetitions are allowed.  
- A multigraph can also be seen as a special case of a pseudograph, which is a graph that allows both loops and multiple edges. A pseudograph can be represented by an ordered pair G = (V, E), where V is a set of vertices and E is a multiset of pairs of vertices, which can be ordered or unordered. A pseudograph can be visualized by drawing the vertices as points and the edges as curves connecting the vertices, with the same conventions as a multigraph.  
- For example, the following is a pseudograph with 4 vertices and 8 edges, including 3 loops and 2 parallel edges:

![pseudograph example](https://i.imgur.com/3q0zjZM.png)

- A multigraph can be useful for modeling situations where there can be more than one connection or relationship between two entities, such as roads, flights, networks, etc.  
- Some properties and concepts of simple graphs can be extended to multigraphs, such as degree, adjacency, path, cycle, connectedness, etc. However, some definitions and results may differ or require modifications. For example, the degree of a vertex in a multigraph is the number of edges incident to it, counting loops twice. A multigraph is connected if there is a path between any two vertices, where a path is a sequence of edges that connects a sequence of vertices, allowing repetitions. A multigraph is Eulerian if it has an Eulerian circuit, which is a cycle that uses every edge exactly once, allowing repetitions of vertices.