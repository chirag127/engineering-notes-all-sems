### Syntactic Phase Errors

- Syntactic errors are detected during the syntax analysis phase of the compiler, which checks if the input program conforms to the grammar rules of the source language.
- The general syntax errors are:
  - Structural errors: missing or extra operators, parentheses, braces, semicolons, etc.
  - Mismatch errors: wrong types, number or order of operands, parameters, arguments, etc.
  - Scope errors: undeclared or redeclared identifiers, illegal use of reserved words, etc.
- The compiler should report the location and nature of the syntax errors to the user, and attempt to recover from them and continue parsing the rest of the input .
- The error recovery strategies for syntactic errors are :
  - Panic mode recovery: the parser discards input symbols until it finds a synchronizing token, such as a delimiter or a keyword, and then resumes normal parsing.
  - Phrase level recovery: the parser performs local corrections on the input, such as inserting, deleting or replacing symbols, to match the expected production.
  - Error productions: the parser adds extra rules to the grammar that can handle common errors, such as missing semicolons or parentheses, and generates error messages accordingly.
  - Global correction: the parser tries to find the minimum number of changes required to make the input syntactically correct, using techniques such as dynamic programming or backtracking.