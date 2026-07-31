# Semantic Errors

Semantic errors are errors that arise when a statement used in a program is not meaningful, that is, it does not correspond to the set of rules (semantics) for that language being used. Semantic errors are detected by the semantic analyzer, which is a component of the compiler that checks the meaning and validity of the source code.

Some of the semantic errors are:

- **Type mismatch**: This occurs when the data types of two operands are not compatible, or when an expression is assigned to a variable of a different type. For example, `int x = "hello";` is a type mismatch error, because a string cannot be assigned to an integer variable. The compiler may try to perform automatic type conversion to resolve this error, but this may not always be possible or desirable .
- **Undeclared variables**: This occurs when a variable is used without being declared first. For example, `x = 10;` is an undeclared variable error, if `x` has not been declared before. The compiler may report this error as an undefined symbol or identifier .
- **Reserved identifier misuse**: This occurs when a variable or a function is given the same name as a reserved word or a predefined identifier in the language. For example, `int main = 0;` is a reserved identifier misuse error, because `main` is a reserved word in C and C++. The compiler may report this error as a syntax error or a redefinition error.

Semantic errors are different from syntax errors, which are errors that violate the rules of grammar or structure of the language. Syntax errors are detected by the syntactic analyzer, which is another component of the compiler that checks the form and arrangement of the source code. For example, `int x = 10;` is a syntax error, if the semicolon is missing at the end.

Semantic errors are also different from runtime errors, which are errors that occur during the execution of the program, such as division by zero, memory overflow, or invalid input. Runtime errors are detected by the interpreter or the operating system, which are responsible for running the program.

Semantic errors are harder to detect and debug than syntax errors, because they do not always produce an error message or a visible output. Semantic errors may cause the program to behave incorrectly or unpredictably, or to produce wrong results. Therefore, it is important for the programmer to write clear and meaningful code, and to use proper tools and techniques to test and verify the logic and functionality of the program.