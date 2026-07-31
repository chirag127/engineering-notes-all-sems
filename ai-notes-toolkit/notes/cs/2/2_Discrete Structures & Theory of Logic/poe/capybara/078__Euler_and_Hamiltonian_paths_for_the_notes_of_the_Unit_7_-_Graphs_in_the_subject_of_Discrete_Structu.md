### Euler and Hamiltonian paths for the notes of the Unit 7 - Graphs in the subject of Discrete Structures & Theory of Logic

Graph theory is an important branch of mathematics that deals with the study of graphs, which are mathematical structures that represent a set of objects and the connections between them. In this unit, we will focus on two important concepts in graph theory: Euler and Hamiltonian paths.

#### Euler Paths

An Euler path is a path in a graph that visits each edge exactly once. More formally, an Euler path is a path that starts at one vertex, visits each vertex exactly once, and ends at another vertex. A graph that contains an Euler path is called an Eulerian graph.

To determine if a graph is Eulerian, we can use the following theorem:

A connected graph is Eulerian if and only if every vertex has an even degree.

In other words, if every vertex in the graph has an even number of edges connected to it, then the graph is Eulerian and contains an Euler path. If there is exactly one vertex with an odd degree, then the graph is semi-Eulerian and contains an Euler path that starts and ends at the vertex with an odd degree.

#### Hamiltonian Paths

A Hamiltonian path is a path in a graph that visits each vertex exactly once. More formally, a Hamiltonian path is a path that starts at one vertex, visits each vertex exactly once, and ends at another vertex. A graph that contains a Hamiltonian path is called a Hamiltonian graph.

Determining if a graph is Hamiltonian is generally more difficult than determining if it is Eulerian. There is no simple theorem or algorithm that can be used to determine if a graph is Hamiltonian. However, there are some necessary conditions that can be used to rule out the possibility of a Hamiltonian path:

- If a graph has a vertex of degree 1, then it cannot be Hamiltonian.
- If a graph has two non-adjacent vertices with a total degree of less than the number of vertices, then it cannot be Hamiltonian.

In general, determining if a graph is Hamiltonian requires a case-by-case analysis of the graph.

#### Conclusion

Euler and Hamiltonian paths are important concepts in graph theory that have many practical applications. In this unit, we have learned how to determine if a graph is Eulerian or Hamiltonian, and some necessary conditions that must be met for a graph to be Hamiltonian. By understanding these concepts, we can better analyze and understand the behavior of complex systems that can be modeled as graphs.