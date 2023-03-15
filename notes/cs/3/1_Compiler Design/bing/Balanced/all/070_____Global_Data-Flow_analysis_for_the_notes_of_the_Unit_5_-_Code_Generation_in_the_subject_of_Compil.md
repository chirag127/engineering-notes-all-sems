# Global Data-Flow Analysis

- Global data-flow analysis is a technique to efficiently optimize the code by collecting and distributing information about the program to each block of the flow graph  .
- A flow graph is a representation of the control flow of a program, where each node is a basic block (a sequence of instructions with no jumps or branches) and each edge is a possible transfer of control.
- Data-flow analysis computes analysis facts for each program point, which are facts about variables, expressions, etc. that are relevant for optimization.
- The analysis facts can be either forward or backward, depending on whether they are propagated along the direction of control flow or the opposite direction.
- The analysis facts can also be either may or must, depending on whether they are conservative or precise approximations of the actual facts.
- Some examples of analysis facts are:

  - Reaching definitions: a definition of a variable x is said to reach a program point p if there is a path from the definition to p that does not redefine x. This is a forward may analysis.
  - Available expressions: an expression e is said to be available at a program point p if every path from the entry of the program to p evaluates e and does not modify any of its operands. This is a forward must analysis.
  - Live variables: a variable x is said to be live at a program point p if there is a path from p to the exit of the program that uses x without redefining it. This is a backward may analysis.
  - Very busy expressions: an expression e is said to be very busy at a program point p if every path from p to the exit of the program evaluates e and does not modify any of its operands. This is a backward must analysis.

- The general framework for data-flow analysis consists of the following steps:

  - Define the domain of analysis facts, which is a set of possible facts that can be computed for each program point.
  - Define the transfer function for each basic block, which is a function that maps the analysis facts at the entry (or exit) of the block to the analysis facts at the exit (or entry) of the block.
  - Define the meet operator for each program point, which is a function that combines the analysis facts from different incoming (or outgoing) edges to the program point.
  - Define the initial analysis facts for each program point, which are usually either the empty set or the universal set depending on the type of analysis.
  - Apply an iterative algorithm to compute the analysis facts for each program point until a fixed point is reached, which means that no more changes occur.

- The data-flow analysis can be used to perform various optimizations, such as:

  - Constant propagation: replacing variables with constant values if they are known to be constant at a program point.
  - Common subexpression elimination: eliminating redundant evaluations of the same expression if it is available at a program point.
  - Dead code elimination: removing instructions that have no effect on the program output or the live variables at a program point.
  - Loop invariant code motion: moving instructions that do not depend on the loop iteration outside the loop.