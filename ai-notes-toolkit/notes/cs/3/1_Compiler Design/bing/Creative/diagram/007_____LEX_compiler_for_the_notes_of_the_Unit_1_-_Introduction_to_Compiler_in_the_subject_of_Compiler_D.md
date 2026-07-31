### LEX compiler

- Lex is a computer program that generates lexical analyzers (\"scanners\" or \"lexers\").
- Lexical analyzers are programs that take a stream of input characters and produce a stream of tokens, which are the basic units of syntax in a programming language.
- Lex is commonly used with the yacc parser generator, which takes a stream of tokens and produces a syntax tree, which is the basic structure of a program.
- Lex is written in the Lex language, which consists of three parts: definitions, rules, and user subroutines.
- Definitions are declarations of variables, constants, regular expressions, and other elements that are used in the rules.
- Rules are patterns that match the input characters and specify the actions to be taken when a match is found.
- User subroutines are C functions that are called by the actions in the rules.
- The Lex compiler transforms a Lex program (usually with the extension .l) to a C program (usually with the name lex.yy.c). 
- The C program lex.yy.c contains the definition of a function called yylex(), which is the lexical analyzer. 
- The C compiler compiles lex.yy.c into an executable file (usually with the name a.out). 
- The executable file a.out takes a stream of input characters (usually from a file or the standard input) and produces a stream of tokens (usually to a file or the standard output). 
- The Lex language is flexible and powerful, allowing the user to specify complex patterns and actions for lexical analysis.
- The Lex language is also portable and compatible, as it can be used on many Unix systems and is specified as part of the POSIX standard.