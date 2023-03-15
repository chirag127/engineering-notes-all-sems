# Deterministic Context Free Languages (DCFL)

- Deterministic context free languages (DCFL) are a proper subset of context free languages (CFL).
- They are the context free languages that can be accepted by a deterministic pushdown automaton (DPDA).
- A DPDA is a pushdown automaton (PDA) that has at most one transition for each combination of input symbol, current state, and top stack symbol.
- DCFLs are always unambiguous, meaning that they admit an unambiguous grammar. An unambiguous grammar is a grammar that generates only one parse tree for each string in the language.
- DCFLs have some properties that make them easier to process than general CFLs. For example:
  - DCFLs can be recognized by a deterministic Turing machine in polynomial time and O(log2 n) space.
  - DCFLs are closed under the following operations: union, intersection with a regular language, concatenation, Kleene star, reversal, and complement.
  - DCFLs have a unique minimal DPDA for each language, up to state renaming.
  - DCFLs can be parsed in linear time using a variant of the LR parsing algorithm.
- Some examples of DCFLs are:
  - The set of all palindromes over a finite alphabet.
  - The set of all strings of balanced parentheses.
  - The set of all strings of the form a^n b^n, where n is a positive integer.
  - The set of all strings of the form a^n b^m c^n, where n and m are positive integers.