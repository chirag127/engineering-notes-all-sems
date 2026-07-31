## Find Minimum Cost Spanning Tree of a given undirected graph using Prim’s algorithm.

Prim’s algorithm is a greedy algorithm used to find the Minimum Spanning Tree (MST) of a given undirected graph. The MST is a tree that spans all the nodes of the graph while minimizing the total cost of the edges. Here are the steps to implement Prim’s algorithm:

1. Initialize a set of visited vertices and a set of unvisited vertices. Choose a starting vertex and add it to the visited set.
2. For each visited vertex, find the adjacent vertices that are not already visited and add them to the unvisited set along with the weight of the edge that connects them to the visited vertex.
3. Select the vertex with the smallest weight in the unvisited set and add it to the visited set. Also, add the weight of the edge that connects it to the visited set to the total cost of the MST.
4. Repeat step 3 until all vertices are visited.

The time complexity of Prim’s algorithm is O(V^2) or O(E log V) depending on the implementation. The space complexity is O(V+E).

Here is the Python code for implementing Prim’s algorithm:

```
def prim_algorithm(graph):
    visited = set()
    unvisited = set(graph.keys())
    start_vertex = next(iter(unvisited))
    visited.add(start_vertex)
    unvisited.remove(start_vertex)
    mst_cost = 0
    while unvisited:
        min_edge = None
        for visited_vertex in visited:
            for unvisited_vertex, weight in graph[visited_vertex].items():
                if unvisited_vertex in unvisited:
                    if min_edge is None or weight < min_edge[2]:
                        min_edge = (visited_vertex, unvisited_vertex, weight)
        visited.add(min_edge[1])
        unvisited.remove(min_edge[1])
        mst_cost += min_edge[2]
    return mst_cost
```

In conclusion, Prim’s algorithm is a useful way to find the Minimum Spanning Tree of a given undirected graph while minimizing the total cost of the edges. It is a simple and efficient algorithm that can be implemented in various programming languages.