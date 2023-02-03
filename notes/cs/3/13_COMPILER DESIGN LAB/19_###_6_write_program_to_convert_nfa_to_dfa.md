### 6. Write program to convert NFA to DFA

- Represent the NFA as a transition table or graph
- Create a start state for the DFA by taking the epsilon closure of the NFA start state
- Create a new state in the DFA for each distinct set of states in the NFA that can be reached from the current state
- For each state in the DFA, create a transition to a new state for each symbol in the alphabet, by taking the epsilon closure of the set of states reachable from the current state in the NFA
- Repeat the process until all states in the NFA have been processed
- Mark the final states in the DFA by checking if any of the states in the NFA are final states.
- The resulting DFA is the equivalent deterministic automaton for the original NFA.
