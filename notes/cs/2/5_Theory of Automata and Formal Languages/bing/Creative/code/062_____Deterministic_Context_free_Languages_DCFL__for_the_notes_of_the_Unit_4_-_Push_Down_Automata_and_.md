# Deterministic Context Free Languages (DCFL)

- Deterministic context-free languages (DCFL) are a proper subset of context-free languages (CFL).
- They are the context-free languages that can be accepted by a deterministic pushdown automaton (DPDA).
- DCFLs are always unambiguous, meaning that they admit an unambiguous grammar.
- DCFLs have some advantages over general CFLs, such as:
  - They can be recognized by a deterministic Turing machine in polynomial time and O(log2 n) space.
  - They can be parsed efficiently by using deterministic top-down or bottom-up parsing algorithms, such as LL or LR parsers.
  - They can be used to model some programming languages, such as Pascal and C.
- DCFLs have some limitations compared to general CFLs, such as:
  - They are not closed under union, intersection, complementation, or Kleene star.
  - They cannot express some natural languages, such as English.
  - They cannot model some programming languages, such as Lisp and Prolog.
- The set of DCFLs is closed under the following operations:
  - Concatenation
  - Reversal
  - Homomorphism
  - Inverse homomorphism
  - Substitution
  - Quotient with regular languages