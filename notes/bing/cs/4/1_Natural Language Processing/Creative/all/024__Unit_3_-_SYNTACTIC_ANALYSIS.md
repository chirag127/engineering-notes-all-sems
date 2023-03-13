## Unit 3 - SYNTACTIC ANALYSIS

- Syntactic analysis is the process of analyzing the structure and meaning of a sentence or a program based on a set of rules or grammar.
- Syntactic analysis is also known as parsing or compiler design.
- Syntactic analysis is important for natural language processing, artificial intelligence, and programming languages.
- Syntactic analysis can be divided into two main types: top-down parsing and bottom-up parsing.

### Top-down parsing
- Top-down parsing is a method of syntactic analysis that starts from the root or the start symbol of the grammar and tries to match the input string with the productions of the grammar.
- Top-down parsing can be implemented using recursive descent or table-driven methods.
- Recursive descent parsing is a technique that uses a set of recursive procedures, one for each non-terminal symbol, to parse the input string.
- Table-driven parsing is a technique that uses a stack and a parsing table to guide the parsing process.
- Advantages of top-down parsing:
  - It is easy to implement and understand.
  - It can handle left-recursive grammars.
  - It can produce leftmost derivations of the input string.
- Disadvantages of top-down parsing:
  - It may generate unnecessary backtracking or left-factoring.
  - It may not be efficient or optimal for some grammars.
  - It may not be able to handle ambiguous grammars.

### Bottom-up parsing
- Bottom-up parsing is a method of syntactic analysis that starts from the input string and tries to reduce it to the root or the start symbol of the grammar using the productions of the grammar.
- Bottom-up parsing can be implemented using shift-reduce or table-driven methods.
- Shift-reduce parsing is a technique that uses a stack and a set of actions (shift, reduce, accept, or error) to parse the input string.
- Table-driven parsing is a technique that uses a stack and a parsing table to guide the parsing process.
- Advantages of bottom-up parsing:
  - It can handle a larger class of grammars than top-down parsing.
  - It can produce rightmost derivations of the input string.
  - It can detect syntactic errors as soon as possible.
- Disadvantages of bottom-up parsing:
  - It is more complex and difficult to implement and understand than top-down parsing.
  - It may not be able to handle ambiguous grammars.
  - It may require more memory and time than top-down parsing.

### Mnemonics and learning tricks
- To remember the difference between top-down and bottom-up parsing, you can use the following mnemonics:
  - Top-down parsing is like building a tree from the top to the bottom, starting from the root and adding branches and leaves.
  - Bottom-up parsing is like pruning a tree from the bottom to the top, starting from the leaves and removing branches until reaching the root.
- To remember the difference between recursive descent and table-driven parsing, you can use the following mnemonics:
  - Recursive descent parsing is like following a recipe, where each step is a procedure that calls other procedures as needed.
  - Table-driven parsing is like following a map, where each step is a location that leads to other locations based on the directions.
- To remember the difference between shift-reduce and table-driven parsing, you can use the following mnemonics:
  - Shift-reduce parsing is like stacking and unstacking plates, where each plate is a symbol and each action is a movement of the plates.
  - Table-driven parsing is like playing a board game, where each symbol is a piece and each action is a move of the pieces based on the rules.