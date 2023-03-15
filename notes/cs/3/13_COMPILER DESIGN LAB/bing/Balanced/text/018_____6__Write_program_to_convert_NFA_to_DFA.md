### 6. Write program to convert NFA to DFA

- NFA stands for Non-deterministic Finite Automaton, which is a mathematical model of computation that accepts or rejects a given string of symbols.
- DFA stands for Deterministic Finite Automaton, which is a special case of NFA where each state has exactly one transition for each symbol in the alphabet.
- To convert an NFA to a DFA, we can use the subset construction algorithm, which works as follows:

  - Start with the initial state of the NFA, which is also the initial state of the DFA.
  - For each symbol in the alphabet, find the set of states that the NFA can reach from the current state using that symbol. This set is called the epsilon-closure of the current state.
  - If the epsilon-closure is not already a state in the DFA, add it as a new state and mark it as final if it contains any final state of the NFA.
  - Add a transition from the current state to the epsilon-closure state using the symbol.
  - Repeat this process for each state in the DFA until no new states are added.

- The following pseudocode illustrates the algorithm:

  ```
  function convert_NFA_to_DFA(NFA):
    # NFA is a tuple of (states, alphabet, transitions, initial, final)
    # DFA is a tuple of (states, alphabet, transitions, initial, final)
    # states is a set of strings
    # alphabet is a set of symbols
    # transitions is a dictionary of (state, symbol) -> set of states
    # initial is a string
    # final is a set of strings

    # initialize the DFA with the initial state of the NFA
    DFA_states = {epsilon_closure(NFA, NFA_initial)}
    DFA_transitions = {}
    DFA_initial = epsilon_closure(NFA, NFA_initial)
    DFA_final = {}

    # create a queue to store the unprocessed states of the DFA
    queue = [DFA_initial]

    # while the queue is not empty, process each state
    while queue is not empty:
      # dequeue the first state
      current_state = queue.pop(0)

      # for each symbol in the alphabet, find the epsilon-closure of the current state
      for symbol in NFA_alphabet:
        next_state = epsilon_closure(NFA, NFA_transitions[current_state, symbol])

        # if the epsilon-closure is not already a state in the DFA, add it as a new state
        if next_state not in DFA_states:
          DFA_states.add(next_state)
          queue.append(next_state)

          # if the epsilon-closure contains any final state of the NFA, mark it as final in the DFA
          if next_state intersects NFA_final:
            DFA_final.add(next_state)

        # add a transition from the current state to the epsilon-closure state using the symbol
        DFA_transitions[current_state, symbol] = next_state

    # return the DFA
    return (DFA_states, NFA_alphabet, DFA_transitions, DFA_initial, DFA_final)
  ```

- The following diagram shows an example of converting an NFA to a DFA using the algorithm:

  ```
  NFA:                 DFA:

    a     b               a     b
  +---+  +---+          +-----+  +-----+
  | 0 |->| 1 |          | {0} |->| {1} |
  +---+  +---+          +-----+  +-----+
    |  /    |              |  /    |
    | /     |              | /     |
    |/      |              |/      |
    a       b              a       b
  +---+  +---+          +-----+  +-----+
  | 2 |->| 3 |          | {2} |->| {3} |
  +---+  +---+          +-----+  +-----+
    |  /    |              |  /    |
    | /     |              | /     |
    |/      |              |/      |
    a       b              a       b
  +---+  +---+          +-----+  +-----+
  | 4 |->| 5 |          | {4} |->| {5} |
  +---+  +---+          +-----+  +-----+
    |  /    |              |  /    |
    | /     |              | /     |
    |/      |              |/      |
    a       b              a       b
  +---+  +---+          +