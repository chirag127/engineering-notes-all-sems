## Find Minimum Cost Spanning Tree of a given connected undirected graph using Kruskal's algorithm. Use Union-Find algorithms in your program.

- A **spanning tree** of a graph is a subgraph that contains all the vertices and is a tree (i.e., has no cycles).
- A **minimum spanning tree (MST)** of a weighted graph is a spanning tree whose sum of edge weights is minimum among all possible spanning trees.
- **Kruskal's algorithm** is a greedy algorithm that finds a MST of a given connected, weighted, undirected graph by selecting the edges with the smallest weights that do not form a cycle with the edges already in the MST.
- **Union-Find** algorithms are data structures and methods that support two operations: **union** (merging two disjoint sets into one) and **find** (finding the representative or leader of a set that contains a given element).
- Union-Find algorithms can be used to efficiently check if adding an edge to the MST would create a cycle or not, by maintaining a set of connected components and updating them as new edges are added.
- The steps of Kruskal's algorithm using Union-Find are:

  1. Sort all the edges in non-decreasing order of their weights.
  2. Initialize a MST as an empty set and a Union-Find data structure with each vertex as a singleton set.
  3. Repeat until the MST has V-1 edges or all the edges are processed:
     - Pick the edge with the smallest weight from the sorted list.
     - If the edge connects two vertices that belong to different sets in the Union-Find data structure, then add the edge to the MST and perform a union operation on the two sets.
     - Otherwise, discard the edge as it would create a cycle in the MST.
  4. Return the MST or report that the graph is not connected.

- The following is a pseudocode for Kruskal's algorithm using Union-Find:

  ```
  function kruskal(graph):
    # graph is a list of edges (u, v, w) where u and v are vertices and w is the weight
    # sort the edges by weight in non-decreasing order
    graph.sort(key=lambda edge: edge[2])
    # initialize an empty MST
    mst = []
    # initialize a Union-Find data structure with each vertex as a singleton set
    uf = UnionFind(graph.vertices)
    # loop through the edges
    for edge in graph:
      # unpack the edge
      u, v, w = edge
      # find the sets that contain u and v
      u_set = uf.find(u)
      v_set = uf.find(v)
      # if the sets are different, then the edge does not create a cycle
      if u_set != v_set:
        # add the edge to the MST
        mst.append(edge)
        # merge the two sets
        uf.union(u_set, v_set)
      # if the MST has V-1 edges, then it is complete
      if len(mst) == graph.vertices - 1:
        break
    # return the MST or report that the graph is not connected
    if len(mst) == graph.vertices - 1:
      return mst
    else:
      return "The graph is not connected"
  ```