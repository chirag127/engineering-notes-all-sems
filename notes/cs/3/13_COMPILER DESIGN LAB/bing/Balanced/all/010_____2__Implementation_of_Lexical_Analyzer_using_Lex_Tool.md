# 2. Implementation of Lexical Analyzer using Lex Tool

- Lex is a tool that generates lexical analyzers or scanners.
- A lexical analyzer is a program that reads an input stream of characters and produces an output stream of tokens.
- Lex uses a specification file that contains rules and actions. The rules define the patterns to be matched in the input and the actions define what to do when a pattern is matched.
- The specification file has three sections: definitions, rules, and user subroutines.
- The definitions section contains declarations of variables, constants, macros, and regular expressions that are used in the rules section.
- The rules section contains the main logic of the lexical analyzer. Each rule has the form: `pattern {action}` where pattern is a regular expression and action is a C code fragment that is executed when the pattern is matched.
- The user subroutines section contains auxiliary C functions that are called by the actions in the rules section.
- Lex processes the specification file and generates a C source file called lex.yy.c that contains the lexical analyzer.
- The lex.yy.c file can be compiled and linked with the user subroutines and the standard library to produce an executable scanner.