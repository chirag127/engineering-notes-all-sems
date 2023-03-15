# 5. Write program to convert NFA with ε transition to NFA without ε transition

An NFA with ε transitions is a type of nondeterministic finite automaton (NFA) that allows transitions between states without consuming any input symbols. These transitions are called ε transitions. To convert an NFA with ε transitions to an NFA without ε transitions, the following steps can be followed:

1. Identify all ε transitions in the NFA.
2. For each ε transition, identify the states that can be reached from the current state without consuming any input symbols.
3. Add transitions from the current state to the identified states for each input symbol that can be consumed to reach those states.
4. Remove the ε transitions from the NFA.

Here is an example of a program that can be used to convert an NFA with ε transitions to an NFA without ε transitions:

```python
def convert_nfa_with_epsilon_transitions(nfa):
    # Create a new NFA without epsilon transitions
    new_nfa = {}
    for state in nfa:
        new_nfa[state] = {}
        for symbol in nfa[state]:
            if symbol != 'ε':
                new_nfa[state][symbol] = nfa[state][symbol]
            else:
                # Find all states reachable by epsilon transitions
                reachable_states = find_epsilon_reachable_states(nfa, state)
                # Add transitions for each input symbol
                for reachable_state in reachable_states:
                    for symbol in nfa[reachable_state]:
                        if symbol != 'ε':
                            if symbol not in new_nfa[state]:
                                new_nfa[state][symbol] = set()
                            new_nfa[state][symbol] |= nfa[reachable_state][symbol]
    return new_nfa

def find_epsilon_reachable_states(nfa, state):
    # Use depth-first search to find all states reachable by epsilon transitions
    stack = [state]
    reachable_states = set()
    while stack:
        current_state = stack.pop()
        if current_state not in reachable_states:
            reachable_states.add(current_state)
            if 'ε' in nfa[current_state]:
                stack.extend(nfa[current_state]['ε'])
    return reachable_states
```

This program takes as input an NFA with ε transitions represented as a dictionary, where the keys are the states and the values are dictionaries representing the transitions from each state. The inner dictionaries have keys representing the input symbols and values representing the set of states that can be reached by consuming the input symbol. The program returns a new NFA without ε transitions represented in the same format. The `find_epsilon_reachable_states` function uses depth-first search to find all states that can be reached from a given state by following ε transitions. These states are then used to add new transitions to the new NFA for each input symbol that can be consumed to reach those states.