### Intermediate code for the notes of the Unit 3 - Syntax-directed Translation in the subject of Compiler Design

- Intermediate code is a form of representation of the source program that is easier to translate into the target machine code.
- Intermediate code eliminates the need of a new full compiler for every unique machine by keeping the analysis portion same for all the compilers. The second part of compiler, synthesis, is changed according to the target machine.
- Intermediate code can be either language-specific (e.g., Bytecode for Java) or language-independent (three-address code).
- The following are commonly used intermediate code representations:
  - Postfix Notation: Also known as reverse Polish notation or suffix notation. The ordinary (infix) way of writing the sum of a and b is with an operator in between: a + b. In postfix notation, the operator follows the operands: a b +. This notation eliminates the need for parentheses and precedence rules.
  - Syntax Trees: A syntax tree is a graphical representation of the abstract syntax of the source program. The leaves of the tree are the tokens of the program, and the internal nodes are the non-terminals of the grammar. The root of the tree is the start symbol of the grammar. Syntax trees can be used to implement syntax-directed translation schemes.
  - Three-Address Code: A three-address code is a linearized representation of a syntax tree, where each statement has at most three operands. A three-address statement is of the form x = y op z, where x, y, and z are names, constants, or compiler-generated temporaries, and op is an operator. Three-address code can be easily translated into assembly language or machine code.
- The intermediate code generator takes the output of the syntax analyzer (parse tree or abstract syntax tree) and produces a sequence of intermediate code statements.
- The intermediate code generator can use various techniques to optimize the intermediate code, such as constant folding, copy propagation, dead code elimination, etc.
- The intermediate code generator can also perform some semantic checks, such as type checking, scope checking, etc.
- The intermediate code generator can be implemented using various methods, such as syntax-directed translation, translation by syntax-directed definition, translation by abstract stack machine, etc.