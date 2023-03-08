 Here is the content in Markdown format:

### Shift reduce parsing

Shift reduce parsing is a bottom up parsing technique where the input is parsed from left to right. It uses a stack to keep track of intermediate results.

The basic steps involved are:

1. Scan the input from left to right.
2. If the token scanned is a terminal, push it onto the stack.
3. If the token is a non-terminal, pop two elements from the stack and combine them according to the production rule of the non-terminal. Push the resulting non-terminal back to the stack.
4. Repeat steps 2 and 3 until the input is scanned completely.
5. If the stack contains only the start symbol, then the input is syntactically correct else it is incorrect.

Advantages:

- Handles ambiguous grammars.
- Parses input efficiently compared to other methods.

Disadvantages:

- Difficult to implement.
- Prone to errors.

Applications: Used in compilers to parse the input and check for syntactic correctness.

[Detailed diagrams and examples can be added here]

### Operator precedence parsing

Operator precedence parsing is a type of bottom up parsing where the precedence and associativity of operators is used to resolve conflicts. The steps involved are:

1. Scan the input and push the operators and operands onto the stack.
2. While scanning, if two operators with equal precedence are encountered, syntax error.
3. If an operator with higher precedence than the top of stack is scanned, push it onto the stack.
4. If an operator with lower precedence than the top of stack is scanned, pop operators from the stack and combine them with operands until an operator with lower precedence or a left parenthesis is encountered. Then, push the scanned operator onto the stack.
5. Repeat steps 2-4 until the input is scanned.
6. Pop and combine remaining operators and operands.

[Detailed diagrams and examples can be added here]

Advantages:

- Handles expression with operators efficiently.

Disadvantages:

- Difficult to implement.
- Precedence and associativity rules must be explicitly defined.

Applications: Used in compilers to parse and evaluate expressions containing operators.