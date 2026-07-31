# Finite Automata and Regular Languages

- A **regular language** is a set of strings that can be described by a simple pattern, such as a sequence of characters, a repetition of a substring, or a choice between alternatives.
- A **finite automaton** is a mathematical model of a machine that can recognize regular languages by moving through a finite number of states according to the input symbols.
- Finite automata and regular expressions are different ways to represent regular languages.
- A **regular expression** is a notation that uses symbols and operators to describe a regular language in a concise and algebraic way.
- The languages accepted by some regular expression are referred to as **regular languages**.
- Finite automata can be used to generate strings in a regular language. A finite automaton for a particular language is “programmed,” in a way, to generate the strings of a given language through its states and transition functions.
- There are two types of finite automata: **deterministic finite automata (DFA)** and **nondeterministic finite automata (NFA)**.
- A **DFA** is a finite automaton that has exactly one transition for each state and input symbol, and can be in only one state at a time.
- An **NFA** is a finite automaton that can have more than one transition for each state and input symbol, and can be in multiple states at a time.
- Every NFA can be converted to an equivalent DFA that accepts the same language, using a process called **subset construction** or **powerset construction**.
- Every DFA can be converted to an equivalent regular expression that describes the same language, using a process called **state elimination** or **Kleene's algorithm**.
- Every regular expression can be converted to an equivalent NFA that accepts the same language, using a process called **Thompson's construction**.
- Regular languages and finite automata can model computational problems that require a very small amount of memory. For example, a finite automaton can generate a regular language to describe if a light switch is on or off, but it cannot keep track of how many times the light was switched on or off.
- Regular languages and finite automata have limitations in their expressive power. They cannot recognize languages that require unbounded memory or recursion, such as the language of balanced parentheses or the language of palindromes.
- A language that is not regular is called a **non-regular language**. A tool to prove that a language is non-regular is the **pumping lemma for regular languages**, which states that if a language is regular, then there exists a constant p such that any string in the language of length at least p can be pumped, or repeated, without leaving the language.