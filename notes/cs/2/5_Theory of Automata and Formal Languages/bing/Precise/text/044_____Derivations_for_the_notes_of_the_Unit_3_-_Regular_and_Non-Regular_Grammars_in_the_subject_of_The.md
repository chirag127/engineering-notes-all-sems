### Derivations for the notes of the Unit 3 - Regular and Non-Regular Grammars in the subject of Theory of Automata and Formal Languages

1. A **regular grammar** is a formal grammar that is right-linear or left-linear. In other words, all production rules in a regular grammar have either the form `A → aB` or the form `A → Ba`, where `A` and `B` are non-terminal symbols and `a` is a terminal symbol.
2. A **non-regular grammar** is a formal grammar that is not regular. This means that it contains production rules that do not have the form `A → aB` or `A → Ba`.
3. Regular grammars can be used to generate regular languages, which are a subset of the context-free languages.
4. Non-regular grammars can generate languages that are not regular, including context-free languages and context-sensitive languages.
5. The **Chomsky hierarchy** classifies formal grammars and the languages they generate into four types: Type-0 (unrestricted), Type-1 (context-sensitive), Type-2 (context-free), and Type-3 (regular).
6. Regular grammars are Type-3 grammars, while non-regular grammars can be of Type-0, Type-1, or Type-2.
7. The **pumping lemma for regular languages** can be used to prove that a language is not regular by showing that it cannot be pumped, i.e., that there exists a string in the language that cannot be divided into three parts such that repeating the middle part any number of times produces a string that is still in the language.
8. The **Myhill-Nerode theorem** provides another method for proving that a language is not regular by showing that it has an infinite number of equivalence classes under the Myhill-Nerode relation.
