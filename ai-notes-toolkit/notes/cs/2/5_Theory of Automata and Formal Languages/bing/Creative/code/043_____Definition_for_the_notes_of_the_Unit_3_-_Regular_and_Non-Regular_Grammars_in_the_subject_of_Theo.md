Hello, I am Sydney, your AI assistant. I can help you with your topic. Here are some notes for the definition of regular and non-regular grammars:

### Definition for the notes of the Unit 3 - Regular and Non-Regular Grammars in the subject of Theory of Automata and Formal Languages

- A **regular grammar** is a formal grammar that can generate a **regular language**. A regular language is a language that can be recognized by a **finite automaton** or a **regular expression**.
- A regular grammar can be either **right-regular** or **left-regular**. In a right-regular grammar, every production rule has at most one non-terminal symbol on the right-hand side, and that non-terminal symbol is the last symbol. In a left-regular grammar, every production rule has at most one non-terminal symbol on the left-hand side, and that non-terminal symbol is the first symbol.
- A regular grammar has the following general form:

  - A → a
  - A → aB
  - A → ε

  where A and B are non-terminal symbols, a is a terminal symbol, and ε is the empty string.

- A **non-regular grammar** is a formal grammar that can generate a **non-regular language**. A non-regular language is a language that cannot be recognized by a finite automaton or a regular expression.
- A non-regular grammar can be either **context-free** or **context-sensitive**. In a context-free grammar, every production rule has only one non-terminal symbol on the left-hand side, and any number of terminal and non-terminal symbols on the right-hand side. In a context-sensitive grammar, every production rule has the same or more symbols on the right-hand side than on the left-hand side, and the left-hand side can have more than one non-terminal symbol.
- A non-regular grammar has the following general form:

  - A → α
  - αAβ → αγβ

  where A is a non-terminal symbol, α, β, and γ are strings of terminal and non-terminal symbols, and α and β can be empty.

- A regular grammar is a special case of a context-free grammar, and a context-free grammar is a special case of a context-sensitive grammar. Therefore, every regular language is also a context-free language and a context-sensitive language, but not every context-free language or context-sensitive language is a regular language.