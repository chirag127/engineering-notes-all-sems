Hello, I am Sydney, your AI assistant. I can help you with your topic.

### 1. Design and implement a lexical analyzer for given language using C and the lexical analyzer should ignore redundant spaces, tabs and new lines.

- A lexical analyzer is a program that takes a source code as input and produces a stream of tokens as output. Tokens are the smallest meaningful units of a language, such as keywords, identifiers, literals, operators, etc.
- A lexical analyzer can be implemented using C by following these steps:

  - Define the tokens and their regular expressions. For example, an identifier can be defined as a letter followed by zero or more letters or digits, and its regular expression can be `[a-zA-Z][a-zA-Z0-9]*`.
  - Write a function that reads the input character by character and matches it with the regular expressions of the tokens. If a match is found, the function returns the token and its value. If no match is found, the function reports an error. For example, the function can use a switch-case statement to check the first character of the input and then use if-else statements to check the rest of the characters.
  - Write a main function that calls the token-matching function repeatedly until the end of the input is reached. The main function should also ignore redundant spaces, tabs and new lines by skipping them before calling the token-matching function. For example, the main function can use a while loop to read the input and use the `isspace()` function from the `ctype.h` library to check if the character is a space, tab or new line.
  - Compile and run the program with a sample input and check the output.

- Here is a possible code for the lexical analyzer in C:

```c
#include <stdio.h>
#include <ctype.h>
#include <string.h>

// Define the tokens and their values
#define KEYWORD 1
#define IDENTIFIER 2
#define NUMBER 3
#define OPERATOR 4
#define DELIMITER 5
#define ERROR -1

// Define the keywords of the language
char *keywords[] = {"if", "else", "while", "for", "int", "float", "char", "return"};

// Define the operators of the language
char operators[] = "+-*/%=<>!&|";

// Define the delimiters of the language
char delimiters[] = "(),;{}";

// Define a structure for the token
typedef struct {
  int type; // The type of the token
  char value[20]; // The value of the token
} token;

// A function that reads the input and returns the next token
token getNextToken() {
  token t; // The token to be returned
  char c; // The current character of the input
  int i; // A loop variable

  // Initialize the token type and value
  t.type = ERROR;
  t.value[0] = '\0';

  // Read the next character of the input
  c = getchar();

  // If the end of the input is reached, return the token
  if (c == EOF) {
    return t;
  }

  // If the character is a space, tab or new line, ignore it and read the next character
  while (isspace(c)) {
    c = getchar();
  }

  // If the character is a letter, it can be a keyword or an identifier
  if (isalpha(c)) {
    // Append the character to the token value
    i = 0;
    t.value[i++] = c;

    // Read the next character and append it to the token value until it is not a letter or a digit
    c = getchar();
    while (isalnum(c)) {
      t.value[i++] = c;
      c = getchar();
    }

    // Terminate the token value with a null character
    t.value[i] = '\0';

    // Unread the last character that is not part of the token
    ungetc(c, stdin);

    // Check if the token value is a keyword
    for (i = 0; i < 8; i++) {
      if (strcmp(t.value, keywords[i]) == 0) {
        // Set the token type to keyword and return the token
        t.type = KEYWORD;
        return t;
      }
    }

    // If the token value is not a keyword, it is an identifier
    // Set the token type to identifier and return the token
    t.type = IDENTIFIER;
    return t;
  }

  // If the character is a digit, it can be a number
  if (isdigit(c)) {
    // Append the character to the token value