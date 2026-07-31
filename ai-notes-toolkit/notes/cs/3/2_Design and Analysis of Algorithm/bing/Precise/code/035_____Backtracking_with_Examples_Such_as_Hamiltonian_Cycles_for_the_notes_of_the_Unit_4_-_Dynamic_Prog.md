### Backtracking with Examples Such as Hamiltonian Cycles

Backtracking is an algorithmic technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time (by time, here, is referred to the time elapsed till reaching any level of the search tree).

One of the examples of backtracking is the Hamiltonian Cycle problem. A Hamiltonian cycle is a closed loop on a graph where every node (vertex) is visited exactly once. Using the backtracking method, we can easily find all the Hamiltonian Cycles present in the given graph. The idea is to use the Depth-First Search algorithm to traverse the graph until all the vertices have been visited.

The backtracking approach uses a state-space tree to check if there exists a Hamiltonian cycle in the graph. The solve() method of the Hamiltonian class is the recursive method implementing the backtracking algorithm. As discussed, using DFS we traverse the graph, and every time we find a cycle (i.e., the base condition is satisfied), we output it and deliberately backtrack (i.e., return) to find more such cycles.

The used backtracking algorithm was Vandegriend-Culberson's, which was supposedly the most efficient of all Hamiltonian backtracking algorithms.