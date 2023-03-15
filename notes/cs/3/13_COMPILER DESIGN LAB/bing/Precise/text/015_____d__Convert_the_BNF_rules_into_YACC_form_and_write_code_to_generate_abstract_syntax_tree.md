### d) Convert the BNF rules into YACC form and write code to generate abstract syntax tree

1. BNF (Backus-Naur Form) is a notation used to formally describe the syntax of programming languages, grammars, and other formal languages. It is used to define the structure of valid strings in a language.
2. YACC (Yet Another Compiler-Compiler) is a tool that generates a parser for a given grammar. It takes a grammar specification in BNF form as input and produces C code for a parser that recognizes valid strings according to the grammar.
3. To convert BNF rules into YACC form, the BNF rules must be rewritten in a format that is compatible with YACC. This involves replacing the BNF symbols with YACC symbols and making sure that the rules follow the YACC syntax.
4. Once the BNF rules have been converted into YACC form, the YACC tool can be used to generate a parser for the grammar. This parser can then be used to parse input strings and generate an abstract syntax tree (AST) for the input.
5. An abstract syntax tree is a tree representation of the structure of a program or other piece of code. It is used to represent the syntactic structure of the code in a way that is easy to manipulate and analyze.
6. To generate an AST using YACC, the YACC specification must include actions that are executed when a rule is matched. These actions can be used to construct the nodes of the AST and connect them to form the tree structure.
7. Here is an example of how BNF rules can be converted into YACC form and used to generate an AST:

```
BNF:
<expr> ::= <term> | <expr> "+" <term>
<term> ::= <factor> | <term> "*" <factor>
<factor> ::= <number> | "(" <expr> ")"

YACC:
%{
#include <stdio.h>
#include "y.tab.h"
typedef struct node {
    char *token;
    struct node *left;
    struct node *right;
} node;
node *mknode(char *token, node *left, node *right);
void printtree(node *tree);
%}
%union {
    node *n;
}
%token NUMBER
%type <n> expr term factor
%%
expr: term { $$ = $1; }
    | expr '+' term { $$ = mknode("+", $1, $3); }
    ;
term: factor { $$ = $1; }
    | term '*' factor { $$ = mknode("*", $1, $3); }
    ;
factor: NUMBER { $$ = mknode(yytext, NULL, NULL); }
    | '(' expr ')' { $$ = $2; }
    ;
%%
node *mknode(char *token, node *left, node *right) {
    node *newnode = (node *)malloc(sizeof(node));
    char *newstr = (char *)malloc(strlen(token)+1);
    strcpy(newstr, token);
    newnode->left = left;
    newnode->right = right;
    newnode->token = newstr;
    return newnode;
}
void printtree(node *tree) {
    if (tree->left || tree->right)
        printf("(");
    printf(" %s ", tree->token);
    if (tree->left)
        printtree(tree->left);
    if (tree->right)
        printtree(tree->right);
    if (tree->left || tree->right)
        printf(")");
}
int main(void) {
    yyparse();
    return 0;
}
int yyerror(char *s) {
    fprintf(stderr, "%s\n", s);
    return 0;
}
```

In this example, the BNF rules for a simple expression grammar are converted into YACC form. The YACC specification includes actions that construct the nodes of the AST and connect them to form the tree structure. The resulting parser can be used to parse input strings and generate an AST for the input.