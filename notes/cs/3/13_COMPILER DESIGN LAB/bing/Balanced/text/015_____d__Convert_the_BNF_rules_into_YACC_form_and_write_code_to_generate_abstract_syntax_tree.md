### d) Convert the BNF rules into YACC form and write code to generate abstract syntax tree

- BNF (Backus-Naur form) is a notation for describing the syntax of a language using production rules.
- YACC (Yet Another Compiler-Compiler) is a tool that generates a parser for a given grammar in C.
- An abstract syntax tree (AST) is a data structure that represents the syntactic structure and meaning of a program.
- To convert BNF rules into YACC form, we need to follow these steps:
  - Identify the non-terminals and terminals in the BNF rules and declare them in the YACC file using `%token` and `%type` directives.
  - Write the YACC rules that correspond to the BNF rules using the `:` and `|` symbols to separate alternatives and the `;` symbol to end a rule.
  - Write the semantic actions that generate the AST nodes for each rule using the `{` and `}` symbols to enclose C code and the `$` symbol to access the attributes of the symbols in the rule.
  - Write the auxiliary functions and data structures that are needed to create and manipulate the AST nodes in the C section of the YACC file.
- For example, suppose we have the following BNF rules for a simple arithmetic expression language:

```
<expr> ::= <term> | <term> + <expr> | <term> - <expr>
<term> ::= <factor> | <factor> * <term> | <factor> / <term>
<factor> ::= <number> | ( <expr> )
<number> ::= <digit> | <digit> <number>
<digit> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
```

- The corresponding YACC file could look like this:

```
%{
/* C section */

#include <stdio.h>
#include <stdlib.h>

/* AST node types */
enum node_type {
  NODE_NUMBER,
  NODE_ADD,
  NODE_SUB,
  NODE_MUL,
  NODE_DIV
};

/* AST node structure */
struct node {
  enum node_type type;
  union {
    int value; /* for number nodes */
    struct node *children[2]; /* for operator nodes */
  } data;
};

/* Function to create a new AST node */
struct node *new_node(enum node_type type, ...) {
  struct node *node = malloc(sizeof(struct node));
  node->type = type;
  va_list args;
  va_start(args, type);
  switch (type) {
    case NODE_NUMBER:
      node->data.value = va_arg(args, int);
      break;
    case NODE_ADD:
    case NODE_SUB:
    case NODE_MUL:
    case NODE_DIV:
      node->data.children[0] = va_arg(args, struct node *);
      node->data.children[1] = va_arg(args, struct node *);
      break;
  }
  va_end(args);
  return node;
}

/* Function to print an AST node */
void print_node(struct node *node) {
  switch (node->type) {
    case NODE_NUMBER:
      printf("%d", node->data.value);
      break;
    case NODE_ADD:
      printf("(");
      print_node(node->data.children[0]);
      printf(" + ");
      print_node(node->data.children[1]);
      printf(")");
      break;
    case NODE_SUB:
      printf("(");
      print_node(node->data.children[0]);
      printf(" - ");
      print_node(node->data.children[1]);
      printf(")");
      break;
    case NODE_MUL:
      printf("(");
      print_node(node->data.children[0]);
      printf(" * ");
      print_node(node->data.children[1]);
      printf(")");
      break;
    case NODE_DIV:
      printf("(");
      print_node(node->data.children[0]);
      printf(" / ");
      print_node(node->data.children[1]);
      printf(")");
      break;
  }
}

/* Function to evaluate an AST node */
int eval_node(struct node *node) {
  switch (node->type) {
    case NODE_NUMBER:
      return node->data.value;
    case NODE_ADD:
      return eval_node(node->data.children[0]) + eval_node(node->data.children[1]);
    case NODE_SUB:
      return eval_node(node->data.children[0]) - eval_node(node->data.children[1]);
    case NODE_MUL:
      return eval_node(node->data.children[0]) * eval_node(node->data.children[1]);
    case NODE_DIV:
      return eval_node(node->data.children[0]) / eval_node(node->data.children[

```
