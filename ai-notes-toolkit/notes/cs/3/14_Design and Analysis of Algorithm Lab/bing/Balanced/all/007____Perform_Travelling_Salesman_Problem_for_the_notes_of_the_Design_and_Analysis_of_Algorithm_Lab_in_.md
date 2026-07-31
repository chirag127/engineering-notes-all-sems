# Perform Travelling Salesman Problem for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- The Travelling Salesman Problem (TSP) is a classic optimization problem that asks for the shortest possible route that visits each city exactly once and returns to the starting point.
- The TSP is an NP-hard problem, meaning that there is no known efficient algorithm that can solve it in polynomial time for any number of cities.
- The TSP has many applications in real time systems, such as scheduling, routing, logistics, and planning.
- The TSP can be formulated as a graph problem, where the cities are the vertices and the distances between them are the edge weights.
- The TSP can be solved using various methods, such as brute force, dynamic programming, branch and bound, heuristic algorithms, and metaheuristic algorithms.
- Brute force is the simplest method that tries all possible permutations of the cities and chooses the one with the minimum total distance. It has a time complexity of O(n!), where n is the number of cities.
- Dynamic programming is a method that uses a table to store and reuse the optimal solutions of subproblems. It has a time complexity of O(n^2 * 2^n), where n is the number of cities.
- Branch and bound is a method that uses a tree to explore the search space and prune the branches that cannot lead to a better solution. It has a time complexity of O(n!), but it can be much faster in practice depending on the quality of the bounding function.
- Heuristic algorithms are methods that use some rules or intuition to find a good solution, but not necessarily the optimal one. They have a lower time complexity than the exact methods, but they have no guarantee of optimality or quality. Some examples of heuristic algorithms are nearest neighbor, greedy, and 2-opt.
- Metaheuristic algorithms are methods that use some general strategies to explore the search space and escape from local optima. They have a lower time complexity than the exact methods, but they have no guarantee of optimality or quality. Some examples of metaheuristic algorithms are simulated annealing, genetic algorithm, and ant colony optimization.