### Global Data-Flow Analysis

- Global data-flow analysis is a technique to efficiently optimize the code by collecting and distributing information about the program to each block of the flow graph  .
- A flow graph is a representation of the control flow of a program, where each node is a basic block (a sequence of instructions with no jumps or branches) and each edge is a possible transfer of control.
- Data-flow analysis computes analysis facts for each program point, which are facts about variables, expressions, etc. that are relevant for optimization .
- There are three types of data-flow analysis problems: reaching definitions, live variables and available expressions.
  - Reaching definitions: A definition of a variable x is said to reach a point p if there is a path from the definition to p that does not contain any other definition of x. This problem helps to eliminate redundant computations and perform constant propagation.
  - Live variables: A variable x is said to be live at a point p if there is a path from p to a use of x that does not contain any definition of x. This problem helps to perform register allocation and dead code elimination.
  - Available expressions: An expression e is said to be available at a point p if for every path from the entry of the flow graph to p, e is computed and not modified. This problem helps to perform common subexpression elimination.
- Data-flow analysis problems can be solved by using a general framework that consists of four components: a domain, a direction, a transfer function and a meet operator .
  - A domain is a set of analysis facts that are of interest for the problem.
  - A direction is either forward or backward, indicating whether the analysis facts are propagated along or against the control flow.
  - A transfer function is a function that maps the analysis facts at the entry (or exit) of a basic block to the analysis facts at the exit (or entry) of the same block, depending on the direction.
  - A meet operator is a binary operator that combines the analysis facts from different paths at a join point (a node with more than one predecessor or successor).
- Data-flow analysis problems can be classified into two categories: distributive and non-distributive, depending on whether the meet operator distributes over the transfer function or not .
  - Distributive problems can be solved by using an iterative algorithm that computes the analysis facts at each program point by applying the transfer function and the meet operator until a fixed point is reached.
  - Non-distributive problems are harder to solve and may require more sophisticated techniques, such as interval analysis or monotone frameworks.