### Predictive Parsers

- A predictive parser is a type of top-down parser that does not require backtracking or backup.
- A predictive parser can predict which production to use by looking at the next input symbol and the current non-terminal.
- A predictive parser can be implemented by a recursive descent parser or a table-driven parser.
- A predictive parser can only handle a subset of context-free grammars, called LL(1) grammars.
- LL(1) grammars have the property that for each non-terminal A and each input symbol a, there is at most one production A -> α that can be applied.
- To construct a predictive parser for an LL(1) grammar, we need to compute two functions: FIRST and FOLLOW.
- FIRST(α) is the set of terminals that can begin a string derived from α, where α is any string of grammar symbols.
- FOLLOW(A) is the set of terminals that can appear immediately to the right of A in some sentential form, where A is any non-terminal.
- Using these functions, we can construct a parsing table M[A, a] that maps each pair of non-terminal A and input symbol a to a production A -> α or an error.
- The predictive parsing algorithm works as follows:
  - Initialize a pointer ip to point to the first symbol of the input string, and a stack to contain the start symbol of the grammar.
  - Repeat until the end of input or an error occurs:
    - Pop the top symbol X from the stack.
    - If X is a terminal, match it with the current input symbol pointed by ip and advance ip to the next symbol.
    - If X is a non-terminal, look up the entry M[X, a] in the parsing table, where a is the current input symbol pointed by ip.
      - If M[X, a] = X -> α, push the symbols of α in reverse order onto the stack.
      - If M[X, a] = error, report a syntax error and terminate the parsing.
    - If X is the end-of-input marker, accept the input as valid and terminate the parsing.