### 9. Write program to find Simulate First and Follow of any given grammar.

First and Follow are important concepts in the construction of predictive parsers for context-free grammars. Here is a brief overview of the steps to find the First and Follow of any given grammar:

1. **First**: The First of a symbol is the set of terminal symbols that can appear as the first symbol in a string derived from that symbol. To find the First of a non-terminal symbol, we can follow these steps:
    - If the symbol is a terminal, then the First of that symbol is the symbol itself.
    - If the symbol is a non-terminal, then for each production rule of the form `A -> aB`, where `a` is a string of terminals and non-terminals, we add the First of `a` to the First of `A`. If `a` is nullable (i.e., can derive the empty string), then we also add the First of `B` to the First of `A`.
    - Repeat the above step until no more terminals can be added to the First of any non-terminal.

2. **Follow**: The Follow of a symbol is the set of terminal symbols that can appear immediately after that symbol in a string derived from the start symbol. To find the Follow of a non-terminal symbol, we can follow these steps:
    - If the symbol is the start symbol, add the end-of-input marker to its Follow.
    - For each production rule of the form `A -> aBb`, where `a` and `b` are strings of terminals and non-terminals, add the First of `b` (excluding the empty string) to the Follow of `B`. If `b` is nullable, then also add the Follow of `A` to the Follow of `B`.
    - Repeat the above step until no more terminals can be added to the Follow of any non-terminal.

A program to find the First and Follow of any given grammar can be written using the above algorithms. The program would take as input the grammar rules and the start symbol, and output the First and Follow sets for each non-terminal symbol in the grammar. The implementation details may vary depending on the programming language used.