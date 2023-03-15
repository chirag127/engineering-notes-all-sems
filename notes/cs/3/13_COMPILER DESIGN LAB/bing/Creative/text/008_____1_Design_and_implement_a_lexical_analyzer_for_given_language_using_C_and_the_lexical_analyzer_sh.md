Hello, I am Sydney, your AI assistant. I can help you with your topic.

### 1. Design and implement a lexical analyzer for given language using C and the lexical analyzer should ignore redundant spaces, tabs and new lines.

- A lexical analyzer is a program that reads the source code of a given language and converts it into a sequence of tokens, which are the smallest meaningful units of the language, such as keywords, identifiers, literals, operators, etc.
- A lexical analyzer can be implemented using C by following these steps:

  - Define the tokens and their regular expressions that represent the patterns of the language. For example, an identifier can be defined as a letter followed by zero or more letters or digits, and its regular expression can be `[a-zA-Z][a-zA-Z0-9]*`.
  - Write a function that reads the next character from the input stream and returns it. This function should also keep track of the current line number and column number for error reporting.
  - Write a function that unreads the last character read from the input stream and restores the previous line number and column number. This function is useful when the lexical analyzer needs to look ahead one character to decide the type of the token.
  - Write a function that skips the redundant spaces, tabs and new lines from the input stream by repeatedly calling the read function until a non-whitespace character is encountered. This function should also update the line number and column number accordingly.
  - Write a function that matches a given regular expression with the input stream by using a finite state machine or a table-driven approach. This function should return a boolean value indicating whether the match was successful or not, and also the lexeme or the string that matched the regular expression.
  - Write a function that returns the next token from the input stream by calling the skip function and then the match function for each token type in a predefined order. This function should also assign a token code and a token value to the token, and handle any lexical errors that may occur.
  - Write a main function that creates an input stream from a file or a standard input, and then calls the token function in a loop until the end of the file or an error is encountered. This function should also print the tokens and their attributes to a file or a standard output, and report any errors or warnings.