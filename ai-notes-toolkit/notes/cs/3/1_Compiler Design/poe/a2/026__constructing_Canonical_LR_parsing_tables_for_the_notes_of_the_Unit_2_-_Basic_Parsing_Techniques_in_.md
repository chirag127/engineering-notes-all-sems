 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Constructing Canonical LR Parsing Tables

1. Find the DOT(.) items of the grammar. These are essentially the states of the machine.
2. Find the goto transitions between states. These transitions are based on the next available input.
3. Find the reduce transitions. These occur when a state contains a complete right-hand side of a production. The state must then transition to the state corresponding to the left-hand side of the production.
4. Arrange the states in a table as per the canonical LR algorithm. The states are arranged in rows and columns based on the input symbol. Transitions are marked in the cells.
5. Resolve any conflicts -Shift/Reduce or Reduce/Reduce. This is done based on precedences assigned to the grammar symbols.

The canonical LR parsing algorithm allows us to algorithmically construct the LR parsing table for any context-free grammar. This table can then be used by the LR parser to efficiently parse the input string and derive the parse tree.

How's this? I have written the points in a formal tone without any emojis or external links as requested. Let me know if you would like me to modify or expand the content.