### c) Implementation of Calculator using LEX and YACC

- LEX and YACC are tools that help in creating lexical analyzers and parsers for a given grammar.
- A lexical analyzer is a program that converts a stream of characters into a stream of tokens, such as numbers, operators, identifiers, etc.
- A parser is a program that analyzes the syntactic structure of a stream of tokens and checks if it conforms to a given grammar. It can also perform semantic actions, such as evaluation, translation, etc.
- A calculator is a simple example of an application that requires both lexical analysis and parsing. It can take an arithmetic expression as input and compute its value.
- To implement a calculator using LEX and YACC, we need to do the following steps:

  1. Define the tokens and the regular expressions that match them in the LEX file. For example, we can define tokens for numbers, operators, parentheses, etc.
  2. Define the grammar rules and the semantic actions for the arithmetic expressions in the YACC file. For example, we can define rules for addition, subtraction, multiplication, division, etc. and use the C operators to perform the calculations.
  3. Compile the LEX file using the lex command to generate a C source file that contains the lexical analyzer function.
  4. Compile the YACC file using the yacc command with the -d option to generate a C source file and a header file that contain the parser function and the token definitions.
  5. Compile and link the generated C files using the cc command to create an executable file that can run the calculator.
  6. Test the calculator by giving it some arithmetic expressions as input and checking the output.

- Here is an example of a LEX file that defines the tokens for a simple calculator:

```
%{
#include "y.tab.h"
%}

%%

[0-9]+  { yylval = atoi(yytext); return NUMBER; }
[ \t]   { /* ignore whitespace */ }
\n      { return 0; }
.       { return yytext[0]; }

%%
```

- Here is an example of a YACC file that defines the grammar rules and the semantic actions for a simple calculator:

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
    | exp '\n'  { printf("%d\n", $1); }
    ;

exp: NUMBER             { $$ = $1; }
   | exp '+' exp        { $$ = $1 + $3; }
   | exp '-' exp        { $$ = $1 - $3; }
   | exp '*' exp        { $$ = $1 * $3; }
   | exp '/' exp        { $$ = $1 / $3; }
   | '(' exp ')'        { $$ = $2; }
   ;

%%

extern int yylex();
extern int yyparse();
extern FILE *yyin;

int main() {
  yyin = stdin;

  do {
    yyparse();
  } while (!feof(yyin));

  return 0;
}

void yyerror(char *s) {
  fprintf(stderr, "%s\n", s);
}
```

- Here is an example of how to compile and run the calculator:

```
$ lex calc.l
$ yacc -d calc.y
$ cc y.tab.c lex.yy.c -o calc
$ ./calc
2+3
5
(4*5)-6
14
7/0
Division by zero
```