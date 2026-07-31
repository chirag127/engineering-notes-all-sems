### Top-Down Parsing for the Notes of the Unit 2 - Basic Parsing Techniques in the Subject of Compiler Design

- Top-down parsing is a method of parsing the input string provided by the lexical analyzer and generating a parse tree for it using leftmost derivation.
- Top-down parsing starts from the root node (start symbol) and expands it using the grammar productions until all the leaves are terminals that match the input string.
- Top-down parsing can be classified into two types: recursive descent parsing and predictive parsing.
- Recursive descent parsing is a top-down parsing technique that uses a procedure for each non-terminal in the grammar. Each procedure tries to match the input string with the right-hand side of the production for that non-terminal.
- Recursive descent parsing may require backtracking, which means undoing the previous choices and trying other alternatives, if the input string does not match the expected production.
- Predictive parsing is a top-down parsing technique that does not require backtracking. It uses a parsing table and a stack to determine which production to apply next based on the current input symbol and the top of the stack.
- Predictive parsing can only be applied to a special class of grammars called LL(1) grammars, which have the following properties:
  - They are unambiguous, which means there is only one possible parse tree for any input string.
  - They are left-factored, which means there is no common prefix in the right-hand side of any two productions for the same non-terminal.
  - They do not have left recursion, which means there is no production of the form A -> Aα, where A is a non-terminal and α is a string of terminals and non-terminals.