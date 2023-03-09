### c) Implementation of Calculator using LEX and YACC

Lex and YACC are tools that can be used to generate programs that can recognize and process specific patterns in text. These tools are often used together to create simple programming languages or calculators.

Here are the steps to implement a calculator using Lex and YACC:

1. Define the grammar: The first step is to define the grammar for the calculator language. This can be done using Backus-Naur Form (BNF) notation. For example, the grammar for a simple calculator might be:

    ```
    expr: term
        | expr '+' term
        | expr '-' term
    term: factor
        | term '*' factor
        | term '/' factor
    factor: NUMBER
        | '(' expr ')'
    ```

2. Write the Lex file: The next step is to write the Lex file. This file defines the patterns that the calculator program will recognize. For example, the Lex file for the above grammar might look like this:

    ```
    %{
    #include "y.tab.h"
    %}
    
    %%
    
    [0-9]+      { yylval = atoi(yytext); return NUMBER; }
    [\+\-\*\/]  { return yytext[0]; }
    [\(\)]      { return yytext[0]; }
    [\t\n]      { /* ignore whitespace */ }
    .           { printf("Invalid character: %c\n", *yytext); }
    
    %%
    ```

3. Write the YACC file: The final step is to write the YACC file. This file defines the actions that the calculator program will take when it recognizes a pattern. For example, the YACC file for the above grammar might look like this:

    ```
    %{
    #include <stdio.h>
    %}
    
    %token NUMBER
    
    %%
    
    expr:   term
            | expr '+' term  { printf("%d\n", $1 + $3); }
            | expr '-' term  { printf("%d\n", $1 - $3); }
    
    term:   factor
            | term '*' factor    { printf("%d\n", $1 * $3); }
            | term '/' factor    { printf("%d\n", $1 / $3); }
    
    factor: NUMBER            { $$ = $1; }
            | '(' expr ')'    { $$ = $2; }
    
    %%
    
    int main() {
        yyparse();
        return 0;
    }
    ```

Advantages of using Lex and YACC:

- Allows for the creation of custom programming languages or calculators.
- Can be used to create programs that are easy to read and maintain.
- Provides a way to separate the recognition of patterns from the actions taken when a pattern is recognized.

Disadvantages of using Lex and YACC:

- Requires knowledge of BNF notation.
- Can be time-consuming to set up and learn.
- May not be suitable for large and complex programs.

Example:

Suppose we want to implement a calculator that can handle basic arithmetic operations. We can use Lex and YACC to create a program that recognizes patterns like "2+3" and "4*5" and performs the appropriate calculations.

Application:

Lex and YACC can be used in a variety of applications, including:

- Creating custom programming languages
- Writing parsers for configuration files
- Developing compilers for other programming languages