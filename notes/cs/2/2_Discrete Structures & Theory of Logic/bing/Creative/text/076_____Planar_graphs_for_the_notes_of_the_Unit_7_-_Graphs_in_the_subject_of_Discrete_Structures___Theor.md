### Planar Graphs

- A planar graph is a graph that can be drawn on a plane without any edges crossing.
- A plane graph is a planar graph with a specific way of drawing it on a plane, such that the edges are represented by curves that do not intersect except at their endpoints.
- A planar graph can have different plane graphs, depending on how it is drawn. For example, the following graph is planar and has two different plane graphs:

```
    A-----B
   / \   / \
  /   \ /   \
 C-----D-----E
```

```
    A-----B
   / \   / \
  /   \ /   \
 C     D     E
  \   / \   /
   \ /   \ /
    F-----G
```

- A planar graph divides the plane into regions called faces. The number of faces depends on the plane graph. For example, the first plane graph above has four faces, while the second one has six faces.
- A planar graph has some properties that relate the number of vertices, edges, and faces. For example, Euler's formula states that for any connected plane graph, the following equation holds:

```
V - E + F = 2
```

where V is the number of vertices, E is the number of edges, and F is the number of faces.
- A planar graph also has some limitations on the number and degree of its vertices and edges. For example, Kuratowski's theorem states that a graph is planar if and only if it does not contain a subgraph that is homeomorphic to K5 (the complete graph on five vertices) or K3,3 (the complete bipartite graph on six vertices).