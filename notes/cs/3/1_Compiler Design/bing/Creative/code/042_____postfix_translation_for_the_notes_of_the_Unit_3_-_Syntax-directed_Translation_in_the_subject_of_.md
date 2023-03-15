# Postfix Translation

- Postfix translation is a technique to generate intermediate code for expressions in a compiler.
- Postfix translation uses a syntax-directed translation scheme (SDT) that has semantic actions at the end of each production.
- Postfix translation produces a postfix notation of the expression, also known as reverse Polish notation, where the operator appears after the operands.
- Postfix translation can be implemented by using a stack to store the operands and operators, and popping them when a semantic action is encountered.
- Postfix translation can be done by factoring the productions to achieve postfix form, or by using inherited attributes to pass the postfix notation from the children to the parent nodes in the syntax tree.

## Example

- Consider the following grammar for arithmetic expressions:

```
E -> E + T | T
T -> T * F | F
F -> (E) | id
```

- To generate postfix notation for this grammar, we can use the following SDT:

```
E -> E + T {print('+')} | T
T -> T * F {print('*')} | F
F -> (E) | id {print(id.lexeme)}
```

- For example, the input expression `a * (b + c)` will produce the following output:

```
a b c + * 
```