Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on how to convert BNF rules into YACC form and write code to generate abstract syntax tree.

- BNF (Backus-Naur form) is a notation for describing the syntax of a language using production rules. Each rule consists of a non-terminal symbol on the left-hand side and a sequence of terminal and non-terminal symbols on the right-hand side. For example, the rule `expr -> expr + term` means that an expression can be formed by adding a term to another expression.
- YACC (Yet Another Compiler-Compiler) is a tool that generates a parser from a grammar specification in BNF form. The grammar specification consists of three sections: definitions, rules, and user code. The definitions section contains declarations of tokens, variables, and other elements. The rules section contains the BNF rules with optional semantic actions enclosed in curly braces. The user code section contains any additional C code that is needed for the parser. For example, the following is a YACC specification for a simple calculator:

```
%{
#include <stdio.h>
#include <stdlib.h>
%}

%token NUMBER
%left '+' '-'
%left '*' '/'

%%

expr: expr '+' expr { printf("%d\n", $1 + $3); }
    | expr '-' expr { printf("%d\n", $1 - $3); }
    | expr '*' expr { printf("%d\n", $1 * $3); }
    | expr '/' expr { printf("%d\n", $1 / $3); }
    | NUMBER        { $$ = $1; }
    ;

%%

int main() {
  yyparse();
  return 0;
}

int yyerror(char *s) {
  fprintf(stderr, "%s\n", s);
  return 0;
}
```

- An abstract syntax tree (AST) is a data structure that represents the syntactic structure and meaning of a program or expression. It is composed of nodes that correspond to syntactic constructs, such as operators, operands, statements, declarations, etc. Each node has a type and a value, and may have zero or more children nodes. For example, the expression `2 + 3 * 4` can be represented by the following AST:

```
    +
   / \
  2   *
     / \
    3   4
```

- To generate an AST from a YACC specification, one needs to modify the semantic actions to create and link the nodes of the tree. This can be done by using a function that allocates a new node and assigns its type, value, and children. For example, the following is a modified YACC specification for the calculator that generates an AST:

```
%{
#include <stdio.h>
#include <stdlib.h>

typedef struct node {
  int type;
  int value;
  struct node *left;
  struct node *right;
} node;

node *new_node(int type, int value, node *left, node *right) {
  node *n = malloc(sizeof(node));
  n->type = type;
  n->value = value;
  n->left = left;
  n->right = right;
  return n;
}

#define PLUS 1
#define MINUS 2
#define TIMES 3
#define DIVIDE 4
#define NUMBER 5

%}

%token NUMBER
%left '+' '-'
%left '*' '/'

%%

expr: expr '+' expr { $$ = new_node(PLUS, 0, $1, $3); }
    | expr '-' expr { $$ = new_node(MINUS, 0, $1, $3); }
    | expr '*' expr { $$ = new_node(TIMES, 0, $1, $3); }
    | expr '/' expr { $$ = new_node(DIVIDE, 0, $1, $3); }
    | NUMBER        { $$ = new_node(NUMBER, $1, NULL, NULL); }
    ;

%%

int main() {
  node *root = NULL;
  yyparse();
  root = yylval; // the root of the AST is the last value returned by the parser
  print_tree(root); // a function that prints the AST in a readable format
  return 0;
}

int yyerror(char *s) {
  fprintf(stderr, "%s\n", s);
  return 0;
}
```

I hope this helps you understand how to convert BNF rules into YACC form and write code to generate abstract syntax tree.