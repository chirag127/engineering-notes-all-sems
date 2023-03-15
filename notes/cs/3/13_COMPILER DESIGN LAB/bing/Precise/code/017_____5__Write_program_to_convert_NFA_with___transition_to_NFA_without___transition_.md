### 5. Write program to convert NFA with ε transition to NFA without ε transition.

An NFA with ε transitions (also called ε-NFA) is a type of NFA where transitions can occur without any input symbol, via the use of ε transitions. To convert an ε-NFA to an NFA without ε transitions, we can follow these steps:

1. **Identify ε-closure of states**: For each state in the ε-NFA, identify the set of states that can be reached from it via zero or more ε transitions. This set of states is called the ε-closure of the state.

2. **Create new transition function**: For each state and input symbol in the ε-NFA, find the set of states that can be reached from the ε-closure of the state via the input symbol. This set of states will be the value of the transition function for the corresponding state and input symbol in the new NFA.

3. **Update initial and final states**: The initial state of the new NFA will be the ε-closure of the initial state of the ε-NFA. The set of final states of the new NFA will be the set of states in the ε-NFA whose ε-closure contains at least one final state of the ε-NFA.

Here is an example of a program in Python that converts an ε-NFA to an NFA without ε transitions:

```python
def e_closure(state, transition_function):
    stack = [state]
    closure = set(stack)
    while stack:
        current_state = stack.pop()
        next_states = transition_function.get((current_state, ''), set())
        for next_state in next_states:
            if next_state not in closure:
                stack.append(next_state)
                closure.add(next_state)
    return closure

def convert_nfa_with_epsilon_to_nfa_without_epsilon(nfa_with_epsilon):
    states, input_symbols, transition_function, initial_state, final_states = nfa_with_epsilon
    new_transition_function = {}
    for state in states:
        closure = e_closure(state, transition_function)
        for symbol in input_symbols:
            next_states = set()
            for closure_state in closure:
                next_states |= transition_function.get((closure_state, symbol), set())
            new_transition_function[(state, symbol)] = next_states
    new_initial_state = e_closure(initial_state, transition_function)
    new_final_states = set()
    for state in states:
        closure = e_closure(state, transition_function)
        if any(final_state in closure for final_state in final_states):
            new_final_states.add(state)
    return (states, input_symbols, new_transition_function, new_initial_state, new_final_states)
```

This program takes as input an ε-NFA represented as a tuple of its states, input symbols, transition function, initial state, and final states. The transition function is represented as a dictionary where the keys are tuples of a state and an input symbol (or the empty string for ε transitions), and the values are sets of next states. The program returns a new NFA without ε transitions, represented in the same format.

The `e_closure` function takes as input a state and the transition function of the ε-NFA, and returns the ε-closure of the state. The `convert_nfa_with_epsilon_to_nfa_without_epsilon` function uses this function to compute the new transition function, initial state, and final states of the new NFA, following the steps described above.