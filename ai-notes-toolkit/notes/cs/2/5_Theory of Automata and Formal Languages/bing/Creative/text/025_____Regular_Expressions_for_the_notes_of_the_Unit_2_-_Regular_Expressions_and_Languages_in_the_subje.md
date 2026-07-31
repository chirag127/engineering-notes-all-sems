### Regular Expressions for the notes of the Unit 2 - Regular Expressions and Languages in the subject of Theory of Automata and Formal Languages

- A regular expression is a **pattern** that can be used to describe a **set of strings** that belong to a **regular language**  .
- A regular language is a language that can be **recognized** by a **finite automaton**  .
- A regular expression is defined **recursively** over an **alphabet** Σ as follows :
  - The **empty set** ∅ is a regular expression that denotes the language ∅.
  - The **empty string** ε is a regular expression that denotes the language {ε}.
  - For any **symbol** a ∈ Σ, a is a regular expression that denotes the language {a}.
  - If R and S are regular expressions, then the following are also regular expressions:
    - **Concatenation**: RS denotes the language {rs | r ∈ L(R) and s ∈ L(S)}.
    - **Union**: R + S denotes the language {x | x ∈ L(R) or x ∈ L(S)}.
    - **Kleene star**: R* denotes the language {r1r2...rn | n ≥ 0 and ri ∈ L(R) for 1 ≤ i ≤ n}.
  - **Parentheses** can be used to change the **precedence** of the operators. The precedence order is: * (highest), concatenation (middle), + (lowest).
- A regular expression can be **represented** by a **regular grammar** or a **finite automaton** .
  - A regular grammar is a grammar that has **rules** of the form A → a or A → aB or A → ε, where A and B are **non-terminals** and a is a **terminal**.
  - A finite automaton is a **machine** that has a **finite number of states**, a **start state**, a **set of final states**, and a **transition function** that maps each state and input symbol to a next state .
- Regular expressions can be used to **specify** and **manipulate** text patterns, such as **searching**, **replacing**, **validating**, or **extracting** information .
- Regular expressions have many **applications** in computer science, such as **text processing**, **compilers**, **lexical analysis**, **pattern matching**, **data compression**, **bioinformatics**, and **artificial intelligence** .