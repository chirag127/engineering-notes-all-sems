 Here are the notes for the topic -

Backtracking, Branch and Bound with Examples Such as Travelling Salesman Problem

### Backtracking
- Backtracking is a general algorithmic technique that considers all possible candidates for a solution and abandons each partial candidate ("backtracks") as soon as it is clear that it cannot lead to a valid full solution.
- It is often used for finding all (or some) solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a partial candidate as soon as it determines that the candidate cannot possibly lead to a valid solution.

### Branch and Bound
- Branch and bound is a general algorithmic method for discrete and combinatorial optimization. It consists of an organized search of a solution space by means of dividing it into smaller subspaces and performing bounds computation to remove subspaces that provably do not contain an optimal solution. 
- The two main components of the branch and bound method are:
1. Branching: Dividing the problem into smaller subproblems.
2. Bounding: Computing upper and lower bounds on the optimal solution value.

### Travelling Salesman Problem (TSP)
- The travelling salesman problem (TSP) asks the following question: "Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?".
- It is a classic NP-hard problem in combinatorial optimization. The goal is to find the shortest tour through a given list of cities. The TSP has important applications in logistics and transportation.
- Backtracking and Branch and Bound algorithms can be used to solve the TSP.

[Further details and examples on the topics]