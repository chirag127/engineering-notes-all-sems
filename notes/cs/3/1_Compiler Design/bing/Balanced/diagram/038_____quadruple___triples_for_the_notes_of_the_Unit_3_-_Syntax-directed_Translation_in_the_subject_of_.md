### Quadruples and Triples

- Quadruples and triples are two ways of representing three-address code in compiler design.
- Three-address code is an intermediate representation of a source program that uses at most three operands for each instruction.
- Quadruples and triples are useful for generating and optimizing code for target machines.

#### Quadruples

- A quadruple is a structure that consists of four fields: op, arg1, arg2, and result.
- op denotes the operator, arg1 and arg2 denote the two operands, and result is used to store the result of the expression.
- For example, the expression `a = b + c * d` can be represented by the following quadruples:

| op | arg1 | arg2 | result |
|----|------|------|--------|
| *  | c    | d    | t1     |
| +  | b    | t1   | t2     |
| =  | t2   |      | a      |

- The advantage of quadruples is that they are easy to rearrange for global optimization, since the result field can be changed without affecting the other fields.
- The disadvantage of quadruples is that they require more space than triples, since they use a separate field for the result.

#### Triples

- A triple is a structure that consists of three fields: op, arg1, and arg2.
- op denotes the operator, and arg1 and arg2 denote the two operands.
- The result of the expression is stored in the same place as one of the operands, or in a new temporary variable.
- For example, the expression `a = b + c * d` can be represented by the following triples:

| op | arg1 | arg2 |
|----|------|------|
| *  | c    | d    |
| +  | b    | (0)  |
| =  | (1)  | a    |

- The parentheses indicate the position of the triple in the list of triples, starting from zero.
- The advantage of triples is that they require less space than quadruples, since they do not use a separate field for the result.
- The disadvantage of triples is that they are harder to rearrange for global optimization, since changing the result field may affect the other fields.