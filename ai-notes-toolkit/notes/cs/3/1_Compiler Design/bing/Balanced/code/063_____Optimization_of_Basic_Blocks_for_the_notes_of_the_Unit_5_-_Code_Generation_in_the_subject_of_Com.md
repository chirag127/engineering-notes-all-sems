### Optimization of Basic Blocks

- Optimization is the process of transforming a program that improves the code by consuming fewer resources and delivering high speed.
- Optimization can be applied to the basic blocks after the intermediate code generation phase of the compiler.
- A basic block is a sequence of consecutive statements in which the flow of control enters at the beginning and leaves at the end without halt or possibility of branching.
- There are two types of basic block optimizations:
  - Structure preserving transformations: These are the transformations that do not change the structure of the basic block, but only replace some expressions or statements by equivalent ones that are more efficient. For example, constant folding, constant propagation, copy propagation, dead code elimination, etc.
  - Algebraic transformations: These are the transformations that use algebraic identities or rules to simplify or eliminate expressions or statements. For example, strength reduction, common subexpression elimination, induction variable elimination, etc.
- To apply an optimization technique to a basic block, a directed acyclic graph (DAG) can be used as a representation of the three-address code that is generated as the result of an intermediate code generation.
- A DAG is a data structure that consists of nodes and edges, where each node represents an operation or a variable, and each edge represents a dependency or a flow of data.
- A DAG facilitates the transformation of basic blocks by eliminating redundant computations, detecting common subexpressions, and exposing more opportunities for optimization.
- The steps to construct a DAG for a basic block are:
  - Create a node for each statement in the basic block.
  - For each node, check if there is an existing node with the same operation and operands. If yes, then merge the nodes and update the labels. If no, then create a new node and add the edges from the operands to the node.
  - For each node, check if there is an existing node with the same label. If yes, then delete the node and redirect the edges to the existing node. If no, then keep the node and label it with the statement.
  - The root nodes of the DAG are the statements that have no successors in the basic block.
- The steps to generate optimized code from a DAG are:
  - Traverse the DAG in postorder (visit the children before the parent) and assign a temporary name to each node that has no label.
  - For each node, generate a three-address code statement of the form `label = op child1 child2`, where label is the node's label or temporary name, op is the node's operation, and child1 and child2 are the node's children or operands.
  - The optimized code is the sequence of statements generated for the root nodes of the DAG.