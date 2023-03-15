### 2. Implementation of Lexical Analyzer using Lex Tool

- Lex is a tool that generates lexical analyzers or scanners.
- A lexical analyzer is a program that reads an input stream of characters and produces an output stream of tokens.
- Lex uses a specification file that contains rules and actions. The rules define the patterns to be matched in the input and the actions define what to do when a pattern is matched.
- The specification file has three sections: definitions, rules, and user subroutines.
- The definitions section contains declarations of variables, constants, macros, and regular expressions that are used in the rules section.
- The rules section contains the main logic of the lexical analyzer. Each rule has the form: `pattern {action}` where pattern is a regular expression and action is a C code fragment that is executed when the pattern is matched.
- The user subroutines section contains auxiliary C functions that are called by the actions in the rules section.
- Lex converts the specification file into a C source file that implements the lexical analyzer. The C source file can be compiled and linked with other C files to create an executable program.
- The lexical analyzer can be invoked by calling the function `yylex()`. This function returns the next token from the input stream, or 0 if the end of the input is reached.
- The lexical analyzer can communicate with the parser or the main program by using global variables such as `yytext`, `yyleng`, `yylineno`, and `yyin`.
- `yytext` is a string that contains the text of the matched pattern.
- `yyleng` is an integer that contains the length of `yytext`.
- `yylineno` is an integer that contains the current line number of the input.
- `yyin` is a file pointer that points to the input stream. It can be changed to read from different sources.