# Declarations and Case Statements

## Declarations
- A declaration in a program is a statement that provides the information about the name and type of data objects to the compiler.
- Declarations can be used to allocate storage for variables, constants, functions, procedures, types, etc.
- Declarations can also specify the scope and visibility of the names, such as global, local, static, extern, etc.
- Declarations can be translated into intermediate code by using the following steps:
  - As the sequence of declarations in a procedure or block is examined, we can lay out storage for names local to the procedure.
  - We can use a symbol table to store the information about the names, such as their type, size, offset, etc.
  - We can generate code to initialize the names with their initial values, if any.
  - We can also generate code to handle nested scopes, such as opening and closing brackets, using stack or heap allocation.

## Case Statements
- A case statement is a statement that allows the execution of one of several alternative statements based on the value of an expression.
- Case statements can be used to implement multiple branching, such as switch statements in C or Java.
- Case statements can be translated into intermediate code by using the following methods:
  - By a sequence of conditional goto statements, if the number of cases is small.
  - By creating a table of pairs, with each pair consisting of a value and a label for the code of the corresponding statement. The compiler generates a loop to compare the value of the expression with each value in the table, and jumps to the matching label if found.
  - By creating a binary search tree of pairs, with each pair consisting of a value and a label for the code of the corresponding statement. The compiler generates code to traverse the tree based on the value of the expression, and jumps to the matching label if found.
  - By creating a hash table of pairs, with each pair consisting of a value and a label for the code of the corresponding statement. The compiler generates code to compute the hash value of the expression, and jumps to the matching label if found.