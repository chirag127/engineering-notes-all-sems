### Syntactic Phase Errors

- Syntactic errors are detected during the syntax analysis phase of the compiler, which checks if the input program conforms to the grammar rules of the source language .
- The general syntax errors are:
  - Structural errors: missing operators, parentheses, semicolons, etc.
  - Mismatch errors: incompatible types, wrong number of arguments, etc.
  - Scope errors: undeclared or redeclared identifiers, etc.
- The syntax analysis phase can use different strategies to handle syntactic errors, such as  :
  - Panic mode recovery: skip the input until a synchronizing token (such as a delimiter or a keyword) is found and resume parsing from there.
  - Phrase level recovery: replace, delete, or insert a prefix of the input that leads to a successful parse.
  - Error productions: modify the grammar to include common errors and generate appropriate error messages when they are encountered.
  - Global correction: find the minimum number of changes to the input that result in a valid parse.
- The goal of error handling in the syntax analysis phase is to report meaningful and accurate error messages to the user, and to recover from the errors gracefully without affecting the rest of the compilation process.