### Equivalence of NFA's with and without ε-Transition

- An NFA is a non-deterministic finite automaton that can have multiple transitions for the same input symbol and state.
- An ε-transition is a special transition that does not consume any input symbol and can be taken spontaneously.
- An ε-NFA is an NFA that can have ε-transitions.
- An NFA without ε-transitions is also called a DFA (deterministic finite automaton).
- An NFA and an ε-NFA are equivalent if they accept the same language.
- To prove the equivalence, we need to show how to convert an ε-NFA to an NFA and vice versa.

#### Converting an ε-NFA to an NFA

- The main idea is to eliminate the ε-transitions by finding the set of states that can be reached from any state by taking zero or more ε-transitions. This set is called the ε-closure of a state.
- For each state q and input symbol a, we define a new transition function δ1 as follows:

  - δ1(q, a) = ε-closure(δ(ε-closure(q), a))

  where δ is the original transition function of the ε-NFA.

- The new transition function δ1 is the transition function of the equivalent NFA without ε-transitions.
- The initial state of the new NFA is the ε-closure of the initial state of the ε-NFA.
- The final states of the new NFA are those states that contain a final state of the ε-NFA in their ε-closure.

#### Converting an NFA to an ε-NFA

- The main idea is to introduce ε-transitions to merge the transitions for the same input symbol and state.
- For each state q and input symbol a, we define a new transition function δ2 as follows:

  - δ2(q, a) = {q} ∪ δ(q, a)

  where δ is the original transition function of the NFA.

- The new transition function δ2 is the transition function of the equivalent ε-NFA with ε-transitions.
- The initial state and the final states of the new ε-NFA are the same as the original NFA.