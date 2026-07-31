# Postfix Translation

- Postfix translation is a technique of generating intermediate code in compiler design that uses postfix notation for expressions.
- Postfix notation, also known as reverse Polish notation, is a way of writing arithmetic expressions without parentheses or precedence rules, where the operator appears after the operands.
- For example, the infix expression `a * d - (b + c)` can be written in postfix notation as `a d * b c + -`.
- Postfix translation can be implemented using syntax-directed translation schemes, which are context-free grammars with embedded semantic actions.
- A semantic action is a piece of code that performs some computation or output based on the attributes of the grammar symbols.
- A syntax-directed translation scheme is called postfix if the semantic actions appear at the right end of the productions.
- For example, the following grammar is a postfix translation scheme for infix expressions:

```
E -> E + T { print('+') }
E -> E - T { print('-') }
E -> T
T -> T * F { print('*') }
T -> T / F { print('/') }
T -> F
F -> ( E )
F -> id { print(id.lexeme) }
```

- The semantic actions print the lexeme of the identifier or the operator symbol to generate the postfix code.
- For example, the input `a * d - (b + c)` will produce the output `a d * b c + -` by following the derivation:

```
E -> E - T { print('-') }
  -> E - T * F { print('*') }
  -> E - T * id { print(id.lexeme) }
  -> E - id * id { print(id.lexeme) }
  -> E - T { print('-') }
  -> E - T + F { print('+') }
  -> E - T + id { print(id.lexeme) }
  -> E - id + id { print(id.lexeme) }
  -> E - T { print('-') }
  -> T - T { print('-') }
  -> F - T { print('-') }
  -> id - T { print(id.lexeme) }
  -> a - T { print('a') }
```

- Postfix translation has some advantages over infix translation, such as:
  - It eliminates the need for parentheses and precedence rules in expressions.
  - It simplifies the evaluation of expressions using a stack data structure.
  - It reduces the number of intermediate variables and temporary storage.