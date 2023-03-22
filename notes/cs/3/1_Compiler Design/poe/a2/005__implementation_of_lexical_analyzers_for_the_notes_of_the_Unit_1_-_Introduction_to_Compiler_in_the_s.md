 Here is the formal content in Markdown format without any emojis or external links for the topic - Implementation of Lexical Analyzers for the notes of Unit 1 - Introduction to Compiler of the subject Compiler Design:

### Implementation of Lexical Analyzers

1. Read the input source code character by character.
2. Identify the type of each character. The characters can be:
- Alphabets (A-Z, a-z)
- Digits (0-9)
- Special symbols ( (, ), {, }, [, ], ., ;, etc.)
- Whitespace (space, tab, newline, etc.)
- Operators (+, -, *, /, etc.)
3. Group the consecutive characters of the same type into a lexeme, also known as a token. For example, if the input is "x = y", it will form two lexemes - "x" and "= y".
4. Provide the lexeme as output along with the token type like identifier, operator, keyword, constant, etc.
5. Repeat the steps#1,#2,#3,#4 until there are no more input characters left.

The lexical analyzer plays an important role in the compiler as the compiler depends upon the tokens or lexemes output by the lexical analyzer to proceed for syntax analysis and further compilation phases. The lexical analyzer must be efficient enough to tokenize the source code at high speed and should handle errors like invalid input characters or symbols.

The above points cover the key steps involved in implementing a lexical analyzer for recognizing the basic tokens in a source code.