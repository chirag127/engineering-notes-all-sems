# Intermediate Code Generation

Intermediate code generation is a phase in the compiler design that produces an intermediate representation of the source program. The intermediate code is independent of the source language and the target machine, and it can be easily translated into the machine code. The intermediate code can also be used for code optimization and analysis.

The following are some of the advantages of intermediate code generation :

- It simplifies the design of the compiler by separating the analysis and synthesis phases.
- It eliminates the need of a new full compiler for every unique machine by keeping the analysis portion same for all the compilers. The second part of compiler, synthesis, is changed according to the target machine.
- It allows the compiler to perform machine-independent optimizations on the intermediate code, which can improve the quality and efficiency of the generated code.
- It facilitates the portability of the compiler to different machines and platforms, as only the back-end of the compiler needs to be modified for each target machine.

The following are some of the commonly used intermediate code representations:

- Postfix Notation: Also known as reverse Polish notation or suffix notation. The ordinary (infix) way of writing the sum of a and b is with an operator in between, as in a + b. In postfix notation, the operator follows the operands, as in a b +. Postfix notation eliminates the need for parentheses and precedence rules, and it can be easily evaluated using a stack.
- Prefix Notation: Also known as Polish notation or prefix notation. The operator precedes the operands, as in + a b. Prefix notation also eliminates the need for parentheses and precedence rules, and it can be easily evaluated using a stack.
- Three-Address Code: A form of intermediate code that consists of a sequence of instructions, each of which has at most three operands. An operand can be a constant, a variable, a temporary variable, or a label. A label is used to mark the target of a jump instruction. Three-address code can be represented in various ways, such as quadruples, triples, or indirect triples.
- Syntax Trees: A graphical representation of the syntactic structure of the source program. The nodes of the tree are labeled by the grammar symbols, and the leaves are labeled by the tokens. Syntax trees can be used to generate intermediate code by traversing the tree in a suitable order and generating code for each node.
- Directed Acyclic Graphs (DAGs): A simplified version of syntax trees that eliminates the common subexpressions. A DAG has a unique node for each operand and operator, and the edges represent the operands of the operators. DAGs can be used to generate intermediate code by traversing the graph in a suitable order and generating code for each node.

The following is an example of intermediate code generation for the expression a = b * - c + b * - c using three different representations :

- Postfix Notation: b c - * b c - * + a =
- Prefix Notation: = a + * b - c * b - c
- Three-Address Code:

```
t1 = - c
t2 = b * t1
t3 = b * t1
t4 = t2 + t3
a = t4
```

- Syntax Tree:

![Syntax Tree](https://www.geeksforgeeks.org/wp-content/uploads/Intermediate-Code-Generation-1.png)

- DAG:

![DAG](https://www.geeksforgeeks.org/wp-content/uploads/Intermediate-Code-Generation-2.png)