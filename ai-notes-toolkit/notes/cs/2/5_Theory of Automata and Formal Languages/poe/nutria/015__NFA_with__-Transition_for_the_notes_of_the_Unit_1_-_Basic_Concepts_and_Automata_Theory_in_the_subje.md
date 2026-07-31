
### NFA with ε-Transition

* An NFA with ε-transitions (also known as an **ε-NFA**) is a type of nondeterministic finite automaton (NFA) in which a transition from one state to another is allowed to occur without consuming any input symbol.
* ε-transitions can be thought of as "empty" transitions, since they do not consume any input symbol.
* A ε-NFA can be constructed from an NFA by adding an ε-transition from each state to itself, and from each state to any other state.
* A ε-NFA is equivalent to an NFA in terms of language recognition.
* A ε-NFA can be converted to an equivalent deterministic finite automaton (DFA) by the method of subset construction.
* The language accepted by a ε-NFA is the same as the language accepted by the equivalent DFA.