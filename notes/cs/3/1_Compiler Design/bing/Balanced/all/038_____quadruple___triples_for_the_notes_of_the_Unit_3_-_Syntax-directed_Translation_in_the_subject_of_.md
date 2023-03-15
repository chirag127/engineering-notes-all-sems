# Quadruples and Triples

- Quadruples and triples are intermediate representations of source code that are used in syntax-directed translation.
- Quadruples and triples are linearized forms of syntax trees that capture the structure and semantics of the source code.
- Quadruples and triples are useful for code optimization and code generation.

## Quadruples

- A quadruple is a record of four fields: (op, arg1, arg2, result), where op is the operator, arg1 and arg2 are the operands, and result is the place to store the value of the operation.
- A quadruple can represent an assignment, an arithmetic operation, a logical operation, a relational operation, a conditional jump, an unconditional jump, a procedure call, a parameter passing, or a return statement.
- A quadruple can be stored in a table, where each row corresponds to a quadruple, and each column corresponds to a field.
- A quadruple can be generated from a syntax tree by traversing the tree in postorder and generating a quadruple for each node.
- A quadruple can be converted back to a syntax tree by using a stack to store the result fields of the quadruples, and popping two operands and pushing a new node for each operator.

## Triples

- A triple is a record of three fields: (op, arg1, arg2), where op is the operator, and arg1 and arg2 are the operands.
- A triple can represent the same operations as a quadruple, except that the result field is omitted.
- A triple can be stored in a table, where each row corresponds to a triple, and each column corresponds to a field.
- A triple can be generated from a syntax tree by traversing the tree in postorder and generating a triple for each node.
- A triple can be converted back to a syntax tree by using a stack to store the row numbers of the triples, and popping two operands and pushing a new node for each operator.

## Comparison

- Quadruples and triples have the same expressive power, but quadruples are more compact and efficient, while triples are more flexible and modular.
- Quadruples require less memory and fewer table entries than triples, but quadruples may introduce unnecessary temporary variables and assignments.
- Triples avoid temporary variables and assignments, but triples may require more table lookups and indirections than quadruples.