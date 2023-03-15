### Postfix Translation

- Postfix translation is a technique of generating intermediate code in compiler design that uses postfix notation for expressions.
- Postfix notation, also known as reverse Polish notation, is a way of writing arithmetic expressions without parentheses, where the operator appears after the operands.
- For example, the infix expression `a * d - (b + c)` can be written in postfix notation as `a d * b c + -`.
- Postfix notation has the advantage of being easy to evaluate using a stack, where operands are pushed onto the stack and operators pop the operands, perform the operation, and push the result back onto the stack.
- Postfix translation can be achieved by using syntax-directed translation schemes, which are context-free grammars with embedded semantic actions that generate the intermediate code.
- A syntax-directed translation scheme is said to be postfix if the semantic actions appear at the end of the productions, i.e., after the right-hand side symbols.
- For example, the following grammar is a postfix translation scheme for arithmetic expressions:

```
E -> E + T {print('+')}
E -> E - T {print('-')}
E -> T
T -> T * F {print('*')}
T -> T / F {print('/')}
T -> F
F -> (E)
F -> id {print(id.lexeme)}
```

- The semantic actions print the lexeme of the identifier or the operator symbol to generate the postfix notation.
- For example, the input `a * d - (b + c)` will produce the output `a d * b c + -` by using the following derivation:

```
E -> E - T {print('-')}
  -> E - T * F {print('*')}
  -> E - T * (E) {print(')')}
  -> E - T * (E + T) {print('+')}
  -> E - T * (T + T) {print('+')}
  -> E - T * (F + T) {print('+')}
  -> E - T * (id + T) {print(id.lexeme)}
  -> E - T * (b + T) {print('b')}
  -> E - T * (b + F) {print('+')}
  -> E - T * (b + id) {print(id.lexeme)}
  -> E - T * (b + c) {print('c')}
  -> T - T * (b + c) {print('-')}
  -> F - T * (b + c) {print('-')}
  -> id - T * (b + c) {print(id.lexeme)}
  -> a - T * (b + c) {print('a')}
  -> a - F * (b + c) {print('-')}
  -> a - id * (b + c) {print(id.lexeme)}
  -> a - d * (b + c) {print('d')}
  -> a d * b c + - {print('*')}
```

- The output is the postfix notation of the input expression.