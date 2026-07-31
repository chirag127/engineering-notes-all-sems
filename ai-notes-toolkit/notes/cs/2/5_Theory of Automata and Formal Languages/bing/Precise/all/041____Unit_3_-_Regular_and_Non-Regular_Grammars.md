## Unit 3 - Regular and Non-Regular Grammars

- A **grammar** is a set of rules that define a language.
- A **regular grammar** is a type of grammar that generates a regular language.
- A **regular language** is a language that can be recognized by a finite automaton.
- A **non-regular grammar** is a type of grammar that generates a non-regular language.
- A **non-regular language** is a language that cannot be recognized by a finite automaton.
- Regular grammars can be either **right-linear** or **left-linear**.
- A **right-linear grammar** is a regular grammar where all productions are of the form `A -> aB` or `A -> a`, where `A` and `B` are non-terminals and `a` is a terminal.
- A **left-linear grammar** is a regular grammar where all productions are of the form `A -> Ba` or `A -> a`, where `A` and `B` are non-terminals and `a` is a terminal.
- Regular grammars are a subset of **context-free grammars**.
- A **context-free grammar** is a type of grammar where all productions are of the form `A -> w`, where `A` is a non-terminal and `w` is a string of terminals and non-terminals.
- Non-regular grammars can generate languages that are more complex than regular languages.
- An example of a non-regular language is the language `{a^n b^n | n >= 0}`, which cannot be recognized by a finite automaton.
- The **pumping lemma** can be used to prove that a language is non-regular.
- The **pumping lemma** states that for any regular language `L`, there exists a constant `p` such that for any string `s` in `L` with length greater than or equal to `p`, `s` can be divided into three substrings `s = xyz` such that `|xy| <= p`, `|y| >= 1`, and for all `i >= 0`, `xy^iz` is also in `L`.
- The **pumping lemma** can be used to show that the language `{a^n b^n | n >= 0}` is non-regular by showing that no matter how `s` is divided into `xyz`, `xy^iz` is not in the language for some `i >= 0`.