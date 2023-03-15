### 6. Write program to convert NFA to DFA

An NFA (Nondeterministic Finite Automaton) is a finite state machine where, for some cases, when a single input is given to the current state, the machine goes to multiple states. It is not necessary for the machine to go to different states every time the same input is given to the same state.

A DFA (Deterministic Finite Automaton) is a finite state machine where, for each input symbol, there is one and only one transition from the current state to a next state.

Here are the steps to convert an NFA to a DFA:

1. Create a start state for the DFA by taking the epsilon closure of the start state of the NFA.
2. For each state in the DFA, find the set of NFA states reachable by each possible input symbol. Take the epsilon closure of this set to get the next state in the DFA.
3. Repeat step 2 until no new states are added to the DFA.
4. For each state in the DFA, if any of the NFA states it represents is an accepting state, make the DFA state an accepting state as well.

Here is an example of a program that converts an NFA to a DFA in Python:

```python
def convert_nfa_to_dfa(nfa):
    dfa = {}
    nfa_states = list(nfa.keys())
    dfa_states = []
    dfa_start_state = nfa['start_state']
    dfa_states.append(dfa_start_state)
    dfa['start_state'] = dfa_start_state
    dfa['final_states'] = []
    for state in dfa_states:
        dfa[state] = {}
        for symbol in nfa['symbols']:
            next_state = set()
            for nfa_state in state:
                if symbol in nfa[nfa_state]:
                    next_state = next_state.union(set(nfa[nfa_state][symbol]))
            next_state = tuple(sorted(list(next_state)))
            dfa[state][symbol] = next_state
            if next_state not in dfa_states:
                dfa_states.append(next_state)
    for state in dfa_states:
        for nfa_state in state:
            if nfa_state in nfa['final_states']:
                dfa['final_states'].append(state)
                break
    return dfa
```

This program takes as input an NFA represented as a dictionary, where the keys are the states of the NFA, and the values are dictionaries representing the transitions from that state. The start state is represented by the key 'start_state', and the final states are represented by the key 'final_states'. The symbols are represented by the key 'symbols'. The output is a DFA represented in the same format.