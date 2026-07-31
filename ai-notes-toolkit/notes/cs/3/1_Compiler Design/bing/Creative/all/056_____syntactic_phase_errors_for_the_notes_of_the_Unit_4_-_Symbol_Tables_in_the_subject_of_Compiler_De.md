# Syntactic Phase Errors

Syntactic phase errors are errors that occur during the syntax analysis phase of the compiler. Syntax analysis is the process of checking whether the input program conforms to the grammar rules of the source language. The syntax analyzer or parser uses a grammar specification to generate a parse tree or an abstract syntax tree for the input program. If the input program does not match the grammar rules, the parser reports a syntactic error.

Some of the common types of syntactic errors are:

- **Structural errors**: These are errors that violate the basic structure of the source language, such as missing operators, parentheses, semicolons, braces, etc. For example, `a = b + c` is a valid expression, but `a = b +` is not, because it is missing an operand after the `+` operator.
- **Mismatched errors**: These are errors that occur when the expected token or symbol does not match the actual token or symbol in the input. For example, `if (x > y) then z = x;` is a valid statement, but `if (x > y) then z = x)` is not, because it has a mismatched parenthesis at the end.
- **Undefined errors**: These are errors that occur when the parser encounters an undefined symbol or identifier in the input. For example, `x = y + z;` is a valid statement, but `x = y + w;` is not, if `w` is not declared or defined anywhere in the program.

The parser should be able to detect and report syntactic errors as soon as possible, and also recover from them and continue to parse the rest of the input. There are different strategies for error recovery, such as:

- **Panic mode recovery**: In this method, the parser discards the input tokens one by one until it finds a synchronizing token, which is a delimiter or a keyword that marks the end of a statement or a block. For example, if the parser encounters an error in an expression, it can skip the tokens until it finds a semicolon or a closing brace, and then resume parsing from the next statement.
- **Phrase level recovery**: In this method, the parser tries to replace or insert a token or a phrase that can make the input syntactically correct. For example, if the parser encounters an error in an expression, it can insert a missing operator or operand, or replace an invalid token with a valid one, and then continue parsing the expression.
- **Error productions recovery**: In this method, the parser uses special error-handling rules in the grammar that can handle common syntactic errors. For example, the parser can have a rule like `expr -> expr + error` that can match an expression with a missing operand after the `+` operator, and then report and recover from the error.

The parser should also provide informative and helpful error messages to the user, indicating the location, type, and possible cause of the error. The parser should also avoid reporting spurious or cascading errors, which are errors that are caused by a previous error and not by the actual input. For example, if the parser encounters a missing semicolon at the end of a statement, it should not report an error for the next statement, which may be syntactically correct.