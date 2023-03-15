### Linear Bounded Automata

- A linear bounded automaton (LBA) is a type of Turing machine that has a finite tape of bounded length and can only access the part of the tape that contains the input and two special symbols that mark the left and right ends of the tape  .
- An LBA can be defined as an 8-tuple (Q, X, ∑, q 0, ML, MR, δ, F) where :
  - Q is a finite set of states
  - X is the tape alphabet
  - ∑ is the input alphabet, which is a subset of X and does not include the endmarkers ML and MR
  - q 0 is the initial state
  - ML and MR are the left and right endmarkers, respectively
  - δ is the transition function, which maps Q × X to a subset of Q × X × {L, R, S}, where L, R, and S are the tape head movements (left, right, and stay)
  - F is the set of final or accepting states
- An LBA accepts an input string w if there exists a sequence of transitions that starts from the initial configuration (q 0, MLwMR) and ends in a final configuration (q f, MLwMR), where q f is in F .
- An LBA is nondeterministic, meaning that it can have more than one possible transition for a given state and tape symbol  .
- An LBA is multi-track, meaning that it can have more than one symbol in each tape cell, separated by a delimiter .
- The length of the tape of an LBA is a function of the length of the input string and a constant c, such that memory information ≤ c × input information .
- The language accepted by an LBA is called a context-sensitive language (CSL), which is a subset of the recursively enumerable languages (REL)  .
- An LBA is equivalent to a context-sensitive grammar (CSG), meaning that for every LBA there exists a CSG that generates the same language, and vice versa  .
- An LBA is less powerful than a general Turing machine, which has an infinite tape and can access any part of it  .
- An LBA is more powerful than a pushdown automaton (PDA), which has a finite tape and a stack that can only be accessed from the top  .

: Linear bounded automaton - Wikipedia
: Linear Bounded Automata - tutorialspoint.com
: Introduction to Linear Bounded Automata (LBA) - GeeksforGeeks
: Linear Bounded Automata (LBA) Definition - YouTube