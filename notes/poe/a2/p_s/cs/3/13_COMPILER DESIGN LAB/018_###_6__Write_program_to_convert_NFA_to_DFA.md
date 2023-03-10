 Here is the content in markdown format:

### 6. Write program to convert NFA to DFA

- An NFA (Non-Deterministic Finite Automaton) can have epsilon transitions and multiple transitions on the same input symbol. A DFA (Deterministic Finite Automaton) has at most one transition for each state-input pair.
- To convert an NFA to DFA:

1. Take the starting state of the NFA as the starting state of the DFA
2. For each state `q` in the NFA and for each possible input symbol `a`, do the following:
    - Find all states reachable from `q` via epsilon transitions
    - Find all states reachable from the states found in the above steps via `a` transitions
    - Add a transition from `q` to a new state `q'` on input `a`. `q'` is a newly generated state.
3. Repeat step#2 until all states and transitions of the DFA are determined
4. Mark final states of the DFA: A state `q'` is final if it contains a final state of the NFA

- The time complexity is exponential in the number of states as the number of states in the DFA can be exponential in the number of states of the NFA.
- Conversion is useful in implementing NFA using DFA based mechanisms (as DFAs are easier to implement). Also, the DFA obtained may be further minimized.
- Here's an [example](https://www.cs.cmu.edu/~fp/courses/15411-s07/automata/nfa-dfa-convert-example.html) to understand the conversion process.
- **Advantages**: Conversion allows us to use efficient DFA based algorithms/implementations to recognize languages accepted by NFAs.
- **Disadvantages**: The number of states may increase exponentially in the worst case.
- This conversion finds applications in compilers, parsers, network protocol implementations, etc. to convert regex based patterns into DFAs for efficient processing.