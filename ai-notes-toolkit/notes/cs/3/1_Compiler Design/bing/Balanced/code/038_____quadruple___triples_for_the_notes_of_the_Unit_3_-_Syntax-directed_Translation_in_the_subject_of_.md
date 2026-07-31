### Quadruples and Triples in Compiler Design

- Quadruples and triples are two ways of representing three-address code in compiler design.
- Three-address code is an intermediate representation of a source program that uses at most three operands for each instruction.
- Quadruples and triples are useful for code optimization and code generation phases of a compiler.

#### Quadruples

- A quadruple is a record with four fields: op, arg1, arg2, and result.
- op is the operator of the instruction, such as +, -, *, /, =, etc.
- arg1 and arg2 are the operands of the instruction, which can be constants, variables, or temporary names.
- result is the name of the location where the result of the instruction is stored, which can also be a constant, variable, or temporary name.
- Quadruples can be stored in a table with four columns, where each row corresponds to an instruction.
- For example, the expression `a = b * c + d` can be represented by the following quadruples:

| op  | arg1 | arg2 | result |
| --- | ---- | ---- | ------ |
| *   | b    | c    | t1     |
| +   | t1   | d    | t2     |
| =   | t2   |      | a      |

- The advantage of quadruples is that they are easy to rearrange for code optimization, since each instruction has a unique result name.
- The disadvantage of quadruples is that they may require more space than triples, since they introduce more temporary names.

#### Triples

- A triple is a record with three fields: op, arg1, and arg2.
- op is the operator of the instruction, such as +, -, *, /, =, etc.
- arg1 and arg2 are the operands of the instruction, which can be constants, variables, or references to other triples.
- Triples can be stored in a table with three columns, where each row corresponds to an instruction and has a unique index.
- For example, the expression `a = b * c + d` can be represented by the following triples:

| index | op  | arg1 | arg2 |
| ----- | --- | ---- | ---- |
| 0     | *   | b    | c    |
| 1     | +   | (0)  | d    |
| 2     | =   | a    | (1)  |

- The advantage of triples is that they save space by avoiding temporary names and reusing previous instructions.
- The disadvantage of triples is that they are harder to rearrange for code optimization, since changing the order of instructions may affect the references to other triples.