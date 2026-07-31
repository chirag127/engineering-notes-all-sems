# Predictive Parsers

- A predictive parser is a type of top-down parser that does not require backtracking or backup  .
- A predictive parser can predict which production to use by looking at the next input symbol .
- A predictive parser uses a look-ahead pointer to point to the next input symbol.
- A predictive parser can be implemented by a recursive descent parser or a table-driven parser  .
- A predictive parser can only handle a subset of context-free grammars called LL(1) grammars .
- A predictive parser has the following advantages:
  - It is simple and easy to implement .
  - It does not suffer from backtracking or ambiguity .
  - It can handle left recursion and left factoring .
- A predictive parser has the following disadvantages:
  - It cannot handle all context-free grammars .
  - It may require grammar transformations to make it LL(1) .
  - It may produce a large parsing table .
- A predictive parser algorithm can be summarized as follows:
  - Make a transition diagram (DFA/NFA) for every rule of grammar.
  - Optimize the DFA by reducing the number of states, yielding the final transition diagram.
  - Simulate the string on the transition diagram to parse a string.