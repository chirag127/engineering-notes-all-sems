### d) Convert the BNF rules into YACC form and write code to generate abstract syntax tree

- BNF (Backus-Naur form) is a notation for describing the syntax of a language using production rules.
- YACC (Yet Another Compiler-Compiler) is a tool that generates a parser from a grammar specification in BNF form.
- An abstract syntax tree (AST) is a data structure that represents the syntactic structure of a program or an expression.
- To convert BNF rules into YACC form, we need to follow some steps:
  - Identify the terminals and non-terminals of the grammar and declare them using `%token` and `%type` directives in the YACC file.
  - Write the production rules in the form of `non-terminal : symbol-sequence` where `symbol-sequence` can be a combination of terminals and non-terminals. Use `|` to separate alternative symbol-sequences for the same non-terminal.
  - Use `;` to end each production rule.
  - Use `{` and `}` to enclose C code that will be executed when a production rule is matched by the parser. This code can be used to create AST nodes and link them together.
  - Use `$$` to refer to the value of the current non-terminal and `$n` to refer to the value of the n-th symbol in the symbol-sequence.
  - Use `%start` directive to specify the start symbol of the grammar.
  - Use `%union` directive to define a union type that can hold different types of values for the non-terminals and terminals.
  - Use `%left`, `%right` and `%nonassoc` directives to specify the associativity and precedence of the operators in the grammar.
- To write code to generate AST, we need to define a data structure that can represent different kinds of nodes, such as operators, operands, identifiers, literals, etc. We also need to define functions that can create and manipulate these nodes. For example, we can use the following C code to define an AST node:

```c
typedef enum { OP, ID, NUM, STR } node_type;

typedef struct node {
  node_type type;
  union {
    char op; // for operators
    char *id; // for identifiers
    int num; // for numbers
    char *str; // for strings
  } value;
  struct node *left; // for left child
  struct node *right; // for right child
} node;

node *new_node(node_type type, void *value, node *left, node *right) {
  node *n = (node *)malloc(sizeof(node));
  n->type = type;
  switch (type) {
    case OP: n->value.op = *(char *)value; break;
    case ID: n->value.id = (char *)value; break;
    case NUM: n->value.num = *(int *)value; break;
    case STR: n->value.str = (char *)value; break;
  }
  n->left = left;
  n->right = right;
  return n;
}
```

- Then, we can use the C code in the YACC file to create and link the nodes according to the production rules. For example, if we have the following BNF rule for an expression:

```
expr ::= expr '+' expr
       | expr '-' expr
       | expr '*' expr
       | expr '/' expr
       | '(' expr ')'
       | ID
       | NUM
```

- We can write the corresponding YACC rule as:

```
expr : expr '+' expr { $$ = new_node(OP, "+", $1, $3); }
     | expr '-' expr { $$ = new_node(OP, "-", $1, $3); }
     | expr '*' expr { $$ = new_node(OP, "*", $1, $3); }
     | expr '/' expr { $$ = new_node(OP, "/", $1, $3); }
     | '(' expr ')' { $$ = $2; }
     | ID { $$ = new_node(ID, $1, NULL, NULL); }
     | NUM { $$ = new_node(NUM, $1, NULL, NULL); }
     ;
```

- This way, we can convert the BNF rules into YACC form and write code to generate AST for any given grammar.