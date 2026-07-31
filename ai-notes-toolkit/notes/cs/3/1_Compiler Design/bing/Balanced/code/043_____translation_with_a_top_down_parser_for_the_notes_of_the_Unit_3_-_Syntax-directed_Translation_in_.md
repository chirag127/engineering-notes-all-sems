### Translation with a top down parser

- Translation is the process of mapping an input string to an output string according to a set of rules or a grammar.
- A top down parser is a type of parser that constructs a parse tree from the root node (the start symbol of the grammar) to the leaf nodes (the input string) by using leftmost derivation.
- A syntax-directed translation (SDT) is a method of attaching semantic actions to the grammar rules and executing them during the parsing process to produce the output string.
- A semantic action is a piece of code that performs some computation or operation on the input string, the parse tree, or the attributes of the nodes.
- An attribute is a value associated with a node of the parse tree that stores some information about the node or its subtree.
- There are two types of attributes: synthesized attributes and inherited attributes.
- A synthesized attribute is an attribute that depends only on the attributes of the children of the node.
- An inherited attribute is an attribute that depends on the attributes of the parent or siblings of the node.
- A top down parser can implement SDT by using two techniques: recursive descent parsing and predictive parsing.
- A recursive descent parser is a type of top down parser that uses a set of mutually recursive procedures, one for each nonterminal of the grammar, to parse the input string and execute the semantic actions.
- A predictive parser is a type of top down parser that uses a parsing table, which is constructed from the grammar using the First and Follow sets of the nonterminals, to determine which production to apply and which semantic action to execute at each step of the parsing process.