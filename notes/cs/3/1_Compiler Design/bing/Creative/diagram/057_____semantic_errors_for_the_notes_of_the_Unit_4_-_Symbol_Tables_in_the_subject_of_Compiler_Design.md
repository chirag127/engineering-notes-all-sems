### Semantic errors

Semantic errors are errors that arise when a statement used in a program is not meaningful, that is, it does not correspond to the set of rules (semantics) for that language being used. Semantic errors are detected by the semantic analyzer, which is a component of the compiler that checks the meaning and validity of the source code.

Some of the semantic errors are:

- Type mismatch: This occurs when the data types of two operands are not compatible, such as adding a string and an integer. Some compilers may automatically perform type conversion, but this may lead to unexpected results or loss of precision.
- Undeclared variables: This occurs when a variable is used without being declared in the scope. This may cause the compiler to assume a default type or generate an error.
- Reserved identifier misuse: This occurs when a keyword or a predefined name is used as a variable or a function name. This may cause a conflict or confusion with the language syntax or semantics.

Some of the semantic errors can be detected by the compiler at compile time, and the compiler may generate a message indicating the type of error and the position in the source code where the error occurred. However, some semantic errors may not be detected by the compiler, because they do not violate the grammar of the language, but the intent of the programmer. These errors may cause the program to behave incorrectly or produce wrong results at run time. Therefore, it is important for the programmer to write clear and meaningful code, and to test and debug the program thoroughly.