# Bipartite Graphs

- A **bipartite graph** is a graph whose vertices can be divided into two disjoint and independent sets, such that every edge connects a vertex in one set to a vertex in the other set .
- The two sets are usually called the **parts** of the graph, and are denoted by and .
- A bipartite graph can also be defined as a graph that is **two-colorable**, meaning that the vertices can be colored with two colors such that no two adjacent vertices have the same color .
- A bipartite graph is a special case of a **k-partite graph** with .
- A **complete bipartite graph** is a bipartite graph where every vertex in one part is adjacent to every vertex in the other part. It is denoted by , where and are the sizes of the two parts.
- A **bipartite matching** is a set of edges in a bipartite graph such that no two edges share a common vertex. A **maximum bipartite matching** is a bipartite matching with the largest possible number of edges.
- A **perfect matching** is a bipartite matching that covers all the vertices of the graph. A bipartite graph has a perfect matching if and only if it satisfies the **Hall's condition**, which states that for every subset of vertices in one part, the number of neighbors in the other part is at least as large as the size of the subset.
- Bipartite graphs are mostly used in modeling relationships, especially between two entire separate classes of object. For example, a bipartite graph can represent the preferences of students and schools in a college admission problem, or the assignments of workers and tasks in a scheduling problem.