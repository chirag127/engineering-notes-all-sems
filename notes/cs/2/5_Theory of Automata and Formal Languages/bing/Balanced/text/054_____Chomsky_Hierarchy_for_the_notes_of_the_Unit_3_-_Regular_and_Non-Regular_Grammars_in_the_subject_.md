### Chomsky Hierarchy

- The Chomsky hierarchy is a **containment hierarchy** of classes of formal grammars, as described by Noam Chomsky in 1956 .
- It is an essential tool used in formal language theory, computer science, and linguistics.
- This unique structure can be represented in the form of a **pyramid**, with type 0 at the base and type 3 at the peak.
- The following table summarizes each of Chomsky's four types of grammars, the class of language it generates, the type of automaton that recognizes it, and the form its rules must have .

| Type | Grammar | Language | Automaton | Rule Form |
| --- | --- | --- | --- | --- |
| 0 | Unrestricted | Recursively enumerable | Turing machine | α → β |
| 1 | Context-sensitive | Context-sensitive | Linear bounded automaton | αAβ → αγβ |
| 2 | Context-free | Context-free | Pushdown automaton | A → γ |
| 3 | Regular | Regular | Finite automaton | A → aB |
|  |  |  |  | A → a |

- The Chomsky hierarchy shows that **every regular language is context-free, every context-free language is context-sensitive, and every context-sensitive language is recursively enumerable** .
- However, the converse is not true, meaning that there are languages that are not regular but context-free, not context-free but context-sensitive, and not context-sensitive but recursively enumerable .
- The Chomsky hierarchy is relevant to natural language processing because it can help us model the syntax and semantics of natural languages using formal grammars.
- For example, regular grammars are too simple to capture the recursive nature of natural languages, while unrestricted grammars are too complex and undecidable.
- Context-free grammars are often used to describe the syntax of natural languages, while context-sensitive grammars can capture some semantic constraints.