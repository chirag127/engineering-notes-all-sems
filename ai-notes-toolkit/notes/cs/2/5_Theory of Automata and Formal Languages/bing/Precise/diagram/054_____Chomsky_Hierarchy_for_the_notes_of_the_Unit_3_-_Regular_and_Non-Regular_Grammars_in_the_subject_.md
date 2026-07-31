### Chomsky Hierarchy

The Chomsky Hierarchy is a containment hierarchy of classes of formal grammars. This hierarchy of grammars was described by Noam Chomsky in 1956. It is an essential tool used in formal language theory, computer science, and linguistics.

- The hierarchy can be represented in the form of a pyramid, with type 0 at the base and type 3 at the peak.
- Type 0 is known as unrestricted grammar.
- Type 1 is known as context-sensitive grammar.
- Type 2 is known as a context-free grammar.
- Type 3 is known as Regular Grammar.

The following table summarizes each of Chomsky's four types of grammars, the class of language it generates, the type of automaton that recognizes it, and the form its rules must have.

| Type | Grammar | Language | Automaton | Rule Form |
|------|---------|----------|-----------|-----------|
| 0 | Unrestricted | Recursively Enumerable | Turing Machine | α → β |
| 1 | Context-Sensitive | Context-Sensitive | Linear Bounded Automaton | αAβ → αγβ |
| 2 | Context-Free | Context-Free | Pushdown Automaton | A → γ |
| 3 | Regular | Regular | Finite Automaton | A → aB or A → a |