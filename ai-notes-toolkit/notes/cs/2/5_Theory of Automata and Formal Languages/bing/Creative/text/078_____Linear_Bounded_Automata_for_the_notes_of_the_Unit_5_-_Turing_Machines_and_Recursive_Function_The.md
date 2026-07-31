### Linear Bounded Automata

- A linear bounded automaton (LBA) is a type of Turing machine that has a finite and fixed amount of tape to perform computations on.
- An LBA can be formally defined as an 8-tuple (Q, X, ∑, q 0, ML, MR, δ, F) where :
  - Q is a finite set of states
  - X is the tape alphabet, which includes two special symbols ML and MR, serving as left and right endmarkers
  - ∑ is the input alphabet, a subset of X without ML and MR
  - q 0 is the initial state
  - ML and MR are the left and right endmarkers, respectively
  - δ is the transition function, which maps Q × X to a subset of Q × X × {L, R, S}, where L, R, and S are the tape head movements (left, right, and stay)
  - F is the set of final or accepting states, a subset of Q
- An LBA accepts an input string w ∈ ∑* if there exists a sequence of transitions that leads from the initial configuration MLwMRq 0 to a final configuration MLxq fMR, where q f ∈ F and x ∈ X* .
- An LBA is equivalent to a multi-track Turing machine with a bounded finite length of the tape.
- The class of languages recognized by LBAs is called context-sensitive languages (CSLs) .
- LBAs are more powerful than pushdown automata, but less powerful than general Turing machines .
- LBAs can be used to model some real-world problems, such as parsing context-sensitive grammars, checking array bounds, and verifying program properties.