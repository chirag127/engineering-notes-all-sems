### 4. Write program to find ε – closure of all states of any given NFA with ε transition.

The ε-closure of a state `q` in an NFA with ε transition is the set of all states that can be reached from `q` by following only ε-transitions. The ε-closure of a set of states `Q` is the union of the ε-closures of all the states in `Q`.

Here is an algorithm to find the ε-closure of all states of a given NFA with ε transition:

1. Initialize an empty stack `S` and an empty set `ε-closure(q)` for each state `q` in the NFA.
2. For each state `q` in the NFA, push `q` onto the stack `S` and add `q` to `ε-closure(q)`.
3. While the stack `S` is not empty:
    1. Pop the top state `q` from the stack `S`.
    2. For each state `p` that can be reached from `q` by following only ε-transitions:
        1. If `p` is not already in `ε-closure(q)`, add `p` to `ε-closure(q)` and push `p` onto the stack `S`.
4. The set `ε-closure(q)` now contains the ε-closure of state `q` for all states `q` in the NFA.

This algorithm can be implemented in a programming language of your choice. It is important to note that the ε-closure of a state may include the state itself. Also, the ε-closure of a set of states is the union of the ε-closures of all the states in the set.