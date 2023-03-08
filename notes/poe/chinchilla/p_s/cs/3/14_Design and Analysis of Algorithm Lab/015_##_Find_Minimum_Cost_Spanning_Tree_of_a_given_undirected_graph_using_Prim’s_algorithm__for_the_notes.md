## Find Minimum Cost Spanning Tree of a given undirected graph using Prim’s algorithm

Prim's algorithm is a greedy algorithm used to find the minimum cost spanning tree of a given undirected graph. It starts with a single vertex and keeps adding vertices to the tree until all the vertices are included in the tree. 

### Algorithm

1. Create a set `S` of vertices that are already included in the minimum spanning tree.
2. Create a priority queue `Q` of edges that connect a vertex in `S` to a vertex not in `S`.
3. Initialize `S` with any vertex and `Q` with all the edges that connect to that vertex.
4. While `Q` is not empty:
   - Remove the edge with minimum weight from `Q`.
   - If the edge connects a vertex in `S` to a vertex not in `S`, add the vertex not in `S` to `S` and add all the edges that connect to that vertex to `Q`.
5. The minimum spanning tree is formed by the edges in `S`.

### Example

Let's take the following undirected graph with 5 vertices and 7 edges:

```
     4
  A-----B
  |\   /|\
5| \ / | \3
  |  C  |
5| / \ | /2
  |/   \|
  D-----E
     4
```

We can start with vertex A and add it to the set `S`. Then we add all the edges that connect to vertex A to the priority queue `Q`. The edges in `Q` are:

```
(AB, 4)
(AC, 5)
(AD, 5)
```

We remove the edge with minimum weight from `Q`, which is edge (AB, 4). Vertex B is not in `S`, so we add it to `S`. Then we add all the edges that connect to vertex B to `Q`. The edges in `Q` are:

```
(BC, 3)
(BD, 5)
(BE, 2)
```

We remove the edge with minimum weight from `Q`, which is edge (BE, 2). Vertex E is not in `S`, so we add it to `S`. Then we add all the edges that connect to vertex E to `Q`. The edges in `Q` are:

```
(BC, 3)
(BD, 5)
(CE, 4)
```

We remove the edge with minimum weight from `Q`, which is edge (BC, 3). Vertex C is not in `S`, so we add it to `S`. Then we add all the edges that connect to vertex C to `Q`. The edges in `Q` are:

```
(BD, 5)
(CE, 4)
(CD, 5)
```

We remove the edge with minimum weight from `Q`, which is edge (CE, 4). Vertex D is not in `S`, so we add it to `S`. Then we add all the edges that connect to vertex D to `Q`. The edges in `Q` are:

```
(BD, 5)
(CD, 5)
```

We remove the edge with minimum weight from `Q`, which is edge (CD, 5). All the vertices are now included in `S`, so we stop. The minimum spanning tree is formed by the edges in `S`:

```
     4
  A-----B
      / |\
    2/  | \3
    /   |  \
  D-----E   C
     5     5
```

### Advantages

- It is easy to understand and implement.
- It always produces a minimum spanning tree.

### Disadvantages

- It can be slow for large graphs.
- It may not be efficient for sparse graphs.

### Applications

- Network design
- Circuit design
- Transportation planning
- Image segmentation