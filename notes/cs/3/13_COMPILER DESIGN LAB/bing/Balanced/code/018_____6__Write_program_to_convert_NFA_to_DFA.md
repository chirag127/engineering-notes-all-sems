### 6. Write program to convert NFA to DFA

- NFA stands for nondeterministic finite automaton, which is a mathematical model of computation that can have multiple transitions for the same input symbol and state.
- DFA stands for deterministic finite automaton, which is a special case of NFA where each state has exactly one transition for each input symbol.
- To convert an NFA to a DFA, we can use the subset construction algorithm, which works as follows:

  - Start with the initial state of the NFA, and mark it as the initial state of the DFA.
  - For each input symbol, find the set of states that the NFA can reach from the current state using that symbol. This set is called the epsilon-closure of the current state.
  - If the epsilon-closure is not already a state in the DFA, add it as a new state and mark it as final if it contains any final state of the NFA.
  - Add a transition from the current state to the epsilon-closure state in the DFA using the input symbol.
  - Repeat this process for each state and symbol until all states and transitions are covered.
  - Minimize the DFA by removing any redundant or unreachable states and transitions.

- Here is a pseudocode for the algorithm:

  ```
  function convert_NFA_to_DFA(NFA):
    # NFA is a tuple of (states, alphabet, transitions, initial, final)
    # DFA is a tuple of (states, alphabet, transitions, initial, final)
    # states is a set of strings
    # alphabet is a set of characters
    # transitions is a dictionary of (state, symbol) -> set of states
    # initial is a string
    # final is a set of strings

    # initialize the DFA
    DFA_states = set()
    DFA_transitions = dict()
    DFA_initial = epsilon_closure(NFA, NFA_initial)
    DFA_final = set()

    # create a queue of states to process
    queue = [DFA_initial]

    # loop until the queue is empty
    while queue is not empty:
      # dequeue a state
      current_state = queue.pop()

      # add it to the DFA states
      DFA_states.add(current_state)

      # check if it is final
      if current_state intersects NFA_final:
        DFA_final.add(current_state)

      # loop through each symbol in the alphabet
      for symbol in NFA_alphabet:
        # find the epsilon-closure of the next state
        next_state = epsilon_closure(NFA, NFA_transitions[current_state, symbol])

        # add it to the DFA transitions
        DFA_transitions[current_state, symbol] = next_state

        # if it is not already in the DFA states, enqueue it
        if next_state not in DFA_states:
          queue.append(next_state)

    # return the DFA
    return (DFA_states, NFA_alphabet, DFA_transitions, DFA_initial, DFA_final)
  ```

- Here is an example of converting an NFA to a DFA using the algorithm:

  - The NFA is given by the following transition table:

    | State | a | b | ε |
    | ----- | - | - | - |
    | q0    | q1 | q2 | q3 |
    | q1    | q1 | q2 | -  |
    | q2    | q1 | q2 | -  |
    | q3    | q4 | -  | -  |
    | q4    | q4 | q4 | -  |

    The initial state is q0 and the final state is q4.

  - The DFA is given by the following transition table:

    | State    | a    | b    |
    | -------- | ---- | ---- |
    | {q0,q3}  | {q1,q4} | {q2}  |
    | {q1,q4}  | {q1,q4} | {q2,q4} |
    | {q2}     | {q1}  | {q2}  |
    | {q2,q4}  | {q1,q4} | {q2,q4} |
    | {q1}     | {q1}  | {q2}  |

    The initial state is {q0,q3} and the final state is {q1,q4}, {q2,q4}, and {q4}.