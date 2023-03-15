### 3. Generate YACC specification for a few syntactic categories.

- YACC stands for Yet Another Compiler-Compiler, which is a tool that generates a parser for a given grammar.
- A parser is a program that analyzes the syntactic structure of a given input, usually a source code of a programming language, and checks if it conforms to the rules of the grammar.
- A grammar is a set of rules that define the syntax of a language, i.e., how the symbols and words of the language can be combined to form valid sentences or expressions.
- A syntactic category is a group of symbols or words that can be used interchangeably in a given context, such as a noun, a verb, an expression, a statement, etc.
- A YACC specification consists of three sections: declarations, rules, and user subroutines.
- The declarations section defines the tokens, the start symbol, and the precedence and associativity of operators.
- The rules section defines the production rules of the grammar, i.e., how each non-terminal symbol can be derived from a sequence of terminal and non-terminal symbols.
- The user subroutines section contains the C code that is executed when a rule is matched by the parser, such as semantic actions, error handling, etc.
- Here are some examples of YACC specifications for a few syntactic categories:

```yacc
/* A YACC specification for arithmetic expressions */

%token NUM
%left '+' '-'
%left '*' '/'

%%

expr: expr '+' expr { printf("%d\n", $1 + $3); }
    | expr '-' expr { printf("%d\n", $1 - $3); }
    | expr '*' expr { printf("%d\n", $1 * $3); }
    | expr '/' expr { printf("%d\n", $1 / $3); }
    | '(' expr ')'   { $$ = $2; }
    | NUM            { $$ = $1; }
    ;

%%
```

```yacc
/* A YACC specification for boolean expressions */

%token TRUE FALSE AND OR NOT

%%

bool: bool AND bool { $$ = $1 && $3; }
    | bool OR bool  { $$ = $1 || $3; }
    | NOT bool      { $$ = !$2; }
    | '(' bool ')'  { $$ = $2; }
    | TRUE          { $$ = 1; }
    | FALSE         { $$ = 0; }
    ;

%%
```

```yacc
/* A YACC specification for assignment statements */

%token ID ASSIGN SEMI

%%

stmt: ID ASSIGN expr SEMI { printf("%s = %d\n", $1, $3); }
    ;

expr: expr '+' expr { $$ = $1 + $3; }
    | expr '-' expr { $$ = $1 - $3; }
    | expr '*' expr { $$ = $1 * $3; }
    | expr '/' expr { $$ = $1 / $3; }
    | '(' expr ')'  { $$ = $2; }
    | NUM           { $$ = $1; }
    ;

%%
```