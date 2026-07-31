# Linear Bounded Automata

- A linear bounded automaton (LBA) is a type of Turing machine that has a finite amount of tape to work with.
- The tape is divided into cells, each containing a symbol from the tape alphabet.
- The tape alphabet includes two special symbols, called left and right endmarkers, that mark the boundaries of the tape.
- The LBA has a finite set of states and a transition function that determines how it moves from one state to another, depending on the current state and the symbol under the tape head.
- The LBA can also write a new symbol on the tape cell, replacing the old one, and move the tape head one cell to the left or right.
- The LBA can be deterministic or nondeterministic, meaning that it can have one or more possible transitions for a given state and symbol.
- The LBA can be multi-track, meaning that it can have more than one tape head and more than one symbol per cell.
- The LBA can accept or reject an input string by entering a special state, called an accepting or rejecting state, respectively.
- The LBA can also halt without accepting or rejecting, if it has no applicable transition for the current state and symbol.
- The LBA is said to recognize a language if it accepts all and only the strings that belong to that language.
- The LBA is more powerful than a finite automaton or a pushdown automaton, but less powerful than a general Turing machine.
- The LBA can recognize context-sensitive languages, which are a subset of recursively enumerable languages.
- The LBA can also decide context-sensitive languages, which are a subset of recursive languages.
- The LBA is equivalent to a Turing machine with a tape length that is a linear function of the input length.
- The LBA is also equivalent to a grammar that generates context-sensitive languages, called a linear bounded grammar.

: Linear bounded automaton - Wikipedia
: Linear Bounded Automata - tutorialspoint.com
: Introduction to Linear Bounded Automata (LBA) - GeeksforGeeks