### Postfix Notation

- Postfix notation is a way of writing expressions where the operator appears after the operands, i.e., the operator between operands is taken out and is attached after operands.
- For example, the infix expression `a * d - (b + c)` can be written in postfix notation as `a d * b c + -`.
- Postfix notation is also known as reverse Polish notation or suffix notation.
- Postfix notation has some advantages over infix notation, such as:
  - It does not require parentheses to specify the order of operations.
  - It is easier to parse for a machine, as there is no need to consider operator precedence or associativity.
  - It can be evaluated using a stack data structure, where operands are pushed onto the stack and operators pop and operate on the topmost operands.
- Postfix notation can be used in intermediate code generation in compiler design, as it is a convenient and compact representation of expressions .
- To convert an infix expression to postfix notation, one can use the following algorithm:
  - Scan the infix expression from left to right.
  - If the scanned symbol is an operand, output it.
  - If the scanned symbol is an opening parenthesis, push it onto the stack.
  - If the scanned symbol is a closing parenthesis, pop and output symbols from the stack until an opening parenthesis is encountered. Discard the pair of parentheses.
  - If the scanned symbol is an operator, then:
    - If the stack is empty or the top of the stack is an opening parenthesis, push the operator onto the stack.
    - If the operator has higher precedence than the top of the stack, push the operator onto the stack.
    - If the operator has lower or equal precedence than the top of the stack, pop and output symbols from the stack until the stack is empty or the top of the stack has lower precedence than the operator. Then push the operator onto the stack.
  - After scanning the infix expression, pop and output any remaining symbols from the stack.