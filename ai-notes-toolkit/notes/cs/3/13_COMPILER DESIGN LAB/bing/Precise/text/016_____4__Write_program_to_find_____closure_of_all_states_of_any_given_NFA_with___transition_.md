### 4. Write program to find ε – closure of all states of any given NFA with ε transition.

The ε-closure of a state `q` in an NFA with ε transition is the set of all states that can be reached from `q` by following only ε-transitions. This can be calculated using a depth-first search algorithm.

Here is an example of a program in Python that calculates the ε-closure of all states of a given NFA with ε transition:

```python
def epsilon_closure(nfa, state):
    stack = [state]
    closure = set()
    while stack:
        current_state = stack.pop()
        closure.add(current_state)
        if current_state in nfa.transitions and None in nfa.transitions[current_state]:
            for next_state in nfa.transitions[current_state][None]:
                if next_state not in closure:
                    stack.append(next_state)
    return closure

def epsilon_closure_all_states(nfa):
    closures = {}
    for state in nfa.states:
        closures[state] = epsilon_closure(nfa, state)
    return closures
```

This program takes as input an NFA object with a `states` attribute representing the set of states and a `transitions` attribute representing the transition function. The `epsilon_closure` function calculates the ε-closure of a single state, while the `epsilon_closure_all_states` function calculates the ε-closure of all states by calling the `epsilon_closure` function for each state.

The `epsilon_closure` function uses a stack to keep track of the states that need to be visited. It starts with the given state and adds it to the closure set. Then, it checks if the current state has ε-transitions and, if so, adds the next states to the stack if they are not already in the closure set. This process is repeated until the stack is empty, at which point the closure set contains the ε-closure of the given state.

The `epsilon_closure_all_states` function simply calls the `epsilon_closure` function for each state in the NFA and stores the result in a dictionary, where the keys are the states and the values are the corresponding ε-closures.

This program can be used to find the ε-closure of all states of any given NFA with ε transition. It is important to note that the ε-closure of a state can include the state itself.