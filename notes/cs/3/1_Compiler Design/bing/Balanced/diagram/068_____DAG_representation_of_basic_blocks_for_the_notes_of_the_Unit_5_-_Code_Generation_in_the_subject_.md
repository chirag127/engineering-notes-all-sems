### DAG representation of basic blocks

- A **basic block** is a sequence of consecutive statements in which the flow of control enters at the beginning and leaves at the end without halt or possibility of branching.
- A **directed acyclic graph (DAG)** is a graph that has no cycles and has a direction for each edge.
- A **DAG representation of a basic block** is a way of showing the structure and flow of values within the block, as well as identifying common subexpressions and redundant computations  .
- To construct a DAG for a basic block, the following steps are followed:
  - The leaves of the DAG are labeled by unique identifiers, which can be variable names or constants.
  - The interior nodes of the DAG are labeled by operators, such as arithmetic, logical, or relational operators.
  - For each statement in the basic block, starting from the first one, do the following:
    - If the statement is an assignment of the form x = y op z, where op is an operator and y and z are operands, then find or create nodes for y and z, and create a new node for op with y and z as its children. Then, if x is already a leaf node, replace its label with the node for op. Otherwise, create a new leaf node for x and label it with the node for op.
    - If the statement is an assignment of the form x = y, where y is an operand, then find or create a node for y, and label it with y. Then, if x is already a leaf node, replace its label with the node for y. Otherwise, create a new leaf node for x and label it with the node for y.
    - If the statement is not an assignment, then create a new node for the statement and label it with the statement. Then, find or create nodes for the operands of the statement, and make them the children of the statement node.
  - The root of the DAG is the node for the last statement in the basic block.
- A DAG representation of a basic block has the following advantages  :
  - It eliminates the need for temporary variables, as the nodes can be directly used for code generation.
  - It reveals the common subexpressions in the basic block, as they are represented by nodes with multiple parents.
  - It allows for local optimizations, such as constant folding, algebraic simplification, copy propagation, and dead code elimination, by modifying or removing nodes and edges in the DAG.
- A DAG representation of a basic block has the following limitations :
  - It does not preserve the order of evaluation of the expressions, which may affect the side effects and the accuracy of the results.
  - It does not handle control flow statements, such as branches and loops, which require additional information and analysis.
  - It may not be unique, as different orderings of the statements or different choices of the nodes may result in different DAGs for the same basic block.

- An example of a DAG representation of a basic block is shown below:

```
Basic block:
t1 = a + b
t2 = a - b
t3 = t1 * t2
t4 = a * b
t5 = t3 + t4
x = t5

DAG representation:

    x
    |
    +
   / \
  *   *
 / \ / \
a  - a  b
   / \
  a   b
```