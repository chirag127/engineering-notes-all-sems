### 5. Write program to convert NFA with ε transition to NFA without ε transition.

- An NFA with ε transition is a nondeterministic finite automaton that can move from one state to another without consuming any input symbol, by using a special transition labeled ε.
- An NFA without ε transition is a nondeterministic finite automaton that can only move from one state to another by consuming an input symbol from the alphabet.
- To convert an NFA with ε transition to an NFA without ε transition, we need to perform the following steps:

  - Step 1: For each state in the NFA with ε transition, find the set of states that can be reached from it by using only ε transitions. This set is called the ε-closure of the state.
  - Step 2: For each state in the NFA with ε transition, and for each input symbol in the alphabet, find the set of states that can be reached from it by using one input symbol followed by any number of ε transitions. This set is called the transition function of the state and the symbol.
  - Step 3: Construct a new NFA without ε transition, with the same set of states and final states as the original NFA with ε transition. For each state and each input symbol, add a transition from the state to the set of states obtained in step 2. This is the transition function of the new NFA without ε transition.

- Here is an example of a program to convert an NFA with ε transition to an NFA without ε transition, written in Python:

```python
# Define the NFA with epsilon transition
states = {"q0", "q1", "q2", "q3"} # Set of states
alphabet = {"a", "b"} # Set of input symbols
initial_state = "q0" # Initial state
final_states = {"q3"} # Set of final states
epsilon_transitions = { # Dictionary of epsilon transitions
  "q0": {"q1", "q2"},
  "q1": {"q2"},
  "q2": set(),
  "q3": set()
}
transitions = { # Dictionary of transitions
  ("q0", "a"): set(),
  ("q0", "b"): set(),
  ("q1", "a"): {"q3"},
  ("q1", "b"): set(),
  ("q2", "a"): set(),
  ("q2", "b"): {"q3"},
  ("q3", "a"): set(),
  ("q3", "b"): set()
}

# Define a function to find the epsilon closure of a state
def epsilon_closure(state):
  closure = {state} # Initialize the closure with the state itself
  stack = [state] # Initialize a stack with the state
  while stack: # While the stack is not empty
    s = stack.pop() # Pop a state from the stack
    for t in epsilon_transitions[s]: # For each epsilon transition from s
      if t not in closure: # If t is not in the closure
        closure.add(t) # Add t to the closure
        stack.append(t) # Push t to the stack
  return closure # Return the closure

# Define a function to find the transition function of a state and a symbol
def transition_function(state, symbol):
  result = set() # Initialize an empty set for the result
  for s in epsilon_closure(state): # For each state in the epsilon closure of the state
    for t in transitions[(s, symbol)]: # For each transition from s with the symbol
      result = result.union(epsilon_closure(t)) # Union the result with the epsilon closure of t
  return result # Return the result

# Construct the new NFA without epsilon transition
new_transitions = {} # Initialize an empty dictionary for the new transitions
for state in states: # For each state in the NFA
  for symbol in alphabet: # For each symbol in the alphabet
    new_transitions[(state, symbol)] = transition_function(state, symbol) # Add the new transition to the dictionary

# Print the new NFA without epsilon transition
print("The new NFA without epsilon transition is:")
print("States:", states)
print("Alphabet:", alphabet)
print("Initial state:", initial_state)
print("Final states:", final_states)
print("Transitions:")
for key, value in new_transitions.items():
  print(key, "->", value)
```

- The output of the program is:

```
The new NFA without epsilon transition is:
States: {'q0', 'q1', 'q2', 'q3'}
Alphabet

```
