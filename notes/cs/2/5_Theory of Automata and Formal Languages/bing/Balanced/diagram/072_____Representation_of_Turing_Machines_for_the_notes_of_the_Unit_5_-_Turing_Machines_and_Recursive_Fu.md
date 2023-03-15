### Representation of Turing Machines

- A Turing machine is a mathematical model of computation describing an abstract machine that manipulates symbols on a strip of tape according to a table of rules.
- A Turing machine can be specified by a five-tuple (Q, Σ, Γ, δ, q0), where :
  - Q is a finite set of states
  - Σ is a finite set of input symbols
  - Γ is a finite set of tape symbols, such that Σ ⊆ Γ
  - δ is a partial function from Q × Γ to Q × Γ × {L, R}, called the transition function
  - q0 is the initial state
- A Turing machine can be represented visually by state diagrams. The diagrams are composed of state cells connected by arrows. Unsurprisingly, each state cell represents a state of the machine.
- Each arrow represents a transition from one state to another, and is labeled with the current symbol, the new symbol, and the direction of movement. For example, an arrow labeled 0/1,R means that if the current symbol is 0, replace it with 1 and move the tape head to the right.
- Machine tables are another way of representing Turing machines. Machine tables have the tape alphabet displayed on the x-axis, and the set of machine states across the y-axis. Inside the table, at the intersection of each state and symbol, is written the rest of the instruction—the new state, new symbol, and direction of movement.
- For example, the following machine table represents a Turing machine that adds one to a binary number:

|     | 0   | 1   | B   |
| --- | --- | --- | --- |
| q0  | q1,0,R | q0,1,R | q2,B,L |
| q1  | q1,0,R | q1,1,R | q3,B,L |
| q2  | q4,1,L | q2,0,L | q5,B,R |
| q3  | q3,0,L | q3,1,L | q0,B,R |
| q4  | q4,0,L | q4,1,L | q5,B,R |
| q5  |     |     |     |

- Here, B is the blank symbol, and q5 is the final state. The table can be read as follows: if the machine is in state q0 and reads 0, it writes 0, moves to the right, and goes to state q1. If the machine is in state q2 and reads B, it writes B, moves to the left, and goes to state q5.
- A Turing machine can also be represented by a string of symbols, using a standard encoding scheme. For example, one possible encoding scheme is to use the symbols #, 0, 1, L, R, and B to represent the components of a Turing machine, and separate them by commas. The encoding scheme can be defined as follows:
  - The set of states Q is encoded by the binary numbers 0, 1, 10, 11, ..., in the order of their appearance in Q.
  - The set of input symbols Σ is encoded by the binary numbers 0, 1, 10, 11, ..., in the order of their appearance in Σ.
  - The set of tape symbols Γ is encoded by the binary numbers 0, 1, 10, 11, ..., in the order of their appearance in Γ, followed by B for the blank symbol.
  - The initial state q0 is encoded by the binary number corresponding to its position in Q.
  - The transition function δ is encoded by a list of quadruples, each consisting of the current state, the current symbol, the new state, and the new symbol, followed by L or R for the direction of movement. Each quadruple is separated by a comma, and the list is terminated by a # symbol.
  - The final state qf is encoded by the binary number corresponding to its position in Q, followed by a # symbol.
- For example, using this encoding scheme, the Turing machine that adds one to a binary number can be represented by the following string:

0,0,1,0,R,0,1,0,1,R,0,B,10,B,L,1,0,1,0,R,1,1,1