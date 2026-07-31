### Postfix Translation

- Postfix translation is a technique of generating intermediate code for a compiler that uses a syntax-directed translation scheme with semantic actions at the end of the productions .
- Postfix translation is also known as postfix syntax-directed translation or postfix SDT.
- Postfix translation is based on the idea that the order of the semantic actions in a production reflects the order of the operations in the target code .
- Postfix translation can be implemented by using a stack to store the intermediate results of the semantic actions and popping them when needed .
- Postfix translation can be applied to any context-free grammar, but it is especially useful for translating expressions into postfix notation  .
- Postfix notation is a way of writing arithmetic expressions without using parentheses or precedence rules, where the operator appears after the operands.
- Postfix notation is also known as reverse Polish notation or RPN.
- Postfix notation has the advantage of being easy to evaluate by a stack machine or a recursive algorithm.
- Postfix notation can be obtained from infix notation (where the operator appears between the operands) by using the following rules:
  - Scan the infix expression from left to right.
  - If an operand is encountered, output it or push it onto the stack.
  - If an operator is encountered, pop two operands from the stack, apply the operator to them, and push the result back onto the stack or output it.
  - If a left parenthesis is encountered, push it onto the stack.
  - If a right parenthesis is encountered, pop and output the stack elements until a left parenthesis is popped. Discard the pair of parentheses.
  - At the end of the expression, pop and output the remaining stack elements.

- For example, the infix expression `a * d - (b + c)` can be translated into postfix notation as `a d * b c + -` by using the following steps:
  - Scan `a`, output `a`.
  - Scan `*`, push `*` onto the stack.
  - Scan `d`, output `d`.
  - Scan `-`, pop `*` from the stack and output it, push `-` onto the stack.
  - Scan `(`, push `(` onto the stack.
  - Scan `b`, output `b`.
  - Scan `+`, push `+` onto the stack.
  - Scan `c`, output `c`.
  - Scan `)`, pop `+` from the stack and output it, pop `(` from the stack and discard it.
  - At the end of the expression, pop `-` from the stack and output it.

- The postfix translation of a grammar can be obtained by attaching semantic actions to the right end of the productions, where each semantic action generates a piece of intermediate code or performs a stack operation .
- The semantic actions can be written as `print x` to output `x`, `push x` to push `x` onto the stack, or `pop x` to pop `x` from the stack .
- For example, the following grammar can be used to translate infix expressions into postfix notation :

```
E -> E + T { print '+' }
E -> E - T { print '-' }
E -> T
T -> T * F { print '*' }
T -> T / F { print '/' }
T -> F
F -> ( E ) { pop '(' }
F -> id { print id }
```

- The following table shows the postfix translation of the infix expression `a * d - (b + c)` by using the above grammar :

| Stack | Input | Output | Action |
| ----- | ----- | ------ | ------ |
|       | a * d - (b + c) | | |
| E -> | * d - (b + c) | a | print id |
| E -> T -> | * d - (b + c) | a | |
| E -> T -> T -> | d - (b + c) | a | |
| E -> T -> T -> F -> | d - (b + c) | a | |
| E -> T -> T -> F -> id -> | - (b + c) | a d | print id |
| E