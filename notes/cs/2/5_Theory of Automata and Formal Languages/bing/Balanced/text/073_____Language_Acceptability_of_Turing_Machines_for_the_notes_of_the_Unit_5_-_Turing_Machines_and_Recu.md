### Language Acceptability of Turing Machines

- A Turing machine (TM) is a mathematical model of computation that can perform any algorithmic task by manipulating symbols on an infinite tape according to a finite set of rules.
- A TM accepts a language if it enters into a final state for any input string w that belongs to the language .
- A TM decides a language if it accepts it and enters into a rejecting state for any input not in the language .
- A language is recursively enumerable (RE) if it is accepted by a TM . RE languages are also called Turing-recognizable or semi-decidable languages.
- A language is recursive if it is decided by a TM . Recursive languages are also called Turing-decidable or decidable languages.
- Recursive languages are a subset of RE languages, since every TM that decides a language also accepts it, but not vice versa .
- The size of the language accepted by a TM is the number of strings that the TM accepts. It can be finite or infinite, depending on the TM and the language.