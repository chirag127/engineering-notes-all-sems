# Intermediate code generation for simple expressions

- Intermediate code is a representation of a program that is between the source code and the target code.
- Intermediate code can be in the form of abstract syntax trees, three-address code, quadruples, triples, or static single assignment form.
- Intermediate code generation is the process of translating the source code into intermediate code.
- Intermediate code generation can be done by using syntax-directed translation, which is a method of attaching semantic actions to the productions of a grammar.
- Syntax-directed translation can be implemented by using either a top-down or a bottom-up parser.
- A simple expression is an expression that consists of operands and operators, such as `a + b * c`.
- To generate intermediate code for a simple expression, the following steps can be followed:

  - Construct a parse tree or an abstract syntax tree for the expression, using the rules of the grammar and the precedence and associativity of the operators.
  - Traverse the parse tree or the abstract syntax tree in postorder, and generate intermediate code for each node.
  - For each node, create a temporary variable to store the result of the computation, and generate a three-address code instruction of the form `t = x op y`, where `t` is the temporary variable, `x` and `y` are the operands, and `op` is the operator.
  - For the leaf nodes, the operands are either constants or identifiers, so the intermediate code is simply `t = x` or `t = y`.
  - For the root node, the intermediate code is the final result of the expression, so it can be assigned to another variable or used in another computation.

- For example, consider the expression `a + b * c`. The parse tree for this expression is:

```
     +
    / \
   a   *
      / \
     b   c
```

- The postorder traversal of this parse tree is: `a b c * +`.
- The intermediate code generated for this expression is:

```
t1 = b * c
t2 = a + t1
```

- The intermediate code can be further optimized by using techniques such as constant folding, algebraic simplification, common subexpression elimination, copy propagation, dead code elimination, etc.