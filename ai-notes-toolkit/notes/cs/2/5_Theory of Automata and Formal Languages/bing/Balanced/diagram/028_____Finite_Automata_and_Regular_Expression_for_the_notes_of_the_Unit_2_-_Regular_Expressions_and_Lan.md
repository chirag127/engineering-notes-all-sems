### Finite Automata and Regular Expression

- Finite automata are abstract machines that can recognize patterns in strings and accept or reject them based on some rules .
- Regular expressions are algebraic notations that can describe the set of strings accepted by finite automata .
- Regular expressions and finite automata are equivalent in expressive power, meaning that for every regular expression, there exists a finite automaton that accepts the same language, and vice versa  .
- There are two types of finite automata: deterministic finite automata (DFA) and nondeterministic finite automata (NFA). DFA have only one transition for each input symbol and state, while NFA can have multiple transitions or no transitions for the same input symbol and state .
- NFA can also have epsilon transitions, which are transitions that do not consume any input symbol and can be taken spontaneously .
- Every NFA can be converted to an equivalent DFA using the subset construction algorithm, which creates a new state for each subset of states in the NFA .
- DFA can be minimized by removing unreachable states and merging equivalent states, which are states that have the same behavior for all input strings .
- Regular expressions can be constructed from finite automata using the state elimination method, which removes states one by one and replaces the transitions with equivalent regular expressions until only the initial and final states remain.
- Finite automata can be constructed from regular expressions using the state decomposition method, which breaks down the regular expression into simpler components and creates states and transitions for each component .
- Regular expressions can be defined recursively using the following rules :
  - The empty set ∅, the empty string ε, and any single symbol a are regular expressions.
  - If r and s are regular expressions, then so are (r + s), (r.s), and (r*), where + denotes union, . denotes concatenation, and * denotes Kleene closure.
  - Nothing else is a regular expression.