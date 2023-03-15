# Definition for the notes of the Unit 3 - Regular and Non-regular Grammars in the subject of Theory of Automata and Formal Languages

- A **regular grammar** is a formal grammar that can generate only regular languages, which are a subset of context-free languages.
- A regular grammar can be either **right-regular** or **left-regular**, depending on the position of the non-terminal symbol in the production rules.
- A **right-regular grammar** has production rules of the form `A -> a`, `A -> aB`, or `A -> ε`, where `A` and `B` are non-terminal symbols, `a` is a terminal symbol, and `ε` is the empty string.
- A **left-regular grammar** has production rules of the form `A -> a`, `A -> Ba`, or `A -> ε`, where `A` and `B` are non-terminal symbols, `a` is a terminal symbol, and `ε` is the empty string.
- A regular grammar is **unambiguous** if there is only one production rule for each non-terminal symbol, and **ambiguous** otherwise.
- A **non-regular grammar** is a formal grammar that can generate languages that are not regular, such as context-free languages, context-sensitive languages, or recursively enumerable languages.
- A non-regular grammar can have production rules that do not follow the restrictions of regular grammars, such as `A -> aBb`, `A -> BC`, or `A -> a^n b^n`, where `A`, `B`, and `C` are non-terminal symbols, `a` and `b` are terminal symbols, and `n` is a positive integer.
- A non-regular grammar can be **ambiguous** if there is more than one way to derive a string from the start symbol, or **unambiguous** otherwise.