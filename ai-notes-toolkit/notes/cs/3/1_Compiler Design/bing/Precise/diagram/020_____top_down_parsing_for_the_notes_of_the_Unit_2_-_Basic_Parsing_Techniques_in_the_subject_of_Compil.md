### Top Down Parsing

Top-down parsing is a parsing technique that starts from the start symbol and derives the input string by applying production rules. It is also known as recursive-descent parsing or predictive parsing.

Here are some key points to remember about top-down parsing:

1. Top-down parsing constructs a parse tree from the top to the bottom, starting with the start symbol.
2. It uses a leftmost derivation, which means that the leftmost non-terminal symbol is always expanded first.
3. Top-down parsing can be implemented using a recursive-descent parser, which is a type of parser that consists of a set of mutually recursive procedures, one for each non-terminal symbol in the grammar.
4. Predictive parsing is a type of top-down parsing that uses a parsing table to determine which production rule to apply based on the current non-terminal symbol and the next input symbol.
5. Top-down parsing can handle left-recursive grammars, but it may result in infinite recursion. To avoid this, left recursion must be eliminated from the grammar before using top-down parsing.
