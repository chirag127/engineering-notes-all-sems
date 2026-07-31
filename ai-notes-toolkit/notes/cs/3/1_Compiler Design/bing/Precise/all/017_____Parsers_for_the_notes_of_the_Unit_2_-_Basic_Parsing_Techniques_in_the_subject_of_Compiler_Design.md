# Parsers for the notes of the Unit 2 - Basic Parsing Techniques in the subject of Compiler Design

A parser is a software component that takes input data (frequently text) and builds a data structure – often some kind of parse tree, abstract syntax tree or other hierarchical structure, giving a structural representation of the input while checking for correct syntax.

There are two main types of parsing techniques:
1. Top-down parsing: This type of parsing starts from the start symbol and tries to transform it into the input string by using the productions in reverse. The parser chooses a production and tries to match the input. If the chosen production is incorrect, the parser must backtrack and try another production. Recursive descent parsing is an example of top-down parsing.
2. Bottom-up parsing: This type of parsing starts from the input symbols and tries to construct the parse tree up to the start symbol. The parser tries to find the right-most derivations of the input string in reverse. Shift-reduce parsing is an example of bottom-up parsing.

Both top-down and bottom-up parsing techniques have their advantages and disadvantages. The choice of parsing technique depends on the specific requirements of the language being parsed. For example, top-down parsing is more intuitive and easier to implement, but may not be able to handle left-recursive grammars. Bottom-up parsing, on the other hand, can handle a wider range of grammars, but may be more complex to implement.