### Three Address Code

- Three address code (TAC) is a form of intermediate code used by optimizing compilers to aid in the implementation of code-improving transformations.
- Each TAC instruction has at most three operands and is typically a combination of assignment and a binary operator. For example, `t1 := t2 + t3`.
- TAC is easy to generate and can be easily converted to machine code.
- TAC can represent expressions, control flow, function calls and returns, arrays, pointers, and records.
- TAC can be represented in different forms, such as quadruples, triples, indirect triples, and static single assignment form.
- Some common forms of TAC are:

  - Quadruples: A quadruple is a four-tuple that consists of an operator, two operands, and a result. For example, `(+, a, b, t1)` represents `t1 := a + b`.
  - Triples: A triple is a three-tuple that consists of an operator and two operands. The result is implicitly stored in a temporary variable whose index is the same as the triple's index. For example, `(+, a, b)` represents `t1 := a + b` if it is the first triple.
  - Indirect triples: An indirect triple is a one-tuple that consists of an index to a triple. The result is implicitly stored in a temporary variable whose index is the same as the indirect triple's index. For example, `(1)` represents `t1 := a + b` if it is the first indirect triple and `(+, a, b)` is the first triple.
  - Static single assignment form: A static single assignment form (SSA) is a form of TAC where each variable is assigned exactly once. SSA uses a special operator called phi to merge the values of different variables at control flow join points. For example, `x1 := a + b; if c then x2 := x1 + d else x3 := x1 - d; x4 := phi(x2, x3)` represents `x := a + b; if c then x := x + d else x := x - d`.

- TAC can be used to perform various code optimization techniques, such as constant folding, common subexpression elimination, dead code elimination, loop invariant code motion, and register allocation .