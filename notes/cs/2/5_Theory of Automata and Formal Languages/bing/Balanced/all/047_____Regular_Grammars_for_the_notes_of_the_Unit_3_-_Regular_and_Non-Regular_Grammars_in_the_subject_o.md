# Regular Grammars

- A regular grammar is a grammar that is right-regular or left-regular.
- A grammar is right-regular if all production rules have at most one non-terminal symbol and that symbol is always at the end of the rule's right-hand side.
- A grammar is left-regular if all production rules have at most one non-terminal symbol and that symbol is always at the start of the rule's right-hand side.
- A regular grammar can be formally defined as a mathematical object, G, with four components, G = (N, Σ, P, S), where :
  - N is a nonempty, finite set of non-terminal symbols
  - Σ is a finite set of terminal symbols, or alphabet, symbols
  - P is a finite set of production rules of the form A → xB or A → x, where A and B are non-terminal symbols and x is a string of terminal symbols
  - S is a special non-terminal symbol called the start symbol
- A regular grammar can generate a regular language, which is a language that can be recognized by a finite automaton.
- A regular grammar can be converted to a regular expression, which is a concise way of describing a regular language using symbols and operators.
- A regular grammar can also be converted to a right-linear grammar or a left-linear grammar, which are equivalent forms of regular grammar with different conventions for the placement of non-terminal symbols.