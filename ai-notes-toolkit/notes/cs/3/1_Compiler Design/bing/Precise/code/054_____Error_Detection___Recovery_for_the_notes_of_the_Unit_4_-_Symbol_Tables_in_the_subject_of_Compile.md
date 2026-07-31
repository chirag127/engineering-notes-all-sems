### Error Detection & Recovery

Error detection and recovery is an important aspect of compiler design. It refers to the process of identifying and correcting errors that may occur during the compilation process. These errors can be of various types, including lexical, syntactic, and semantic errors.

1. **Lexical errors** occur when the compiler encounters an invalid character sequence in the source code. For example, an unrecognized symbol or a misspelled keyword. The compiler can detect these errors by comparing the input against the rules of the language's lexical grammar.

2. **Syntactic errors** occur when the compiler encounters an invalid sequence of tokens in the source code. For example, a missing semicolon or an unmatched parenthesis. The compiler can detect these errors by comparing the input against the rules of the language's syntactic grammar.

3. **Semantic errors** occur when the compiler encounters a valid sequence of tokens that does not make sense in the context of the program. For example, using a variable before it is declared or assigning a value of the wrong type to a variable. The compiler can detect these errors by performing semantic analysis on the input.

Once an error is detected, the compiler must attempt to recover from it in order to continue the compilation process. There are several strategies for error recovery, including panic mode, phrase level, and error productions.

1. **Panic mode** recovery involves skipping ahead in the input until a synchronization token is found. This token is typically a statement delimiter, such as a semicolon or a newline character.

2. **Phrase level** recovery involves attempting to correct the error by inserting or deleting tokens in the input. This can be done by using heuristics or by consulting a table of common errors and their corrections.

3. **Error productions** are special grammar rules that allow the parser to recognize and recover from common errors. These rules are added to the language's grammar and can be used to generate more meaningful error messages.

Error detection and recovery is an important part of ensuring that the compiler can handle invalid input gracefully and provide useful feedback to the programmer. It is a complex and challenging task, but one that is essential for the development of robust and reliable compilers.