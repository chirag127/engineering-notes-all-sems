### Syntactic Phase Errors

- Syntactic errors are detected during the syntax analysis phase of the compiler, which checks if the input program conforms to the grammar rules of the source language .
- The general syntax errors are:
  - Structural errors: missing operators, parentheses, semicolons, etc.
  - Mismatch errors: incompatible types, wrong number of arguments, etc.
  - Scope errors: undeclared or redeclared variables, functions, etc.
- Error recovery for syntactic phase errors is the process of handling the errors and continuing the parsing of the rest of the input . Some common methods of error recovery are:
  - Panic mode recovery: in this method, successive characters from the input are removed one at a time until a designated set of synchronizing tokens is found. Synchronizing tokens are delimiters such as `;` or `}` that indicate the end of a statement or a block.
  - Phrase level recovery: in this method, the parser performs local corrections on the remaining input, such as replacing, inserting, or deleting tokens, to make the input match the expected production.
  - Error productions: in this method, the grammar is augmented with special rules that generate erroneous constructs, such as `expr -> expr + error`. The parser can then use these rules to handle the errors and resume the normal parsing.
  - Global correction: in this method, the parser tries to find the minimum number of changes required to make the entire input syntactically correct. This method is more complex and costly than the others, but it can produce better results.
- Error reporting for syntactic phase errors is the process of providing informative and helpful messages to the user about the errors. Some guidelines for error reporting are:
  - Report the location of the error, such as the line number, column number, or token position.
  - Report the nature of the error, such as the expected token, the missing symbol, or the invalid construct.
  - Report the possible causes of the error, such as a typo, a forgotten declaration, or a misplaced operator.
  - Report the possible solutions or suggestions for the error, such as correcting the spelling, adding the declaration, or moving the operator.
  - Report the severity of the error, such as fatal, warning, or note. Fatal errors prevent the compilation from proceeding, while warnings and notes indicate potential problems or hints.