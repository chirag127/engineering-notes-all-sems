### 5. Write program to convert NFA with ε transition to NFA without ε transition.

```python
# Define a function to convert NFA with epsilon transition to NFA without epsilon transition
def convert(NFA):
  # Initialize an empty dictionary to store the new NFA
  new_NFA = {}
  # Loop through each state in the NFA
  for state in NFA:
    # Initialize an empty dictionary to store the new transitions for the state
    new_transitions = {}
    # Loop through each symbol in the NFA alphabet
    for symbol in NFA[state]:
      # Initialize an empty set to store the new states for the symbol
      new_states = set()
      # Add the original states for the symbol to the new states
      new_states.update(NFA[state][symbol])
      # Check if epsilon is in the original states
      if 'ε' in NFA[state][symbol]:
        # Loop through each epsilon state
        for epsilon_state in NFA[state][symbol]:
          # Add the states for epsilon transition to the new states
          new_states.update(NFA[epsilon_state]['ε'])
      # Remove epsilon from the new states
      new_states.discard('ε')
      # Assign the new states to the new transitions for the symbol
      new_transitions[symbol] = new_states
    # Assign the new transitions to the new NFA for the state
    new_NFA[state] = new_transitions
  # Return the new NFA
  return new_NFA

# Define an example NFA with epsilon transition
NFA = {
  'q0': {'0': {'q0'}, '1': {'q0', 'q1'}, 'ε': {'q2'}},
  'q1': {'0': {'q3'}, '1': {'q3'}, 'ε': set()},
  'q2': {'0': {'q4'}, '1': {'q4'}, 'ε': set()},
  'q3': {'0': set(), '1': set(), 'ε': set()},
  'q4': {'0': set(), '1': set(), 'ε': {'q3'}}
}

# Print the original NFA
print("Original NFA:")
for state in NFA:
  print(state, NFA[state])

# Convert the NFA to NFA without epsilon transition
new_NFA = convert(NFA)

# Print the new NFA
print("New NFA:")
for state in new_NFA:
  print(state, new_NFA[state])
```