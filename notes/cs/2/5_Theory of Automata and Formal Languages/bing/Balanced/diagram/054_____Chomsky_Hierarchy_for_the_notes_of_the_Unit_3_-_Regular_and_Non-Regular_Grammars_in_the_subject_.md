### Chomsky Hierarchy

- The Chomsky hierarchy is a classification of formal languages based on the types of grammars that generate them .
- A grammar is a set of rules that describe how to form valid sentences from a given alphabet of symbols .
- The Chomsky hierarchy consists of four types of grammars, numbered from 0 to 3, with type 0 being the most general and type 3 being the most restricted  .
- The following table summarizes the main characteristics of each type of grammar, the class of language it generates, and the type of automaton that recognizes it  .

| Type | Grammar | Language | Automaton | Rule Form |
| --- | --- | --- | --- | --- |
| 0 | Unrestricted | Recursively enumerable | Turing machine | `α → β` |
| 1 | Context-sensitive | Context-sensitive | Linear bounded automaton | `αAβ → αγβ` |
| 2 | Context-free | Context-free | Pushdown automaton | `A → γ` |
| 3 | Regular | Regular | Finite automaton | `A → aB` or `A → a` |

- In the rule form column, `α`, `β`, and `γ` are strings of symbols, `A` and `B` are non-terminal symbols, and `a` is a terminal symbol .
- The Chomsky hierarchy is a containment hierarchy, meaning that every regular language is also context-free, every context-free language is also context-sensitive, and every context-sensitive language is also recursively enumerable  .
- However, the converse is not true, meaning that there are languages that are not regular, not context-free, or not context-sensitive  .
- The Chomsky hierarchy is useful for studying the properties and limitations of different types of languages and grammars, as well as for designing and analyzing algorithms and models for natural language processing .