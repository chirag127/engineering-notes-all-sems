
### Postfix Notation for Unit 3 - Syntax-Directed Translation in Compiler Design

1. Postfix notation, also known as reverse Polish notation, is a way of representing arithmetic expressions in which the operator follows its operands. 

2. It is a notation in which each operator follows all of its operands. This is in contrast to the more common infix notation, where operators are placed between operands.

3. Postfix notation is useful for writing expressions in a syntax-directed translation as it eliminates the need for parentheses.

4. Postfix notation is also known as a stack-based notation, as it is based on the use of a stack. 

5. To evaluate an expression written in postfix notation, the computer scans the expression from left to right. 

6. When the computer encounters an operand, it is pushed onto the stack. 

7. When the computer encounters an operator, it pops the top two operands off the stack, applies the operator to them, and pushes the result back onto the stack. 

8. After the expression is evaluated, the result will be the only item left on the stack.