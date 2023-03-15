### Top-Down Parsing for the Notes of the Unit 2 - Basic Parsing Techniques in the Subject of Compiler Design

- Top-down parsing is a method of parsing the input string provided by the lexical analyzer. The top-down parser parses the input string and then generates the parse tree for it. Construction of the parse tree starts from the root node i.e. the start symbol of the grammar.
- Top-down parsing is also called as predictive parsing or LL parsing.
- Top-down parsing can be done by two techniques: recursive descent parsing and non-recursive predictive parsing .
- Recursive descent parsing is a top-down parsing technique that constructs the parse tree from the top and the input is read from left to right. It uses procedures for every terminal and non-terminal entity. It is called recursive because it may call itself recursively to handle the sub-parts of the production .
- Non-recursive predictive parsing is a top-down parsing technique that avoids recursion and backtracking by using a stack and a parsing table. The parsing table is constructed by using the First and Follow sets of the grammar. It is also called as LL(1) parsing .
- Advantages of top-down parsing are: it is easy to implement, it can handle left recursion and left factoring, and it can detect syntax errors early in the input .
- Disadvantages of top-down parsing are: it may require backtracking which is inefficient, it cannot handle left recursive grammars, and it may generate multiple parse trees for ambiguous grammars .