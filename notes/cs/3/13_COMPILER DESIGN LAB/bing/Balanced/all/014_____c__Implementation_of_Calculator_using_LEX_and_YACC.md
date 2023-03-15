# c) Implementation of Calculator using LEX and YACC

- LEX and YACC are tools that help in creating lexical analyzers and parsers for a given grammar.
- A lexical analyzer is a program that converts a stream of characters into a stream of tokens, such as numbers, operators, identifiers, etc.
- A parser is a program that analyzes the syntactic structure of a stream of tokens and checks if it conforms to a given grammar. It can also perform semantic actions, such as evaluation, translation, etc.
- A calculator is a simple example of a program that can be implemented using LEX and YACC.
- The steps to implement a calculator using LEX and YACC are:

  - Define the tokens and the regular expressions that match them in the LEX file. For example, the token for a number can be defined as `[0-9]+(\.[0-9]+)?` and the token for an operator can be defined as `[+\-*/^()]`.
  - Define the grammar rules and the semantic actions for the calculator in the YACC file. For example, the rule for an expression can be defined as `expr: expr '+' expr { $$ = $1 + $3; } | expr '-' expr { $$ = $1 - $3; } | ... | '(' expr ')' { $$ = $2; } | NUMBER { $$ = $1; };`.
  - Compile the LEX file using the `lex` command to generate a C source file that contains the lexical analyzer function `yylex()`.
  - Compile the YACC file using the `yacc` command with the `-d` option to generate two C source files: one that contains the parser function `yyparse()` and another that contains the token definitions.
  - Compile and link the generated C source files using the `cc` command to produce the executable calculator program.
  - Run the calculator program and enter arithmetic expressions to evaluate them. For example, `2 + 3 * 4` should output `14`.