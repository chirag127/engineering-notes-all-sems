 Here are the notes on NP-Completeness and Approximation Algorithms with Examples Such as Sum of Subsets:

### NP-Completeness

- A decision problem is in NP if a 'Yes' answer can be verified in polynomial time.
- A problem is NP-hard if every problem in NP can be reduced to it in polynomial time.
- A problem is NP-complete if it is both NP and NP-hard.
- Examples: SAT, Hamiltonian cycle, clique problem, subset sum problem, graph coloring, TSP, etc.

### Approximation Algorithms

- For NP-hard problems, we cannot hope to find efficient exact solutions.
- We look for efficient algorithms that find approximate solutions - i.e., solutions that are 'close' to optimal.
- Measured using approximation ratio (ratio of approximate solution value to optimal value).
- Examples:
-- For set cover, greedy algorithm achieves approximation ratio of log n.
-- For vertex cover, greedy algorithm achieves approximation ratio of 2.
-- For TSP, nearest neighbor heuristic achieves approximation ratio of n (very poor).
-- For clique problem, greedy coloring achieves approximation ratio of Delta + 1 where Delta is maximum degree in graph.

### Sum of Subsets problem

- Given a set of integers, find a non-empty subset whose sum is zero.
- This is NP-complete.
- A greedy approach may not work - counter-example: {-1, 1, 5, 6}.
- An approximation approach is to find a subset that minimizes the sum (makes it closest to zero). This can be done in polynomial time but no constant approximation ratio can be achieved unless P = NP.