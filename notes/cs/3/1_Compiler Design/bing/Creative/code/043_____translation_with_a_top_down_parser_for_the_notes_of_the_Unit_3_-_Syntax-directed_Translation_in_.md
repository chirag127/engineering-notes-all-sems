### Translation with a top down parser

- Translation is the process of mapping an input string to an output string according to a set of rules.
- A top down parser is a type of parser that constructs a parse tree from the top (root) to the bottom (leaves) by applying the grammar rules in a leftmost derivation .
- A syntax-directed translation (SDT) is a method of translating an input string to an output string using attributes attached to the nodes of the parse tree .
- A top down parser can perform syntax-directed translation by evaluating the attributes of the nodes as they are created during the parsing process.
- The attributes can be evaluated in two ways: synthesized or inherited .
  - Synthesized attributes are computed from the attributes of the children nodes or the lexical values of the leaves .
  - Inherited attributes are computed from the attributes of the parent node or the siblings nodes .
- A top down parser can use the following steps to perform syntax-directed translation:
  - Define the grammar rules and the attributes for each non-terminal and terminal symbol.
  - Define the semantic actions to compute the attributes for each production.
  - Write a recursive-descent parser that matches the input string with the grammar rules.
  - Insert the semantic actions at appropriate places in the parser code.
  - Execute the parser and the semantic actions on the input string to produce the output string.