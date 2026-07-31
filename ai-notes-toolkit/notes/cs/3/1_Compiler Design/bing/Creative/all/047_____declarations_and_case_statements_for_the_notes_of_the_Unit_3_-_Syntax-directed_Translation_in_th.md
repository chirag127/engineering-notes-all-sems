# Declarations and Case Statements

## Declarations
- A declaration in a program is a statement that provides the information about the name and type of data objects to the compiler.
- Declarations can be used to allocate storage for variables, constants, functions, procedures, types, etc.
- Declarations can also specify the scope and visibility of the names, such as global, local, static, extern, etc.
- Declarations can be classified into two categories: explicit and implicit.
  - Explicit declarations are those that are explicitly written by the programmer, such as `int x;` or `float y = 3.14;`.
  - Implicit declarations are those that are inferred by the compiler from the context, such as `x = 5;` or `y++;`.
- The syntax and semantics of declarations depend on the programming language and the compiler design.
- As the sequence of declarations in a procedure or block is examined, the compiler can lay out storage for names local to the procedure.
- The compiler can also generate intermediate code for initializing the declared names, such as assigning values or calling constructors.
- The compiler can also check for errors and warnings in the declarations, such as duplicate names, incompatible types, uninitialized variables, etc.

## Case Statements
- A case statement is a control structure that allows the execution of one of several alternative statements based on the value of an expression.
- A case statement typically consists of a switch expression, a set of case labels, and a set of case statements.
- The syntax and semantics of case statements depend on the programming language and the compiler design.
- A common way to implement case statements is by using a sequence of conditional goto statements, if the number of cases is small.
  - For example, the following C code:

```c
switch (x) {
  case 1: 
    s1;
    break;
  case 2:
    s2;
    break;
  default:
    s3;
}
```
  - Can be translated into the following intermediate code:

```c
if x == 1 goto L1
if x == 2 goto L2
goto L3
L1: s1
goto L4
L2: s2
goto L4
L3: s3
L4:
```
- Another way to implement case statements is by creating a table of pairs, with each pair consisting of a value and a label for the code of the corresponding statement.
  - The compiler generates a loop to compare the value of the expression with each value in the table, and jumps to the appropriate label if a match is found.
  - For example, the following C code:

```c
switch (x) {
  case 1: 
    s1;
    break;
  case 2:
    s2;
    break;
  default:
    s3;
}
```
  - Can be translated into the following intermediate code:

```c
table = [(1, L1), (2, L2)]
i = 0
while i < length(table) do
  if x == table[i].value then goto table[i].label
  i = i + 1
end
goto L3
L1: s1
goto L4
L2: s2
goto L4
L3: s3
L4:
```
- Some programming languages and compilers may also use other techniques to optimize the implementation of case statements, such as binary search, hashing, jump tables, etc.