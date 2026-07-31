# Statements that alter the flow of control

- Statements that alter the flow of control are the statements that change the flow of execution of statements.
- They are used to implement conditional or iterative logic in a program.
- Examples of statements that alter the flow of control are: if, if-else, switch-case, while, do-while, for, break, continue, goto, return, etc.
- The syntax and semantics of these statements vary depending on the programming language and the compiler design.
- The translation of these statements into intermediate code or target code requires the use of labels, jumps, conditional branches, and loops.
- The compiler also needs to construct a control flow graph (CFG) for each function or procedure in the program, which represents the possible paths of execution and the basic blocks of statements.
- The CFG is used for various optimizations and analyses, such as data flow analysis, dead code elimination, loop invariant code motion, etc.
- The following are some examples of how to translate some common statements that alter the flow of control into intermediate code or target code:

## If statement

- The if statement has the form: `if (E) S`, where E is a Boolean expression and S is a statement.
- The translation of the if statement can be done using a conditional jump instruction, such as `ifFalse` or `ifTrue`, which jumps to a label if the condition is false or true, respectively.
- For example, the following if statement:

```
if (x > y) z = x;
```

- Can be translated into the following intermediate code:

```
ifFalse x > y goto L1
z = x
L1: ...
```

- Or the following target code (assuming x, y, and z are stored in registers R1, R2, and R3):

```
cmp R1, R2
jle L1
mov R3, R1
L1: ...
```

## If-else statement

- The if-else statement has the form: `if (E) S1 else S2`, where E is a Boolean expression and S1 and S2 are statements.
- The translation of the if-else statement can be done using two conditional jump instructions, one for the true branch and one for the false branch, and an unconditional jump instruction to skip the false branch after executing the true branch.
- For example, the following if-else statement:

```
if (x > y) z = x; else z = y;
```

- Can be translated into the following intermediate code:

```
ifFalse x > y goto L1
z = x
goto L2
L1: z = y
L2: ...
```

- Or the following target code (assuming x, y, and z are stored in registers R1, R2, and R3):

```
cmp R1, R2
jle L1
mov R3, R1
jmp L2
L1: mov R3, R2
L2: ...
```

## While statement

- The while statement has the form: `while (E) S`, where E is a Boolean expression and S is a statement.
- The translation of the while statement can be done using a loop label, a conditional jump instruction to exit the loop, and an unconditional jump instruction to repeat the loop.
- For example, the following while statement:

```
while (x < y) x = x + 1;
```

- Can be translated into the following intermediate code:

```
L1: ifFalse x < y goto L2
x = x + 1
goto L1
L2: ...
```

- Or the following target code (assuming x and y are stored in registers R1 and R2):

```
L1: cmp R1, R2
jge L2
inc R1
jmp L1
L2: ...
```

## Switch-case statement

- The switch-case statement has the form: `switch (E) { case C1: S1; ... case Cn: Sn; default: Sd; }`, where E is an expression, C1, ..., Cn are constants, and S1, ..., Sn, Sd are statements.
- The translation of the switch-case statement can be done using a jump table, which is an array of labels corresponding to each case, and a default label for the default case.
- The expression E is evaluated and used as an index to the jump table, and the control is transferred to the corresponding