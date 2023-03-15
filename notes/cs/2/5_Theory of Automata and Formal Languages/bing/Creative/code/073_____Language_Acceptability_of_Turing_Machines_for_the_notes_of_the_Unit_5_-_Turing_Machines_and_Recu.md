### Language Acceptability of Turing Machines

- A Turing machine (TM) is a mathematical model of computation that can perform any algorithmic task.
- A TM consists of a finite control, an infinite tape divided into cells, and a tape head that can read and write symbols on the tape and move left or right.
- A TM can be in one of a finite number of states, including a special start state and one or more final states.
- A TM accepts an input string if it starts in the start state with the input on the tape, and eventually halts in a final state.
- A TM rejects an input string if it either halts in a non-final state, or does not halt at all.
- A TM decides a language if it accepts all the strings in the language and rejects all the strings not in the language.
- A language is Turing-acceptable if there exists a TM that accepts it.
- A language is Turing-decidable or recursive if there exists a TM that decides it.
- A language is recursively enumerable or semi-decidable if there exists a TM that accepts it, but may or may not halt on strings not in the language.
- A language is not recursively enumerable if there is no TM that accepts it.
- Every Turing-decidable language is also Turing-acceptable and recursively enumerable, but the converse is not true.
- The class of Turing-acceptable languages is equivalent to the class of Type-0 languages in the Chomsky hierarchy.
- The class of Turing-decidable languages is a proper subset of the class of Turing-acceptable languages.