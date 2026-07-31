### Global Data-Flow Analysis

- Global data-flow analysis is a technique to optimize the code by collecting and distributing information about the program to each block of the control flow graph  .
- The information can be about the definition and use of data, such as variables, expressions, constants, etc.
- The analysis can help to perform optimizations such as constant propagation, dead code elimination, common subexpression elimination, etc.
- The analysis is based on the following concepts :
  - Data-flow values: the facts that are of interest for the analysis, such as the set of variables that are defined or used at a program point.
  - Data-flow equations: the relations that define how the data-flow values are computed for each block and each program point, based on the control flow graph and the transfer functions of the instructions.
  - Data-flow frameworks: the formalization of the data-flow analysis problem, including the data-flow values, the data-flow equations, the direction of the analysis (forward or backward), and the meet operator that combines the data-flow values from different paths.
  - Data-flow algorithms: the methods to solve the data-flow equations and compute the data-flow values for each program point, such as the iterative algorithm, the worklist algorithm, etc.
- The analysis can be classified into different types based on the following criteria :
  - The scope of the analysis: local analysis is performed within a single block, while global analysis is performed across the whole program or a procedure.
  - The direction of the analysis: forward analysis propagates the data-flow values from the entry to the exit of the program or a block, while backward analysis propagates the data-flow values from the exit to the entry of the program or a block.
  - The nature of the data-flow values: may analysis computes the data-flow values that may hold at a program point, while must analysis computes the data-flow values that must hold at a program point.
  - The confluence of the data-flow values: distributive analysis uses a meet operator that is distributive over the transfer functions, while non-distributive analysis uses a meet operator that is not distributive over the transfer functions.