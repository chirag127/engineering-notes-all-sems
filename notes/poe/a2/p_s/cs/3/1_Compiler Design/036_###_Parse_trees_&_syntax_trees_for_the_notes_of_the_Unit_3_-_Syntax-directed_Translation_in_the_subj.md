 Here is the content in markdown format for the given topic:

### Parse trees & syntax trees

A parse tree or syntax tree is a structural representation of the input string of a language that shows the syntactic structure of the string. They are used to represent the structure of the input string in a tree-like format.

- Parse trees show the syntactic structure of the input string. They have the following properties:
- The root node represents the start symbol of the grammar.
- Each internal node is labeled by a grammar symbol and has a number of children corresponding to the symbols on the right-hand side of the grammar rule.
- The leaf nodes are labeled by the terminal symbols and correspond to the input strings.
- Syntax trees are a collapsed form of the parse tree where the nodes are labeled by the lexical categories of their constituents and functional information is added. They provide an interface between the parsing process and semantic interpretation.

Parse trees are generally used for showing the derivation of the input string while syntax trees are used to add additional semantic information for further processing. Both are useful representations to understand the structural organization of the input string as per the grammar rules. They help in implementing parsers and understanding the translation of the source code.

Advantages:
- Help understand the structure of the input string.
- Aid in implementing parsers.
- Provide a link between syntax and semantics.

Disadvantages:
- Can become quite large and complex for practical grammars and input strings.
- Do not show the ordering of siblings. The ordering of siblings is lost in the tree structure.

Examples of parse trees and syntax trees can be shown using ASCII diagrams for expressions, statements, etc. They can be useful to understand the concept and process of parsing.

Applications:
- Used in compiler design for implementing parsers.
- Help understand the conversion of the source code to the intermediate representation.
- Aid in translating the structural syntax of the input to semantics.