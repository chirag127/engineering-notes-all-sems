# Decision Properties for the Notes of the Unit 2 - Regular Expressions and Languages in the Subject of Theory of Automata and Formal Languages

- Decision properties are questions that can be answered yes or no for a given language or a class of languages.
- For example, given a regular expression R, is the language L(R) empty? Or, given two regular expressions R1 and R2, are the languages L(R1) and L(R2) equal?
- Decision properties are important for analyzing and manipulating languages and their representations, such as regular expressions and finite automata.
- Some common decision properties for regular languages are:

  - Emptiness: Given a regular expression R, is L(R) = ∅?
  - Non-emptiness: Given a regular expression R, is L(R) ≠ ∅?
  - Finiteness: Given a regular expression R, is L(R) finite?
  - Infiniteness: Given a regular expression R, is L(R) infinite?
  - Membership: Given a regular expression R and a string w, is w ∈ L(R)?
  - Equality: Given two regular expressions R1 and R2, is L(R1) = L(R2)?
  - Containment: Given two regular expressions R1 and R2, is L(R1) ⊆ L(R2)?
  - Disjointness: Given two regular expressions R1 and R2, is L(R1) ∩ L(R2) = ∅?

- All these decision properties are decidable for regular languages, meaning that there exists an algorithm that can answer them in finite time.
- One way to decide these properties is to convert the regular expressions to deterministic finite automata (DFA) and use the properties and operations of DFA to answer the questions.
- For example, to decide emptiness, we can convert R to a DFA A and check if the set of final states of A is empty or not.
- To decide equality, we can convert R1 and R2 to DFA A1 and A2 and check if the symmetric difference of L(A1) and L(A2) is empty or not. This can be done by constructing a DFA for L(A1) ∆ L(A2) and applying the emptiness test.
- To decide membership, we can convert R to a DFA A and simulate the input w on A and check if it reaches a final state or not.