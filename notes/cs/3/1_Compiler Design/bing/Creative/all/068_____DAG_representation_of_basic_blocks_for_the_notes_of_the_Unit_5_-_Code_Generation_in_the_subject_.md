# DAG representation of basic blocks

- A **basic block** is a sequence of statements that has a single entry point and a single exit point.
- A **directed acyclic graph (DAG)** is a graph that has no cycles and has a direction for each edge.
- A **DAG representation of a basic block** is a way of showing the structure and flow of values within a basic block using a DAG.
- The benefits of using a DAG representation of a basic block are:
  - It can help to identify and eliminate common subexpressions, which are expressions that are computed more than once in the same basic block.
  - It can help to perform other optimizations, such as constant folding, copy propagation, dead code elimination, etc.
  - It can help to generate efficient code for the target machine, by minimizing the number of registers and memory accesses needed.
- The steps to construct a DAG representation of a basic block are:
  - Identify the atomic operands (variables or constants) and operators in the basic block.
  - Create a leaf node for each unique operand and label it with the operand name or value.
  - Create an interior node for each operator and label it with the operator symbol.
  - Connect the interior nodes to the leaf nodes or other interior nodes according to the order of evaluation of the expressions.
  - If an interior node has more than one parent, it means that it is a common subexpression.
  - If an interior node has no parent, it means that it is a dead code.
- An example of a DAG representation of a basic block is:

```
a = b + c
d = a - e
b = b + c
f = d + e
```

The DAG representation of this basic block is:

```
    +     -
   / \   / \
  b   c a   e
 / \     \
a   b     +
         / \
        d   e
       / \
      f   d
```

In this DAG, we can see that:

  - The expression `b + c` is a common subexpression, as it is computed twice and has two parents.
  - The expression `a - e` is a dead code, as it is not used in any subsequent statement and has no parent.
  - The expression `d + e` is not a common subexpression, as it is computed only once and has one parent.
  - The expression `a` is a copy of `b + c`, as it is assigned the same value and has the same child.