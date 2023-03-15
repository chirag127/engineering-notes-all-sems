# Lexical Phase Errors

- Lexical phase errors are errors that occur during the lexical analysis phase of the compiler, which is responsible for scanning the source code and generating tokens.
- A token is a sequence of characters that matches the pattern of a valid lexical unit, such as a keyword, an identifier, a constant, an operator, etc.
- A lexical error is a sequence of characters that does not match the pattern of any token, and therefore cannot be recognized by the lexical analyzer.
- Some examples of lexical errors are:
  - Invalid characters, such as @, #, $, etc. that are not part of the language syntax.
  - Exceeding the length of identifiers or numeric constants, such as 12345678901234567890 or abcdefghijklmnopqrstuvwxyz.
  - Missing or mismatched delimiters, such as quotes, brackets, parentheses, etc.
  - Improperly formed strings, such as "Hello or 'World'.
  - Incorrect spelling of keywords, such as intger, whle, etc.
- Lexical errors can be detected and reported by the lexical analyzer, or they can be ignored and passed to the next phase of the compiler, depending on the design of the compiler and the language specification.
- Some possible ways of handling lexical errors are:
  - Printing an error message and terminating the compilation process.
  - Printing an error message and skipping the invalid character or token and continuing the compilation process.
  - Replacing the invalid character or token with a valid one and continuing the compilation process.
  - Inserting a missing delimiter or removing an extra one and continuing the compilation process.
  - Correcting the spelling of a keyword or an identifier and continuing the compilation process.
- The choice of error handling strategy depends on the severity of the error, the ease of recovery, and the impact on the semantics of the program.