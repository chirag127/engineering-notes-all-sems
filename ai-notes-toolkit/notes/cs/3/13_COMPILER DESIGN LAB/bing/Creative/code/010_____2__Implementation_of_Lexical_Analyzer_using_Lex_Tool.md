### 2. Implementation of Lexical Analyzer using Lex Tool

- Lex is a tool used to generate a lexical analyzer .
- A lexical analyzer is a program that transforms an input stream of characters into a sequence of tokens .
- Tokens are the basic units of a source code, such as identifiers, keywords, operators, literals, etc.
- Lex takes a set of regular expressions as input from an input file and translates them into a C implementation of a corresponding finite state machine .
- A finite state machine is a mathematical model of computation that can recognize patterns in the input stream.
- Lex also provides some predefined functions and variables that can be used to perform actions on the tokens, such as printing, counting, storing, etc .
- The basic steps to implement a lexical analyzer using Lex are :

  - Write the regular expressions for the tokens in a file with .l extension.
  - Run the lex command on the file to generate a C source file called lex.yy.c.
  - Compile the C source file using a C compiler to generate an executable file.
  - Run the executable file on the input stream to produce the tokens as output.

- The general format of a Lex input file is  :

  ```
  %{ 
    /* C declarations and definitions */ 
  %} 
  %% 
    /* Rules: regular expressions and actions */ 
  %% 
    /* C code to be copied verbatim */ 
  ```

- The first section contains the C declarations and definitions that are needed for the lexical analyzer, such as header files, macros, variables, functions, etc  .
- The second section contains the rules that define the regular expressions for the tokens and the actions to be performed on them, such as printing, counting, storing, etc  .
- The third section contains the C code that is copied verbatim to the end of the generated C source file, such as the main function, the input and output functions, etc  .
- The rules section has the following format  :

  ```
  regular_expression { action }
  ```

- The regular expression is a pattern that matches a token in the input stream  .
- The action is a C code that is executed when the token is recognized  .
- The action can use some predefined variables and functions provided by Lex, such as  :

  - yytext: a pointer to the matched token as a string.
  - yyleng: the length of the matched token as an integer.
  - yyin: the input file pointer.
  - yyout: the output file pointer.
  - yylex(): the function that invokes the lexical analyzer.
  - yywrap(): the function that is called when the end of input is reached.

- The following is an example of a Lex input file that recognizes identifiers, keywords, operators, and numbers in a C program :

  ```
  %{ 
    #include <stdio.h> 
    #include <string.h> 
    int keywords = 0; 
    int identifiers = 0; 
    int operators = 0; 
    int numbers = 0; 
  %} 
  %% 
    "int"|"float"|"char"|"double" { keywords++; printf("Keyword: %s\n", yytext); } 
    [a-zA-Z][a-zA-Z0-9]* { identifiers++; printf("Identifier: %s\n", yytext); } 
    "+"|"-"|"*"|"/"|"=" { operators++; printf("Operator: %s\n", yytext); } 
    [0-9]+ { numbers++; printf("Number: %s\n", yytext); } 
    [ \t\n]+ { /* ignore whitespace */ } 
    . { printf("Invalid character: %s\n", yytext); } 
  %% 
    int main() { 
      printf("Enter a C program:\n"); 
      yylex

```
