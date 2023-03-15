### 3. Generate YACC specification for a few syntactic categories.

- YACC stands for Yet Another Compiler-Compiler, which is a tool that generates a parser for a given grammar.
- A parser is a program that analyzes the syntactic structure of a given input, usually a source code of a programming language, and checks if it conforms to the rules of the grammar.
- A grammar is a set of rules that define the syntax of a language, i.e., how the symbols and words of the language can be combined to form valid sentences or expressions.
- A YACC specification consists of three parts: declarations, rules, and user subroutines.
- Declarations are used to define the tokens, types, and variables used in the grammar.
- Rules are used to specify the production rules of the grammar, i.e., how a non-terminal symbol can be derived from a sequence of terminal and non-terminal symbols.
- User subroutines are used to provide additional code that can be executed during the parsing process, such as semantic actions, error handling, or output generation.
- A few examples of syntactic categories and their YACC specifications are:

  - Arithmetic expressions: These are expressions that involve numbers, operators, and parentheses, such as `2 + (3 * 4) - 5`. The YACC specification for this category is:

    ```
    %token NUM
    %left '-' '+'
    %left '*' '/'
    %%
    expr: NUM
        | expr '+' expr
        | expr '-' expr
        | expr '*' expr
        | expr '/' expr
        | '(' expr ')'
    ;
    %%
    ```

  - Boolean expressions: These are expressions that evaluate to either true or false, and involve logical operators, such as `a && b || !c`. The YACC specification for this category is:

    ```
    %token ID
    %left '||'
    %left '&&'
    %right '!'
    %%
    bool: ID
        | bool '||' bool
        | bool '&&' bool
        | '!' bool
        | '(' bool ')'
    ;
    %%
    ```

  - Assignment statements: These are statements that assign a value to a variable, such as `x = y + 1;`. The YACC specification for this category is:

    ```
    %token ID NUM ';'
    %left '-' '+'
    %left '*' '/'
    %%
    stmt: ID '=' expr ';'
    ;
    expr: NUM
        | ID
        | expr '+' expr
        | expr '-' expr
        | expr '*' expr
        | expr '/' expr
        | '(' expr ')'
    ;
    %%
    ```