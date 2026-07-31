# Equivalence of DFA and NFA

- A **DFA** (Deterministic Finite Automaton) is a finite state machine that accepts or rejects a given string of symbols, where each state has exactly one transition for each symbol in the alphabet.
- An **NFA** (Nondeterministic Finite Automaton) is a finite state machine that accepts or rejects a given string of symbols, where each state can have zero, one or more transitions for each symbol in the alphabet, or even transitions without any symbols (called epsilon-transitions).
- A DFA and an NFA are called **equivalent** if they recognize the same language, that is, if they accept exactly the same set of strings.
- The **equivalence theorem** states that for any NFA, there exists a DFA that recognizes the same language, and vice versa .
- The proof of the equivalence theorem consists of two parts:
  - **From NFA to DFA**: Given an NFA N, we can construct a DFA D that simulates the behavior of N on any input string, by keeping track of all the possible states that N can be in after reading each symbol. This is done by using the **subset construction** algorithm, which creates a new state in D for each subset of states in N, and defines the transitions and the final states accordingly.
  - **From DFA to NFA**: Given a DFA D, we can construct an NFA N that mimics the behavior of D on any input string, by simply copying the states, transitions and final states of D. This is trivial, since every DFA is also an NFA.