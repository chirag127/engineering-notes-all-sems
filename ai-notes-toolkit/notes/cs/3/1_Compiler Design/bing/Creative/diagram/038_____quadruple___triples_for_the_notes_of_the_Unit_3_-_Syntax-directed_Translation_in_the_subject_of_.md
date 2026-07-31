### Quadruples and Triples

- Quadruples and triples are two ways of representing three-address code in compiler design.
- Three-address code is an intermediate representation of a source program that uses at most three operands for each instruction.
- Quadruples and triples are useful for code optimization and code generation.

#### Quadruples

- A quadruple is a structure that consists of four fields: op, arg1, arg2, and result.
- op denotes the operator, arg1 and arg2 denote the two operands, and result is used to store the result of the expression.
- For example, the expression `a = b + c * d` can be represented by the following quadruples:

| op  | arg1 | arg2 | result |
| --- | ---- | ---- | ------ |
| *   | c    | d    | t1     |
| +   | b    | t1   | t2     |
| =   | t2   |      | a      |

- Quadruples have the advantage of being easy to rearrange for code optimization, as each instruction has a unique result field.
- Quadruples have the disadvantage of requiring more space than triples, as each instruction has a separate result field.

#### Triples

- A triple is a structure that consists of three fields: op, arg1, and arg2.
- op denotes the operator, and arg1 and arg2 denote the two operands.
- The result of the expression is stored in the same place as one of the operands, or in a new temporary variable.
- For example, the expression `a = b + c * d` can be represented by the following triples:

| op  | arg1 | arg2 |
| --- | ---- | ---- |
| *   | c    | d    |
| +   | b    | (0)  |
| =   | (1)  | a    |

- The parentheses indicate the position of the triple in the list of triples, starting from zero.
- Triples have the advantage of requiring less space than quadruples, as each instruction does not have a separate result field.
- Triples have the disadvantage of being harder to rearrange for code optimization, as each instruction does not have a unique result field.