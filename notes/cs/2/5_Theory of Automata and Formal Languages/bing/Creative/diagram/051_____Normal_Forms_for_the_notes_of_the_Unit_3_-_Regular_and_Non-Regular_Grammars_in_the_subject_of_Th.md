### Normal Forms

- A normal form is a standard way of writing the production rules of a grammar to simplify its analysis and manipulation.
- Normal forms can also help in designing efficient parsing algorithms for context-free languages.
- There are different types of normal forms for different classes of grammars, such as regular, context-free, context-sensitive, etc.
- Two common normal forms for context-free grammars are Chomsky normal form and Greibach normal form.

#### Chomsky Normal Form

- A context-free grammar is in Chomsky normal form if all its production rules are of the form:

  - A → BC, where A, B, and C are non-terminal symbols
  - A → a, where A is a non-terminal symbol and a is a terminal symbol
  - S → ε, where S is the start symbol and ε is the empty string

- Any context-free grammar can be converted to an equivalent grammar in Chomsky normal form by applying a series of transformations, such as eliminating ε-productions, unit productions, and useless symbols, and introducing new non-terminal symbols.
- A grammar in Chomsky normal form can be parsed in polynomial time using the CYK algorithm, which is a dynamic programming technique that uses a table to store the results of subproblems.

#### Greibach Normal Form

- A context-free grammar is in Greibach normal form if all its production rules are of the form:

  - A → aα, where A is a non-terminal symbol, a is a terminal symbol, and α is a string of non-terminal symbols

- Any context-free grammar can be converted to an equivalent grammar in Greibach normal form by applying a series of transformations, such as eliminating left recursion, left factoring, and introducing new non-terminal symbols.
- A grammar in Greibach normal form can be parsed in linear time using a recursive-descent parser, which is a top-down technique that uses a stack to store the remaining symbols to be matched.