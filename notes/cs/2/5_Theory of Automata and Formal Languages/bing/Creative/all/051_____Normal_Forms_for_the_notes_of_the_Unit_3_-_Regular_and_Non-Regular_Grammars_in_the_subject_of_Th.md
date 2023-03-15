# Normal Forms for the notes of the Unit 3 - Regular and Non-Regular Grammars in the subject of Theory of Automata and Formal Languages

- A normal form is a standard way of writing the production rules of a grammar that satisfies certain properties or constraints.
- Normal forms are useful for simplifying the analysis and manipulation of grammars, such as parsing, generating, and proving properties of languages.
- There are different types of normal forms for different types of grammars, such as regular, context-free, context-sensitive, and unrestricted grammars.
- Some of the most common normal forms for context-free grammars are Chomsky normal form and Greibach normal form.

## Chomsky normal form

- A context-free grammar is in Chomsky normal form if all of its production rules are of the form:

  - A → BC, where A, B, and C are nonterminal symbols
  - A → a, where A is a nonterminal symbol and a is a terminal symbol
  - S → ε, where S is the start symbol and ε is the empty string

- Any context-free grammar can be converted to an equivalent grammar in Chomsky normal form by applying a series of transformations, such as eliminating ε-productions, unit productions, and useless symbols, and introducing new nonterminal symbols.
- Chomsky normal form is useful for designing efficient parsing algorithms, such as the CYK algorithm, which can determine whether a given string belongs to the language of a grammar in Chomsky normal form in polynomial time.

## Greibach normal form

- A context-free grammar is in Greibach normal form if all of its production rules are of the form:

  - A → aα, where A is a nonterminal symbol, a is a terminal symbol, and α is a (possibly empty) string of nonterminal symbols

- Any context-free grammar can be converted to an equivalent grammar in Greibach normal form by applying a series of transformations, such as eliminating left recursion, left factoring, and introducing new nonterminal symbols.
- Greibach normal form is useful for designing recursive-descent parsing algorithms, which can construct a parse tree for a given string by recursively applying the production rules of the grammar.