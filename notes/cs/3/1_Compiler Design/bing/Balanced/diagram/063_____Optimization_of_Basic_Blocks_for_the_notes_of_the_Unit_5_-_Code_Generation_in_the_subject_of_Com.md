### Optimization of Basic Blocks

- Optimization is the process of transforming a program that improves the code by consuming fewer resources and delivering high speed.
- Optimization can be applied to the basic blocks after the intermediate code generation phase of the compiler.
- A basic block is a sequence of consecutive statements in which the flow of control enters at the beginning and leaves at the end without halt or possibility of branching.
- There are two types of basic block optimizations:
  - Structure preserving transformations: These are the transformations that do not change the structure of the basic block, but only replace some expressions with equivalent ones. For example, constant folding, constant propagation, strength reduction, etc.
  - Algebraic transformations: These are the transformations that change the structure of the basic block by eliminating some expressions or statements that are redundant or unnecessary. For example, common subexpression elimination, dead code elimination, copy propagation, etc.
- To apply an optimization technique to a basic block, a directed acyclic graph (DAG) can be used as a representation of the three-address code that is generated as the result of an intermediate code generation.
- A DAG is a data structure that consists of nodes and edges, where each node represents an operation or a variable, and each edge represents a dependency or a flow of data.
- A DAG facilitates the transformation of basic blocks by identifying the common subexpressions, eliminating the redundant computations, and minimizing the number of temporary variables.
- The following diagram shows an example of a basic block and its corresponding DAG:

![Basic block and DAG](https://media.geeksforgeeks.org/wp-content/uploads/20210621144934/basic-block-and-dag.png)

- The following table summarizes some of the common optimization techniques and their effects on the basic block and the DAG   :

| Optimization technique | Effect on basic block | Effect on DAG |
| ---------------------- | --------------------- | ------------- |
| Constant folding | Replaces a constant expression with its value. For example, x = 2 + 3 becomes x = 5. | Reduces the number of nodes and edges. |
| Constant propagation | Replaces a variable that has a constant value with that value. For example, if x = 5, then y = x + 1 becomes y = 5 + 1. | Reduces the number of nodes and edges. |
| Strength reduction | Replaces a complex or expensive operation with a simpler or cheaper one. For example, x = y * 2 becomes x = y + y. | Changes the type of nodes and edges. |
| Common subexpression elimination | Eliminates the repeated computation of the same expression. For example, x = a + b and y = a + b become x = a + b and y = x. | Merges the nodes and edges that represent the same expression. |
| Dead code elimination | Eliminates the statements that have no effect on the output of the program. For example, x = y + z is dead code if x is never used. | Removes the nodes and edges that are not reachable from the output nodes. |
| Copy propagation | Replaces a variable that has the same value as another variable with that variable. For example, if x = y, then z = x + 1 becomes z = y + 1. | Merges the nodes and edges that represent the same variable. |