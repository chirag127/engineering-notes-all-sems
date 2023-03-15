### Bipartite Graphs

- A **bipartite graph** is a graph whose vertices can be divided into two disjoint and independent sets, such that every edge connects a vertex in one set to a vertex in the other set.
- The two sets of vertices are usually called the **parts** of the graph. They can be denoted by and .
- A bipartite graph can also be defined as a graph that has no odd cycle, that is, a cycle with an odd number of vertices.
- A bipartite graph is a special case of a **-partite graph** with .
- A bipartite graph is equivalent to a **two-colorable graph**, that is, a graph that can be colored with two colors such that no two adjacent vertices have the same color.
- All **acyclic graphs** (graphs that have no cycles) are bipartite.
- A **cyclic graph** (a graph that has at least one cycle) is bipartite if and only if all the cycles involved are of even length.
- According to **König's line coloring theorem**, all bipartite graphs are **class 1 graphs**, that is, graphs that can be edge-colored with colors, where is the maximum degree of the graph.

#### Examples of Bipartite Graphs

- The following graph is an example of a bipartite graph, with the parts and shown in different colors:

![bipartite graph example](https://www.gatevidyalay.com/wp-content/uploads/2018/07/Bipartite-Graph-Example.png)

- The **complete bipartite graph** is a bipartite graph where every vertex in is adjacent to every vertex in . It is denoted by , where and are the sizes of the parts . For example, the graph is a complete bipartite graph with 3 vertices in each part:

![complete bipartite graph example](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Complete_bipartite_graph_K3_3.svg/1200px-Complete_bipartite_graph_K3_3.svg.png)

- The **Heawood graph** is a bipartite graph with 14 vertices and 21 edges. It is also a **cubic graph** (a graph where every vertex has degree 3) and a **cage graph** (a graph with the smallest possible number of edges for its girth, which is the length of the shortest cycle) . It is shown below:

![Heawood graph example](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Heawood_graph.svg/1200px-Heawood_graph.svg.png)

#### Applications of Bipartite Graphs

- Bipartite graphs can be used to model many real-world situations, such as:
  - **Matching problems**, where one set of vertices represents a set of agents and the other set represents a set of tasks, and the edges represent the possible assignments of agents to tasks .
  - **Network flow problems**, where one set of vertices represents a set of sources and the other set represents a set of sinks, and the edges represent the capacities of the channels between them .
  - **Graph coloring problems**, where one set of vertices represents a set of regions and the other set represents a set of colors, and the edges represent the constraints on the coloring of the regions .
  - **Social network analysis**, where one set of vertices represents a set of users and the other set represents a set of groups, and the edges represent the memberships of users in groups .