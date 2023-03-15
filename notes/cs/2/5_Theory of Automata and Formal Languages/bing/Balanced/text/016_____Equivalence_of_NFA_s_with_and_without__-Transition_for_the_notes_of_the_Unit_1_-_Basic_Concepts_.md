### Equivalence of NFA's with and without ε-Transition

- An NFA (Non-deterministic Finite Automaton) is a finite state machine that can have multiple transitions for the same input symbol and state.
- An ε-transition is a special transition that does not consume any input symbol and can be taken spontaneously.
- An ε-NFA is an NFA that has one or more ε-transitions.
- An NFA without ε-transitions is also called a DFA (Deterministic Finite Automaton), because it has a unique transition for each input symbol and state.
- An NFA with ε-transitions can be converted to an equivalent NFA without ε-transitions by the following steps:
  - For each state q, find the set of states that are reachable from q by taking only ε-transitions. This set is called the ε-closure of q, denoted by ε-closure(q).
  - For each state q and input symbol a, find the set of states that are reachable from q by taking a transition followed by zero or more ε-transitions. This set is called the ε-transition function of q and a, denoted by δε(q,a).
  - Construct a new NFA without ε-transitions by using the ε-transition function as the new transition function. The new NFA has the same set of states and final states as the original NFA, and the same start state. The new transition function is defined as δ'(q,a) = δε(q,a) for each state q and input symbol a.
- The equivalence of NFA's with and without ε-transitions means that for any regular language L, there exists an NFA with ε-transitions that accepts L, and there exists an NFA without ε-transitions that accepts L. Moreover, these two NFA's can be obtained from each other by the conversion algorithm described above.