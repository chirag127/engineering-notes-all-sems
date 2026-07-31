### DAG representation of basic blocks

- A **directed acyclic graph (DAG)** is a graph that has no cycles and has a direction for each edge.
- A **basic block** is a sequence of statements that has a single entry point and a single exit point.
- A DAG can be used to represent the structure and the flow of values of a basic block in a compiler.
- A DAG can also be used to apply optimization techniques to a basic block, such as eliminating common subexpressions, dead code, and redundant calculations.
- To construct a DAG for a basic block, the following steps are followed:
  - The leaves of the DAG are labeled by unique identifiers, which can be variable names or constants.
  - The interior nodes of the DAG are labeled by operators, such as arithmetic, logical, or assignment operators.
  - The edges of the DAG represent the operands of the operators.
  - The order of evaluation of the nodes is determined by the topological sorting of the DAG, which is a linear ordering of the nodes such that for every edge from node u to node v, u comes before v in the ordering.
  - If a node has multiple parents, it means that it is a common subexpression, and it can be computed only once and reused later.
  - If a node has no parents, it means that it is a dead code, and it can be removed from the DAG.
- For example, consider the following basic block:

```c
a = b + c;
d = a - e;
f = b + c;
g = f - e;
```

- The DAG representation of this basic block is:

```
    -     -
   / \   / \
  +   e +   e
 / \   / \
b   c a   f
```

- In this DAG, we can see that:
  - The node labeled by + has two parents, which means that b + c is a common subexpression, and it can be computed only once and stored in a temporary variable, say t1.
  - The node labeled by a has no parents, which means that a = b + c is a dead code, and it can be removed from the DAG.
  - The node labeled by f has no parents, which means that f = b + c is a dead code, and it can be removed from the DAG.
  - The optimized basic block after applying the DAG representation is:

```c
t1 = b + c;
d = t1 - e;
g = t1 - e;
```