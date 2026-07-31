### 5. Write program to convert NFA with ε transition to NFA without ε transition.

An NFA with ε transition is a type of non-deterministic finite automaton (NFA) that allows transitions between states without consuming any input symbols. This is achieved through the use of ε transitions, which are transitions that can be taken without consuming any input symbols.

To convert an NFA with ε transitions to an NFA without ε transitions, the following steps can be taken:

1. Identify all ε transitions in the NFA.
2. For each ε transition, identify the states that are reachable from the source state of the ε transition without consuming any input symbols.
3. For each state that is reachable from the source state of the ε transition, add transitions from the source state to the reachable state for each input symbol that has a transition from the reachable state.
4. Remove all ε transitions from the NFA.

Here is an example of a program that can be used to convert an NFA with ε transitions to an NFA without ε transitions:

```python
def remove_epsilon_transitions(nfa):
    # Step 1: Identify all ε transitions
    epsilon_transitions = []
    for state in nfa.states:
        for transition in state.transitions:
            if transition.symbol == 'ε':
                epsilon_transitions.append(transition)

    # Step 2: For each ε transition, identify the states that are reachable from the source state
    for epsilon_transition in epsilon_transitions:
        source_state = epsilon_transition.source
        reachable_states = find_reachable_states(source_state, nfa)

        # Step 3: For each reachable state, add transitions from the source state for each input symbol
        for reachable_state in reachable_states:
            for transition in reachable_state.transitions:
                if transition.symbol != 'ε':
                    source_state.add_transition(transition.symbol, transition.destination)

    # Step 4: Remove all ε transitions
    for state in nfa.states:
        state.transitions = [transition for transition in state.transitions if transition.symbol != 'ε']

def find_reachable_states(state, nfa, visited=None):
    if visited is None:
        visited = set()
    visited.add(state)
    reachable_states = set()
    for transition in state.transitions:
        if transition.symbol == 'ε' and transition.destination not in visited:
            reachable_states.add(transition.destination)
            reachable_states |= find_reachable_states(transition.destination, nfa, visited)
    return reachable_states
```

This program takes as input an NFA with ε transitions and returns an equivalent NFA without ε transitions. The `remove_epsilon_transitions` function follows the steps outlined above to convert the NFA. The `find_reachable_states` function is a helper function that is used to find all states that are reachable from a given state without consuming any input symbols.