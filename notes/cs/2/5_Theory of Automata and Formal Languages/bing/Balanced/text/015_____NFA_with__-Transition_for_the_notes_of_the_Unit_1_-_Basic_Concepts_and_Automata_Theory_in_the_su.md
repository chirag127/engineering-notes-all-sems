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
  - For the initial state q0, the equivalent NFA has the initial state ε-closure(q0).
  - For each final state qf, the equivalent NFA has the same final state qf.

- An example of an NFA with ε-transition and its equivalent NFA without ε-transition is shown below:

![NFA with ε-transition](https://web.cecs.pdx.edu/~sheard/course/CS311/Fall2013/ppt/NfaEpsilonDefined_files/image002.gif)

![NFA without ε-transition](https://web.cecs.pdx.edu/~sheard/course/CS311/Fall2013/ppt/NfaEpsilonDefined_files/image004.gif)