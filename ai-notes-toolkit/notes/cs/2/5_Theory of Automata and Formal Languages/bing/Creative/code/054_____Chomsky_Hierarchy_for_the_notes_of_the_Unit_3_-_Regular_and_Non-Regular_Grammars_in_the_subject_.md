# Chomsky Hierarchy

- The Chomsky hierarchy is a containment hierarchy of classes of formal grammars, as described by Noam Chomsky in 1956 .
- It is an essential tool used in formal language theory, computer science, and linguistics .
- It can be represented in the form of a pyramid, with type 0 at the base and type 3 at the peak.
- Each type of grammar generates a class of language that is recognized by a type of automaton .
- The following table summarizes the four types of grammars, the languages they generate, the automata that recognize them, and the form of their rules .

| Type | Grammar | Language | Automaton | Rule Form |
| --- | --- | --- | --- | --- |
| 0 | Unrestricted | Recursively enumerable | Turing machine | α → β |
| 1 | Context-sensitive | Context-sensitive | Linear bounded automaton | αAβ → αγβ |
| 2 | Context-free | Context-free | Pushdown automaton | A → γ |
| 3 | Regular | Regular | Finite automaton | A → aB or A → a |

- The Chomsky hierarchy implies that every regular language is context-free, every context-free language is context-sensitive, and every context-sensitive language is recursively enumerable .
- However, the converse is not true, meaning that there are languages that are not regular but context-free, not context-free but context-sensitive, and not context-sensitive but recursively enumerable .
- The Chomsky hierarchy is useful for understanding the expressive power and computational complexity of different classes of languages and grammars .
- It is also relevant for natural language processing, as natural languages can be modeled by different types of grammars depending on the level of analysis.