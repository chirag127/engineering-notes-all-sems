### YACC for the notes of the Unit 1 - Introduction to Compiler in the subject of Compiler Design

- YACC stands for Yet Another Compiler-Compiler. It is a tool that generates a parser for a given grammar.
- A parser is a program that analyzes the syntactic structure of a source code and checks if it conforms to the rules of a language.
- A grammar is a set of rules that define the syntax of a language. It consists of terminals, non-terminals, and production rules.
- YACC is often used with a lexical analyzer tool such as lex, which is used to tokenize the input source code into a stream of tokens. Tokens are the smallest meaningful units of a language.
- YACC uses LALR(1) algorithm to generate a parser. LALR(1) stands for LookAhead, Left-to-right, Rightmost derivation with 1 lookahead token. It is a variant of LR(1) algorithm that reduces the size of the parser table.
- YACC input file is divided into three parts: definitions, rules, and user subroutines. Definitions contain declarations of tokens, variables, and other information. Rules contain the grammar rules and the associated actions. User subroutines contain the main function and other helper functions.
- YACC output file is a C program that contains the parser and the user subroutines. It can be compiled and linked with the lexical analyzer to form a complete compiler.