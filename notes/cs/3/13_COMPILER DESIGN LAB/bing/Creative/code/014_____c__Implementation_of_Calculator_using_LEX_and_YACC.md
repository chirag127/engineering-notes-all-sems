### c) Implementation of Calculator using LEX and YACC

- LEX and YACC are tools that help in creating lexical analyzers and parsers for a given grammar.
- A lexical analyzer is a program that converts a stream of characters into a stream of tokens, such as numbers, operators, identifiers, etc.
- A parser is a program that analyzes the syntactic structure of a stream of tokens and checks if it conforms to a given grammar. It can also perform semantic actions, such as evaluation, translation, etc.
- A calculator is a simple example of a program that can be implemented using LEX and YACC.
- The steps to implement a calculator using LEX and YACC are:

  1. Define the tokens and the grammar for the calculator. The tokens can be numbers, operators, parentheses, etc. The grammar can be a set of rules that define how expressions are formed and evaluated. For example, a possible grammar for a calculator is:

     ```
     expr: expr '+' term
         | expr '-' term
         | term
         ;

     term: term '*' factor
         | term '/' factor
         | factor
         ;

     factor: '(' expr ')'
           | NUMBER
           ;
     ```

     This grammar defines an expression as a sum or difference of terms, a term as a product or quotient of factors, and a factor as a number or a parenthesized expression. The grammar also specifies the precedence and associativity of the operators.

  2. Write a LEX file that defines the tokens and the regular expressions that match them. The LEX file also specifies the actions to be performed when a token is recognized, such as returning the token type and value to the parser. For example, a possible LEX file for a calculator is:

     ```
     %{
     #include "y.tab.h"
     %}

     DIGIT [0-9]
     NUMBER {DIGIT}+(\.{DIGIT}+)?

     %%

     {NUMBER} { yylval = atof(yytext); return NUMBER; }
     "+"      { return '+'; }
     "-"      { return '-'; }
     "*"      { return '*'; }
     "/"      { return '/'; }
     "("      { return '('; }
     ")"      { return ')'; }
     "\n"     { return '\n'; }
     [ \t]    { /* ignore whitespace */ }
     .        { /* ignore other characters */ }

     %%

     int yywrap() {
       return 1;
     }
     ```

     This LEX file defines two patterns: DIGIT and NUMBER. The pattern DIGIT matches a single digit, and the pattern NUMBER matches a number that consists of one or more digits, optionally followed by a decimal point and one or more digits. The LEX file also defines the actions to be performed when a token is recognized. For example, when a NUMBER token is recognized, the action is to convert the string yytext into a floating-point value and store it in yylval, which is a global variable that holds the semantic value of the token. The action also returns the token type NUMBER to the parser. Similarly, when an operator or a parenthesis token is recognized, the action is to return the corresponding character as the token type to the parser. When a newline token is recognized, the action is to return the character '\n' as the token type to the parser. When a whitespace or any other character is recognized, the action is to ignore it.

  3. Write a YACC file that defines the grammar and the actions to be performed when a rule is reduced. The YACC file also specifies the token types and the semantic values that are expected from the lexical analyzer. For example, a possible YACC file for a calculator is:

     ```
     %{
     #include <stdio.h>
     #include <math.h>
     %}

     %token NUMBER

     %left '+' '-'
     %left '*' '/'

     %%

     expr: expr '+' term   { $$ = $1 + $3; }
         | expr '-' term   { $$ = $1 - $3; }
         | term            { $$ = $1; }
         ;

     term: term '*' factor { $$ = $1 * $3; }
         | term '/' factor { $$ = $1 / $3; }
         | factor          { $$ = $1; }
         ;

     factor: '(' expr ')'  { $$ = $2; }
           | NUMBER        { $$ = $1; }
           ;

     %%

     int main() {
       printf("Enter an

```
