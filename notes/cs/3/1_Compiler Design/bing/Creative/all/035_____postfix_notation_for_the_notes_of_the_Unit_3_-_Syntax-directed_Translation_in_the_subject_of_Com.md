# Postfix Notation

- Postfix notation is a way of writing arithmetic expressions without using parentheses or brackets.
- In postfix notation, the operator appears after the operands, i.e., the operator between operands is taken out and is attached after operands.
- For example, the infix expression `a * d - (b + c)` can be written in postfix notation as `a d * b c + -`.
- Postfix notation is also known as reverse Polish notation or suffix notation.
- Postfix notation has some advantages over infix notation, such as:
  - It is easier to parse for a machine, as there is no need to check the operator precedence or associativity.
  - It can be used to generate intermediate code in compiler design, as it reflects the order of evaluation of the operands and operators .
  - It can be evaluated using a stack data structure, by pushing the operands onto the stack and popping them when an operator is encountered.
- Postfix notation has some disadvantages over infix notation, such as:
  - It is less familiar and intuitive for human readers, as it does not follow the conventional order of writing arithmetic expressions.
  - It may require more space to write, as it may need more operators than infix notation.
  - It may not be suitable for function calls, as they are usually written in prefix notation, i.e., the operator before the operands.