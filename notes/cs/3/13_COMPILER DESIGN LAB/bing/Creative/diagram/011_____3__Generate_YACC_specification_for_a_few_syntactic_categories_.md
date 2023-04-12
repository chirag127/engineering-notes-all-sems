### 3. Generate YACC specification for a few syntactic categories.

YACC stands for Yet Another Compiler Compiler. It is a tool that generates a parser for a given grammar. A parser is a program that analyzes the syntactic structure of a given input and checks if it conforms to the rules of the grammar. A grammar is a set of rules that define the syntax of a language.

A YACC specification consists of three parts: declarations, rules, and user subroutines. The declarations part contains the definitions of tokens, variables, and other information that are used in the rules part. The rules part contains the grammar rules that specify how the tokens can be combined to form syntactic categories. The user subroutines part contains the code that is executed when a rule is matched.

A syntactic category is a group of tokens that can function as a unit in a sentence. For example, a noun phrase is a syntactic category that can act as a subject or an object of a verb. A verb phrase is a syntactic category that can express an action or a state of being.

To generate a YACC specification for a few syntactic categories, we need to follow these steps:

- Define the tokens that are used in the language. For example, we can use the following tokens: ID (identifier), NUM (number), PLUS (+), MINUS (-), MUL (*), DIV (/), LPAREN ((), RPAREN ()), SEMI (;), ASSIGN (=), IF, THEN, ELSE, WHILE, DO, BEGIN, END.
- Define the precedence and associativity of the operators. For example, we can use the following declarations:

```
%token ID NUM
%token PLUS MINUS
%token MUL DIV
%token LPAREN RPAREN
%token SEMI ASSIGN
%token IF THEN ELSE WHILE DO BEGIN END
%left PLUS MINUS
%left MUL DIV
```

- Define the rules for the syntactic categories. For example, we can use the following rules:

```
program: stmt_list
       ;

stmt_list: stmt
        | stmt_list SEMI stmt
        ;

stmt: assign_stmt
    | if_stmt
    | while_stmt
    | compound_stmt
    ;

assign_stmt: ID ASSIGN expr
           ;

if_stmt: IF expr THEN stmt
       | IF expr THEN stmt ELSE stmt
       ;

while_stmt: WHILE expr DO stmt
          ;

compound_stmt: BEGIN stmt_list END
             ;

expr: term
    | expr PLUS term
    | expr MINUS term
    ;

term: factor
    | term MUL factor
    | term DIV factor
    ;

factor: ID
      | NUM
      | LPAREN expr RPAREN
      ;
```

- Define the user subroutines that are executed when a rule is matched. For example, we can use the following code:

```
#include <stdio.h>
#include <stdlib.h>
int yylex();
void yyerror(char *s);

int main()
{
  yyparse();
  return 0;
}

void yyerror(char *s)
{
  fprintf(stderr, "Error: %s\n", s);
  exit(1);
}
```

- Save the YACC specification in a file with the extension .y. For example, we can save it as syntax.y.
- Run the YACC tool on the file to generate the parser. For example, we can use the following command:

```
yacc -d syntax.y
```

- This will generate two files: y.tab.c and y.tab.h. The y.tab.c file contains the C code for the parser, and the y.tab.h file contains the definitions of the tokens and the syntactic categories.
- Compile the y.tab.c file with a C compiler. For example, we can use the following command:

```
gcc y.tab.c -o syntax
```

- This will generate an executable file called syntax, which is the parser for the language.
- Run the parser on an input file that contains the source code of the language. For example, we can use the following input file:

```
a = 10;
b = 20;
if (a > b) then
  c = a - b;
else
  c = b - a;
end
```

- To run the parser on this file, we can use the following command:

```
./syntax < input.txt
```

- If the input file is syntactically correct, the parser will accept it and terminate normally. If the input file is syntactically incorrect, the parser will report an error and exit. For example, if we change the input file to:

```
a = 10;
b = 20;
if (a >

```
