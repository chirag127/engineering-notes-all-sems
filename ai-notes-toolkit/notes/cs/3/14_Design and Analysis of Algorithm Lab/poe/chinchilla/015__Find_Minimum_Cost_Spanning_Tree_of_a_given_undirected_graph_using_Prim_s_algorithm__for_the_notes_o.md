## Find Minimum Cost Spanning Tree of a given undirected graph using Prim’s algorithm

Prim's algorithm is a popular algorithm for finding the minimum cost spanning tree of a given undirected graph. It is an example of a greedy algorithm that works by selecting the minimum weight edge that connects any two trees in the graph at each iteration, until all the vertices are included in the tree. The algorithm has a time complexity of O(ElogV), where E is the number of edges and V is the number of vertices in the graph.

Here are the steps to implement Prim's algorithm:

1. Initialize a set of visited vertices to an empty set and a set of unvisited vertices to all vertices in the graph.

2. Choose any vertex from the unvisited set as the starting vertex, and add it to the visited set.

3. For each adjacent vertex to the starting vertex, create a new edge with the weight of the edge connecting the two vertices.

4. Add these new edges to a priority queue or a heap, sorted by their weight.

5. While the priority queue or heap is not empty, remove the edge with the smallest weight from the queue.

6. If the vertices connected by the edge are already in the visited set, discard the edge.

7. Otherwise, add the edge to the minimum spanning tree and add the new vertex to the visited set.

8. Repeat steps 3 to 7 until all vertices are in the visited set.

9. The minimum cost spanning tree is the collection of edges in the minimum spanning tree.

Here is an example implementation of Prim's algorithm in Python:

```
# Python implementation of Prim's algorithm for finding minimum cost spanning tree
import heapq

def prim(graph):
    visited = set()
    unvisited = set(graph.keys())
    start = next(iter(unvisited))
    visited.add(start)
    unvisited.remove(start)
    heap = []
    for dest, weight in graph[start].items():
        heapq.heappush(heap, (weight, start, dest))
    mst = []
    while heap:
        weight, src, dest = heapq.heappop(heap)
        if dest in visited:
            continue
        visited.add(dest)
        unvisited.remove(dest)
        mst.append((src, dest, weight))
        for dest2, weight2 in graph[dest].items():
            if dest2 not in visited:
                heapq.heappush(heap, (weight2, dest, dest2))
    return mst
```

In this implementation, the graph is represented as a dictionary where the keys are the vertices and the values are another dictionary that maps adjacent vertices to the weight of the connecting edge. The function returns a list of tuples representing the edges in the minimum cost spanning tree.

In conclusion, Prim's algorithm is a simple and efficient way to find the minimum cost spanning tree of a given undirected graph. The algorithm works by greedily choosing the minimum weight edge at each iteration, and has a time complexity of O(ElogV).