### 2. Implementation of Lexical Analyzer using Lex Tool

- Lex is a tool that generates lexical analyzers or scanners.
- A lexical analyzer is a program that reads an input stream of characters and produces an output stream of tokens or symbols.
- Lex is commonly used with another tool called Yacc, which generates parsers or syntax analyzers.
- Lex and Yacc are widely used for implementing compilers, interpreters, and other language processing applications.

- The basic steps for using Lex are:

  - Write a specification file that defines the rules for tokenizing the input. The file has three sections: definitions, rules, and user subroutines.
  - Run the Lex tool on the specification file to generate a C source file called lex.yy.c, which contains the lexical analyzer function yylex().
  - Compile and link the C source file with the user subroutines and the Lex library to produce an executable program.

- The specification file has the following format:

  - %{ /* C code to be copied verbatim */ %}
  - definitions
  - %%
  - rules
  - %%
  - user subroutines

- The definitions section contains declarations of variables, macros, and regular expressions that are used in the rules section.
- The rules section contains pairs of patterns and actions that specify how to recognize and process tokens. A pattern is a regular expression that matches a sequence of characters in the input. An action is a C code fragment that is executed when the pattern is matched. The action can use the global variable yytext to access the matched text, and the global variable yyleng to access its length.
- The user subroutines section contains C functions that are called by the actions or the main function. The main function usually calls yylex() in a loop to scan the input and perform the desired tasks.

- An example of a Lex specification file that recognizes identifiers, keywords, numbers, and operators in a simple language is:

  - %{ /* definitions section */
  - #include <stdio.h>
  - #include <stdlib.h>
  - %}
  - /* regular expressions */
  - letter [A-Za-z]
  - digit [0-9]
  - id {letter}({letter}|{digit})*
  - number {digit}+(\.{digit}+)?(E[+-]?{digit}+)?
  - %%
  - /* rules section */
  - "if"|"else"|"while"|"for"|"return" { printf("Keyword: %s\n", yytext); }
  - {id} { printf("Identifier: %s\n", yytext); }
  - {number} { printf("Number: %s\n", yytext); }
  - "+"|"-"|"*"|"/"|"="|"=="|"!="|"<"|">"|"<="|">=" { printf("Operator: %s\n", yytext); }
  - [ \t\n]+ { /* ignore whitespace */ }
  - . { printf("Invalid character: %c\n", yytext[0]); }
  - %%
  - /* user subroutines section */
  - int main() {
  -   yylex(); /* call the scanner */
  -   return 0;
  - }