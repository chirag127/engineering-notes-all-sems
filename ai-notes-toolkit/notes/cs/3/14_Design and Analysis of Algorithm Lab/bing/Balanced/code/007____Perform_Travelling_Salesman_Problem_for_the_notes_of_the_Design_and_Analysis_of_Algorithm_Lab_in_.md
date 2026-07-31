# Perform Travelling Salesman Problem for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- The Travelling Salesman Problem (TSP) is a classic optimization problem that asks for the shortest possible route that visits each city exactly once and returns to the origin city.
- The TSP is NP-hard, meaning that there is no known efficient algorithm that can solve it in polynomial time for any arbitrary input.
- The TSP has many applications in real time systems, such as scheduling, routing, logistics, and network design.
- To perform the TSP for the notes of the Design and Analysis of Algorithm Lab, one possible approach is as follows:

  - Represent the notes as nodes in a graph, where the distance between two nodes is the time required to study them.
  - Use a heuristic algorithm, such as nearest neighbor, to find an initial solution that visits all the nodes and returns to the start node.
  - Use a local search algorithm, such as 2-opt, to improve the solution by swapping pairs of edges and checking if the total distance decreases.
  - Repeat the local search until no further improvement is possible or a time limit is reached.
  - Evaluate the quality of the solution by comparing it with the optimal solution (if known) or a lower bound (such as the minimum spanning tree).

- An example of performing the TSP for the notes of the Design and Analysis of Algorithm Lab is shown below:

  - Suppose there are four notes to study: A, B, C, and D, and the time required to study them are as follows:

    | A | B | C | D |
    |---|---|---|---|
    | 0 | 2 | 4 | 6 |
    | 2 | 0 | 3 | 5 |
    | 4 | 3 | 0 | 4 |
    | 6 | 5 | 4 | 0 |

  - Using the nearest neighbor heuristic, we start from note A and choose the closest note to visit next. The initial solution is A-B-C-D-A, with a total time of 2 + 3 + 4 + 6 = 15.
  - Using the 2-opt local search, we swap pairs of edges and check if the total time decreases. For example, we can swap the edges A-B and C-D to get a new solution A-D-C-B-A, with a total time of 6 + 4 + 3 + 2 = 15. This solution is not better than the previous one, so we reject it. We can also swap the edges B-C and D-A to get a new solution A-C-B-D-A, with a total time of 4 + 3 + 5 + 6 = 18. This solution is worse than the previous one, so we reject it as well. We continue to swap edges until no improvement is possible. The final solution is A-B-C-D-A, with a total time of 15.
  - To evaluate the quality of the solution, we can compare it with the optimal solution or a lower bound. The optimal solution for this example is A-B-D-C-A, with a total time of 2 + 5 + 4 + 4 = 15. The lower bound for this example is the minimum spanning tree, which is A-B-C-D, with a total time of 2 + 3 + 4 = 9. The solution we found is optimal, but not guaranteed to be so for every input. The solution we found is also 66.67% longer than the lower bound, which indicates that there is room for improvement.