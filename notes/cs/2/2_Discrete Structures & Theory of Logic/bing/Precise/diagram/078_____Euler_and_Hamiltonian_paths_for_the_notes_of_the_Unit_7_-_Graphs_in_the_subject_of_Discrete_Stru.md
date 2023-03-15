### Unit 7 - Graphs: Euler and Hamiltonian paths

#### Euler paths and circuits
- An Euler path is a path in a graph that visits every edge exactly once.
- An Euler circuit is an Euler path that starts and ends at the same vertex.
- A graph has an Euler circuit if and only if it is connected and every vertex has an even degree.
- A graph has an Euler path if and only if it is connected and has exactly two vertices of odd degree.

#### Hamiltonian paths and cycles
- A Hamiltonian path is a path in a graph that visits every vertex exactly once.
- A Hamiltonian cycle is a Hamiltonian path that starts and ends at the same vertex.
- Unlike Euler paths and circuits, there is no known efficient algorithm for determining whether a graph has a Hamiltonian path or cycle.
- The problem of finding a Hamiltonian cycle is known as the Hamiltonian cycle problem and is NP-complete.

#### Key differences
- Euler paths and circuits involve visiting every edge exactly once, while Hamiltonian paths and cycles involve visiting every vertex exactly once.
- There are efficient algorithms for determining the existence of Euler paths and circuits, while the problem of finding Hamiltonian paths and cycles is NP-complete.