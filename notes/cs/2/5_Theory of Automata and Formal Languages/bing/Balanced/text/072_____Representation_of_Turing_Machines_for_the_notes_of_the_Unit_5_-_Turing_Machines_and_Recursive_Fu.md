### Representation of Turing Machines

- A Turing machine is a mathematical model of computation describing an abstract machine that manipulates symbols on a strip of tape according to a table of rules.
- A Turing machine can be specified by a five-tuple (Q, Σ, Γ, δ, q0), where:
  - Q is a finite set of states
  - Σ is a finite set of input symbols
  - Γ is a finite set of tape symbols, such that Σ ⊆ Γ and a special blank symbol ∈ Γ
  - δ is a partial function from Q × Γ to Q × Γ × {L, R}, where L and R denote the left and right movement of the tape head
  - q0 is the initial state
- A Turing machine can be represented visually by state diagrams. The diagrams are composed of state cells connected by arrows. Each state cell represents a state of the machine, and each arrow represents an instruction of the form (current symbol, new symbol, direction).
- Machine tables are another way of representing Turing machines. Machine tables have the tape alphabet displayed on the x-axis, and the set of machine states across the y-axis. Inside the table, at the intersection of each state and symbol, is written the rest of the instruction—the new state, new symbol, and direction of movement.
- Here is an example of a Turing machine that accepts the language {0^n1^n | n ≥ 0} and its representation by a state diagram and a machine table:

![State diagram of Turing machine](https://gyires.inf.unideb.hu/GyBITT/26/images/tm1.png)

| State \ Symbol | 0 | 1 | X | Y | blank |
| -------------- | - | - | - | - | ----- |
| q0             | (q1, X, R) | (q4, Y, R) | (q0, X, R) | (q0, Y, R) | (q5, blank, L) |
| q1             | (q1, 0, R) | (q2, Y, L) | (q1, X, R) | (q1, Y, R) | - |
| q2             | (q3, X, L) | (q2, 1, L) | (q2, X, L) | (q2, Y, L) | - |
| q3             | (q3, 0, L) | (q3, 1, L) | (q0, X, R) | (q3, Y, L) | - |
| q4             | - | (q4, Y, R) | (q4, X, R) | (q4, Y, R) | (q5, blank, L) |
| q5             | - | - | - | - | - |