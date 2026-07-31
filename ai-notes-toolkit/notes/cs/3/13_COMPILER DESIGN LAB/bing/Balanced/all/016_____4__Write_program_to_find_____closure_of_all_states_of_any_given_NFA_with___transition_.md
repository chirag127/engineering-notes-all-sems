# 4. Write program to find ε – closure of all states of any given NFA with ε transition.

- An NFA with ε transition is a nondeterministic finite automaton that can move from one state to another without consuming any input symbol, by using a special transition labeled with ε (the empty string).
- The ε-closure of a state q is the set of all states that can be reached from q by following only ε transitions, including q itself.
- The ε-closure of a set of states Q is the union of the ε-closures of all the states in Q.
- To find the ε-closure of all states of an NFA with ε transition, we can use the following algorithm:

  - Initialize an empty dictionary called `closure` to store the ε-closure of each state as a key-value pair.
  - For each state q in the NFA:
    - Initialize an empty stack called `stack` and push q onto it.
    - Initialize an empty set called `visited` and add q to it.
    - Initialize an empty set called `eclosure` and add q to it.
    - While `stack` is not empty:
      - Pop the top element of `stack` and call it `current`.
      - For each state p that has an ε transition from `current`:
        - If p is not in `visited`:
          - Push p onto `stack`.
          - Add p to `visited`.
          - Add p to `eclosure`.
    - Add the key-value pair (q, eclosure) to `closure`.
  - Return `closure` as the output.

- Here is an example of a Python program that implements the algorithm:

```python
# Define the NFA with epsilon transition as a dictionary
# The keys are the states and the values are dictionaries of transitions
# The transitions are represented as key-value pairs of symbols and sets of states
nfa = {
  "q0": {"a": {"q1"}, "b": {"q2"}, "ε": {"q3"}},
  "q1": {"a": {"q1"}, "b": {"q2"}, "ε": {"q4"}},
  "q2": {"a": {"q1"}, "b": {"q2"}, "ε": set()},
  "q3": {"a": {"q1"}, "b": {"q2"}, "ε": {"q4"}},
  "q4": {"a": {"q1"}, "b": {"q2"}, "ε": set()}
}

# Define a function to find the epsilon closure of all states
def epsilon_closure(nfa):
  # Initialize an empty dictionary to store the epsilon closure of each state
  closure = {}
  # For each state in the NFA
  for q in nfa:
    # Initialize an empty stack and push the state onto it
    stack = [q]
    # Initialize an empty set to store the visited states and add the state to it
    visited = {q}
    # Initialize an empty set to store the epsilon closure of the state and add the state to it
    eclosure = {q}
    # While the stack is not empty
    while stack:
      # Pop the top element of the stack and call it current
      current = stack.pop()
      # For each state that has an epsilon transition from current
      for p in nfa[current]["ε"]:
        # If the state is not visited
        if p not in visited:
          # Push the state onto the stack
          stack.append(p)
          # Add the state to the visited set
          visited.add(p)
          # Add the state to the epsilon closure set
          eclosure.add(p)
    # Add the key-value pair (state, epsilon closure) to the closure dictionary
    closure[q] = eclosure
  # Return the closure dictionary as the output
  return closure

# Call the function and print the result
print(epsilon_closure(nfa))
```

- The output of the program is:

```python
{'q0': {'q0', 'q3', 'q4'}, 'q1': {'q1', 'q4'}, 'q2': {'q2'}, 'q3': {'q3', 'q4'}, 'q4': {'q4'}}
```

- This means that the ε-closure of q0 is {q0, q3, q4}, the ε-closure of q1 is {q1, q4}, and so on.