# Finite state machines and regular expressions and their applications to lexical analysis

- Finite state machines (FSMs) are abstract models of computation that can process a sequence of inputs and change their state accordingly.
- Regular expressions (REs) are algebraic notations that can specify a set of strings, called a regular language, using symbols and operators.
- Lexical analysis is the first phase of a compiler, where the source code is scanned and divided into meaningful units, called tokens.
- The applications of FSMs and REs to lexical analysis are:

  - FSMs can be used as recognizers for REs, that is, given a RE and an input string, an FSM can determine whether the string belongs to the language specified by the RE.
  - REs can be used as generators for FSMs, that is, given a RE, an algorithm can construct an equivalent FSM that accepts the same language as the RE.
  - Lexical analyzers can be implemented using FSMs, either directly or indirectly. Directly, a lexical analyzer can be a deterministic finite automaton (DFA) that reads the input character by character and changes its state until it reaches a final state, which corresponds to a token type. Indirectly, a lexical analyzer can be a nondeterministic finite automaton (NFA) that is converted to a DFA using a standard algorithm.
  - REs can be used as a convenient way of specifying the tokens of a language, using a notation that is concise, expressive and easy to manipulate. For example, the RE `a*b` specifies the token that consists of zero or more `a`s followed by a `b`.
  - FSMs and REs can be combined with other techniques, such as symbol tables, error handling, and buffering, to improve the efficiency and robustness of lexical analyzers.