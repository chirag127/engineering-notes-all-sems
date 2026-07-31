# Equivalence of NFA's with and without ε-Transition

- An NFA (Non-deterministic Finite Automaton) is a finite state machine that can have multiple transitions for the same input symbol and state.
- An ε-transition is a special transition that does not consume any input symbol and can be taken spontaneously.
- An ε-NFA is an NFA that has one or more ε-transitions.
- An NFA without ε-transitions is also called a DFA (Deterministic Finite Automaton), since it has a unique transition for each input symbol and state.
- An NFA and an ε-NFA are equivalent if they accept the same language, i.e., the set of strings that make them reach a final state.
- To prove the equivalence of NFA and ε-NFA, we need to show that for any NFA, there exists an equivalent ε-NFA, and vice versa.

## Converting NFA to ε-NFA

- Given an NFA, we can construct an equivalent ε-NFA by adding ε-transitions from each state to itself, and from the initial state to all the final states.
- This way, the ε-NFA can simulate the behavior of the NFA by taking the same transitions as the NFA, or by skipping some states using the ε-transitions.
- For example, consider the following NFA that accepts the language {0, 01, 001}:

![NFA](https://i.stack.imgur.com/0y0Yw.png)

- We can convert it to an equivalent ε-NFA by adding ε-transitions as shown below:

![ε-NFA](https://i.stack.imgur.com/6q3y7.png)

- The ε-NFA accepts the same language as the NFA, since it can take the same transitions as the NFA, or use the ε-transitions to skip some states.

## Converting ε-NFA to NFA

- Given an ε-NFA, we can construct an equivalent NFA by removing the ε-transitions and replacing them with appropriate transitions for each input symbol.
- To do this, we need to find the ε-closure of each state, which is the set of states that can be reached from that state by taking only ε-transitions.
- Then, for each state and input symbol, we find the set of states that can be reached from the ε-closure of that state by taking that input symbol, and add a transition for that symbol to that set of states.
- We also make the initial state of the NFA the ε-closure of the initial state of the ε-NFA, and make any state that contains a final state of the ε-NFA a final state of the NFA.
- For example, consider the following ε-NFA that accepts the language {a, ab, abb}:

![ε-NFA](https://i.stack.imgur.com/0y0Yw.png)

- We can convert it to an equivalent NFA by removing the ε-transitions and adding appropriate transitions as shown below:

![NFA](https://i.stack.imgur.com/6q3y7.png)

- The NFA accepts the same language as the ε-NFA, since it can reach the same set of states as the ε-NFA for any input string.