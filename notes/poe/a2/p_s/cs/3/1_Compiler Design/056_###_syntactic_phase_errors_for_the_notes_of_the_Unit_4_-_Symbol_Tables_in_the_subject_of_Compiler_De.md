 Here is the content in markdown format for the topic ### syntactic phase errors for the notes of the Unit 4 - Symbol Tables in the subject of Compiler Design:

### Syntactic Phase Errors

The syntactic phase of a compiler analyzes the structure of the source program and groups its symbols into meaningful sequences called syntactical units. The compiler ensures that:

1. The source program is written in the correct syntax of the programming language.
2. The syntactical units are properly nested or sequenced.

If the source program does not conform to the syntactic rules of the programming language, the compiler reports syntactic errors. Some common syntactic errors are:

- Misspelled keywords or identifiers: The compiler will flag an error if a keyword or identifier is misspelled. For example, `int` misspelled as `itn` will be reported as an error.
- Unmatched parentheses, braces, or brackets: The compiler checks that every opening parenthesis, brace, or bracket has a matching closing one. If they do not match, it reports a syntax error. For example, `(x + y` or `if (x > y {` will be flagged as errors due to unmatched parentheses and braces respectively.
- Invalid operator precedence or association: The compiler checks that operators are used with the correct precedence and are properly associated. For example, `x + y * z` is correct but `x * y + z` or `x + y * z)` (with unmatched parenthesis) will be reported as syntax errors.
- Missing semicolons: In many languages like C/C++, each statement must be ended with a semicolon. If a semicolon is missing, the compiler will report a syntax error.
- Illegal character: If the source code contains an illegal character like `@` or `#` in the middle of an identifier or keyword, the compiler will report it as a syntax error.

The compiler reports the location (line number and position) of a syntax error and may try to recover from it and continue compilation. However, too many syntax errors may prevent the compiler from proceeding further. The programmer must then fix the syntax errors and recompile the source program.