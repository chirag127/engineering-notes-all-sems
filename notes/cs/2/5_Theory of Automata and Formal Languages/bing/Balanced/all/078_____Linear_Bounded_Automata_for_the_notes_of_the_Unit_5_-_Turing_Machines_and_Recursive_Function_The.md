# Linear Bounded Automata

- A linear bounded automaton (LBA) is a type of Turing machine that has a finite amount of tape to work with.
- The tape is divided into cells, each containing a symbol from a finite alphabet.
- The tape has two special symbols, called left and right endmarkers, that mark the boundaries of the tape.
- The LBA has a finite set of states and a transition function that determines how it moves from one state to another, depending on the current state and the symbol under the tape head.
- The LBA can also change the symbol under the tape head, except for the endmarkers.
- The LBA can move the tape head left or right, but not beyond the endmarkers.
- The LBA can be deterministic or nondeterministic, meaning that it can have one or more possible transitions for a given state and symbol.
- The LBA can accept or reject an input string by entering a special state, called an accepting or rejecting state, respectively.
- The LBA can also halt without accepting or rejecting, by entering a state that has no transitions defined.
- The LBA is a restricted model of computation, since it cannot use more tape than the length of the input string, multiplied by a constant factor.
- The LBA can recognize a class of languages, called context-sensitive languages, that are more expressive than context-free languages, but less expressive than recursively enumerable languages.
- The LBA can be defined formally as an 8-tuple (Q, X, ∑, q0, ML, MR, δ, F), where:

  - Q is a finite set of states
  - X is the tape alphabet, which includes the endmarkers ML and MR
  - ∑ is the input alphabet, which is a subset of X without the endmarkers
  - q0 is the initial state
  - ML and MR are the left and right endmarkers, respectively
  - δ is the transition function, which maps Q × X to a subset of Q × X × {L, R}, where L and R are the left and right tape head movements, respectively
  - F is the set of accepting states, which is a subset of Q

- An example of an LBA that accepts the language {a^n b^n c^n | n ≥ 1} is shown below:

![LBA example](https://i.imgur.com/9gQFQ0M.png)

- The LBA starts with the input string between the endmarkers, and then scans the tape from left to right, marking each a with an A, each b with a B, and each c with a C, while checking that the number of a's, b's, and c's are equal.
- If the LBA finds a mismatch or an invalid symbol, it rejects the input by entering the state qR.
- If the LBA reaches the right endmarker without finding any errors, it accepts the input by entering the state qF.