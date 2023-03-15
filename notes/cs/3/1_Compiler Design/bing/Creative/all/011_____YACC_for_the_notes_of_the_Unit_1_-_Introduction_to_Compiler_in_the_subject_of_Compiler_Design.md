# YACC for the notes of the Unit 1 - Introduction to Compiler in the subject of Compiler Design

- YACC stands for Yet Another Compiler-Compiler. It is a tool that generates a parser for a given grammar.
- A parser is a program that analyzes the syntactic structure of a source code and checks if it conforms to the rules of a language.
- A grammar is a set of rules that define the syntax of a language. It consists of terminals, non-terminals, and production rules.
- YACC is often used with a lexical analyzer tool such as lex, which is used to tokenize the input source code into a stream of tokens.
- YACC is based on the LALR(1) parsing algorithm, which stands for LookAhead, Left-to-right, Rightmost derivation with 1 lookahead token. It is a variant of the LR(1) algorithm, which is more efficient and compact.
- YACC takes a grammar specification file as input and produces a C program as output. The grammar specification file has three sections: definitions, rules, and user code.
- The definitions section contains declarations of tokens, variables, and other information that are used by the parser.
- The rules section contains the production rules of the grammar, each followed by an optional action that is executed when the rule is applied.
- The user code section contains any C code that is needed by the parser, such as header files, global variables, or functions.
- YACC can handle ambiguous grammars, but it may produce a parser that is not deterministic or correct. It can also detect and report syntax errors in the input source code.
- YACC is widely used for compiler design, as it simplifies the task of writing a parser and allows the programmer to focus on the semantics and optimization of the language.