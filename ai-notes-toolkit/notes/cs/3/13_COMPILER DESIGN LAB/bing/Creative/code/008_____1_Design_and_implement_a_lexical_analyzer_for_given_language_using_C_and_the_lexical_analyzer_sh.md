Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some content in markdown format that you can use for your study material.

### 1. Design and implement a lexical analyzer for given language using C and the lexical analyzer should ignore redundant spaces, tabs and new lines.

- A lexical analyzer is a program that reads the source code of a given language and converts it into a sequence of tokens, which are the basic units of meaning in the language.
- A token can be a keyword, an identifier, a constant, an operator, a delimiter, or a comment.
- A lexical analyzer can be implemented using C by following these steps:

  - Define the structure of a token, which should contain the type and the value of the token.
  - Define the regular expressions or patterns for each type of token, using characters, metacharacters, and operators.
  - Define a buffer to store the input source code and a pointer to scan the buffer character by character.
  - Define a function to get the next character from the buffer and update the pointer.
  - Define a function to unget the last character from the buffer and decrement the pointer.
  - Define a function to skip the redundant spaces, tabs and new lines from the buffer by calling the get and unget functions.
  - Define a function to get the next token from the buffer by matching the patterns with the characters and returning the token structure.
  - Define a main function to open the source code file, read it into the buffer, and call the get token function repeatedly until the end of file is reached or an error occurs.

- Here is an example of a lexical analyzer for a simple language that has four keywords (if, else, while, and print), identifiers (starting with a letter and followed by zero or more letters or digits), integers (one or more digits), operators (+, -, *, /, =, <, >, and ==), delimiters (, ; ( ) { and }), and comments (starting and ending with #).

```c
// Define the token types
#define KEYWORD 1
#define IDENTIFIER 2
#define INTEGER 3
#define OPERATOR 4
#define DELIMITER 5
#define COMMENT 6
#define END_OF_FILE 7
#define ERROR 8

// Define the token structure
typedef struct {
  int type; // The type of the token
  char* value; // The value of the token
} token;

// Define the patterns for each type of token
char* keywords[] = {"if", "else", "while", "print"};
char* operators[] = {"+", "-", "*", "/", "=", "<", ">", "=="};
char* delimiters[] = {",", ";", "(", ")", "{", "}"};

// Define the buffer and the pointer
char* buffer;
int pointer;

// Define the function to get the next character from the buffer
char get_char() {
  return buffer[pointer++];
}

// Define the function to unget the last character from the buffer
void unget_char() {
  pointer--;
}

// Define the function to skip the redundant spaces, tabs and new lines
void skip_spaces() {
  char c;
  while ((c = get_char()) == ' ' || c == '\t' || c == '\n');
  unget_char();
}

// Define the function to get the next token from the buffer
token get_token() {
  token t; // The token to return
  char c; // The current character
  int i; // The loop index
  int len; // The length of the token value
  char* temp; // The temporary string to store the token value

  skip_spaces(); // Skip the redundant spaces, tabs and new lines

  c = get_char(); // Get the next character

  if (c == '\0') { // If the end of file is reached
    t.type = END_OF_FILE; // Set the token type to end of file
    t.value = NULL; // Set the token value to null
    return t; // Return the token
  }

  if (isalpha(c)) { // If the character is a letter
    len = 0; // Initialize the length to zero
    temp = (char*) malloc(sizeof(char)); // Allocate memory for the temporary string
    temp[len++] = c; // Append the character to the temporary string
    while (isalnum(c = get_char())) { // While the character is a letter or a digit
      temp = (char*) realloc(temp, (len + 1) * sizeof(char)); // Reallocate memory for the temporary string
      temp[len++] = c; // Append the character to the

```
