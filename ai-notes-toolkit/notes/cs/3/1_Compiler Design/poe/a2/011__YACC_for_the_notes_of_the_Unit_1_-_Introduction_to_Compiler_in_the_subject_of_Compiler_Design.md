 Here are the notes in markdown format without any emojis or external links:

### YACC for the notes of the Unit 1 - Introduction to Compiler in the subject of Compiler Design

1. YACC stands for Yet Another Compiler Compiler. It is a tool which generates a parser from the grammar specification written in BNF format.
2. The grammar specified in YACC is called LALR grammar which is a subset of LR grammars. LALR parsers are efficient and handle reasonably complex grammars.
3. A YACC specification contains
    - %token declarations - tokens used in the grammar are declared. Tokens can be terminal symbols or non-terminals.
    - %start symbol - Starting symbol for parsing is specified.
    - Grammar rules - Set of rules in BNF format are written to specify the language.
    - C code sections - Embedded C code to provide semantic actions on matching a grammar rule.
4. YACC generates a C function yyparse() which parses the input by recursively calling itself to match grammar rules.
5. A YACC program must also contain a lex specification to define lexemes (tokens) and a C code file including the YACC generated parser code and the main() function.
6. YACC facilitates writing parsers which are robust, maintainable and handles reasonably complex grammars. It makes the task of writing a parser easier compared to manually writing the parsing code.

The notes cover the key points about YACC and its usage in writing parsers. The points are written in a formal tone with headings and lists as specified. No emojis or external links are included. Let me know if you would like me to modify or add any other points to the notes.