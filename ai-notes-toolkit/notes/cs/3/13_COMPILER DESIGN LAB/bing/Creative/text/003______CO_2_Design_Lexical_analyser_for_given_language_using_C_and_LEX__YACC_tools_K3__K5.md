#### CO 2 Design Lexical analyser for given language using C and LEX /YACC tools K3, K5

- A lexical analyzer is a program that scans the source code of a given language and produces a sequence of tokens that represent the lexical units of the language.
- A token is a pair of a token name and an optional attribute value. For example, the token `ID(x)` represents an identifier with the name `x`.
- LEX is a tool that generates a lexical analyzer from a specification file that contains regular expressions and actions for each token.
- YACC is a tool that generates a parser from a specification file that contains grammar rules and actions for each production.
- C is a programming language that can be used to write the actions for LEX and YACC, as well as the main function that invokes the lexical analyzer and the parser.
- To design a lexical analyzer for a given language using C and LEX /YACC tools, the following steps are required:

  - Define the tokens and the regular expressions for each token in the LEX specification file. For example, `digit [0-9]`, `letter [A-Za-z]`, `ID {letter}({letter}|{digit})*`, etc.
  - Define the actions for each token in the LEX specification file. For example, `return ID;`, `return NUM;`, `return PLUS;`, etc.
  - Define the grammar rules and the actions for each production in the YACC specification file. For example, `expr: expr PLUS term { $$ = $1 + $3; }`, `term: NUM { $$ = $1; }`, etc.
  - Define the main function in the C file that invokes the lexical analyzer and the parser, and prints the output. For example, `yyparse();`, `printf("%d\n", result);`, etc.
  - Compile the LEX and YACC specification files using the commands `lex file.l` and `yacc file.y`, which will generate the files `lex.yy.c` and `y.tab.c`, respectively.
  - Compile the C file and the generated files using the command `gcc file.c lex.yy.c y.tab.c -o file`, which will generate the executable file `file`.
  - Run the executable file with the input source code of the given language, and observe the output. For example, `./file < input.txt`, `3 + 4`, `7`, etc.