### Quadruples and Triples in Compiler Design

- Quadruples and triples are two ways of representing three-address code in compiler design.
- Three-address code is an intermediate representation of source code that uses at most three operands for each instruction.
- Quadruples consist of four fields: op, arg1, arg2, and result. op is the operator, arg1 and arg2 are the operands, and result is the temporary variable that stores the value of the expression.
- Triples consist of three fields: op, arg1, and arg2. op is the operator, and arg1 and arg2 are the operands. The result is stored in the same place as one of the operands, or in a new temporary variable.
- Quadruples and triples are useful for code optimization and code generation in compiler design.
- Quadruples have the advantage of being easy to rearrange for global optimization, but they require more space than triples.
- Triples have the advantage of being more compact than quadruples, but they require more bookkeeping for code movement and register allocation.
- Indirect triples are a variation of triples that use a separate list of pointers to the triple structure. This allows for more flexibility and efficiency in code manipulation.