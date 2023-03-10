 Here is the content in markdown format:

### d) Convert the BNF rules into YACC form and write code to generate abstract syntax tree

1. BNF (Backus-Naur Form) is a metasyntax used to express context-free grammars. It describes a language in terms of production rules.
2. YACC (Yet Another Compiler Compiler) is a parser generator tool which takes grammar specifications in BNF form and generates a parser for that grammar in the C programming language.
3. To convert BNF rules to YACC form:

- Replace all uppercase symbols with lowercase symbols and remove spaces.
- Remove all options enclosed within square brackets [ ].
- Replace the ::= symbol with :.
- Add %start, %token and %left, %right or %nonassoc declarations.

For example:

<expr> ::= <term> | <term> + <expr>

is converted to:

%start expr
%token term
expr: term
expr: term '+' expr

4. To generate abstract syntax tree from YACC rules:

- Declare non-terminal symbols as structure/node types.
- Within the parsing functions, create a node of appropriate type for each recognized phrase.
- For each subphrase, call the parsing function recursively and add the returned tree as a child of the current node.

For example:

%start expr
%token term

struct node {
    char *label;
    struct node *child;
};

void expr(void) {
    struct node *n = malloc(sizeof(struct node));
    n->label = "expr";
    n->child = term();
    if (lookahead == '+') {
        gettoken();
        n->child = make_node2('+', n->child, expr());
    }
    return n;
}

// Other functions

This will generate an abstract syntax tree with 'expr' as root having 'term' and '+' nodes as children.

The advantages of using YACC are:
- It simplifies writing parsers.
- It enforces a standard structure for parsers.
- It handles ambiguity and conflicts in grammar.
The disadvantages are:
- The generated code can be difficult to understand and debug.
- It may not generate efficient parsers.

YACC has applications in compilers, interpreters, code generators, etc. It is a very useful tool for implementing parsers in software systems.