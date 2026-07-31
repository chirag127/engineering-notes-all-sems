### Equivalence of NFA's with and without ε-Transition

- An NFA is a non-deterministic finite automaton that can accept a regular language by having multiple possible transitions for a given input symbol and state.
- An ε-transition is a special kind of transition that does not consume any input symbol and can be taken spontaneously from a state.
- An NFA with ε-transitions (also called ε-NFA) is an NFA that allows ε-transitions in addition to the regular transitions.
- An NFA without ε-transitions is an NFA that does not have any ε-transitions in its transition function.
- The equivalence of NFA's with and without ε-transitions means that for any given ε-NFA, there exists an equivalent NFA without ε-transitions that accepts the same language, and vice versa.
- The equivalence can be proved by showing how to convert an ε-NFA to an NFA without ε-transitions, and how to convert an NFA without ε-transitions to an ε-NFA.

#### Conversion of ε-NFA to NFA without ε-transitions

- The conversion of ε-NFA to NFA without ε-transitions is based on the idea of finding the ε-closure of each state, which is the set of all states that can be reached from that state by following only ε-transitions.
- The steps for the conversion are as follows:

  1. For each state q in the ε-NFA, find the ε-closure(q) and label it as a new state Q in the NFA without ε-transitions.
  2. For each state Q in the NFA without ε-transitions, and for each input symbol a, find the set of states that can be reached from Q by reading a, and then taking the ε-closure of each state in that set. This set is the transition of Q on a in the NFA without ε-transitions.
  3. The initial state of the NFA without ε-transitions is the ε-closure of the initial state of the ε-NFA.
  4. The final states of the NFA without ε-transitions are those that contain at least one final state of the ε-NFA.

- Example: Convert the following ε-NFA to an equivalent NFA without ε-transitions.

![ε-NFA](https://www.tutorialspoint.com/how-to-convert-nfa-with-epsilon-to-without-epsilon/images/nfa_with_epsilon.jpg)

- Solution:

  1. The ε-closures of each state are as follows:

     - ε-closure(q0) = {q0, q1, q2}
     - ε-closure(q1) = {q1}
     - ε-closure(q2) = {q2, q3}
     - ε-closure(q3) = {q3}

  2. The transitions of each state Q on each input symbol a are as follows:

     - δ({q0, q1, q2}, 0) = ε-closure(δ({q0, q1, q2}, 0)) = ε-closure({q1, q3}) = {q1, q3}
     - δ({q0, q1, q2}, 1) = ε-closure(δ({q0, q1, q2}, 1)) = ε-closure({q2}) = {q2, q3}
     - δ({q1}, 0) = ε-closure(δ({q1}, 0)) = ε-closure({q1}) = {q1}
     - δ({q1}, 1) = ε-closure(δ({q1}, 1)) = ε-closure(∅) = ∅
     - δ({q2, q3}, 0) = ε-closure(δ({q2, q3}, 0)) = ε-closure({q3}) = {q3}
     - δ({q2, q3}, 1) = ε-closure(δ({q2, q3}, 1)) = ε-closure(∅) = ∅
     - δ({q3}, 0) = ε-closure(δ({q3}, 0)) = ε-closure(∅) = ∅
     - δ({q3}, 1) = ε-closure(δ({q3}, 1)) = ε-closure(∅) = ∅

  3. The initial state of the NFA without ε