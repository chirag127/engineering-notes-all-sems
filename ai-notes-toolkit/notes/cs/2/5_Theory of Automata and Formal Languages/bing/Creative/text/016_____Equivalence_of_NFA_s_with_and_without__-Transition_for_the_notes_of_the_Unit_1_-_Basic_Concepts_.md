### Equivalence of NFA's with and without ε-Transition

- An NFA (Non-deterministic Finite Automaton) is a finite state machine that can have multiple transitions for the same input symbol and state.
- An ε-transition is a special kind of transition that does not consume any input symbol and can be taken spontaneously.
- An ε-NFA is an NFA that has one or more ε-transitions.
- An NFA without ε-transitions is also called a DFA (Deterministic Finite Automaton), because it has a unique transition for each input symbol and state.
- An NFA with ε-transitions can be converted to an equivalent NFA without ε-transitions by using the following steps :
  - For each state q, find the set of states that are reachable from q by taking only ε-transitions. This set is called the ε-closure of q, denoted by ε-closure(q).
  - For each state q and input symbol a, find the set of states that are reachable from q by taking a transition on a followed by any number of ε-transitions. This set is called the ε-transition function of q on a, denoted by δε(q,a).
  - Construct a new NFA without ε-transitions by using the following rules:
    - The set of states of the new NFA is the same as the original NFA.
    - The initial state of the new NFA is the same as the original NFA.
    - The set of final states of the new NFA is the set of states that contain at least one final state of the original NFA in their ε-closure.
    - The transition function of the new NFA is defined as δ'(q,a) = δε(q,a) for each state q and input symbol a.
- The equivalence of NFA's with and without ε-transitions means that they accept the same language, i.e., they have the same set of strings that make them reach a final state.
- The equivalence can be proved by showing that for any string w, the original NFA reaches a final state if and only if the new NFA reaches a final state.
- The conversion of NFA's with ε-transitions to NFA's without ε-transitions is useful for simplifying the design and implementation of finite state machines, as well as for converting them to regular expressions or regular grammars.