### YACC

- YACC stands for **Yet Another Compiler-Compiler**. It is a tool that generates a **parser** for a given grammar .
- A parser is the part of a compiler that tries to make syntactic sense of the source code, based on a formal grammar.
- YACC is an **LALR(1)** parser generator, which means it produces a parser that uses **LookAhead, Left-to-right, Rightmost** derivation with **1** lookahead token .
- YACC was originally designed to be complemented by **Lex**, a tool that generates a **lexical analyzer** or **scanner** .
- A lexical analyzer is the part of a compiler that converts the source code into a stream of **tokens**, which are the basic units of meaning in a language.
- YACC input file is divided into three parts, separated by **%%** :
  - The first part contains **declarations** of tokens, variables, and other information that are shared with Lex and the C program.
  - The second part contains the **grammar rules** that define the syntax of the language and the associated **semantic actions** that specify what to do when a rule is matched.
  - The third part contains the **C code** that implements the main function, error handling, and other auxiliary functions.
- YACC output file is a C program that contains the **parser function** and the **parsing tables** that guide the parsing process.
- YACC can be used to generate parsers for various languages, such as C, Pascal, SQL, etc. It can also be used to implement **interpreters**, **calculators**, **command-line interfaces**, and other applications that involve parsing .