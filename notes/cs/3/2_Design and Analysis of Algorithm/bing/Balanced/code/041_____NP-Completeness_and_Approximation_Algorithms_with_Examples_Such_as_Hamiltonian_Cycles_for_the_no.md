# NP-Completeness and Approximation Algorithms

- NP-Completeness is a concept that deals with the complexity of decision problems, i.e., problems that have a yes or no answer.
- A problem is NP if it can be verified in polynomial time, i.e., given a solution, we can check if it is correct in polynomial time.
- A problem is NP-Complete if it is NP and every other NP problem can be reduced to it in polynomial time, i.e., it is the hardest problem in NP.
- Examples of NP-Complete problems are: Hamiltonian Cycle, Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Sum of Subsets, etc.
- If there is a polynomial time algorithm for any NP-Complete problem, then there is a polynomial time algorithm for all NP problems, which implies P = NP. However, this is widely believed to be false.
- Approximation Algorithms are a way of dealing with NP-Completeness for optimization problems, i.e., problems that have a numerical objective function to minimize or maximize.
- An Approximation Algorithm does not guarantee the optimal solution, but it guarantees a solution that is close to the optimal within a certain factor or bound, called the approximation ratio.
- The approximation ratio is the ratio of the cost of the solution obtained by the algorithm to the cost of the optimal solution, for minimization problems, or the inverse for maximization problems.
- The goal of an Approximation Algorithm is to achieve the best possible approximation ratio in polynomial time, for a given optimization problem.
- Examples of Approximation Algorithms are: 2-Approximation for Vertex Cover, 7/8-Approximation for Max 3-SAT, 2-Approximation for Travelling Salesman Problem with triangle inequality, etc.