### DAG representation of basic blocks

- A **directed acyclic graph (DAG)** is a graph that has no cycles and has a direction for each edge.
- A **basic block** is a sequence of statements that has a single entry point and a single exit point, and no jumps or branches within it.
- A **DAG representation of a basic block** is a way of showing the structure and flow of values within a basic block, and also a way of applying optimization techniques to it.
- A DAG representation of a basic block has the following properties:
  - The **nodes** of the DAG are labeled by operators, variables, or constants.
  - The **leaves** of the DAG are labeled by unique identifiers, which can be variable names or constants.
  - The **interior nodes** of the DAG are labeled by operators, such as arithmetic, logical, or relational operators.
  - The **edges** of the DAG represent the operands of the operators, and point from the source operand to the destination operator.
  - A node can have **multiple parents**, which means that it is a **common subexpression** that is used by more than one operator.
  - A node can have **multiple children**, which means that it is a **value** that is used by more than one operator.
  - A node can have **no children**, which means that it is a **dead code** that is not used by any operator.
- A DAG representation of a basic block can be used for the following purposes:
  - To **visualize** the structure and flow of values within a basic block, and to identify the dependencies and redundancies among the statements.
  - To **optimize** the basic block by applying techniques such as **common subexpression elimination**, **copy propagation**, **constant folding**, **dead code elimination**, and **code motion**.
  - To **generate** efficient code for the basic block by using a **bottom-up** traversal of the DAG, and by selecting appropriate registers or memory locations for the nodes.
- An example of a DAG representation of a basic block is shown below:

```text
t1 = a + b
t2 = c + d
t3 = t1 * t2
t4 = a + b
t5 = t4 * t2
t6 = t3 + t5
```

![DAG representation of a basic block](https://i.imgur.com/2Q0wZ7l.png)

- In this example, the DAG has the following features:
  - The nodes are labeled by operators (+, *) or identifiers (a, b, c, d, t1, t2, t3, t4, t5, t6).
  - The leaves are labeled by unique identifiers (a, b, c, d).
  - The interior nodes are labeled by operators (+, *).
  - The edges represent the operands of the operators, and point from the source operand to the destination operator.
  - The node labeled by t1 has two parents, which means that it is a common subexpression that is used by both t3 and t4.
  - The node labeled by t4 has no children, which means that it is a dead code that is not used by any operator.
  - The node labeled by t6 has no parents, which means that it is the final result of the basic block.