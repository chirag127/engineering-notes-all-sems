### 4. Write program to find ε – closure of all states of any given NFA with ε transition.

An NFA with ε transition is a non-deterministic finite automaton that can have ε (epsilon) transitions, which allow it to move from one state to another without reading any input symbol. The ε-closure of a state in an NFA is the set of all states that can be reached from that state by following ε transitions.

To find the ε-closure of all states in an NFA with ε transitions, we can write a program in any programming language that follows the steps below:

1. Define the NFA: The NFA can be defined using a set of states, the alphabet, the transition function, the start state, and the set of final states.

2. Initialize the ε-closure of each state as itself: For each state in the NFA, we can initialize its ε-closure as the set containing only itself.

3. Find the ε-closure for each state: We can iterate through each state in the NFA and compute its ε-closure by recursively following all ε transitions from that state and adding all reachable states to the ε-closure set. This process can be repeated until no new states can be added to the ε-closure set.

4. Output the ε-closure of all states: After computing the ε-closure of each state, we can output the ε-closure sets for all states in the NFA.

Here is an example Python program that finds the ε-closure of all states in an NFA with ε transitions:

```python
def epsilon_closure(nfa, state):
    closure = set([state])
    stack = [state]
    while len(stack) > 0:
        current_state = stack.pop()
        if current_state in nfa and 'e' in nfa[current_state]:
            for next_state in nfa[current_state]['e']:
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state)
    return closure

def find_e_closure(nfa):
    e_closure = {}
    for state in nfa:
        e_closure[state] = epsilon_closure(nfa, state)
    return e_closure

# Example usage:
nfa = {
    0: {'e': [1, 7]},
    1: {'a': [2]},
    2: {'b': [3], 'e': [4]},
    3: {'c': [6]},
    4: {'d': [5]},
    5: {'e': [6]},
    6: {},
    7: {'f': [8]},
    8: {'g': [9]},
    9: {}
}

e_closure = find_e_closure(nfa)
for state in e_closure:
    print('ε-closure({}): {}'.format(state, e_closure[state]))
```

In this example, the NFA has 10 states and the alphabet {a, b, c, d, e, f, g}. The ε-closure of each state is computed using the `find_e_closure()` function, which calls the `epsilon_closure()` function for each state. The output shows the ε-closure sets for all states in the NFA.

By following the above steps and using a programming language of your choice, you can easily write a program to find the ε-closure of all states in any given NFA with ε transitions.