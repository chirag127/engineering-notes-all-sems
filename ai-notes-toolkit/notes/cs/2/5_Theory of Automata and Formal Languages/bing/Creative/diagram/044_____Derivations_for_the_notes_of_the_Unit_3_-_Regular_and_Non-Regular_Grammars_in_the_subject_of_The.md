### Derivations for the notes of the Unit 3 - Regular and Non-Regular Grammars in the subject of Theory of Automata and Formal Languages

- A derivation is a sequence of applications of the rules of a grammar that produces a finished string of terminals.
- A leftmost derivation is where we always substitute for the leftmost nonterminal as we apply the rules (we can similarly define a rightmost derivation).
- A derivation is also called a parse.
- A regular grammar is a formal grammar (N, Σ, P, S) in which all production rules in P are of one of the following forms:
  - A → a
  - A → aB
  - A → ε
  where A, B, S ∈ N are non-terminal symbols, a ∈ Σ is a terminal symbol, and ε denotes the empty string, i.e. the string of length 0.
- A regular grammar can be either right-regular or left-regular, depending on whether the non-terminal symbol is on the right or left side of the production rule.
- A regular grammar can generate a regular language, which is a language that can be recognized by a finite automaton.
- A non-regular grammar is a context-free grammar that cannot be expressed as a regular grammar.
- A non-regular grammar can generate a non-regular language, which is a language that cannot be recognized by a finite automaton.
- An ambiguous grammar is a context-free grammar for which there exists a string that has more than one leftmost derivation, while an unambiguous grammar is a context-free grammar for which every valid string has a unique leftmost derivation.
- A regular grammar is always unambiguous, but a non-regular grammar can be ambiguous or unambiguous.
- An example of a regular grammar is:
  - S → aA | bB | ε
  - A → aA | bB | ε
  - B → aB | bA | ε
- An example of a non-regular grammar is:
  - S → aSb | ε
- An example of an ambiguous grammar is:
  - S → S + S | S * S | a
- An example of an unambiguous grammar is:
  - E → E + T | T
  - T → T * F | F
  - F → (E) | a