### Regular Grammars

- A regular grammar is a type of formal grammar that can generate regular languages, which are the languages that can be accepted by finite automata.
- A regular grammar consists of four components: a finite set of non-terminal symbols, a finite set of terminal symbols, a start symbol, and a finite set of production rules.
- A production rule is a pair of a non-terminal symbol and a string of symbols (either terminal or non-terminal) that can be derived from the non-terminal symbol.
- There are two types of regular grammars: right-regular and left-regular. In a right-regular grammar, the production rules are of the form A -> aB or A -> a, where A and B are non-terminal symbols and a is a terminal symbol. In a left-regular grammar, the production rules are of the form A -> Ba or A -> a, where A and B are non-terminal symbols and a is a terminal symbol.
- A regular grammar can be converted into an equivalent nondeterministic finite automaton (NFA) by following these steps:
  - Create a state for each non-terminal symbol and an additional state for the final state.
  - Mark the state corresponding to the start symbol as the initial state and the final state as the accepting state.
  - For each production rule of the form A -> aB, create a transition from the state corresponding to A to the state corresponding to B with the label a.
  - For each production rule of the form A -> a, create a transition from the state corresponding to A to the final state with the label a.
- A regular grammar can also be converted into an equivalent regular expression by applying the Arden's theorem, which states that if A -> aB + b, where A and B are non-terminal symbols and a and b are strings of symbols, then A -> b(a*B) is a solution.
- Regular grammars are useful for describing the syntax of simple programming languages, such as arithmetic expressions, and for designing lexical analyzers, which are programs that scan the input and identify the tokens .
- Regular grammars are the simplest type of grammars in the Chomsky hierarchy, which classifies formal languages based on their complexity and expressiveness. The other types of grammars are context-free, context-sensitive, and recursively enumerable.