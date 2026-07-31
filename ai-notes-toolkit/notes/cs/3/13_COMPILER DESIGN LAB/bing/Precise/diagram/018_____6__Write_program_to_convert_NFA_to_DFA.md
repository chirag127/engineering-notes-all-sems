### 6. Write program to convert NFA to DFA

An NFA (Nondeterministic Finite Automaton) is a finite state machine where for each pair of state and input symbol, there may be several possible next states. A DFA (Deterministic Finite Automaton) is a finite state machine where for each pair of state and input symbol, there is one and only one possible next state.

Here are the steps to convert an NFA to a DFA:

1. Create a start state for the DFA by taking the ε-closure of the start state of the NFA.
2. For each state in the DFA, find the set of NFA states reachable by each possible input symbol. Take the ε-closure of this set to get the next state in the DFA.
3. Repeat step 2 until no new states are added to the DFA.
4. For each state in the DFA, if any of the NFA states it represents is an accepting state, make the DFA state an accepting state as well.
5. The resulting DFA will be equivalent to the original NFA.

Here is an example of a program that converts an NFA to a DFA:

```python
def nfa_to_dfa(nfa):
    # Create a start state for the DFA by taking the ε-closure of the start state of the NFA
    start_state = epsilon_closure(nfa.start_state)
    dfa = DFA(start_state)

    # Create a list of unprocessed DFA states
    unprocessed_states = [start_state]

    # Process each unprocessed state
    while unprocessed_states:
        current_state = unprocessed_states.pop()

        # For each possible input symbol
        for symbol in nfa.symbols:
            # Find the set of NFA states reachable by this symbol
            next_states = set()
            for state in current_state:
                next_states.update(nfa.transitions[state][symbol])

            # Take the ε-closure of this set to get the next state in the DFA
            next_state = epsilon_closure(next_states)

            # Add the transition to the DFA
            dfa.add_transition(current_state, symbol, next_state)

            # If this is a new state, add it to the list of unprocessed states
            if next_state not in dfa.states:
                unprocessed_states.append(next_state)

    # For each state in the DFA, if any of the NFA states it represents is an accepting state, make the DFA state an accepting state as well
    for state in dfa.states:
        if any(nfa_state in nfa.accepting_states for nfa_state in state):
            dfa.accepting_states.add(state)

    return dfa
```

This program takes an NFA as input and returns an equivalent DFA. It uses a function `epsilon_closure` to compute the ε-closure of a set of states. This function is not shown here, but it can be implemented using a depth-first search or breadth-first search algorithm. The program also uses a `DFA` class to represent the resulting DFA. This class is not shown here, but it can be implemented using a dictionary to store the transitions and a set to store the accepting states.