### 4. Write program to find ε – closure of all states of any given NFA with ε transition.

- An NFA with ε transition is a nondeterministic finite automaton that can move from one state to another without consuming any input symbol, by using a special transition labeled ε.
- The ε-closure of a state q is the set of all states that can be reached from q by following only ε transitions, including q itself.
- The ε-closure of a set of states Q is the union of the ε-closures of all the states in Q.
- To find the ε-closure of all states of an NFA with ε transition, we can use the following algorithm:

  - Initialize an empty dictionary called `closure` to store the ε-closure of each state as a key-value pair.
  - For each state q in the NFA:
    - Initialize an empty stack called `stack` and push q onto it.
    - Initialize an empty set called `visited` and add q to it.
    - Initialize an empty set called `eclosure` and add q to it.
    - While `stack` is not empty:
      - Pop the top element from `stack` and call it `current`.
      - For each state p that has an ε transition from `current`:
        - If p is not in `visited`:
          - Push p onto `stack`.
          - Add p to `visited`.
          - Add p to `eclosure`.
    - Add the key-value pair (q, `eclosure`) to `closure`.
  - Return `closure` as the output.