

### Equivalence of NFA’s with and without ε-Transition

- An NFA (Non-Deterministic Finite Automaton) is a type of automaton that can have one or more transitions from a single state on the same input symbol. 

- NFA's with ε-transition, also known as epsilon-NFA's, are a type of NFA that can have transitions on empty string (ε).

- NFA's without ε-transition are regular NFA's that do not have transitions on empty string.

- It is important to note that ε-transition can be simulated by regular transition in an NFA without ε-transition.

- The equivalence of NFA's with and without ε-transition can be proven by constructing an equivalent NFA without ε-transition for every NFA with ε-transition.

- This means that any language that can be recognized by an NFA with ε-transition can also be recognized by an NFA without ε-transition.

- This equivalence is an important concept in automata theory as it allows us to simplify the construction of automata for a given language.

- It also helps us to understand the expressive power of different types of automata and their ability to recognize languages.

- In conclusion, the equivalence of NFA's with and without ε-transition is a fundamental concept in automata theory that allows us to simplify the construction of automata and understand their expressive power.