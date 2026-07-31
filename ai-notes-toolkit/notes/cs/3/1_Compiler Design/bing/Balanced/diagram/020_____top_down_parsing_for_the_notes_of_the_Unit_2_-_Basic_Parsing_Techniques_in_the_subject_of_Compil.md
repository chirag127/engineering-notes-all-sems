### Top-Down Parsing for the Notes of the Unit 2 - Basic Parsing Techniques in the Subject of Compiler Design

- Top-down parsing is a method of parsing the input string provided by the lexical analyzer and generating a parse tree for it using leftmost derivation.
- Top-down parsing starts from the root node (start symbol) of the parse tree and expands it until all the leaves are terminals that match the input string.
- Top-down parsing can be classified into two types: recursive descent parsing and predictive parsing.
- Recursive descent parsing is a technique that uses a procedure for each non-terminal in the grammar. Each procedure tries to match the input string with the productions of the corresponding non-terminal.
- Recursive descent parsing may require backtracking, which is the process of returning to a previous choice point and trying a different alternative when the current choice fails to match the input string.
- Predictive parsing is a technique that avoids backtracking by using a look-ahead symbol to determine which production to apply. Predictive parsing requires the grammar to be LL(1), which means that the parser can decide the next production by looking at the next input symbol and the current non-terminal.
- Predictive parsing can be implemented by using a stack and a parsing table. The stack contains the symbols that need to be matched with the input string. The parsing table contains the productions for each non-terminal and terminal pair.
- The algorithm for predictive parsing is as follows:
  - Initialize the stack with the start symbol and the end-of-input marker ($).
  - Repeat the following steps until either the stack or the input is empty:
    - If the top of the stack is a terminal, compare it with the next input symbol. If they are the same, pop the stack and advance the input. Otherwise, report an error.
    - If the top of the stack is a non-terminal, look up the parsing table entry for the non-terminal and the next input symbol. If there is a production in the entry, pop the stack and push the right-hand side of the production in reverse order. Otherwise, report an error.
    - If the top of the stack is the end-of-input marker, check if the input is also empty. If yes, accept the input. Otherwise, report an error.