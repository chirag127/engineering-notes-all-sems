 Here is the content in Markdown format:

### Problem solving Methods for the notes of the Unit 2 - PROBLEM SOLVING METHODS in the subject of ARTIFICIAL INTELLIGENCE KCS

1. Brute-force search: This is an exhaustive method that systematically checks every possibility and guarantees to find the optimal solution. However, this is not practical for problems with a large number of possibilities.
2. Hill-climbing: This starts with an arbitrary solution and then repeatedly moves to the neighbor solution that maximizes the objective function. It stops when no neighbor is better. While simple, this can get stuck in local optima.
3. Beam search: This extends hill-climbing to keep track of multiple candidates, thereby trading off breadth for depth. A beam widens or narrows down promising candidates.
4. Simulated annealing: This is a randomized search technique inspired by the metallurgical process of annealing. It allows for the acceptance of worse solutions occasionally, enabling the method to escape local optima. The acceptance probability depends on a parameter called temperature which is gradually decreased.
5. Genetic algorithms: These are biologically-inspired methods that mimic evolution. A population of candidate solutions undergoes selection, crossover, and mutation repeatedly to obtain improved solutions. Crossover combines parts of multiple solutions to generate new ones. Mutation induces random changes to maintain diversity.

The above methods can be applied to various problems including optimization, planning, and machine learning. They have their own pros and cons in terms of computation time, scalability, and solution quality. The choice of a method depends on the nature of the problem and available resources. Detailed examples and pseudocodes can be included for further clarification.