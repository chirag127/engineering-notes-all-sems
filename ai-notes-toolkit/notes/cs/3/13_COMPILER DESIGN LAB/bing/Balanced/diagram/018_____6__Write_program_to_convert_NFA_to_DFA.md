### 6. Write program to convert NFA to DFA

- NFA stands for nondeterministic finite automaton, which is a mathematical model of computation that accepts or rejects a given string of symbols.
- DFA stands for deterministic finite automaton, which is a special case of NFA where each state has exactly one transition for each symbol in the alphabet.
- To convert an NFA to a DFA, we can use the subset construction algorithm, which works as follows:

  - Start with the initial state of the NFA, which is a subset of states that contains the start state of the NFA.
  - For each symbol in the alphabet, find the set of states that can be reached from the current subset by following transitions labeled with that symbol. This is called the epsilon-closure of the subset.
  - If the resulting set of states is not already in the set of subsets, add it as a new state of the DFA and mark it as unprocessed.
  - Repeat this process until all subsets are processed.
  - The final states of the DFA are those subsets that contain any of the final states of the NFA.

- Here is an example of a program in Python that implements the subset construction algorithm:

```python
# Define the NFA as a dictionary of dictionaries
# The keys are the states and the values are dictionaries of transitions
# The keys of the inner dictionaries are the symbols and the values are sets of states
# Epsilon transitions are denoted by the empty string ''
nfa = {
    'q0': {'0': {'q0'}, '1': {'q0', 'q1'}, '': {'q2'}},
    'q1': {'0': {'q3'}, '1': {'q2'}},
    'q2': {'0': {'q3'}, '1': {'q4'}},
    'q3': {'0': {'q3'}, '1': {'q3'}},
    'q4': {'0': {'q4'}, '1': {'q4'}}
}

# Define the alphabet as a set of symbols
alphabet = {'0', '1'}

# Define the start state of the NFA
nfa_start = 'q0'

# Define the final states of the NFA as a set of states
nfa_final = {'q2', 'q4'}

# Define a function to compute the epsilon-closure of a set of states
def epsilon_closure(states):
    # Initialize the closure as the given set of states
    closure = states.copy()
    # Initialize a stack to store the unprocessed states
    stack = list(states)
    # Loop until the stack is empty
    while stack:
        # Pop a state from the stack
        state = stack.pop()
        # For each epsilon transition from the state
        for next_state in nfa[state].get('', set()):
            # If the next state is not in the closure
            if next_state not in closure:
                # Add it to the closure
                closure.add(next_state)
                # Push it to the stack
                stack.append(next_state)
    # Return the closure
    return closure

# Define a function to convert the NFA to a DFA
def nfa_to_dfa(nfa, alphabet, nfa_start, nfa_final):
    # Initialize the DFA as an empty dictionary
    dfa = {}
    # Initialize the set of subsets as an empty set
    subsets = set()
    # Initialize a queue to store the unprocessed subsets
    queue = []
    # Compute the epsilon-closure of the start state of the NFA
    start = epsilon_closure({nfa_start})
    # Add it to the set of subsets
    subsets.add(frozenset(start))
    # Enqueue it as the start state of the DFA
    queue.append(start)
    # Loop until the queue is empty
    while queue:
        # Dequeue a subset from the queue
        current = queue.pop(0)
        # For each symbol in the alphabet
        for symbol in alphabet:
            # Initialize an empty set to store the next subset
            next = set()
            # For each state in the current subset
            for state in current:
                # For each transition from the state labeled with the symbol
                for next_state in nfa[state].get(symbol, set()):
                    # Add the epsilon-closure of the next state to the next subset
                    next.update(epsilon_closure({next_state}))
            # If the next subset is not empty
            if next:
                # If the next subset is not in the set of subsets
                if frozenset(next) not in subsets:
                    # Add it to the set of subsets

```
