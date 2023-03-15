### YACC tools (Unix/Linux utilities)

- YACC stands for Yet Another Compiler-Compiler. It is a program that generates a parser for a given grammar .
- A parser is a program that analyzes the syntax of a source code and checks if it conforms to a set of rules .
- A grammar is a formal description of the syntax of a language, using symbols and rules .
- YACC is a standard utility on BSD and AT&T Unix systems, and it is also available on GNU-based Linux distributions as Bison, which is a compatible replacement.
- YACC can produce parsers for simple or complex languages, such as a desk calculator or a programming language .
- YACC takes a grammar specification as input and generates a C source code file as output, which contains the parser function .
- The grammar specification consists of three sections: definitions, rules, and user code.
  - The definitions section contains declarations of symbols, types, and variables.
  - The rules section contains the grammar rules, which specify how the symbols can be combined to form valid sentences in the target language.
  - The user code section contains C code that is copied verbatim to the output file, and can be used to perform actions when a rule is matched.
- YACC uses the LALR(1) algorithm to generate the parser, which is a type of bottom-up parsing that uses a lookahead symbol to resolve ambiguities .
- YACC also generates a header file that contains the definitions of the symbols and tokens used in the grammar.
- YACC can be used in conjunction with a lexical analyzer, such as lex or flex, which converts the input stream into tokens that are fed to the parser .