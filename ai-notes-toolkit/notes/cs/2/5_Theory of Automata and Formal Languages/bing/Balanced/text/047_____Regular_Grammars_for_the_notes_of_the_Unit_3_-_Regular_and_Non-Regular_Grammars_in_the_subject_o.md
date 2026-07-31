### Regular Grammars

- A regular grammar is a type of formal grammar that can generate regular languages, which are the languages that can be accepted by finite automata.
- A regular grammar consists of four components: a finite set of non-terminal symbols, a finite set of terminal symbols, a start symbol that is a non-terminal, and a finite set of production rules.
- A production rule is of the form A -> aB or A -> a, where A and B are non-terminals and a is a terminal. The former is called a right-linear rule and the latter is called a right-regular rule.
- A regular grammar is called right-regular if it has only right-linear and right-regular rules. Similarly, a regular grammar is called left-regular if it has only left-linear and left-regular rules, where a left-linear rule is of the form A -> Ba and a left-regular rule is of the form A -> a.
- A regular grammar can be converted into an equivalent nondeterministic finite automaton (NFA) by following these steps:
  - Create a state for each non-terminal symbol and an additional state for the end of the input.
  - Mark the state corresponding to the start symbol as the initial state and the additional state as the final state.
  - For each right-linear rule A -> aB, create a transition from the state A to the state B with the label a.
  - For each right-regular rule A -> a, create a transition from the state A to the final state with the label a.
  - For each left-linear rule A -> Ba, create a transition from the state B to the state A with the label a.
  - For each left-regular rule A -> a, create a transition from the initial state to the state A with the label a.
- The NFA obtained from a regular grammar can accept the same language as the grammar generates. Conversely, any NFA can be converted into an equivalent regular grammar by reversing the steps above.
- Regular grammars are useful for describing the syntax of regular expressions, which are a concise way of specifying regular languages. They are also useful for modeling simple patterns and sequences in natural languages, such as phone numbers, email addresses, and identifiers.