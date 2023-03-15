### 5. Write program to convert NFA with ε transition to NFA without ε transition

An NFA with ε transitions (also called ε-NFA) is a type of NFA that allows transitions between states without consuming any input symbols. These transitions are called ε transitions. To convert an ε-NFA to an NFA without ε transitions, the following algorithm can be used:

1. For each state `q` in the ε-NFA, find the set of states that can be reached from `q` by following only ε transitions. This set is called `ε-closure(q)`.
2. For each state `q` in the ε-NFA and for each input symbol `a`, find the set of states that can be reached from `q` by consuming the input symbol `a` and then following only ε transitions. This set is called `δ'(q, a)`.
3. Create a new NFA without ε transitions. The set of states and the set of input symbols of the new NFA are the same as those of the ε-NFA.
4. For each state `q` in the ε-NFA and for each input symbol `a`, add a transition from `q` to each state in `δ'(q, a)` in the new NFA.
5. For each state `q` in the ε-NFA, if `q` is an accepting state or if any state in `ε-closure(q)` is an accepting state, then make `q` an accepting state in the new NFA.
6. The start state of the new NFA is the same as the start state of the ε-NFA.

This algorithm can be implemented in a program to convert an ε-NFA to an NFA without ε transitions. The resulting NFA will accept the same language as the original ε-NFA.