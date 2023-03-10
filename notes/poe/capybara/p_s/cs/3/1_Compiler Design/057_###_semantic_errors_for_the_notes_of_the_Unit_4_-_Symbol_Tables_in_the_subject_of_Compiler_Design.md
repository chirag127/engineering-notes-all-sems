### Semantic Errors for the Notes of the Unit 4 - Symbol Tables in the Subject of Compiler Design

In compiler design, semantic errors refer to the errors that occur due to the misuse or incorrect interpretation of the meaning of programming language statements. These errors are different from syntax errors, which are detected by the compiler during the parsing phase.

Semantic errors are more complex and difficult to detect since they are related to the meaning and interpretation of the program code. These errors can lead to unexpected program behavior or even program crashes.

Some common examples of semantic errors include:

- Type mismatch errors: When a program tries to perform an operation on two variables of different data types, a type mismatch error occurs.
- Variable scope errors: When a variable is used outside its scope, such as when it is not initialized or has already been destroyed, a variable scope error occurs.
- Array index out of bounds errors: When a program tries to access an array element that does not exist, an array index out of bounds error occurs.
- Function call errors: When a program calls a function with the wrong number or type of arguments, a function call error occurs.

To detect semantic errors, compilers use symbol tables, which are data structures that store information about the variables, functions, and other symbols used in the program. Symbol tables help the compiler to verify the correct use of symbols and detect semantic errors.

There are several advantages and disadvantages of using symbol tables for semantic error detection. Some of the advantages include:

- They provide a centralized location for storing and accessing symbol information.
- They help to detect semantic errors at compile time, which can save time and effort in debugging.
- They can be used to optimize program execution by providing information about symbol usage.

Some of the disadvantages of using symbol tables for semantic error detection include:

- They can be complex and difficult to implement, especially for large programs.
- They may not be able to detect all types of semantic errors, such as those related to program logic or design.
- They may require additional memory and processing time, which can impact program performance.

In conclusion, semantic errors are a crucial aspect of compiler design, and symbol tables play a vital role in detecting and correcting these errors. Understanding how semantic errors occur and how they can be detected can help programmers to write more reliable and efficient code.