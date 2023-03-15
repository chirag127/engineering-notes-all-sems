### Chomsky Hierarchy

- The Chomsky hierarchy is a containment hierarchy of classes of formal grammars, as described by Noam Chomsky in 1956 .
- It is an essential tool used in formal language theory, computer science, and linguistics .
- It can be represented in the form of a pyramid, with type 0 at the base and type 3 at the peak.
- The following table summarizes each of Chomsky's four types of grammars, the class of language it generates, the type of automaton that recognizes it, and the form its rules must have .

| Type | Grammar | Language | Automaton | Rule Form |
| --- | --- | --- | --- | --- |
| 0 | Unrestricted | Recursively enumerable | Turing machine | α → β |
| 1 | Context-sensitive | Context-sensitive | Linear bounded automaton | αAβ → αγβ |
| 2 | Context-free | Context-free | Pushdown automaton | A → γ |
| 3 | Regular | Regular | Finite automaton | A → aB or A → a |

- The Chomsky hierarchy shows that the classes of languages are nested, meaning that every regular language is also context-free, every context-free language is also context-sensitive, and every context-sensitive language is also recursively enumerable .
- However, the converse is not true, meaning that there are languages that are not regular but context-free, not context-free but context-sensitive, and not context-sensitive but recursively enumerable .
- The Chomsky hierarchy is useful for understanding the expressive power and computational complexity of different types of grammars and languages .
- It also helps to analyze natural languages and design artificial languages for various applications .