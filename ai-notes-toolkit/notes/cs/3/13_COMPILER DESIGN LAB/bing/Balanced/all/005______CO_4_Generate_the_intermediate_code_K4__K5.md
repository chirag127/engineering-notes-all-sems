#### CO 4 Generate the intermediate code K4, K5

- Intermediate code is a representation of a program that is between the source code and the target code. It is used to facilitate the analysis and optimization of the program, as well as to simplify the translation to the target code.
- K4 and K5 are two types of intermediate code that are based on the three-address code (TAC) format. TAC is a linear sequence of instructions, each of which has at most three operands. The operands can be constants, variables, or temporary names.
- K4 is a type of intermediate code that uses labels to indicate the targets of conditional and unconditional jumps. For example, the following TAC:

```
if x < y goto L1
t1 = x + y
x = t1
goto L2
L1: t2 = x - y
y = t2
L2: print x, y
```

can be represented in K4 as:

```
L1: x < y
t1 = x + y
x = t1
L2: print x, y
t2 = x - y
y = t2
```

- K5 is a type of intermediate code that uses relative offsets to indicate the targets of conditional and unconditional jumps. For example, the same TAC as above can be represented in K5 as:

```
x < y, 4
t1 = x + y
x = t1
print x, y, -3
t2 = x - y
y = t2
```

- The relative offset is the number of instructions to skip or go back from the current instruction. A positive offset means to skip forward, while a negative offset means to go back. For example, `x < y, 4` means to skip four instructions if `x < y` is true, while `print x, y, -3` means to go back three instructions after printing `x` and `y`.
- To generate the intermediate code K4 or K5 from a given source code, the following steps can be followed:

  - Perform lexical analysis and syntactic analysis to obtain the abstract syntax tree (AST) of the source code.
  - Traverse the AST in a depth-first order and generate the corresponding TAC instructions for each node. Use temporary names to store intermediate values and labels to mark the entry and exit points of loops and conditional statements.
  - To convert the TAC to K4, replace the `goto` instructions with the corresponding labels and reorder the instructions to match the control flow of the program.
  - To convert the TAC to K5, replace the labels with the relative offsets and eliminate the `goto` instructions. The relative offsets can be calculated by counting the number of instructions between the current instruction and the target label.