### NFA with ε-Transition

- An NFA with ε-transition is a type of nondeterministic finite automaton (NFA) that allows the machine to change its state without consuming any input symbol.
- An ε-transition is represented by an arc labeled with ε in the state diagram of the NFA.
- An NFA with ε-transition can have zero, one or more ε-transitions from any state.
- An NFA with ε-transition accepts an input string if there is some path from the initial state to a final state that matches the input string along with any number of ε-transitions.
- An NFA with ε-transition can be converted to an equivalent NFA without ε-transition by using the ε-closure of each state.
- The ε-closure of a state q is the set of all states that can be reached from q by following only ε-transitions.
- The ε-closure of a set of states Q is the union of the ε-closures of each state in Q.
- The transition function of the equivalent NFA without ε-transition is defined as follows:

  - For each state q and input symbol a, δ(q, a) = ε-closure(δ'(q, a)), where δ' is the transition function of the NFA with ε-transition.
  - For each state q, δ(q, ε) = ∅, meaning there are no ε-transitions in the equivalent NFA.

- The following example illustrates an NFA with ε-transition and its equivalent NFA without ε-transition:

![NFA with ε-transition and its equivalent NFA without ε-transition](https://i.imgur.com/0zZ0Q2x.png)

- The NFA with ε-transition has four states: q0, q1, q2 and q3. The initial state is q0 and the final state is q3. The input alphabet is {a, b}.
- The NFA without ε-transition has three states: q0, q1 and q2. The initial state is q0 and the final state is q2. The input alphabet is {a, b}.
- The states q1 and q3 of the NFA with ε-transition are merged into one state q2 of the NFA without ε-transition, because they are in the same ε-closure.
- The transition function of the NFA without ε-transition is obtained by applying the ε-closure to the transition function of the NFA with ε-transition. For example, δ(q0, a) = ε-closure(δ'(q0, a)) = ε-closure({q1}) = {q1, q3} = {q2}.