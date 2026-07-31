# Definition for the notes of the Unit 3 - Regular and Non-Regular Grammars in the subject of Theory of Automata and Formal Languages

- A **regular grammar** is a formal grammar that can generate a **regular language** .
- A regular language is a language that can be recognized by a **finite automaton**.
- A regular grammar can be either **right-regular** or **left-regular**.
- In a **right-regular grammar**, every production rule has at most one non-terminal on the **right-hand side**, and that non-terminal is the **last symbol** in the right-hand side.
- In a **left-regular grammar**, every production rule has at most one non-terminal on the **left-hand side**, and that non-terminal is the **first symbol** in the left-hand side.
- The general form of a right-regular grammar is:

  - A → a
  - A → aB
  - A → ε

  where A, B are non-terminals, a is a terminal, and ε is the empty string.

- The general form of a left-regular grammar is:

  - A → a
  - A → Ba
  - A → ε

  where A, B are non-terminals, a is a terminal, and ε is the empty string.

- A **non-regular grammar** is a formal grammar that can generate a **non-regular language**.
- A non-regular language is a language that cannot be recognized by a finite automaton.
- A non-regular grammar can have production rules that are not in the form of a regular grammar.
- For example, a non-regular grammar can have production rules like:

  - A → aAa
  - A → B
  - B → bBb
  - B → ε

  where A, B are non-terminals, a, b are terminals, and ε is the empty string.

- A non-regular grammar can also be a **context-free grammar** or a **context-sensitive grammar**.
- A context-free grammar is a grammar that has only one non-terminal on the left-hand side of each production rule.
- A context-sensitive grammar is a grammar that has no restrictions on the form of the production rules.