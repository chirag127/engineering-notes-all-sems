## Find Minimum Cost Spanning Tree of a given connected undirected graph using Kruskal's algorithm. Use Union-Find algorithms in your program.

- A **spanning tree** of a graph is a subgraph that contains all the vertices and is a tree (i.e., has no cycles).
- A **minimum spanning tree (MST)** of a weighted graph is a spanning tree whose sum of edge weights is minimum among all possible spanning trees.
- **Kruskal's algorithm** is a greedy algorithm that finds a MST of a given connected, weighted, undirected graph by selecting the edges with the smallest weights that do not form a cycle with the previously selected edges.
- **Union-Find** algorithms are data structures and methods that support two operations: **union** (merging two disjoint sets into one) and **find** (determining which set a given element belongs to).
- Union-Find algorithms can be used to implement **disjoint-set** data structures, which can efficiently keep track of the connected components of a graph and check if adding an edge creates a cycle or not.

The steps of Kruskal's algorithm using Union-Find algorithms are:

1. Sort all the edges of the graph in non-decreasing order of their weights.
2. Initialize a disjoint-set data structure with each vertex as a separate set.
3. Initialize an empty set to store the edges of the MST.
4. For each edge in the sorted order, do the following:
   - Find the sets that contain the two endpoints of the edge using the **find** operation.
   - If the sets are different, it means the edge does not create a cycle and can be added to the MST. Perform the **union** operation to merge the two sets and add the edge to the MST set.
   - If the sets are the same, it means the edge creates a cycle and cannot be added to the MST. Ignore the edge and continue.
5. Repeat step 4 until either the MST set has V-1 edges, where V is the number of vertices in the graph, or all the edges are processed.
6. Return the MST set as the output.

The following is a pseudocode for the algorithm:

```
function kruskal(graph):
  // graph is a list of edges with weights
  // each edge is a tuple (u, v, w) where u and v are vertices and w is the weight
  // assume the graph is connected, weighted and undirected
  // initialize an empty list to store the MST edges
  mst = []
  // sort the graph edges by weights in non-decreasing order
  graph.sort(key=lambda edge: edge[2])
  // initialize a disjoint-set data structure with each vertex as a separate set
  ds = DisjointSet()
  for v in graph.vertices:
    ds.make_set(v)
  // loop through the sorted edges
  for edge in graph.edges:
    // get the endpoints and weight of the edge
    u, v, w = edge
    // find the sets that contain u and v
    u_set = ds.find(u)
    v_set = ds.find(v)
    // if the sets are different, the edge does not create a cycle
    if u_set != v_set:
      // add the edge to the MST
      mst.append(edge)
      // merge the sets
      ds.union(u_set, v_set)
    // if the MST has V-1 edges, break the loop
    if len(mst) == graph.vertices - 1:
      break
  // return the MST
  return mst
```

The following is an example of applying the algorithm on a graph:

![graph](https://www.programiz.com/sites/tutorial2program/files/kruskal-initial-graph.png)

The sorted edges are:

| Edge | Weight |
|------|--------|
| AD   | 1      |
| AG   | 2      |
| AB   | 4      |
| BE   | 4      |
| EG   | 5      |
| CF   | 6      |
| AC   | 7      |
| CD   | 7      |
| DF   | 8      |
| DE   | 9      |
| FG   | 9      |
| BC   | 10     |

The MST edges are:

| Edge | Weight |
|------|--------|
| AD   | 1      |
| AG   | 2      |
| AB   | 4      |
| BE   | 4      |
| CF   | 6