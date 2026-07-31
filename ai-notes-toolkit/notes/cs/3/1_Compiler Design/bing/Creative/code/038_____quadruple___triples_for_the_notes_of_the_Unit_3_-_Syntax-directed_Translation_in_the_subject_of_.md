# Quadruples and Triples for Syntax-directed Translation

- Syntax-directed translation is a technique to generate intermediate code from a syntax tree.
- Intermediate code is a representation of the source program that is close to the target machine code, but is easier to manipulate and optimize.
- Intermediate code can be in various forms, such as postfix notation, three-address code, or quadruples and triples.
- Quadruples and triples are two ways of implementing three-address code as a record with address fields.
- Three-address code is a linearized representation of a syntax tree, where each statement has at most three operands and one operator.
- Three-address code can be easily translated into assembly language or machine code.

## Quadruples

- A quadruple is a structure that consists of four fields: op, arg1, arg2, and result.
- op denotes the operator, arg1 and arg2 denote the two operands, and result denotes the location where the result of the operation is stored.
- Quadruples are stored in a table, where each row corresponds to a statement in the three-address code.
- Quadruples have the advantage of being easy to rearrange for global optimization, as the result field can be changed without affecting the other fields.
- Quadruples have the disadvantage of requiring extra space for temporary variables, as each intermediate result needs a distinct location.

## Triples

- A triple is a structure that consists of three fields: op, arg1, and arg2.
- op denotes the operator, and arg1 and arg2 denote the two operands.
- Triples are stored in a table, where each row corresponds to a statement in the three-address code.
- Triples do not have a result field, instead the result of each operation is stored in the same location as the triple itself, and is referenced by its index in the table.
- Triples have the advantage of saving space for temporary variables, as the same location can be reused for multiple intermediate results.
- Triples have the disadvantage of being difficult to rearrange for global optimization, as changing the order of the triples may affect the meaning of the code.

## Example

- Consider the following expression: `a = b * c + d * e`
- The syntax tree for this expression is:

```
     =
    / \
   a   +
      / \
     *   *
    / \ / \
   b c d e
```

- The three-address code for this expression is:

```
t1 = b * c
t2 = d * e
a = t1 + t2
```

- The quadruples for this expression are:

| op  | arg1 | arg2 | result |
| --- | ---- | ---- | ------ |
| *   | b    | c    | t1     |
| *   | d    | e    | t2     |
| +   | t1   | t2   | a      |

- The triples for this expression are:

| op  | arg1 | arg2 |
| --- | ---- | ---- |
| *   | b    | c    |
| *   | d    | e    |
| +   | (0)  | (1)  |

- Note that the operands in the last triple are the indices of the previous triples, not the values of t1 and t2.