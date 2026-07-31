# Bipartite Graphs

- A **bipartite graph** is a graph whose vertices can be divided into two disjoint and independent sets, such that every edge connects a vertex in one set to a vertex in the other set .
- The two sets of vertices are usually called the **parts** of the graph. They can be denoted by and  .
- A bipartite graph can be represented by a **bipartition** , which is a pair of sets such that and  .
- A bipartite graph can also be characterized by the absence of **odd cycles** (cycles with an odd number of vertices) in the graph  .
- A bipartite graph is **two-colorable**, meaning that the vertices can be colored with two colors such that no two adjacent vertices have the same color .
- All **acyclic graphs** (graphs with no cycles) are bipartite .
- A **cyclic graph** (a graph with at least one cycle) is bipartite if and only if all the cycles in the graph have **even length** .
- A bipartite graph is a special case of a **-partite graph** with .
- According to **König's line coloring theorem**, all bipartite graphs are **class 1 graphs**, meaning that the minimum number of colors needed to color the edges of the graph is equal to the maximum degree of the graph .

## Examples of Bipartite Graphs

- The following graph is an example of a bipartite graph with parts and :

![bipartite graph example](https://www.gatevidyalay.com/wp-content/uploads/2018/08/Bipartite-Graph-Example.png)

- The following graph is an example of a bipartite graph with parts and , and a bipartition :

![bipartite graph example 2](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Complete_bipartite_graph_K3_3.svg/1200px-Complete_bipartite_graph_K3_3.svg.png)

- The following graph is an example of a bipartite graph with parts and , and a bipartition :

![bipartite graph example 3](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Heawood_graph.svg/1200px-Heawood_graph.svg.png)

- The following graph is an example of a non-bipartite graph, because it contains an odd cycle of length 3:

![non-bipartite graph example](https://www.gatevidyalay.com/wp-content/uploads/2018/08/Non-Bipartite-Graph-Example.png)