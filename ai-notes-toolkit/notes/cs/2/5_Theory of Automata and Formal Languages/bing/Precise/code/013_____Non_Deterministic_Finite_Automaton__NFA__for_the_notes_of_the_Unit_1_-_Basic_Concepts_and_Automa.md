### Non Deterministic Finite Automaton (NFA)

- A Non-Deterministic Finite Automaton (NFA) is a type of finite automaton that allows for multiple transitions from a single state for the same input symbol.
- Unlike a Deterministic Finite Automaton (DFA), an NFA can have multiple possible next states for a given state and input symbol.
- An NFA can also have transitions that do not consume any input symbols, known as epsilon transitions.
- The set of all possible next states for a given state and input symbol is known as the epsilon closure of that state.
- An NFA can be converted into an equivalent DFA using the powerset construction.
- The powerset construction involves creating a new state in the DFA for each possible subset of states in the NFA.
- The transition function for the DFA is then defined such that the next state for a given state and input symbol is the union of the epsilon closures of all the states in the corresponding subset of the NFA.
- The acceptance condition for the DFA is defined such that a state is accepting if and only if it contains at least one accepting state from the NFA.
- NFAs are useful for modeling systems where the next state is not uniquely determined by the current state and input symbol.
- NFAs are also useful for constructing regular expressions, as they can be used to represent the different possible ways that a regular expression can match a string.
