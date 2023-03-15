### Implementation of Lexical Analyzers

- Lexical analysis is the first phase of a compiler, where the input source code is scanned and divided into a sequence of tokens.
- A token is a unit of information that represents a lexeme, which is a meaningful string of characters in the source code.
- A lexical analyzer is a program that implements the process of lexical analysis, by reading the input characters and producing the output tokens.
- A lexical analyzer can be implemented using various techniques, such as finite automata, regular expressions, transition diagrams, etc.
- The main tasks of a lexical analyzer are :
  - To remove whitespace and comments from the input source code.
  - To identify the lexemes that match the patterns of tokens defined by the syntax of the language.
  - To assign attributes and codes to the tokens, and store them in a symbol table.
  - To report any lexical errors, such as invalid characters or identifiers, that are encountered during the scanning process.
  - To pass the tokens to the next phase of the compiler, which is the syntax analysis or parsing.