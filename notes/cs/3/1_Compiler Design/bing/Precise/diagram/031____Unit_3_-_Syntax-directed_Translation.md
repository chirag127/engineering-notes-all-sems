## Unit 3 - Syntax-directed Translation

Syntax-directed translation is a method of translating the source program into the target program using the context-free grammar of the source language. It is a technique used by compilers to generate intermediate code or the target code.

1. **Syntax-Directed Definitions**: A syntax-directed definition associates with each grammar symbol an ordered list of attributes and with each production a set of semantic rules for computing the values of the attributes associated with the symbols appearing in the production.

2. **Syntax-Directed Translation Schemes**: A syntax-directed translation scheme is a context-free grammar in which program fragments called semantic actions are embedded within the right sides of productions.

3. **Translation of Assignment Statements**: Assignment statements can be translated using syntax-directed translation by associating a semantic rule with the production for assignment statements.

4. **Translation of Boolean Expressions**: Boolean expressions can be translated using syntax-directed translation by associating semantic rules with the productions for boolean expressions.

5. **Translation of Control Flow Statements**: Control flow statements such as if-else and while can be translated using syntax-directed translation by associating semantic rules with the productions for control flow statements.

6. **Intermediate Code Generation**: Syntax-directed translation can be used to generate intermediate code, which is a representation of the source program that is closer to the target machine code than the source code.

7. **Postfix Notation**: Postfix notation is a way of writing arithmetic expressions in which the operators follow their operands. It is also known as Reverse Polish Notation (RPN). Syntax-directed translation can be used to translate infix expressions into postfix notation.

8. **Three-Address Code**: Three-address code is a type of intermediate code used by compilers to represent the source program. It consists of a sequence of instructions, each of which has at most three operands. Syntax-directed translation can be used to generate three-address code.

9. **Abstract Syntax Trees**: An abstract syntax tree (AST) is a tree representation of the abstract syntactic structure of the source code. Syntax-directed translation can be used to construct an AST for the source program.

10. **Directed Acyclic Graphs**: A directed acyclic graph (DAG) is a graph with directed edges and no cycles. DAGs can be used to represent expressions in intermediate code. Syntax-directed translation can be used to construct a DAG for an expression.