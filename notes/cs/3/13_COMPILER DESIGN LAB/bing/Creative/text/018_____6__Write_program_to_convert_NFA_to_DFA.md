### 6. Write program to convert NFA to DFA

- NFA stands for nondeterministic finite automaton, which is a mathematical model of computation that accepts or rejects a given string of symbols.
- DFA stands for deterministic finite automaton, which is a special case of NFA where each state has exactly one transition for each symbol in the alphabet.
- To convert an NFA to a DFA, we can use the subset construction algorithm, which works as follows:

  - Start with the initial state of the NFA, which is a subset of states that contains the start state of the NFA. This is the initial state of the DFA.
  - For each symbol in the alphabet, find the set of states that can be reached from the current subset by following transitions labeled with that symbol. This is the next subset of states for the DFA.
  - If the next subset is not already in the DFA, add it as a new state and repeat the process for each symbol in the alphabet.
  - If the next subset is already in the DFA, use the existing state as the transition target and skip the process for that symbol.
  - Mark the final states of the DFA as the subsets that contain any of the final states of the NFA.
  - The resulting DFA is equivalent to the given NFA in terms of accepting the same language.

- Here is an example of a Python program that implements the subset construction algorithm:

  ```python
  # Define the NFA as a dictionary of dictionaries
  # The keys are the states and the values are dictionaries of transitions
  # The keys of the inner dictionaries are the symbols and the values are sets of states
  # The special symbol 'e' denotes epsilon transitions
  nfa = {
      'q0': {'e': {'q1', 'q3'}},
      'q1': {'0': {'q1'}, '1': {'q2'}},
      'q2': {'0': {'q2'}, '1': {'q2'}},
      'q3': {'0': {'q4'}},
      'q4': {'0': {'q3'}, '1': {'q5'}},
      'q5': {'0': {'q5'}, '1': {'q5'}}
  }

  # Define the alphabet as a set of symbols
  alphabet = {'0', '1'}

  # Define the start state of the NFA
  nfa_start = 'q0'

  # Define the final states of the NFA as a set of states
  nfa_final = {'q2', 'q5'}

  # Define a function to find the epsilon closure of a set of states
  # The epsilon closure is the set of states that can be reached by following epsilon transitions
  def epsilon_closure(states):
      # Initialize the closure as the given set of states
      closure = states.copy()
      # Initialize a stack to keep track of the states to explore
      stack = list(states)
      # Loop until the stack is empty
      while stack:
          # Pop a state from the stack
          state = stack.pop()
          # Check if the state has any epsilon transitions
          if 'e' in nfa[state]:
              # Loop through the epsilon transitions
              for next_state in nfa[state]['e']:
                  # Check if the next state is not already in the closure
                  if next_state not in closure:
                      # Add the next state to the closure
                      closure.add(next_state)
                      # Push the next state to the stack
                      stack.append(next_state)
      # Return the closure
      return closure

  # Define a function to find the next set of states for a given set of states and a symbol
  # The next set of states is the epsilon closure of the union of the states that can be reached by following transitions labeled with the symbol
  def next_states(states, symbol):
      # Initialize the next set of states as an empty set
      next_states = set()
      # Loop through the given set of states
      for state in states:
          # Check if the state has any transitions labeled with the symbol
          if symbol in nfa[state]:
              # Add the states that can be reached by following the transitions to the next set of states
              next_states.update(nfa[state][symbol])
      # Return the epsilon closure of the next set of states
      return epsilon_closure(next_states)

  # Define a function to convert the NFA to a DFA using the subset construction algorithm
  def nfa_to_dfa():
      # Initialize the DFA as an empty dictionary
      dfa = {}
      # Initialize a list of subsets of states to explore
      subsets = [epsilon