### Representation of Turing Machines

A Turing machine is a theoretical model of computation that can perform any algorithmic task. A Turing machine consists of:

- A tape that is divided into cells, each cell containing a symbol from a finite alphabet.
- A tape head that can read and write symbols on the tape, and move left or right one cell at a time.
- A finite set of states, one of which is designated as the initial state, and some of which are designated as final or accepting states.
- A transition function that specifies, for each state and symbol, what the machine should do: the new state, the new symbol, and the direction of movement.

There are different ways of representing Turing machines, such as:

- State diagrams: These are graphical representations of Turing machines, where each state is represented by a circle, and each transition is represented by an arrow labeled with the current symbol, the new symbol, and the direction of movement. For example, the following state diagram represents a Turing machine that accepts the language of even-length palindromes over the alphabet {a, b}:

![State diagram of a Turing machine for even-length palindromes](https://human.libretexts.org/@api/deki/files/1069/TMpalindrome.png)

- Machine tables: These are tabular representations of Turing machines, where each row corresponds to a state, and each column corresponds to a symbol. The entries in the table indicate the new state, the new symbol, and the direction of movement for each state and symbol combination. For example, the following machine table represents the same Turing machine as the state diagram above:

| State | a | b | B |
| --- | --- | --- | --- |
| q0 | q1, a, R | q2, b, R | qf, B, R |
| q1 | q1, a, R | q1, b, R | q3, B, L |
| q2 | q2, a, R | q2, b, R | q4, B, L |
| q3 | q5, B, L | q6, B, L | qf, B, R |
| q4 | q6, B, L | q5, B, L | qf, B, R |
| q5 | q5, a, L | q5, b, L | q0, B, R |
| q6 | q6, a, L | q6, b, L | q0, B, R |
| qf | - | - | - |

- Formal notation: This is a mathematical notation of Turing machines, where a Turing machine is defined by a tuple of the form (Q, Σ, Γ, δ, q0, B, F), where:

  - Q is the set of states
  - Σ is the input alphabet
  - Γ is the tape alphabet, such that Σ ⊆ Γ
  - δ is the transition function, such that δ: Q × Γ → Q × Γ × {L, R}
  - q0 is the initial state
  - B is the blank symbol, such that B ∈ Γ and B ∉ Σ
  - F is the set of final or accepting states, such that F ⊆ Q

  For example, the following formal notation represents the same Turing machine as the state diagram and the machine table above:

  ( {q0, q1, q2, q3, q4, q5, q6, qf}, {a, b}, {a, b, B}, δ, q0, B, {qf} )

  where δ is defined by the table above.