#### CO 2 Design Lexical analyser for given language using C and LEX /YACC tools K3, K5

- Lexical analyzer is a program that transforms an input stream into a sequence of tokens.
- LEX is a tool that generates lexical analyzer from a set of regular expressions.
- YACC (Yet Another Compiler Compiler) is a tool that generates a parser from a set of context-free grammar rules.
- Parser is a program that analyzes the syntactic and semantic structure of the tokens and produces a parse tree.
- C is a programming language that can be used to implement the lexical analyzer and the parser.
- To design a lexical analyzer for a given language using C and LEX /YACC tools, the following steps are required:

  - Define the tokens and the regular expressions for the language in the LEX file.
  - Define the grammar rules and the actions for the language in the YACC file.
  - Compile the LEX file using the command `lex filename.l` to generate the C file `lex.yy.c`.
  - Compile the YACC file using the command `yacc filename.y` to generate the C file `y.tab.c`.
  - Link the two C files using the command `cc lex.yy.c y.tab.c -o filename` to generate the executable file `filename`.
  - Run the executable file with the input stream as the argument to get the output of the lexical analyzer and the parser.