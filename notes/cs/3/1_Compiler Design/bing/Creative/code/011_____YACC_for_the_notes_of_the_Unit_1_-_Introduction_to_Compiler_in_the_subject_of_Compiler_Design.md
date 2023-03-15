```markdown
### YACC

- YACC stands for Yet Another Compiler-Compiler .
- It is a tool that generates a parser for a given grammar  .
- A parser is the part of a compiler that tries to make syntactic sense of the source code.
- YACC is an LALR(1) parser generator, which means it produces a parser that uses LookAhead, Left-to-right, Rightmost derivation with 1 lookahead token .
- YACC was originally designed to be complemented by Lex, a lexical analyzer generator .
- Lex and YACC work together to convert a stream of characters into a stream of tokens, and then check the syntactic structure of the tokens according to the grammar rules.
- YACC input file is divided into three parts: definitions, rules, and user subroutines .
- Definitions section contains declarations of tokens, variables, and constants .
- Rules section contains the grammar rules and the associated actions to be performed when a rule is matched .
- User subroutines section contains the C code that is copied verbatim to the output file .
- YACC output file is a C program that contains the parser and the user subroutines.
- YACC output file can be compiled and linked with the Lex output file to produce an executable parser .
```