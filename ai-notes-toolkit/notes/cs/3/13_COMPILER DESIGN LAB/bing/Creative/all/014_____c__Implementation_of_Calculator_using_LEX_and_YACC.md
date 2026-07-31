# c) Implementation of Calculator using LEX and YACC

- LEX and YACC are tools that help in creating lexical analyzers and parsers for a given grammar.
- A lexical analyzer is a program that converts a stream of characters into a stream of tokens, such as numbers, operators, identifiers, etc.
- A parser is a program that analyzes the syntactic structure of a stream of tokens and checks if it conforms to a given grammar. A grammar is a set of rules that define the syntax of a language.
- A calculator is an example of a program that can be implemented using LEX and YACC. A calculator can perform arithmetic operations on numbers and evaluate expressions.
- To implement a calculator using LEX and YACC, we need to do the following steps:

  - Define the tokens and the regular expressions that match them in a LEX file. For example, we can define tokens for numbers, operators, parentheses, etc.
  - Define the grammar and the actions that are executed when a rule is matched in a YACC file. For example, we can define rules for expressions, terms, factors, etc. and use the actions to perform the calculations and store the results in a variable.
  - Compile the LEX and YACC files using the commands `lex` and `yacc` to generate the C source code for the lexical analyzer and the parser.
  - Compile the C source code using a C compiler and link it with the library `libfl.a` to create the executable file for the calculator.
  - Run the executable file and enter the expressions to be evaluated by the calculator.

- Here is an example of a LEX file for a simple calculator that can handle integers, addition, subtraction, multiplication, and division:

  ```
  %{
  #include "y.tab.h"
  %}

  %%
  [0-9]+  { yylval = atoi(yytext); return NUMBER; }
  [ \t\n] { /* ignore whitespace */ }
  [-+*/()] { return *yytext; }
  . { printf("Invalid character: %s\n", yytext); exit(1); }
  %%
  ```

- Here is an example of a YACC file for a simple calculator that can handle integers, addition, subtraction, multiplication, and division:

  ```
  %{
  #include <stdio.h>
  %}

  %token NUMBER

  %left '+' '-'
  %left '*' '/'

  %%

  expr: expr '+' expr { $$ = $1 + $3; }
      | expr '-' expr { $$ = $1 - $3; }
      | expr '*' expr { $$ = $1 * $3; }
      | expr '/' expr { $$ = $1 / $3; }
      | '(' expr ')' { $$ = $2; }
      | NUMBER { $$ = $1; }
      ;

  %%

  int main() {
    printf("Enter an expression: ");
    yyparse();
    return 0;
  }

  int yyerror(char *s) {
    printf("Error: %s\n", s);
    return 0;
  }
  ```

- To compile and run the calculator, we can use the following commands:

  ```
  lex calc.l
  yacc -d calc.y
  cc y.tab.c -lfl -o calc
  ./calc
  ```