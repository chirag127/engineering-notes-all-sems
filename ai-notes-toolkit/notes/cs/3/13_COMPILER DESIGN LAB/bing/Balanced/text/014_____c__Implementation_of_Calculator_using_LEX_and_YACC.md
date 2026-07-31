### c) Implementation of Calculator using LEX and YACC

- LEX and YACC are tools that help in creating lexical analyzers and parsers for a given grammar.
- A lexical analyzer scans the input stream and converts it into tokens, which are the basic units of syntax.
- A parser takes the tokens and checks if they follow the rules of the grammar, and builds a parse tree that represents the structure of the input.
- A calculator is a common example of an application that requires lexical analysis and parsing, as it needs to recognize valid arithmetic expressions and evaluate them.
- To implement a calculator using LEX and YACC, we need to do the following steps:

  - Define the tokens and the regular expressions that match them in the LEX file. For example, we can define tokens for numbers, operators, parentheses, etc.
  - Define the grammar rules and the actions that perform the calculations in the YACC file. For example, we can define rules for expressions, terms, factors, etc., and use the C language to implement the arithmetic operations.
  - Compile the LEX and YACC files using the commands `lex file.l` and `yacc file.y`, which will generate the C source files `lex.yy.c` and `y.tab.c`.
  - Compile and link the C source files using the command `cc lex.yy.c y.tab.c -o calc`, which will produce the executable file `calc`.
  - Run the executable file and enter the arithmetic expressions to be evaluated. For example, we can enter `2+3*4` and get the result `14`.

- Here is a sample LEX file for a simple calculator:

```
%{
#include "y.tab.h"
%}

%%

[0-9]+ { yylval = atoi(yytext); return NUMBER; }
[ \t] { /* ignore whitespace */ }
\n { return 0; }
. { return yytext[0]; }

%%

int yywrap(void) {
  return 1;
}
```

- Here is a sample YACC file for a simple calculator:

```
%{
#include <stdio.h>
%}

%token NUMBER

%%

input: /* empty */
     | input line
     ;

line: '\n'
    | exp '\n' { printf("%d\n", $1); }
    ;

exp: NUMBER { $$ = $1; }
   | exp '+' exp { $$ = $1 + $3; }
   | exp '-' exp { $$ = $1 - $3; }
   | exp '*' exp { $$ = $1 * $3; }
   | exp '/' exp { $$ = $1 / $3; }
   | '(' exp ')' { $$ = $2; }
   ;

%%

int main(void) {
  yyparse();
  return 0;
}

int yyerror(char *s) {
  fprintf(stderr, "error: %s\n", s);
  return 0;
}
```