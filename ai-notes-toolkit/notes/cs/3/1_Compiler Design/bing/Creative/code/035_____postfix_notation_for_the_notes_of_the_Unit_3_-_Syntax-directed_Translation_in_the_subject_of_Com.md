### Postfix Notation for the Notes of the Unit 3 - Syntax-directed Translation in the Subject of Compiler Design

- Postfix notation is a way of writing expressions where the operator appears after the operands, instead of between them as in infix notation. For example, the infix expression `a * d - (b + c)` can be written in postfix notation as `a d * b c + -`.
- Postfix notation is also known as reverse Polish notation or suffix notation. It is used in intermediate code generation in compiler design because it has some advantages over infix notation, such as:
  - It does not require parentheses to indicate the order of operations, since the position of the operator determines the scope of its operands.
  - It is easier to parse for a machine, since there is no ambiguity about the operator precedence or associativity. The evaluation of a postfix expression can be done using a stack data structure, where operands are pushed onto the stack and operators pop and operate on the topmost operands.
  - It is closer to the assembly language or machine code, where operands are usually stored in registers or memory locations and operators are instructions that operate on them.
- To convert an infix expression to a postfix expression, one can use the following algorithm:
  - Scan the infix expression from left to right.
  - If the scanned symbol is an operand, output it.
  - If the scanned symbol is an opening parenthesis `(`, push it onto the stack.
  - If the scanned symbol is a closing parenthesis `)`, pop and output all the symbols from the stack until an opening parenthesis is encountered. Discard both the parentheses.
  - If the scanned symbol is an operator, then:
    - If the stack is empty or the top of the stack is an opening parenthesis, push the operator onto the stack.
    - If the operator has higher precedence than the top of the stack, push the operator onto the stack.
    - If the operator has lower or equal precedence than the top of the stack, pop and output the top of the stack and repeat this step until the stack is empty or the operator has higher precedence than the top of the stack. Then push the operator onto the stack.
  - After scanning the entire infix expression, pop and output all the remaining symbols from the stack.
- For example, to convert the infix expression `a * (b + c) / d - e` to postfix notation, we can apply the algorithm as follows:

| Infix Expression | Stack | Postfix Expression |
| ---------------- | ----- | ------------------ |
| a * (b + c) / d - e | | |
| * (b + c) / d - e | a | a |
| (b + c) / d - e | a * | a |
| b + c) / d - e | a * ( | a |
| + c) / d - e | a * ( b | a b |
| c) / d - e | a * ( b + | a b |
| ) / d - e | a * ( b + c | a b c |
| / d - e | a * | a b c + |
| d - e | a * / | a b c + |
| - e | a * / d | a b c + / |
| e | a * / d - | a b c + / |
| | a * / d - e | a b c + / |
| | | a b c + / e - |

- The final postfix expression is `a b c + / e -`.