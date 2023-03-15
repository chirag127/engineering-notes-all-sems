### 4. Write program to find ε – closure of all states of any given NFA with ε transition.

- An NFA with ε transition is a nondeterministic finite automaton that can move from one state to another without consuming any input symbol, by using a special transition labeled with ε (the empty string).
- The ε-closure of a state q is the set of all states that can be reached from q by following only ε transitions, including q itself.
- The ε-closure of a set of states Q is the union of the ε-closures of all the states in Q.
- To find the ε-closure of all states of an NFA with ε transition, we can use the following algorithm:

  - Initialize an empty stack S and an empty set E.
  - For each state q in the NFA, do the following steps:
    - Push q onto S and add q to E.
    - While S is not empty, do the following steps:
      - Pop a state p from S.
      - For each state r that has an ε transition from p, do the following steps:
        - If r is not in E, then push r onto S and add r to E.
    - Output E as the ε-closure of q and clear E for the next iteration.

- Here is an example of a Python program that implements the algorithm:

```python
# Define the NFA with epsilon transition as a dictionary
# The keys are the states and the values are dictionaries of transitions
# The transitions are also dictionaries with keys as symbols and values as sets of states
nfa = {
  "q0": {"a": {"q1"}, "b": {"q2"}, "ε": {"q3"}},
  "q1": {"a": {"q0"}, "b": {"q3"}, "ε": set()},
  "q2": {"a": {"q3"}, "b": {"q0"}, "ε": set()},
  "q3": {"a": {"q2"}, "b": {"q1"}, "ε": set()}
}

# Define a function to find the epsilon closure of a state
def epsilon_closure(state):
  # Initialize an empty stack and an empty set
  stack = []
  closure = set()
  # Push the state onto the stack and add it to the closure
  stack.append(state)
  closure.add(state)
  # While the stack is not empty, pop a state and check its epsilon transitions
  while stack:
    current = stack.pop()
    for next in nfa[current]["ε"]:
      # If the next state is not in the closure, push it onto the stack and add it to the closure
      if next not in closure:
        stack.append(next)
        closure.add(next)
  # Return the closure as a sorted list
  return sorted(list(closure))

# Find the epsilon closure of all states and print the results
for state in nfa:
  print(f"The epsilon closure of {state} is {epsilon_closure(state)}")
```

- The output of the program is:

```
The epsilon closure of q0 is ['q0', 'q3']
The epsilon closure of q1 is ['q1']
The epsilon closure of q2 is ['q2']
The epsilon closure of q3 is ['q3']
```