### Semantic errors

Semantic errors are errors that arise when a statement used in a program is not meaningful, that is, it does not correspond to the set of rules (semantics) for that language being used. Semantic errors are detected by the semantic analyzer, which is a component of the compiler that checks the source code for meaningfulness and validity. Semantic errors can cause the program to behave incorrectly or unpredictably, or to terminate abnormally.

Some of the common types of semantic errors are:

- **Type mismatch**: This occurs when the data types of two operands or expressions are not compatible, or when an operation is applied to an incompatible data type. For example, adding a string and an integer, or dividing a boolean by a float. Some languages allow implicit or explicit type conversion to resolve type mismatch errors, while others report them as compile-time or run-time errors .
- **Undeclared variables**: This occurs when a variable is used in the program without being declared or defined in the scope. For example, using a variable `x` that has not been assigned a value or a data type. This can cause the compiler to report an error or assign a default value to the variable, depending on the language .
- **Reserved identifier misuse**: This occurs when a variable or a function is given a name that is already reserved by the language or the system. For example, using `int` or `main` as variable names in C++. This can cause the compiler to report an error or to confuse the user-defined identifier with the reserved one.

Some of the strategies for error recovery in semantic analysis are:

- **Symbol table**: A symbol table is a data structure that stores information about the identifiers used in the program, such as their names, data types, scopes, and values. The semantic analyzer can use the symbol table to check the validity and compatibility of the identifiers and to report or resolve any errors.
- **Type conversion**: Type conversion is the process of changing the data type of a value or an expression to another data type, either implicitly or explicitly. The semantic analyzer can use type conversion to resolve type mismatch errors by converting one operand to the data type of the other, or by casting both operands to a common data type. For example, converting a string to an integer, or casting a float and an integer to a double .
- **Default values**: Default values are the values that are assigned to variables or expressions when they are not explicitly initialized or defined by the user. The semantic analyzer can use default values to resolve undeclared variable errors by assigning a default value to the variable based on its data type or context. For example, assigning 0 to an integer variable, or false to a boolean variable.

Some of the advantages and disadvantages of semantic analysis are:

- **Advantages**:
  - It ensures the meaningfulness and validity of the source code and prevents logical errors or unexpected behavior.
  - It allows basic type conversion, which can simplify the calculations and operations in the program.
  - It helps in optimizing the code by eliminating unnecessary or redundant expressions or statements.
- **Disadvantages**:
  - It can be complex and time-consuming, as it involves checking the semantics of every statement and expression in the program.
  - It can be error-prone, as it depends on the accuracy and completeness of the symbol table and the type conversion rules.
  - It can be restrictive, as it may not allow some expressions or statements that are syntactically correct but semantically invalid.