### 6. Write program to convert NFA to DFA

- An NFA (Non-deterministic Finite Automaton) is a finite state machine that can have multiple transitions for the same input symbol and state.
- A DFA (Deterministic Finite Automaton) is a finite state machine that can have only one transition for the same input symbol and state.
- To convert an NFA to a DFA, we can use the subset construction algorithm, which works as follows:

1. Create a new start state for the DFA, which is the set of all states reachable from the start state of the NFA by epsilon transitions (transitions without any input symbol).
2. For each input symbol, create a new state for the DFA, which is the set of all states reachable from the current state of the NFA by that symbol and epsilon transitions.
3. Mark the new state as final if it contains any final state of the NFA.
4. Repeat steps 2 and 3 for each new state created until no more new states are generated.
5. The resulting DFA will have the same language as the NFA.

- Here is an example of a program in Python that implements the subset construction algorithm:

```python
# Define the NFA as a dictionary of dictionaries
# The keys are the states, and the values are dictionaries of transitions
# The keys of the inner dictionaries are the input symbols, and the values are sets of next states
# Epsilon transitions are denoted by the empty string ''

nfa = {
    'q0': {'': {'q0', 'q1'}},
    'q1': {'0': {'q2'}},
    'q2': {'1': {'q3'}},
    'q3': {'0': {'q4'}},
    'q4': {'': {'q3'}}
}

# Define the start state and the final states of the NFA
nfa_start = 'q0'
nfa_final = {'q3'}

# Define the input symbols of the NFA
nfa_symbols = {'0', '1'}

# Define a function to find the epsilon closure of a set of states
# The epsilon closure is the set of all states reachable by epsilon transitions
def epsilon_closure(states):
    # Initialize the closure as the given set of states
    closure = states.copy()
    # Initialize a stack to store the states to be processed
    stack = list(states)
    # Loop until the stack is empty
    while stack:
        # Pop a state from the stack
        state = stack.pop()
        # For each epsilon transition from the state
        for next_state in nfa[state].get('', set()):
            # If the next state is not in the closure
            if next_state not in closure:
                # Add it to the closure and the stack
                closure.add(next_state)
                stack.append(next_state)
    # Return the closure
    return closure

# Define a function to find the next state of the DFA for a given state and symbol
# The next state is the epsilon closure of the set of all states reachable by the symbol
def next_state(state, symbol):
    # Initialize an empty set to store the next states
    next_states = set()
    # For each state in the given state
    for s in state:
        # For each transition from the state by the symbol
        for next_s in nfa[s].get(symbol, set()):
            # Add the next state to the set
            next_states.add(next_s)
    # Return the epsilon closure of the set
    return epsilon_closure(next_states)

# Define a function to convert the NFA to a DFA using the subset construction algorithm
def nfa_to_dfa():
    # Initialize an empty dictionary to store the DFA
    dfa = {}
    # Initialize an empty set to store the visited states of the DFA
    visited = set()
    # Initialize a queue to store the states to be processed
    queue = []
    # Find the start state of the DFA, which is the epsilon closure of the start state of the NFA
    dfa_start = epsilon_closure({nfa_start})
    # Add the start state to the queue and the visited set
    queue.append(dfa_start)
    visited.add(dfa_start)
    # Loop until the queue is empty
    while queue:
        # Dequeue a state from the queue
        state = queue.pop(0)
        # Create a new entry for the state in the DFA
        dfa[state] = {}
        # For each input symbol
        for symbol in nfa_symbols:
            # Find the next state of the DFA for the current state and symbol
            next_s = next_state(state, symbol)

```
