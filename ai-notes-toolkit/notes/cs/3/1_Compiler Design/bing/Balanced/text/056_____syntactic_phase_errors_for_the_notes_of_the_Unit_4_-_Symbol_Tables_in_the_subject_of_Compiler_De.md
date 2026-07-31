### Syntactic Phase Errors

- Syntactic errors are detected during the syntax analysis phase of the compiler, which checks if the input program conforms to the grammar rules of the source language.
- The general syntax errors are:
  - Structural errors: Missing operators, parentheses, semicolons, etc.
  - Mismatch errors: Mismatched data types, number of arguments, etc.
- Error recovery for syntactic phase errors can be done by various methods, such as:
  - Panic mode recovery: In this method, successive characters from the input are removed one at a time until a designated set of synchronizing tokens is found. Synchronizing tokens are delimiters such as `;` or `}`.
  - Phrase level recovery: In this method, the parser performs local correction on the remaining input, such as replacing, inserting, or deleting symbols.
  - Error productions: In this method, the grammar is augmented with special rules that generate erroneous constructs.
  - Global correction: In this method, the parser tries to find a sequence of minimal changes that can make the input string valid.
- Error reporting for syntactic phase errors should be informative and helpful for the user to fix the error. The error message should include the location, the nature, and the possible cause of the error.