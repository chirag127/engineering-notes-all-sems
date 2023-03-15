### Representation of Turing Machines

- A Turing machine is a mathematical model of computation describing an abstract machine that manipulates symbols on a strip of tape according to a table of rules.
- A Turing machine can be used to distinguish the problems, which problem is solvable and which is unsolvable. It is a very powerful machine as compared with other automata machines.
- A Turing machine can be represented visually by state diagrams or machine tables.
- A state diagram is composed of state cells connected by arrows. Each state cell represents a state of the machine. Each arrow represents an instruction that consists of the current symbol, the new symbol, the new state, and the direction of movement.
- A machine table has the tape alphabet displayed on the x-axis, and the set of machine states across the y-axis. Inside the table, at the intersection of each state and symbol, is written the rest of the instruction—the new state, new symbol, and direction of movement.
- An example of a state diagram and a machine table for a Turing machine that accepts the language {0^n 1^n | n >= 0} is shown below:

![State diagram](https://human.libretexts.org/@api/deki/files/1400/=state_diagram.png)

| | 0 | 1 | B |
|---|---|---|---|
| q0 | q1, 0, R | q4, 1, R | q4, B, R |
| q1 | q1, 0, R | q2, 1, L | q4, B, R |
| q2 | q3, B, L | q2, 1, L | q4, B, R |
| q3 | q0, B, R | q4, 1, R | qf, B, R |
| q4 | q4, 0, R | q4, 1, R | q4, B, R |
| qf | qf, 0, R | qf, 1, R | qf, B, R |