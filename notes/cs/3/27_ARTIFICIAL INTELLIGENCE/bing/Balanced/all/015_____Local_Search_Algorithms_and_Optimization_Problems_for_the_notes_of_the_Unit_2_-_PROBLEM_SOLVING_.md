# Local Search Algorithms and Optimization Problems

- Local search algorithms are algorithms that help in solving optimization problems, where the goal is to find a solution that maximizes or minimizes a criterion among a number of candidate solutions.
- Optimization problems are problems that involve finding the best possible solution from a set of feasible solutions, subject to some constraints.
- Local search algorithms work by starting from an initial solution and iteratively improving it by making small changes, until a local optimum is reached.
- A local optimum is a solution that is better than all its neighboring solutions, but not necessarily the best solution in the entire search space.
- The search space is the set of all possible solutions to a given problem.
- Local search algorithms are widely used for very large and complex problems, where finding the global optimum is too computationally expensive or impossible.
- Local search algorithms can return good but not optimal solutions, and are usually very fast, but can get stuck in local optima.
- Some examples of optimization problems that can be solved by local search algorithms are traveling salesman problem, n-queens problem, scheduling problem, etc.

## Types of Local Search Algorithms

- There are many types of local search algorithms, each with different strategies for exploring the search space and escaping local optima.
- Some of the commonly used local search algorithms are:

  - Hill climbing: This algorithm starts from a random solution and repeatedly moves to the best neighboring solution, until no improvement is possible. It is simple and fast, but can easily get stuck in local optima.
  - Simulated annealing: This algorithm is inspired by the physical process of annealing, where a metal is heated and then slowly cooled to reach a low-energy state. It starts from a random solution and probabilistically decides whether to move to a neighboring solution or not, based on a temperature parameter that decreases over time. It can escape local optima by accepting worse solutions at high temperatures, but can converge to a global optimum as the temperature approaches zero.
  - Genetic algorithms: This algorithm is inspired by the biological process of evolution, where a population of individuals undergoes selection, crossover, and mutation to produce offspring. It starts from a population of random solutions and repeatedly applies these genetic operators to generate new solutions, until a termination criterion is met. It can explore a large and diverse search space, but can also suffer from premature convergence or loss of diversity.

## References

: https://www.section.io/engineering-education/understanding-search-algorithms-in-ai/
: https://www.surfactants.net/local-search-algorithms-in-artificial-intelligence/
: https://www.ics.uci.edu/~rickl/courses/cs-171/cs171-lecture-slides/2020_SS1_CS171/chap_4_Local_Search.pdf
: https://en.wikipedia.org/wiki/Local_search_(optimization)
: https://cs50.harvard.edu/ai/2020/notes/3/