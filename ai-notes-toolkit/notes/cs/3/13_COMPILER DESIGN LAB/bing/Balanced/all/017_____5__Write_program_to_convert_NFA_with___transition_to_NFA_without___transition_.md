# 5. Write program to convert NFA with ε transition to NFA without ε transition.

An NFA with ε transition is a nondeterministic finite automaton that can make transitions without consuming any input symbol. An NFA without ε transition is a nondeterministic finite automaton that can only make transitions by consuming an input symbol.

To convert an NFA with ε transition to an NFA without ε transition, we can use the following algorithm:

- For each state q in the NFA with ε transition, compute the ε-closure of q, which is the set of states that can be reached from q by following only ε transitions. This can be done by using a depth-first or breadth-first search on the transition graph.
- For each state q and each input symbol a in the NFA with ε transition, compute the new transition function δ'(q, a) as the union of the ε-closures of all the states in δ(q, a), where δ is the original transition function. This means that from q, we can go to any state that can be reached by consuming a and then following any number of ε transitions.
- The new set of final states F' is the union of the ε-closures of all the states in F, where F is the original set of final states. This means that any state that can be reached by following only ε transitions from a final state is also a final state.
- The new NFA without ε transition is (Q, Σ, δ', q0, F'), where Q, Σ, and q0 are the same as in the original NFA with ε transition.

Here is an example of the algorithm applied to an NFA with ε transition:

![NFA with ε transition](https://i.imgur.com/6w0Z7q8.png)

The ε-closures of the states are:

- ε-closure(0) = {0, 1, 2}
- ε-closure(1) = {1, 2}
- ε-closure(2) = {2}
- ε-closure(3) = {3}
- ε-closure(4) = {4}

The new transition function is:

- δ'(0, a) = ε-closure(δ(0, a)) = ε-closure({3}) = {3}
- δ'(0, b) = ε-closure(δ(0, b)) = ε-closure({4}) = {4}
- δ'(1, a) = ε-closure(δ(1, a)) = ε-closure({3}) = {3}
- δ'(1, b) = ε-closure(δ(1, b)) = ε-closure({4}) = {4}
- δ'(2, a) = ε-closure(δ(2, a)) = ε-closure({3}) = {3}
- δ'(2, b) = ε-closure(δ(2, b)) = ε-closure({4}) = {4}
- δ'(3, a) = ε-closure(δ(3, a)) = ε-closure({}) = {}
- δ'(3, b) = ε-closure(δ(3, b)) = ε-closure({}) = {}
- δ'(4, a) = ε-closure(δ(4, a)) = ε-closure({}) = {}
- δ'(4, b) = ε-closure(δ(4, b)) = ε-closure({}) = {}

The new set of final states is:

- F' = ε-closure(F) = ε-closure({2, 4}) = {2, 4}

The new NFA without ε transition is:

![NFA without ε transition](https://i.imgur.com/3Z0fW0n.png)

The program to implement the algorithm in Python is:

```python
# Define the NFA with epsilon transition
Q = {0, 1, 2, 3, 4} # set of states
Sigma = {'a', 'b'} # set of input symbols
delta = {(0, 'a'): {3}, (0, 'b'): {4}, (0, ''): {1, 2}, (1, 'a'): {3}, (1, 'b'): {4}, (1, ''): {2}, (2, 'a'): {3}, (2, 'b'): {4}} # transition function as a dictionary
q0 = 0 # initial state
F = {2, 4} # set of final states

# Define a function to compute the epsilon closure of a state
def epsilon_closure(q):
  #

```
