### Deterministic Finite Automaton (DFA)

- A DFA is a mathematical model of a machine that can process a finite set of symbols and produce a binary output (accept or reject) based on the input sequence.
- A DFA consists of five components   :
  - A finite set of states (Q)
  - A finite set of input symbols (Σ)
  - A transition function (δ) that maps each state and input symbol to a next state
  - A start state (q0) that belongs to Q
  - A set of final or accepting states (F) that is a subset of Q
- A DFA can be represented by a state transition diagram, which is a directed graph with nodes as states and edges as transitions labeled by input symbols .
- A DFA accepts an input string if and only if it reaches a final state after reading all the symbols in the string .
- A DFA is deterministic because for each state and input symbol, there is exactly one next state .
- A DFA can be used to model regular languages, which are the languages that can be described by regular expressions .
- A DFA can also be used to implement various applications such as lexical analysis, pattern matching, and syntax validation.