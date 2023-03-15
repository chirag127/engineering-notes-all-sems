# Equivalence of NFA's with and without ε-Transition

- An NFA (Non-deterministic Finite Automaton) is a finite state machine that can have multiple transitions for the same input symbol and state.
- An ε-transition is a special kind of transition that does not consume any input symbol and can be taken spontaneously.
- An ε-NFA is an NFA that has one or more ε-transitions.
- An NFA without ε-transitions is also called a DFA (Deterministic Finite Automaton), because it has a unique transition for each input symbol and state.
- The equivalence of NFA's with and without ε-transitions means that for any given ε-NFA, there exists an equivalent NFA without ε-transitions that accepts the same language, and vice versa.
- The equivalence can be proved by showing how to convert an ε-NFA to an NFA without ε-transitions, and how to convert an NFA without ε-transitions to an ε-NFA.

## Converting an ε-NFA to an NFA without ε-transitions

- The main idea is to find the set of states that can be reached from any state by taking zero or more ε-transitions. This set is called the ε-closure of a state.
- For each state q and input symbol a, we find the set of states that can be reached from q by taking a transition on a, followed by zero or more ε-transitions. This set is called the ε-transition function of q on a, denoted by δε(q,a).
- We construct a new NFA without ε-transitions, where the states are the same as the original ε-NFA, and the transition function is defined by δ'(q,a) = δε(q,a) for all q and a.
- The initial state of the new NFA is the ε-closure of the initial state of the original ε-NFA, and the final states are those that contain at least one final state of the original ε-NFA.

## Converting an NFA without ε-transitions to an ε-NFA

- The main idea is to introduce ε-transitions between states that have the same transition on a given input symbol, and to eliminate the original transitions.
- For each input symbol a, we find the set of pairs of states (p,q) such that δ(p,a) = q. We add an ε-transition from p to q for each such pair, and remove the transition on a from p.
- We construct a new ε-NFA, where the states are the same as the original NFA without ε-transitions, and the transition function is defined by the new ε-transitions and the remaining transitions on other symbols.
- The initial state and the final states of the new ε-NFA are the same as the original NFA without ε-transitions.