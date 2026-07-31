Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of Informed Search for the Unit 2 - PROBLEM SOLVING METHODS in the subject of ARTIFICIAL INTELLIGENCE KCS:

```markdown
# Informed Search

- Informed search is a type of search strategy that uses additional information or heuristics to guide the search process towards the goal state.
- Heuristics are estimates of the cost, distance, or quality of a solution from a given state.
- Informed search algorithms are also called heuristic search algorithms.
- Informed search algorithms can be more efficient and effective than uninformed search algorithms, as they can avoid exploring irrelevant or suboptimal paths.
- Some examples of informed search algorithms are:

  - Greedy best-first search: This algorithm selects the node that is closest to the goal, according to a heuristic function h(n).
  - A* search: This algorithm selects the node that has the lowest sum of the cost so far and the estimated cost to the goal, according to a heuristic function h(n) and a cost function g(n).
  - Hill-climbing search: This algorithm moves to the neighboring node that has the highest value, according to a heuristic function h(n).
  - Simulated annealing: This algorithm moves to a random neighboring node, with a probability that depends on the difference in value and a decreasing temperature parameter.
  - Genetic algorithms: These algorithms use a population of candidate solutions, and apply genetic operators such as selection, crossover, and mutation to generate new solutions.

- Informed search algorithms require a good heuristic function that is:

  - Admissible: It never overestimates the cost to the goal.
  - Consistent: It satisfies the triangle inequality, that is, for any two nodes n and m, h(n) <= h(m) + c(n,m), where c(n,m) is the cost of moving from n to m.
  - Dominant: It dominates another heuristic function, that is, for any node n, h1(n) >= h2(n), where h1 and h2 are two heuristic functions.

- Informed search algorithms have some advantages and disadvantages, such as:

  - Advantages: They can find optimal or near-optimal solutions, they can reduce the search space and the memory requirements, they can exploit domain-specific knowledge.
  - Disadvantages: They can be incomplete or incorrect if the heuristic function is not admissible or consistent, they can be computationally expensive or hard to design, they can be sensitive to the choice of the heuristic function.
```