### Regular Expressions for the notes of the Unit 2 - Regular Expressions and Languages in the subject of Theory of Automata and Formal Languages

- A regular expression is a **pattern** that can be used to **describe** or **match** a set of strings, called a **regular language**.
- A regular language is a language that can be **accepted** by a **finite automaton**.
- Regular expressions are defined over an **alphabet** Σ, which is a finite set of symbols.
- The set of regular expressions over Σ is defined **recursively** as follows:
  - The empty set ∅ is a regular expression, and L(∅) = ∅.
  - The empty string ε is a regular expression, and L(ε) = {ε}.
  - For any symbol a ∈ Σ, a is a regular expression, and L(a) = {a}.
  - If R and S are regular expressions, then so are the following:
    - **Concatenation**: RS is a regular expression, and L(RS) = {xy | x ∈ L(R) and y ∈ L(S)}.
    - **Union**: R + S is a regular expression, and L(R + S) = L(R) ∪ L(S).
    - **Kleene star**: R* is a regular expression, and L(R*) = {x1x2...xn | n ≥ 0 and each xi ∈ L(R)}.
  - Nothing else is a regular expression.
- Regular expressions can be used to **specify** or **construct** regular languages, as well as to **perform** operations on them, such as **union**, **intersection**, **complement**, **difference**, etc .
- Regular expressions can also be **converted** to equivalent **finite automata**, and vice versa, using **algorithms** such as **Thompson's construction**, **Glushkov's construction**, **Kleene's theorem**, etc .
- Regular expressions have many **applications** in **text processing**, **pattern matching**, **searching**, **parsing**, **validation**, etc .