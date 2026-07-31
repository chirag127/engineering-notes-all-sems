### 6. Write program to convert NFA to DFA

An NFA (Nondeterministic Finite Automaton) is a finite state machine where for each pair of state and input symbol, there may be several possible next states. A DFA (Deterministic Finite Automaton) is a finite state machine where for each pair of state and input symbol, there is one and only one possible next state.

Here are the steps to convert an NFA to a DFA:

1. Create a start state for the DFA by taking the epsilon closure of the start state of the NFA.
2. Create a transition table for the DFA using the transition table of the NFA. For each state in the DFA and each input symbol, find the set of NFA states reachable from the current DFA state using the input symbol and take the epsilon closure of this set. This set of NFA states will be a single state in the DFA.
3. For each state in the DFA, if it is made up of one or more accepting states of the NFA, mark it as an accepting state in the DFA.
4. Repeat step 2 until all states and transitions have been added to the DFA.

This is the general algorithm for converting an NFA to a DFA. The specific implementation may vary depending on the programming language and data structures used. It is important to note that the resulting DFA may have more states than the original NFA. This is because the DFA must explicitly keep track of all possible states that the NFA could be in at any given time.