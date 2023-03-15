### a) Program to recognize a valid arithmetic expression that uses operator +, – , * and /.

A valid arithmetic expression is a string of characters that represents a mathematical calculation. The expression can contain numbers, operators, and parentheses. The operators that can be used in the expression are +, -, *, and /. The expression must follow the rules of arithmetic and the order of operations.

Here are the steps to recognize a valid arithmetic expression:

1. Check if the expression contains only numbers, operators, and parentheses. If it contains any other character, the expression is not valid.
2. Check if the parentheses are balanced. This means that for every opening parenthesis, there must be a corresponding closing parenthesis.
3. Check if the operators are used correctly. This means that there must be a number or a closing parenthesis before and after each operator.
4. Check if the expression follows the order of operations. This means that the operations inside the parentheses must be performed first, followed by multiplication and division, and finally addition and subtraction.

A program can be written to implement these steps and recognize if an arithmetic expression is valid or not. The program can use a stack data structure to keep track of the parentheses and the order of operations. The program can also use regular expressions to check if the expression contains only valid characters and if the operators are used correctly.