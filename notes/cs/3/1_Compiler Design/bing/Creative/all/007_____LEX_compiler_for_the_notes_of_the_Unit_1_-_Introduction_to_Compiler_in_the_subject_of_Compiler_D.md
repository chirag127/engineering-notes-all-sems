# LEX compiler

- LEX is a computer program that generates lexical analyzers (\"scanners\" or \"lexers\").
- Lexical analyzer is a program that takes a stream of input characters and produces a stream of tokens as output.
- Tokens are the smallest meaningful units of a program, such as keywords, identifiers, literals, operators, etc.
- LEX is commonly used with the yacc parser generator, which takes a stream of tokens and produces a parse tree as output.
- A parse tree is a hierarchical representation of the syntactic structure of a program.
- LEX uses a special notation to specify the patterns of the tokens and the actions to be performed when a pattern is matched.
- A LEX program consists of three sections: definitions, rules, and user subroutines.
- The definitions section contains declarations of variables, constants, macros, and regular expressions.
- The rules section contains pairs of patterns and actions, where a pattern is a regular expression that describes a token, and an action is a C code fragment that is executed when the pattern is matched.
- The user subroutines section contains additional C functions that are called by the actions or the main function.
- The LEX compiler transforms a LEX program (usually with the extension .l) to a C program (usually with the name lex.yy.c). 
- The C program contains the definition of a function called yylex(), which implements the lexical analyzer.
- The C program also contains the definitions of some global variables and functions, such as yytext, yyin, yyout, etc.
- The C program can be compiled by any C compiler (such as gcc) to produce an executable file (usually with the name a.out).  
- The executable file can be run on any input file or standard input, and it will produce the tokens as output on the standard output or a specified output file.  
- LEX is a powerful and flexible tool for creating lexical analyzers for various applications, such as compilers, interpreters, text editors, etc.