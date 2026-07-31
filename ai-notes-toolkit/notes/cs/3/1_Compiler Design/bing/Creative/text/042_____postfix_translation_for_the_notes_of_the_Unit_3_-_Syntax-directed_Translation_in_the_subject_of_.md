### Postfix Translation

- Postfix translation is a technique of generating intermediate code in compiler design that uses postfix notation .
- Postfix notation, also known as reverse Polish notation, is a way of writing arithmetic expressions without parentheses, where the operator appears after the operands.
- For example, the infix expression `a * d - (b + c)` can be written in postfix notation as `a d * b c + -`.
- Postfix translation can be achieved by using syntax-directed translation schemes , which are context-free grammars with embedded semantic actions.
- Semantic actions are fragments of code that are executed when a production is applied during parsing.
- The semantic actions can be used to generate the postfix code for the non-terminals in the production by concatenating the code translations of the operands and appending the operator at the end .
- For example, the production `E -> E1 + E2` can have the semantic action `E.CODE = E1.CODE || E2.CODE || '+'`, where `||` denotes string concatenation.
- Syntax-directed translation schemes that have semantic actions only at the right end of the productions are called postfix translation schemes.
- Postfix translation schemes have the advantage of being easy to implement and efficient to execute.
- Postfix translation schemes can be used to generate intermediate code for arithmetic expressions, boolean expressions, assignment statements, conditional statements, and loops .