### Definition for the notes of the Unit 3 - Regular and Non-regular Grammars in the subject of Theory of Automata and Formal Languages

- A **regular grammar** is a formal grammar that can generate a **regular language**. A regular language is a language that can be recognized by a **finite automaton**. 
- A regular grammar can be either **right-regular** or **left-regular**. In a right-regular grammar, every production rule has at most one non-terminal on the right-hand side, and that non-terminal is the last symbol. In a left-regular grammar, every production rule has at most one non-terminal on the left-hand side, and that non-terminal is the first symbol. 
- A regular grammar has the following general form: 

  - A → aB
  - A → a
  - A → B
  - A → ε

  where A and B are non-terminals, a is a terminal, and ε is the empty string.

- A **non-regular grammar** is a formal grammar that can generate a **non-regular language**. A non-regular language is a language that cannot be recognized by a finite automaton. 
- A non-regular grammar can have production rules that are not in the form of a regular grammar. For example, a non-regular grammar can have production rules that have more than one non-terminal on either side, or that have a non-terminal in the middle of the right-hand side. 
- A non-regular grammar can generate a **context-free language**, a **context-sensitive language**, or a **recursively enumerable language**, depending on the complexity of the production rules.