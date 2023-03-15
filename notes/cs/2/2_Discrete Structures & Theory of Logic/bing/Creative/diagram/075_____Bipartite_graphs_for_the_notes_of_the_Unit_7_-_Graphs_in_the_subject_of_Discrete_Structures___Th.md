### Bipartite graphs

- A **bipartite graph** is a graph whose vertices can be divided into two disjoint and independent sets, such that every edge connects a vertex in one set to a vertex in the other set .
- The two sets of vertices are usually called the **parts** of the graph, and are denoted by and .
- A bipartite graph can also be seen as a graph that is **two-colorable**, meaning that the vertices can be colored with two colors such that no two adjacent vertices have the same color .
- A **complete bipartite graph** is a bipartite graph where every vertex in one part is connected to every vertex in the other part . It is denoted by , where and are the sizes of the two parts.
- A **bipartite matching** is a set of edges in a bipartite graph such that no two edges share a common vertex. A **maximum bipartite matching** is a bipartite matching with the largest possible number of edges.
- A **bipartite graph** can be represented by a **bipartite adjacency matrix**, which is a matrix with rows and columns, where is the number of vertices in and is the number of vertices in . The entry of the matrix is 1 if there is an edge between vertex and vertex , and 0 otherwise.
- A **bipartite graph** can also be represented by a **bipartite incidence matrix**, which is a matrix with rows and columns, where is the number of vertices in and is the number of edges in the graph. The entry of the matrix is 1 if edge is incident to vertex , and 0 otherwise.

Here is an example of a bipartite graph with 6 vertices and 7 edges, along with its bipartite adjacency matrix and bipartite incidence matrix:

```
   A   B   C
   | \ | / |
   |  \|/  |
   D---E---F
```

Bipartite adjacency matrix:

```
  D E F
A 1 1 0
B 0 1 1
C 0 1 1
```

Bipartite incidence matrix:

```
  AD AE AF BE BF CE CF
A  1  1  0  0  0  0  0
B  0  0  0  1  1  0  0
C  0  0  0  0  0  1  1
D  1  0  0  0  0  0  0
E  0  1  1  1  1  1  1
F  0  0  1  0  1  0  1
```