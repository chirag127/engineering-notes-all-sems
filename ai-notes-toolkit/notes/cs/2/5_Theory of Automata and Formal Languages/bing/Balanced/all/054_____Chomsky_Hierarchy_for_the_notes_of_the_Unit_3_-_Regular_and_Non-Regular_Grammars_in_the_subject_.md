# Chomsky Hierarchy

- The Chomsky hierarchy is a containment hierarchy of classes of formal grammars, as described by Noam Chomsky in 1956 .
- It is an essential tool used in formal language theory, computer science, and linguistics .
- It can be represented in the form of a pyramid, with type 0 at the base and type 3 at the peak.
- Each type of grammar generates a class of language and is recognized by a type of automaton .
- The following table summarizes the four types of grammars, the languages they generate, the automata they recognize, and the form of their rules .

| Type | Grammar | Language | Automaton | Rule Form |
| --- | --- | --- | --- | --- |
| 0 | Unrestricted | Recursively enumerable | Turing machine | `α → β` |
| 1 | Context-sensitive | Context-sensitive | Linear bounded automaton | `αAβ → αγβ` |
| 2 | Context-free | Context-free | Pushdown automaton | `A → γ` |
| 3 | Regular | Regular | Finite state automaton | `A → aB` or `A → a` |

- The Chomsky hierarchy shows the relation between the complexity of the grammar and the language it generates.
- The higher the type, the more restricted the grammar and the simpler the language.
- The lower the type, the more expressive the grammar and the richer the language.
- The Chomsky hierarchy also shows the relation between the power of the automaton and the language it recognizes.
- The higher the type, the less powerful the automaton and the easier the recognition.
- The lower the type, the more powerful the automaton and the harder the recognition.
- The Chomsky hierarchy is useful for studying the properties and limitations of different classes of languages and grammars.
- It also helps to compare and contrast different models of computation and formalisms.
- It is relevant to natural language processing, as natural languages are often modeled by context-free grammars or their extensions.