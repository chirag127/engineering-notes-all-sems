# Finite Automata and Regular Languages

- A **finite automaton** is a mathematical model of a machine that can accept or reject a string of symbols based on its states and transitions .
- A **regular language** is a set of strings that can be described by a **regular expression** or recognized by a finite automaton .
- A **regular expression** is a notation that uses symbols and operators to define a regular language .
- Finite automata and regular expressions are **equivalent** in their expressive power, meaning that for every regular expression, there exists a finite automaton that recognizes the same language, and vice versa . This is known as **Kleene's theorem**.
- Regular languages have some **properties** that make them easy to manipulate and reason about :
  - Regular languages are **closed** under the **regular operations** of union, concatenation, and star . This means that if L and M are regular languages, then so are L ∪ M, LM, and L* .
  - Regular languages can be **pumped**, meaning that any sufficiently long string in a regular language can be divided into three parts, such that repeating the middle part any number of times produces another string in the same language. This is known as the **pumping lemma** for regular languages.
  - Regular languages can be **decided**, meaning that there exists an algorithm that can determine whether a given string belongs to a regular language or not. This is because finite automata are **decidable** machines, meaning that they always halt and give a yes or no answer.
- Regular languages and finite automata can model computational problems that require a very small amount of memory. For example, a finite automaton can generate a regular language to describe if a light switch is on or off, but it cannot keep track of how many times the light was switched on or off.