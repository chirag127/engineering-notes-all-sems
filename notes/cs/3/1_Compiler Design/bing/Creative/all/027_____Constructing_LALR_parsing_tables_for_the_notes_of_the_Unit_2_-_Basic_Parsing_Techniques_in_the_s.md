# Constructing LALR parsing tables

- LALR stands for Lookahead LR, which is a type of bottom-up parser that can handle a large class of context-free grammars.
- LALR parsing tables are constructed from the canonical collection of LR(1) items, which are sets of items that represent the possible states of the parser and the lookahead symbols that determine the next action.
- An item is a production with a dot (.) indicating the position of the parser in the right-hand side of the production. A lookahead symbol is a terminal that can follow the production in a valid derivation.
- The canonical collection of LR(1) items is obtained by applying two operations: closure and goto. Closure adds items that can be derived from the current items by expanding the nonterminal after the dot. Goto moves the dot one position to the right for a given symbol and returns a new set of items.
- The canonical collection of LR(1) items forms the states of the LALR parser. Each state has a number and a set of items. The transitions between states are labeled by the symbols that cause the goto operation.
- The LALR parsing table has two parts: the action table and the goto table. The action table specifies what the parser should do (shift, reduce, accept, or error) for each state and lookahead symbol. The goto table specifies the next state for each state and nonterminal symbol.
- To construct the LALR parsing table, we follow these steps:
  - For each state and terminal symbol, we check the items in the state and assign an action according to these rules:
    - If there is an item of the form A -> α.aβ, where a is the terminal symbol, we assign a shift action and the state number that is the result of the goto operation on a.
    - If there is an item of the form A -> α., where a is the lookahead symbol, we assign a reduce action and the production number A -> α.
    - If there is an item of the form S' -> S., where a is the end-of-input symbol ($), we assign an accept action.
    - If there is no item that matches any of the above rules, we assign an error action.
  - For each state and nonterminal symbol, we check the result of the goto operation on the symbol and assign the state number to the goto table.
  - If there are multiple actions assigned to the same entry of the action table, we have a conflict, which means the grammar is not LALR(1). We can try to resolve the conflict by using precedence and associativity rules, or by modifying the grammar.
- An example of constructing an LALR parsing table is shown below:

![LALR parsing table example](https://www.codeproject.com/KB/recipes/252399/LALRTable.png)