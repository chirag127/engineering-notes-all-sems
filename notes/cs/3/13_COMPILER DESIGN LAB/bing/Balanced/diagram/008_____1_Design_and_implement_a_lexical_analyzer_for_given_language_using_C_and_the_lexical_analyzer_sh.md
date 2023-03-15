Hello, I am Sydney, your AI assistant. I can help you with your topic.

### 1. Design and implement a lexical analyzer for given language using C and the lexical analyzer should ignore redundant spaces, tabs and new lines.

- A lexical analyzer is a program that takes a source code as input and produces a stream of tokens as output. Tokens are the smallest meaningful units of a language, such as keywords, identifiers, literals, operators, etc.
- A lexical analyzer can be implemented using C by following these steps:

  - Define the tokens and their regular expressions. For example, an identifier can be defined as a letter followed by zero or more letters or digits, and its regular expression can be `[a-zA-Z][a-zA-Z0-9]*`.
  - Write a function that reads the input character by character and matches it with the regular expressions of the tokens. If a match is found, the function returns the token and its value. If no match is found, the function reports an error.
  - Write a main function that calls the token-matching function repeatedly until the end of the input is reached. The main function should also ignore redundant spaces, tabs and new lines by skipping them in the input.
  - Compile and run the program with a sample input and check the output.

- Here is a possible code for the lexical analyzer in C:

```c
#include <stdio.h>
#include <ctype.h>
#include <string.h>

// Define the token types
#define KEYWORD 1
#define IDENTIFIER 2
#define NUMBER 3
#define OPERATOR 4
#define DELIMITER 5
#define ERROR -1

// Define the keywords
char *keywords[] = {"int", "float", "char", "if", "else", "while", "return"};

// Define the operators
char operators[] = "+-*/=><!";

// Define the delimiters
char delimiters[] = "(),;{}";

// Define a structure for tokens
typedef struct {
  int type; // The token type
  char value[20]; // The token value
} token;

// A function that returns the next token from the input
token getNextToken() {
  token t; // The token to be returned
  char c; // The current character
  int i; // A loop variable

  // Initialize the token type and value
  t.type = ERROR;
  t.value[0] = '\0';

  // Skip the redundant spaces, tabs and new lines
  while ((c = getchar()) != EOF && (c == ' ' || c == '\t' || c == '\n'));

  // If the end of the file is reached, return an empty token
  if (c == EOF) return t;

  // If the current character is a letter, it can be a keyword or an identifier
  if (isalpha(c)) {
    i = 0; // Initialize the index for the token value
    // Append the current character to the token value
    t.value[i++] = c;
    // Read the next characters until a non-letter or non-digit is found
    while ((c = getchar()) != EOF && (isalpha(c) || isdigit(c))) {
      // Append the current character to the token value
      t.value[i++] = c;
    }
    // Terminate the token value with a null character
    t.value[i] = '\0';
    // Push back the last character to the input stream
    ungetc(c, stdin);
    // Check if the token value is a keyword
    for (i = 0; i < 7; i++) {
      if (strcmp(t.value, keywords[i]) == 0) {
        // Set the token type to keyword and return the token
        t.type = KEYWORD;
        return t;
      }
    }
    // If not a keyword, set the token type to identifier and return the token
    t.type = IDENTIFIER;
    return t;
  }

  // If the current character is a digit, it can be a number
  if (isdigit(c)) {
    i = 0; // Initialize the index for the token value
    // Append the current character to the token value
    t.value[i++] = c;
    // Read the next characters until a non-digit is found
    while ((c = getchar()) != EOF && isdigit(c)) {
      // Append the current character to the token value
      t.value[i++] = c;
    }
    // Terminate the token value with a null character
    t.value[i] = '\0';
    // Push back the last character to the input stream
    ungetc(c, stdin);
    // Set the