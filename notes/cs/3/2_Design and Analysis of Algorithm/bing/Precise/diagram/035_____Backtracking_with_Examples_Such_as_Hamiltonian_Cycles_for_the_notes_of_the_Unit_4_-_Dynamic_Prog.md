### Backtracking with Examples Such as Hamiltonian Cycles

Backtracking is a general algorithmic technique that involves exploring all possible solutions to a problem incrementally and backing up when a partial solution is found to be unworkable. It is often used to solve problems in which the solution is a sequence of choices, such as the Hamiltonian cycle problem.

A Hamiltonian cycle is a cycle in a graph that visits every vertex exactly once. The problem of finding a Hamiltonian cycle in a graph is NP-complete, meaning that there is no known polynomial-time algorithm for solving it. However, backtracking can be used to find Hamiltonian cycles in small graphs.

The backtracking algorithm for finding a Hamiltonian cycle in a graph involves the following steps:

1. Choose a starting vertex and add it to the cycle.
2. For each unvisited vertex adjacent to the current vertex, add it to the cycle and recursively search for a Hamiltonian cycle from the new vertex.
3. If a Hamiltonian cycle is found, return it.
4. If no Hamiltonian cycle is found, remove the last vertex from the cycle and backtrack to the previous vertex.

This algorithm can be implemented using depth-first search and can be used to find all Hamiltonian cycles in a graph. However, it has an exponential time complexity and is not practical for large graphs.

Backtracking can also be used to solve other problems, such as the traveling salesman problem, graph coloring, the n-queen problem, and the sum of subsets problem. In each of these problems, the solution is a sequence of choices, and backtracking can be used to explore all possible solutions incrementally. However, the time complexity of backtracking algorithms is generally exponential, and they are not practical for large problems.