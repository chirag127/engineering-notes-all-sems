### Lexical Phase errors for the notes of the Unit 4 - Symbol Tables in the subject of Compiler Design

The lexical phase is the first phase of the compilation process in which the source code is converted into a sequence of tokens. These tokens are then analyzed by the parser to generate an abstract syntax tree. Any error that occurs during the lexical phase is known as a lexical error. In this section, we will discuss the common lexical errors that can occur during the compilation process.

1. **Misspelled Identifiers:** Identifiers are words used to represent variables, functions, and other user-defined names. If an identifier is misspelled, the compiler will not be able to recognize it, and it will result in a lexical error.

2. **Unterminated Strings:** Strings are a sequence of characters enclosed in double-quotes. If a string is not properly terminated, i.e., the closing double-quote is missing, it will result in a lexical error.

3. **Invalid Characters:** If the source code contains characters that are not recognized by the compiler, it will result in a lexical error. For example, using a special character like "$" in an identifier name.

4. **Wrongly Placed Comments:** Comments are used to provide information about the code to make it more readable. If comments are not placed properly, it can result in a lexical error. For example, if a comment is not properly closed, it can cause the rest of the code to become a comment.

5. **Missing or Extra Spaces:** Whitespace is used to separate tokens in the source code. If there are missing or extra spaces, it can result in a lexical error. For example, if two identifiers are not separated by a space, the compiler will treat them as a single token, resulting in a lexical error.

6. **Missing or Extra Brackets:** Brackets are used to group expressions and define function arguments. If there are missing or extra brackets, it can result in a lexical error. For example, if a closing bracket is missing, the compiler will continue to scan the code until it finds one, resulting in a lexical error.

7. **Invalid Numeric Format:** If a numeric value is not in the correct format, it can result in a lexical error. For example, if a hexadecimal number is not prefixed with "0x", the compiler will not be able to recognize it, resulting in a lexical error.

These are some of the common lexical errors that can occur during the compilation process. As a programmer, it is essential to be careful when writing code and avoid these errors to ensure that the code compiles successfully.