### Lexical Phase errors for the notes of the Unit 4 - Symbol Tables in the subject of Compiler Design

The lexical phase of the compiler is also known as the scanning phase. It is responsible for analyzing the source code and generating a stream of tokens that will be used by the parser to create an abstract syntax tree. During this phase, the compiler may encounter various errors related to the lexical structure of the source code. In this section, we will discuss the most common lexical phase errors and how to identify and fix them.

1. **Illegal characters:** These errors occur when the source code contains characters that are not allowed in the programming language. For example, in C++, the dollar sign ($) is not a valid character in variable names. To fix this error, the programmer should replace the illegal character with a valid one.

2. **Missing or misplaced tokens:** These errors occur when the source code is missing a required token or when a token is placed in the wrong position. For instance, in C++, a semicolon is required at the end of each statement. If a semicolon is missing, the compiler will generate an error message. To fix this error, the programmer should add the missing token or move the misplaced token to the correct position.

3. **Incorrect identifiers:** These errors occur when the programmer uses an incorrect identifier name. For instance, in C++, an identifier name cannot start with a digit. To fix this error, the programmer should choose a valid identifier name.

4. **Mismatched delimiters:** These errors occur when there is a mismatch between opening and closing delimiters such as braces, brackets, and parentheses. For example, in C++, if the programmer forgets to close a brace, the compiler will generate an error message. To fix this error, the programmer should add the missing delimiter.

5. **Unrecognized symbols:** These errors occur when the source code contains unrecognized symbols that are not part of the programming language. For example, in C++, if the programmer uses a symbol such as '@' that is not part of the language, the compiler will generate an error message. To fix this error, the programmer should remove the unrecognized symbol.

In conclusion, the lexical phase of the compiler is responsible for analyzing the source code and generating a stream of tokens. During this phase, the compiler may encounter various errors related to the lexical structure of the source code. By understanding these common errors and how to fix them, programmers can write code that is free of lexical errors and can be compiled successfully.