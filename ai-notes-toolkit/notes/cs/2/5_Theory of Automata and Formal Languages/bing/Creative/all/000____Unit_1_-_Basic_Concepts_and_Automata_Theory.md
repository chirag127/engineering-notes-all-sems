## Unit 1 - Basic Concepts and Automata Theory

- This unit introduces the basic concepts and terminology of formal languages, grammars, and automata theory, which are the foundations of theoretical computer science and compiler design.
- A **formal language** is a set of strings over a finite alphabet. An alphabet is a non-empty set of symbols, such as {0, 1} or {a, b, c, ..., z}. A string is a finite sequence of symbols from an alphabet, such as 0101 or hello. The empty string, denoted by ε, is the string with no symbols. The length of a string is the number of symbols in it, such as |0101| = 4 and |ε| = 0. The set of all strings over an alphabet Σ is denoted by Σ*.
- A **grammar** is a set of rules that describe how to generate strings in a formal language. A grammar consists of four components: a set of non-terminal symbols (also called variables), a set of terminal symbols (also called alphabet), a start symbol (a special non-terminal symbol), and a set of production rules. A production rule has the form A → α, where A is a non-terminal symbol and α is a string of non-terminal and terminal symbols. A grammar can be used to derive strings in a formal language by starting from the start symbol and applying production rules until only terminal symbols are left. For example, the grammar G = ({S, A, B}, {0, 1}, S, {S → 0A, S → 1B, A → 0, A → 0S, A → 1AA, B → 1, B → 1S, B → 0BB}) can generate the string 010011 by the derivation S → 0A → 00S → 001B → 0011.
- A **finite automaton** is a mathematical model of computation that can recognize formal languages. A finite automaton consists of five components: a set of states, a set of input symbols (also called alphabet), a transition function that maps a state and an input symbol to a new state, an initial state, and a set of final states. A finite automaton can process an input string by starting from the initial state and following the transition function for each input symbol until the end of the string. If the final state is in the set of final states, the input string is accepted; otherwise, it is rejected. For example, the finite automaton M = ({q0, q1, q2}, {0, 1}, δ, q0, {q0}) with the transition function δ defined as follows can accept the string 010011:

| state | input | new state |
| ----- | ----- | --------- |
| q0    | 0     | q1        |
| q0    | 1     | q2        |
| q1    | 0     | q0        |
| q1    | 1     | q1        |
| q2    | 0     | q2        |
| q2    | 1     | q0        |

The processing of the input string is shown below:

q0 --0--> q1 --1--> q1 --0--> q0 --0--> q1 --1--> q1 --1--> q0 (accept)

- There are different types of finite automata, such as deterministic finite automata (DFA), nondeterministic finite automata (NFA), and ε-NFA. A DFA is a finite automaton that has exactly one transition for each state and input symbol. An NFA is a finite automaton that can have zero, one, or more transitions for each state and input symbol. An ε-NFA is an NFA that can also have transitions for the empty string ε. An NFA or an ε-NFA can be converted to an equivalent DFA using the subset construction algorithm.
- A **regular expression** is a notation that can describe formal languages using symbols and operators. A regular expression can be defined recursively as follows:

  - ε is a regular expression that denotes the language {ε}.
  - a is a regular expression that denotes the language {a}, where a is any symbol in the alphabet.
  - If r and s are regular expressions, then
    - (r) is a regular expression that denotes the same language as r.
    - (r + s) is a regular expression that denotes the union of the languages denoted by r and s.
    - (rs) is a regular expression that denotes the concatenation of the languages denoted by r and s.
    - (r*)