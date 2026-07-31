### 1. Design and implement a lexical analyzer for given language using C and the lexical analyzer should ignore redundant

- A lexical analyzer is a program that takes a source code as input and produces a stream of tokens as output.
- A token is a meaningful unit of the source code, such as a keyword, an identifier, a constant, an operator, or a delimiter.
- A lexical analyzer should ignore redundant parts of the source code, such as comments, whitespaces, and newlines, as they do not affect the meaning of the program.
- To design and implement a lexical analyzer for a given language using C, the following steps can be followed:

  - Define the tokens and their patterns for the given language. For example, if the language has keywords like `if`, `else`, `while`, etc., then the pattern for a keyword token can be a sequence of alphabetic characters that matches one of the keywords. Similarly, the patterns for other tokens can be defined using regular expressions or finite automata.
  - Write a C program that reads the source code from a file or standard input and uses a buffer to store the characters.
  - Implement a function that scans the buffer and recognizes the tokens based on their patterns. The function should return the next token and its type, and update the buffer pointer accordingly. The function should also ignore the redundant characters and handle errors such as invalid tokens or end of file.
  - Implement a main function that calls the scanning function repeatedly and prints the tokens and their types until the end of file is reached or an error occurs.

- An example of a lexical analyzer for a simple language that has keywords, identifiers, integers, operators, and parentheses is given below:

```c
// Define the token types
#define KEYWORD 1
#define IDENTIFIER 2
#define INTEGER 3
#define OPERATOR 4
#define PARENTHESIS 5
#define END_OF_FILE 6
#define ERROR 7

// Define the keywords
char *keywords[] = {"if", "else", "while", "return"};

// Define the operators
char operators[] = "+-*/=";

// Define the parentheses
char parentheses[] = "()";

// Define the buffer size
#define BUFFER_SIZE 256

// Declare the buffer and the buffer pointer
char buffer[BUFFER_SIZE];
int buffer_ptr = 0;

// Declare the token and the token type
char token[BUFFER_SIZE];
int token_type;

// Declare the file pointer
FILE *fp;

// Function to read the next character from the buffer
char get_char() {
  // If the buffer pointer is at the end of the buffer, fill the buffer with new characters from the file
  if (buffer_ptr == BUFFER_SIZE || buffer_ptr == -1) {
    buffer_ptr = 0;
    int n = fread(buffer, sizeof(char), BUFFER_SIZE, fp);
    // If the end of file is reached, return '\0'
    if (n == 0) {
      return '\0';
    }
  }
  // Return the next character from the buffer and increment the buffer pointer
  return buffer[buffer_ptr++];
}

// Function to return the current character from the buffer
char peek_char() {
  // If the buffer pointer is at the end of the buffer, fill the buffer with new characters from the file
  if (buffer_ptr == BUFFER_SIZE || buffer_ptr == -1) {
    buffer_ptr = 0;
    int n = fread(buffer, sizeof(char), BUFFER_SIZE, fp);
    // If the end of file is reached, return '\0'
    if (n == 0) {
      return '\0';
    }
  }
  // Return the current character from the buffer without incrementing the buffer pointer
  return buffer[buffer_ptr];
}

// Function to check if a character is a letter
int is_letter(char c) {
  return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z');
}

// Function to check if a character is a digit
int is_digit(char c) {
  return c >= '0' && c <= '9';
}

// Function to check if a character is an operator
int is_operator(char c) {
  for (int i = 0; i < sizeof(operators); i++) {
    if (c == operators[i]) {
      return 1;
    }
  }
  return 0;
}

// Function to check if a character is a parenthesis
int is_parenthesis(char c) {
  for (int i = 0; i < sizeof(parentheses); i++) {
    if (c == parentheses[i]) {
      return 1;
    }
  }
  return 0;
}

// Function

```
