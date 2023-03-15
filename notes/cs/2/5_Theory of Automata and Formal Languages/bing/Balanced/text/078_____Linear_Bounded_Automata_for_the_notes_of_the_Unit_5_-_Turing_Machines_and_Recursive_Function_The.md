### Linear Bounded Automata

- A linear bounded automaton (LBA) is a type of Turing machine that has a finite amount of tape to perform computations on.
- An LBA can be defined as an 8-tuple (Q, X, ∑, q 0, ML, MR, δ, F) where :
  - Q is a finite set of states
  - X is the tape alphabet, which includes two special symbols ML and MR, serving as left and right endmarkers
  - ∑ is the input alphabet, a subset of X without ML and MR
  - q 0 is the initial state
  - ML and MR are the left and right endmarkers, respectively
  - δ is the transition function, which maps Q × X to a subset of Q × X × {L, R, S}, where L, R, and S are the tape head movements (left, right, and stay)
  - F is the set of final or accepting states, a subset of Q
- An LBA accepts an input string w if there exists a sequence of transitions that starts from the initial configuration (q 0, MLwMR) and ends in a final configuration (q f, MLwMR), where q f is in F .
- An LBA is nondeterministic, meaning that it can have more than one possible transition for a given state and tape symbol .
- An LBA is multi-track, meaning that it can have more than one symbol in each tape cell, separated by a delimiter .
- An LBA is linear bounded, meaning that it can only use the tape cells that contain the input string and the endmarkers. It cannot move the tape head beyond the endmarkers or overwrite them  .
- An LBA can recognize a class of languages called context-sensitive languages, which are more powerful than context-free languages but less powerful than recursively enumerable languages .
- An LBA can be converted into an equivalent context-sensitive grammar, and vice versa .
- An LBA can be simulated by a Turing machine with a tape of length O(n), where n is the length of the input string .
- An LBA can be used to model some problems that require a bounded amount of memory, such as parsing, pattern matching, and arithmetic operations .

: Linear bounded automaton - Wikipedia
: Linear Bounded Automata - tutorialspoint.com
: Introduction to Linear Bounded Automata (LBA) - GeeksforGeeks