### Linear Bounded Automata

- A linear bounded automaton (LBA) is a type of Turing machine that has a finite tape of bounded length and can only access the part of the tape that contains the input and some extra space  .
- The tape length is a function of the input length, such as c*n, where c is a constant and n is the input length.
- The input alphabet of an LBA contains two special symbols, called left and right endmarkers, that mark the boundaries of the tape  .
- The transition function of an LBA cannot print any other symbols over the endmarkers, and cannot move the head beyond them  .
- An LBA can be defined as an 8-tuple (Q, X, ∑, q0, ML, MR, δ, F), where :
  - Q is a finite set of states
  - X is the tape alphabet, which contains ∑, the input alphabet, and the endmarkers
  - q0 is the initial state
  - ML and MR are the left and right endmarkers, respectively
  - δ is the transition function, which maps Q × X to a subset of Q × X × {L, R, S}, where L, R, and S are the head movements
  - F is the set of final or accepting states
- An LBA accepts an input string w if there is a sequence of transitions that leads from the initial configuration to a final configuration, where the head is on the right endmarker and the state is in F .
- An LBA can be deterministic or nondeterministic, depending on whether the transition function is a function or a relation .
- An LBA can be single-track or multi-track, depending on whether the tape alphabet has one or more symbols per cell .
- The class of languages recognized by LBAs is called context-sensitive languages, and is denoted by CSL  .
- LBAs are more powerful than pushdown automata, but less powerful than general Turing machines  .

#### Examples of Linear Bounded Automata

- An LBA that accepts the language L = {a^n b^n c^n | n ≥ 1} can be defined as follows:
  - Q = {q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11}
  - X = {a, b, c, A, B, C, ML, MR}
  - ∑ = {a, b, c}
  - q0 is the initial state
  - ML and MR are the left and right endmarkers, respectively
  - δ is the transition function, defined by the following table:

| Current state | Current symbol | Next state | Next symbol | Head movement |
|---------------|----------------|------------|-------------|---------------|
| q0 | ML | q1 | ML | R |
| q1 | a | q2 | A | R |
| q1 | MR | q11 | MR | S |
| q2 | a | q2 | a | R |
| q2 | b | q3 | B | R |
| q3 | b | q3 | b | R |
| q3 | c | q4 | C | L |
| q4 | b | q4 | b | L |
| q4 | B | q5 | B | L |
| q5 | a | q5 | a | L |
| q5 | A | q1 | A | R |
| q6 | A | q6 | A | R |
| q6 | B | q7 | B | R |
| q7 | B | q7 | B | R |
| q7 | C | q8 | C | R |
| q8 | C | q8 | C | R |
| q8 | MR | q9 | MR | L |
| q9 | C | q9 | C | L |
| q9 | B | q10 | B | L |
| q10 | B | q10 | B