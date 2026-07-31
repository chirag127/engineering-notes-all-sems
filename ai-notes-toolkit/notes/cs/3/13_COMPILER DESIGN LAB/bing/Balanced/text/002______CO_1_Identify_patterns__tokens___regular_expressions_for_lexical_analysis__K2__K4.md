#### CO 1 Identify patterns, tokens & regular expressions for lexical analysis. K2, K4

- Lexical analysis is the process of converting a sequence of characters from a source program into a sequence of tokens that can be recognized by a compiler or interpreter.
- A token is a basic unit of a language, such as a keyword, an identifier, a constant, an operator, or a delimiter.
- A pattern is a rule that describes how to form a token from a sequence of characters. For example, an identifier may be formed by a letter followed by zero or more letters, digits, or underscores.
- A regular expression is a notation that can specify a set of patterns using symbols and operators. For example, the regular expression `[a-zA-Z][a-zA-Z0-9_]*` can specify the pattern for an identifier.
- A regular expression can be converted into a finite automaton, which is a machine that can recognize a pattern by moving through a sequence of states based on the input characters.
- A finite automaton can be either deterministic (DFA) or nondeterministic (NFA). A DFA has only one transition for each input character and state, while an NFA may have zero, one, or more transitions for each input character and state.
- A DFA can be constructed from an NFA using the subset construction algorithm, which creates a new state for each subset of states in the NFA and determines the transitions based on the input characters and the NFA transitions.
- A DFA can be minimized by eliminating unreachable states and equivalent states, which are states that have the same transitions and acceptance status for all input characters.
- A lexical analyzer can be implemented using a table-driven approach, which uses a transition table to store the DFA and a driver program to read the input characters and move through the table, or a direct-coded approach, which encodes the DFA as a sequence of instructions in a programming language.