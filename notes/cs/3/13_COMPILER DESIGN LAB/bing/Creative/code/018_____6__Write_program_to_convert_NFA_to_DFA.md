```
### 6. Write program to convert NFA to DFA

- NFA stands for nondeterministic finite automaton, which is a mathematical model of computation that accepts strings of symbols as input and changes its state according to the input and a set of transition rules.
- DFA stands for deterministic finite automaton, which is a special case of NFA where each state has exactly one transition for each input symbol and no epsilon transitions (transitions without input).
- To convert an NFA to a DFA, we can use the subset construction algorithm, which works as follows:

  - Start with the initial state of the NFA, which is also the initial state of the DFA.
  - For each input symbol, find the set of states that the NFA can reach from the current state using that symbol and epsilon transitions. This set is called the epsilon-closure of the current state and symbol.
  - If the epsilon-closure is not already a state in the DFA, create a new state and label it with the epsilon-closure. Add a transition from the current state to the new state with the input symbol.
  - Repeat this process for each state and symbol until all possible transitions are explored.
  - Mark the states in the DFA that contain any of the final states of the NFA as final states.

- Here is an example of converting an NFA to a DFA using the subset construction algorithm:

  - The NFA is given by the following transition table and diagram:

    | State | a | b | epsilon |
    | ----- | - | - | ------- |
    | q0    | q1| q2| q3      |
    | q1    | q2| q3| -       |
    | q2    | q3| q1| -       |
    | q3    | q0| q2| -       |

    ![NFA](https://i.imgur.com/5Zl0f8p.png)

  - The DFA is constructed by the following steps:

    - Start with the initial state of the NFA, which is q0. The epsilon-closure of q0 is {q0, q3}, so this is the initial state of the DFA, labeled as A.
    - For the input symbol a, the epsilon-closure of {q0, q3} is {q0, q1, q2, q3}, so this is a new state in the DFA, labeled as B. Add a transition from A to B with a.
    - For the input symbol b, the epsilon-closure of {q0, q3} is {q0, q2, q3}, so this is a new state in the DFA, labeled as C. Add a transition from A to C with b.
    - For the input symbol a, the epsilon-closure of {q0, q1, q2, q3} is {q0, q1, q2, q3}, so this is the same state as B. Add a transition from B to B with a.
    - For the input symbol b, the epsilon-closure of {q0, q1, q2, q3} is {q0, q1, q2, q3}, so this is the same state as B. Add a transition from B to B with b.
    - For the input symbol a, the epsilon-closure of {q0, q2, q3} is {q0, q1, q2, q3}, so this is the same state as B. Add a transition from C to B with a.
    - For the input symbol b, the epsilon-closure of {q0, q2, q3} is {q0, q2, q3}, so this is the same state as C. Add a transition from C to C with b.
    - No more new states or transitions are possible, so the DFA is complete.
    - Mark the states in the DFA that contain any of the final states of the NFA as final states. In this case, q3 is the only final state of the NFA, so A, B, and C are all final states of the DFA.

  - The DFA is given by the following transition table and diagram:

    | State | a | b |
    | ----- | - | - |
    | A     | B | C |
    | B     | B | B |
    | C     | B | C |

    ![DFA](https://i.imgur.com/6ZyX6Xy.png)
```