### Lexical Phase Errors

- Lexical phase errors are errors that occur during the lexical analysis phase of the compiler, which is responsible for scanning the source code and generating tokens.
- A token is a sequence of characters that matches the pattern of a valid lexical unit, such as a keyword, an identifier, a constant, an operator, etc.
- A lexical error is a sequence of characters that does not match the pattern of any token, and therefore cannot be recognized by the lexical analyzer.
- Some examples of lexical errors are:
  - Invalid characters, such as @, #, $, etc. that are not part of the language syntax.
  - Exceeding the length of identifiers or numeric constants, such as a variable name that is too long or a number that is out of range.
  - Improperly formed strings or comments, such as missing quotes or delimiters, or nested comments.
  - Misspelled keywords, such as `wihle` instead of `while`, or `funtion` instead of `function`.
- Lexical errors can be detected and reported by the lexical analyzer, or by the parser, which is the next phase of the compiler that checks the syntax of the tokens.
- Some possible ways to handle lexical errors are:
  - Ignore the error and continue scanning the next character or token, such as skipping over invalid characters or truncating long identifiers or constants.
  - Replace the error with a valid token, such as correcting the spelling of keywords or inserting missing quotes or delimiters.
  - Insert a special error token into the token stream, such as `ERROR` or `INVALID`, and let the parser handle it later.
  - Abort the compilation process and display an error message, such as `Lexical error: invalid character @ at line 5, column 10`.