# Postfix Notation

- Postfix notation is a way of writing arithmetic expressions without using parentheses or brackets.
- In postfix notation, the operator appears after the operands, i.e., the operator between operands is taken out and is attached after operands.
- For example, the infix expression `a * d - (b + c)` can be written in postfix notation as `a d * b c + -`.
- Postfix notation is also known as reverse Polish notation or suffix notation.
- Postfix notation has some advantages over infix notation, such as:
  - It is easier to parse for a machine, as there is no need to check the operator precedence or associativity.
  - It can be used to generate intermediate code in compiler design, as it reflects the order of evaluation of the operands and operators .
  - It can be evaluated using a stack data structure, by pushing the operands onto the stack and popping them when an operator is encountered.
- Postfix notation can be converted from infix notation using the following algorithm:
  - Scan the infix expression from left to right.
  - If an operand is encountered, output it.
  - If an operator is encountered, push it onto the stack.
  - If a left parenthesis is encountered, push it onto the stack.
  - If a right parenthesis is encountered, pop and output the operators from the stack until a left parenthesis is found. Discard the left parenthesis.
  - At the end of the expression, pop and output the remaining operators from the stack.