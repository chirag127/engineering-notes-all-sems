### Translation with a top down parser

- Translation is the process of mapping an input string to an output string according to a set of rules or a grammar.
- A top down parser is a type of parser that constructs a parse tree from the root node (the start symbol of the grammar) to the leaf nodes (the input string) by using leftmost derivation.
- A syntax-directed translation (SDT) is a method of translating an input string to an output string by attaching attributes and actions to the grammar symbols and rules.
- A top down parser can perform syntax-directed translation by passing information bottom-up and/or top-down to the parse tree in form of attributes attached to the nodes.
- The attributes can be either synthesized or inherited. Synthesized attributes are computed from the attributes of the children nodes, while inherited attributes are computed from the attributes of the parent or sibling nodes.
- The actions can be either semantic or inherited. Semantic actions are executed when a production is applied, while inherited actions are executed when a node is visited.
- The following steps are involved in translating an input string with a top down parser:

  1. Initialize the attributes of the root node with the given values or constants.
  2. Read the input string from left to right and match it with the grammar symbols.
  3. Apply the productions that match the input string and construct the parse tree from top to bottom.
  4. Execute the semantic actions associated with the applied productions and compute the synthesized attributes of the nodes.
  5. Execute the inherited actions associated with the visited nodes and compute the inherited attributes of the nodes.
  6. Output the translated string using the attributes of the nodes.