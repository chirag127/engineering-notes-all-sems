# Quadruples and Triples for Syntax-directed Translation

- In compiler design, three address code is an intermediate representation of a source program that uses at most three operands for each instruction.
- Three address code can be implemented as a record with address fields. There are three main representations used: quadruples, triples and indirect triples.
- Quadruples: A quadruple is a structure that consists of four fields: op, arg1, arg2 and result. op denotes the operator, arg1 and arg2 denote the two operands, and result is used to store the result of the expression. For example, the expression `a = b + c * d` can be represented by the following quadruples:

| op | arg1 | arg2 | result |
|----|------|------|--------|
| *  | c    | d    | t1     |
| +  | b    | t1   | t2     |
| =  | t2   |      | a      |

- The advantage of quadruples is that they are easy to rearrange for global optimization, since the result field can be changed without affecting the other fields.
- The disadvantage of quadruples is that they require more space than triples, since they use an extra field for the result.
- Triples: A triple is a structure that consists of three fields: op, arg1 and arg2. op denotes the operator, and arg1 and arg2 denote the two operands. The result of the expression is stored in the same place as one of the operands. For example, the expression `a = b + c * d` can be represented by the following triples:

| op | arg1 | arg2 |
|----|------|------|
| *  | c    | d    |
| +  | b    | (0)  |
| =  | a    | (1)  |

- The advantage of triples is that they require less space than quadruples, since they do not use an extra field for the result.
- The disadvantage of triples is that they are harder to rearrange for global optimization, since changing the result field may affect the other fields.
- Indirect triples: An indirect triple is a combination of triples and a separate list of pointers to the triples. The list of pointers is used to store the result of the expression, and the triples are used to store the operation and the operands. For example, the expression `a = b + c * d` can be represented by the following indirect triples:

| op | arg1 | arg2 |
|----|------|------|
| *  | c    | d    |
| +  | b    | (0)  |
| =  | a    | (1)  |

| 0 | 1 | 2 |
|---|---|---|
| 0 | 1 | 2 |

- The advantage of indirect triples is that they can save some space compared with quadruples if the same temporary value is used more than once, since two or more entries in the pointer list can point to the same triple.
- The disadvantage of indirect triples is that they require an extra level of indirection to access the result of the expression, which may affect the performance.