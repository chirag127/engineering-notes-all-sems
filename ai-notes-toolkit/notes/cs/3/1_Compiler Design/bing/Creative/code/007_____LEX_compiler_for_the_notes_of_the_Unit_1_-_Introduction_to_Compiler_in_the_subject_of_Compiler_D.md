### LEX compiler

- Lex is a computer program that generates lexical analyzers (\"scanners\" or \"lexers\").
- Lexical analyzers are programs that take a stream of input characters and produce a stream of tokens, which are the basic units of syntax in a programming language.
- Lex is commonly used with the yacc parser generator, which takes a stream of tokens and produces a syntax tree or a parse tree.
- Lex is written in the Lex language, which consists of three sections: definitions, rules, and user subroutines.
- The definitions section contains declarations of variables, constants, regular expressions, and macros that are used in the rules section.
- The rules section contains patterns and actions, which specify what to do when a pattern is matched in the input stream.
- The user subroutines section contains auxiliary C functions that are called by the actions in the rules section.
- The Lex compiler transforms a Lex program (usually with the extension .l) to a C program (usually with the name lex.yy.c). 
- The C program contains a function called yylex(), which is the lexical analyzer that can be called by the parser or the main program. 
- The C program also contains a global variable called yytext, which is a string that holds the matched text for the current token. 
- The C program can be compiled by any C compiler (such as gcc) to produce an executable file (usually with the name a.out).  
- The executable file can take a file name or a standard input as the source of input characters, and produce a stream of tokens as the output.