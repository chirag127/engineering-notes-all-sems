# 6. Write program to convert NFA to DFA

An NFA (Nondeterministic Finite Automaton) is a finite state machine where for each pair of state and input symbol, there may be several possible next states. A DFA (Deterministic Finite Automaton) is a finite state machine where for each pair of state and input symbol, there is one and only one possible next state.

Here are the steps to convert an NFA to a DFA:

1. Create a start state for the DFA by taking the epsilon closure of the start state of the NFA.
2. Create a transition table for the DFA using the transition table of the NFA.
3. For each state in the DFA, find the set of NFA states reachable from the current DFA state on each input symbol.
4. If the set of NFA states is not already a state in the DFA, create a new state in the DFA.
5. Repeat the above steps until all states and transitions have been added to the DFA.
6. Mark all states in the DFA that contain an accepting state of the NFA as accepting states.

Here is an example of a program that converts an NFA to a DFA in Python:

```python
def convert_nfa_to_dfa(nfa):
    # Create a start state for the DFA
    dfa_start_state = epsilon_closure(nfa.start_state)
    # Create a transition table for the DFA
    dfa_transition_table = {}
    # Keep track of the states that have been processed
    processed_states = set()
    # Keep track of the states that need to be processed
    unprocessed_states = [dfa_start_state]
    while unprocessed_states:
        current_state = unprocessed_states.pop()
        processed_states.add(current_state)
        dfa_transition_table[current_state] = {}
        for symbol in nfa.symbols:
            next_state = set()
            for state in current_state:
                next_state |= nfa.transition_table[state][symbol]
            next_state = frozenset(epsilon_closure(next_state))
            dfa_transition_table[current_state][symbol] = next_state
            if next_state not in processed_states:
                unprocessed_states.append(next_state)
    # Create the DFA
    dfa = DFA()
    dfa.start_state = dfa_start_state
    dfa.transition_table = dfa_transition_table
    # Mark all states in the DFA that contain an accepting state of the NFA as accepting states
    for state in dfa_transition_table:
        if any(nfa_state in nfa.accepting_states for nfa_state in state):
            dfa.accepting_states.add(state)
    return dfa
```

This program takes an NFA as input and returns the equivalent DFA. The `epsilon_closure` function is used to find the set of NFA states reachable from a given set of NFA states on epsilon transitions. The `DFA` class is used to represent the DFA. The `symbols` attribute of the NFA is used to iterate over all input symbols. The `transition_table` attribute of the NFA is used to find the set of NFA states reachable from a given NFA state on a given input symbol. The `accepting_states` attribute of the NFA is used to determine which states in the DFA should be marked as accepting states.