### Syntactic Phase Errors

- Syntactic errors are detected during the syntax analysis phase of the compiler, which checks if the input program conforms to the grammar rules of the source language .
- The general syntax errors are:
  - Structural errors: missing or extra operators, parentheses, braces, semicolons, etc. For example, `a = b + ;` or `if (x > y) { a = b;`
  - Mismatch errors: using wrong types, modes, or number of operands for an operator or a function. For example, `a = b + "hello";` or `printf("%d", x, y);`
  - Scope errors: using an identifier that is not declared or visible in the current scope. For example, `a = x + y;` where `x` or `y` is not defined.
- The compiler should report the syntactic errors to the user with appropriate error messages, indicating the location and the nature of the error .
- The compiler should also attempt to recover from the syntactic errors and continue to parse the rest of the input, without aborting the compilation process .
- The common techniques for error recovery are:
  - Panic mode recovery: the compiler discards the input symbols until it finds a synchronizing token, such as a delimiter or a keyword, that can resume the normal parsing. For example, if the compiler encounters an error at `a = b + ;`, it can skip the `;` and start parsing the next statement.
  - Phrase level recovery: the compiler replaces or inserts a minimal number of symbols to make the input phrase valid. For example, if the compiler encounters an error at `a = b + ;`, it can insert a `0` after the `+` and parse the expression as `a = b + 0;`.
  - Error productions: the compiler modifies the grammar rules to include common errors as alternative productions. For example, the compiler can add a rule like `expr -> expr ;` to handle the case of an extra semicolon in an expression.
  - Global correction: the compiler uses a measure of similarity between the input and the grammar to find the closest valid input that can be parsed. This technique requires more complex algorithms and may not always find the optimal correction.
- The compiler should also maintain the symbol table during the syntax analysis phase, which stores the information about the identifiers used in the program, such as their names, types, scopes, and values.
- The symbol table helps the compiler to check for semantic errors, such as type mismatches, undeclared variables, or multiple declarations of the same variable.
- The symbol table also helps the compiler to generate intermediate code or target code, by providing the attributes of the identifiers needed for code generation.