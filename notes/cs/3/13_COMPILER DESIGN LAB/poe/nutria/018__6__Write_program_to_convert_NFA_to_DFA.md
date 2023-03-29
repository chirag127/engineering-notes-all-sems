
### 6. Write program to convert NFA to DFA

1. First, define the Non-Deterministic Finite Automata (NFA) as a 5-tuple (Q, Σ, δ, q0, F) with the following components:
    - Q: A finite set of states
    - Σ: A finite set of symbols, called the alphabet
    - δ: A transition function
    - q0: The initial state
    - F: A set of final states
2. To convert an NFA to a Deterministic Finite Automata (DFA), the following steps should be taken:
    - Create a new transition table for the DFA, with the same number of states as the NFA
    - For each state in the NFA, create a corresponding state in the DFA
    - For each transition in the NFA, create a corresponding transition in the DFA
    - For each state in the NFA, add the transitions for all possible symbols in the alphabet
    - Add the initial and final states of the DFA, based on the initial and final states of the NFA
3. Finally, the program should be tested to ensure that it is functioning correctly.