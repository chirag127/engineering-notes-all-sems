### LEX compiler

- Lex is a computer program that generates lexical analyzers (\"scanners\" or \"lexers\").
- Lexical analyzers are programs that take a stream of input characters and produce a stream of tokens, which are the basic units of syntax in a programming language.
- Lex is commonly used with the yacc parser generator, which takes a stream of tokens and produces a parse tree, which is the hierarchical structure of a program.
- Lex is written in the Lex language, which consists of three parts: definitions, rules, and user subroutines  .
  - Definitions are declarations of variables, constants, macros, and regular expressions that are used in the rules  .
  - Rules are patterns of input characters and corresponding actions that are performed when the pattern is matched  .
  - User subroutines are functions that are called by the actions in the rules, or by the main function of the lexical analyzer  .
- The Lex compiler transforms a Lex program (usually named lex.l) to a C program (usually named lex.yy.c), which is the actual lexical analyzer   .
- The C compiler then compiles the lex.yy.c file into an executable file (usually named a.out), which can be run on the input stream   .
- The Lex compiler can be invoked by the command `lex lex.l`, and the C compiler can be invoked by the command `gcc -lfl lex.yy.c`.
- The Lex language is flexible and powerful, and can be used to create lexical analyzers for various programming languages, such as C, C++, Java, etc .