Hello, I am Sydney, your AI assistant. I can help you with your study material for the Unit 2 - PROBLEM SOLVING METHODS in the subject of ARTIFICIAL INTELLIGENCE KCS. Here is the content I have generated for you in markdown format:

# Unit 2 - PROBLEM SOLVING METHODS

## Introduction

- Problem solving is the process of finding a solution to a given situation or task that satisfies some criteria or constraints.
- Problem solving methods are systematic and generalizable techniques that can be applied to different types of problems and domains.
- Problem solving methods can be classified into two categories: search-based and logic-based.

## Search-based methods

- Search-based methods are based on exploring a space of possible solutions or states, and finding a path from an initial state to a goal state that satisfies the problem criteria.
- Search-based methods can be further divided into uninformed and informed search methods.

### Uninformed search methods

- Uninformed search methods are also called blind search methods, because they do not use any domain-specific knowledge or heuristic information to guide the search process.
- Uninformed search methods rely only on the problem definition and the operators that can be applied to the states.
- Uninformed search methods include:

  - Breadth-first search (BFS): It expands the shallowest nodes first, and maintains a queue of nodes to be explored. It is complete and optimal, but has high space and time complexity.
  - Depth-first search (DFS): It expands the deepest nodes first, and maintains a stack of nodes to be explored. It is incomplete and suboptimal, but has low space complexity and can be implemented recursively.
  - Uniform-cost search (UCS): It expands the nodes with the lowest path cost first, and maintains a priority queue of nodes to be explored. It is complete and optimal, but has high space and time complexity.
  - Depth-limited search (DLS): It is a variant of DFS that limits the depth of the search to a predefined value. It is incomplete and suboptimal, but has low space complexity and can avoid infinite loops.
  - Iterative deepening search (IDS): It is a combination of BFS and DLS that iteratively increases the depth limit until a solution is found or the search space is exhausted. It is complete and optimal, but has high time complexity.

### Informed search methods

- Informed search methods are also called heuristic search methods, because they use some domain-specific knowledge or heuristic information to guide the search process.
- Informed search methods estimate the cost or quality of a solution or state using a heuristic function, and prefer the nodes with lower or higher heuristic values depending on the problem.
- Informed search methods include:

  - Greedy best-first search (GBFS): It expands the nodes with the lowest heuristic value first, and maintains a priority queue of nodes to be explored. It is incomplete and suboptimal, but has low time complexity and can be fast and efficient.
  - A* search: It expands the nodes with the lowest sum of path cost and heuristic value first, and maintains a priority queue of nodes to be explored. It is complete and optimal, but has high space complexity and can be slow and memory-intensive.
  - Hill-climbing search (HCS): It is a local search method that starts from a random or given state, and moves to a neighboring state with a higher or lower heuristic value depending on the problem. It is incomplete and suboptimal, but has low space and time complexity and can be simple and effective.
  - Simulated annealing (SA): It is a stochastic local search method that starts from a random or given state, and moves to a neighboring state with a higher or lower heuristic value depending on the problem, with a probability that decreases with the temperature parameter. It is incomplete and suboptimal, but has low space and time complexity and can escape local optima and find global optima.

## Logic-based methods

- Logic-based methods are based on using formal logic systems and rules to represent and reason about the problem domain and the solution criteria.
- Logic-based methods can be further divided into propositional logic, predicate logic, and non-classical logic methods.

### Propositional logic

- Propositional logic is a logic system that uses symbols or variables to represent propositions or statements that can be true or false, and logical connectives to form complex expressions or sentences.
- Propositional logic can be used to encode and solve problems such as satisfiability, validity, entailment, and inference.
- Propositional logic methods include:

  - Truth tables: They are tables that list all the possible combinations of truth values for the variables and expressions in a propositional logic formula. They can be used to check the satisf