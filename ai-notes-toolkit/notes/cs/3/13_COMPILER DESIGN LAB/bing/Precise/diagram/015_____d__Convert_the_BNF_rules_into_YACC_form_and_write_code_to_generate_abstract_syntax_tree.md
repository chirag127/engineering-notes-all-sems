### d) Convert the BNF rules into YACC form and write code to generate abstract syntax tree

1. BNF (Backus-Naur Form) is a notation used to formally describe the syntax of programming languages, grammars, and other formal languages. It is a way to represent context-free grammars.

2. YACC (Yet Another Compiler-Compiler) is a tool that generates a parser for a given grammar. It takes a grammar specification in BNF form as input and produces C code for a parser that recognizes the language described by the grammar.

3. To convert BNF rules into YACC form, the BNF rules must be rewritten in a format that is compatible with YACC. This involves replacing the `::=` symbol with `:` and enclosing the right-hand side of the rule in braces `{}`.

4. For example, a BNF rule such as `expr ::= term | expr + term` would be rewritten in YACC form as `expr : term | expr '+' term ;`

5. Once the BNF rules have been converted into YACC form, they can be used as input to the YACC tool to generate a parser.

6. An abstract syntax tree (AST) is a tree representation of the structure of a program or other piece of code. It is an intermediate representation of the code that is used by compilers and other tools to analyze and manipulate the code.

7. To generate an AST using YACC, code must be added to the YACC specification to construct the tree as the input is parsed. This is typically done by adding actions to the YACC rules that create and manipulate tree nodes as the input is recognized.

8. For example, to generate an AST for an expression such as `2 + 3 * 4`, the YACC specification might include rules such as:

```
expr : term
    | expr '+' term { $$ = make_node('+', $1, $3); }
    ;

term : factor
    | term '*' factor { $$ = make_node('*', $1, $3); }
    ;

factor : NUMBER { $$ = make_leaf($1); }
    ;
```

9. In this example, the actions associated with the `expr` and `term` rules create tree nodes representing the `+` and `*` operators, while the action associated with the `factor` rule creates a leaf node representing a number.

10. The resulting AST would have the structure shown below:

```
    +
   / \
  2   *
     / \
    3   4
```

11. This tree represents the structure of the expression `2 + 3 * 4`, with the `+` and `*` operators as internal nodes and the numbers as leaf nodes. The tree can be used by a compiler or other tool to analyze and manipulate the code.