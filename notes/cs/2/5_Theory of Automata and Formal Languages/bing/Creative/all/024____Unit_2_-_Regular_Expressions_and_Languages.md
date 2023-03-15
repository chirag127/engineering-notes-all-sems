# Unit 2 - Regular Expressions and Languages

## Objectives
- To understand the concept of regular expressions and how they can be used to describe regular languages.
- To learn the syntax and semantics of regular expressions and how to construct them from simpler components.
- To learn how to convert regular expressions to finite automata and vice versa.
- To learn how to apply regular expressions to pattern matching and text processing problems.

## Contents
- Regular expressions are a concise and powerful notation for specifying sets of strings, also known as regular languages.
- Regular expressions can be defined recursively as follows:
  - The empty set ∅, the empty string ε, and any single symbol a are regular expressions.
  - If r and s are regular expressions, then so are (r + s), (r · s), and (r*), where + denotes union, · denotes concatenation, and * denotes Kleene closure.
  - Nothing else is a regular expression.
- The meaning of a regular expression is the set of strings that it describes, also known as the language of the regular expression.
- The language of a regular expression can be defined recursively as follows:
  - L(∅) = ∅, L(ε) = {ε}, and L(a) = {a} for any symbol a.
  - L(r + s) = L(r) ∪ L(s), L(r · s) = L(r) · L(s), and L(r*) = L(r)*, where ∪ denotes set union, · denotes set concatenation, and * denotes set closure.
  - Nothing else is a language of a regular expression.
- Regular expressions can be simplified and manipulated using various laws and properties, such as:
  - Idempotence: r + r = r
  - Commutativity: r + s = s + r
  - Associativity: (r + s) + t = r + (s + t) and (r · s) · t = r · (s · t)
  - Distributivity: r · (s + t) = (r · s) + (r · t) and (r + s) · t = (r · t) + (s · t)
  - Identity: r · ε = ε · r = r
  - Annihilation: r · ∅ = ∅ · r = ∅
  - Zero or more: r* = ε + r · r*
  - One or more: r+ = r · r*
  - Optional: r? = ε + r
- Regular expressions can be converted to finite automata using various algorithms, such as:
  - Thompson's construction: This algorithm constructs a nondeterministic finite automaton (NFA) with ε-transitions from a regular expression by applying a set of rules for each operator in the regular expression.
  - Glushkov's construction: This algorithm constructs a deterministic finite automaton (DFA) from a regular expression by computing the sets of first, last, and follow positions for each symbol in the regular expression.
  - McNaughton-Yamada-Thompson algorithm: This algorithm constructs a DFA from a regular expression by first applying Thompson's construction to obtain an NFA with ε-transitions, then eliminating the ε-transitions, and then minimizing the resulting NFA.
- Finite automata can be converted to regular expressions using various algorithms, such as:
  - State elimination: This algorithm eliminates states from a finite automaton one by one and replaces the transitions involving the eliminated state with regular expressions until only the initial and final states remain.
  - Kleene's theorem: This theorem states that for any finite automaton, there exists a regular expression that describes the same language as the finite automaton. The proof of this theorem provides a method to construct such a regular expression by using a system of equations involving regular expressions.
- Regular expressions can be used to solve various problems involving pattern matching and text processing, such as:
  - Finding all occurrences of a pattern in a text.
  - Validating the format of an input string.
  - Extracting information from a text.
  - Replacing or modifying parts of a text.