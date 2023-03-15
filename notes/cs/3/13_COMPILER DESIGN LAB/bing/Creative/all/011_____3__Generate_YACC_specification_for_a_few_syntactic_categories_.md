# 3. Generate YACC specification for a few syntactic categories.

- YACC stands for Yet Another Compiler-Compiler, which is a tool that generates a parser for a given grammar.
- A parser is a program that analyzes the syntactic structure of a given input and checks if it conforms to the rules of the grammar.
- A grammar is a set of production rules that define the syntax of a language.
- A syntactic category is a group of symbols that can be substituted for each other in a production rule.
- For example, in the grammar of arithmetic expressions, E is a syntactic category that represents any expression, and can be substituted by E + E, E - E, E * E, E / E, or (E).
- To generate a YACC specification for a few syntactic categories, we need to follow these steps:

  - Define the tokens that represent the terminal symbols of the grammar, such as numbers, operators, parentheses, etc.
  - Define the precedence and associativity of the operators, if any.
  - Define the start symbol of the grammar, which is usually the syntactic category that represents the whole input.
  - Define the production rules for each syntactic category, using the tokens and other syntactic categories as symbols.
  - Write the actions that the parser should perform when it recognizes a production rule, such as evaluating the expression, printing the result, etc.

- For example, here is a YACC specification for the syntactic categories of arithmetic expressions, identifiers, and assignments:

```
%token NUM ID
%left '+' '-'
%left '*' '/'
%%
S: E '\n' { printf("%d\n", $1); }
 | ID '=' E '\n' { sym[$1] = $3; }
 ;
E: E '+' E { $$ = $1 + $3; }
 | E '-' E { $$ = $1 - $3; }
 | E '*' E { $$ = $1 * $3; }
 | E '/' E { $$ = $1 / $3; }
 | '(' E ')' { $$ = $2; }
 | NUM { $$ = $1; }
 | ID { $$ = sym[$1]; }
 ;
%%
```

- In this specification, NUM and ID are the tokens that represent numbers and identifiers, respectively.
- The operators have left associativity and precedence as defined by the %left directives.
- The start symbol is S, which represents either an expression followed by a newline, or an assignment followed by a newline.
- The production rules for E, ID, and '=' are defined using the tokens and other syntactic categories as symbols.
- The actions are written in C code inside curly braces, and use the $$ and $n variables to refer to the value of the left-hand side and the n-th right-hand side symbol, respectively.
- The sym array is used to store the values of the identifiers.