# Representation of Turing Machines

- A Turing machine is a mathematical model of computation describing an abstract machine that manipulates symbols on a strip of tape according to a table of rules.
- A Turing machine can be specified by a five-tuple (Q, Σ, Γ, δ, q0), where
  - Q is a finite set of states
  - Σ is a finite set of input symbols
  - Γ is a finite set of tape symbols, such that Σ ⊆ Γ and a special blank symbol ∈ Γ
  - δ is a transition function that maps Q × Γ to Q × Γ × {L, R}, where L and R denote left and right movements of the tape head
  - q0 is the initial state
- A Turing machine can be represented visually by state diagrams or machine tables.
- A state diagram is composed of state cells connected by arrows. Each state cell represents a state of the machine, and each arrow represents an instruction. The arrow is labeled with the current symbol, the new symbol, and the direction of movement. For example, the arrow labeled 0/1,R means that if the current symbol is 0, replace it with 1 and move the tape head to the right.
- A machine table has the tape alphabet displayed on the x-axis, and the set of machine states across the y-axis. Inside the table, at the intersection of each state and symbol, is written the rest of the instruction—the new state, new symbol, and direction of movement. For example, the entry q1,1,L means that if the current state is q0 and the current symbol is 0, then the new state is q1, the new symbol is 1, and the tape head moves to the left.
- Here is an example of a Turing machine that increments a binary number by one, represented by both a state diagram and a machine table:

![State diagram of a Turing machine that increments a binary number by one](https://human.libretexts.org/@api/deki/files/1184/=turing_machine_increment.png)

| State \ Symbol | 0 | 1 | |
| --- | --- | --- | --- |
| q0 | q0,0,R | q0,1,R | |
| q1 | q1,0,L | q1,1,L | |
| q2 | q3,1,R | q2,0,L | |
| q3 | | | HALT |