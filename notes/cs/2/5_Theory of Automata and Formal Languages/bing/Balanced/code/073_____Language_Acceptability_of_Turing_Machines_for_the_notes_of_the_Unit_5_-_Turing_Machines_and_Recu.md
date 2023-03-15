### Language Acceptability of Turing Machines

- A Turing machine (TM) is a mathematical model of computation that can perform any algorithmic task by manipulating symbols on an infinite tape according to a finite set of rules.
- A TM can accept or reject an input string based on whether it reaches a final state or not after processing the input.
- A TM can also decide an input string by halting on either a final state (accept) or a non-final state (reject) for every input.
- A language is a set of strings over some alphabet. A language is accepted by a TM if the TM accepts every string in the language and rejects every string not in the language.
- A language is decided by a TM if the TM decides every string in the language and every string not in the language.
- A language is Turing-acceptable (or recursively enumerable) if there exists a TM that accepts it. A Turing-acceptable language may or may not be decided by a TM.
- A language is Turing-decidable (or recursive) if there exists a TM that decides it. A Turing-decidable language is also Turing-acceptable, but not vice versa.
- The class of Turing-acceptable languages is equivalent to the class of Type-0 languages in the Chomsky hierarchy of grammars. The class of Turing-decidable languages is a proper subset of the class of Turing-acceptable languages.