### Representation of Turing Machines

- A Turing machine is a mathematical model of computation describing an abstract machine that manipulates symbols on a strip of tape according to a table of rules.
- A Turing machine can be specified by a five-tuple (Q, Σ, Γ, δ, q0), where:
  - Q is a finite set of states
  - Σ is a finite set of input symbols
  - Γ is a finite set of tape symbols, such that Σ ⊆ Γ
  - δ is a partial function from Q × Γ to Q × Γ × {L, R}, called the transition function
  - q0 is the initial state
- A Turing machine can be represented visually by state diagrams. The diagrams are composed of state cells connected by arrows. Unsurprisingly, each state cell represents a state of the machine.
- Each arrow represents a transition from one state to another, and is labeled with the current symbol, the new symbol, and the direction of movement. For example, an arrow labeled 0/1R means that if the current symbol is 0, replace it with 1 and move the head right.
- Machine tables are another way of representing Turing machines. Machine tables have the tape alphabet displayed on the x-axis, and the set of machine states across the y-axis. Inside the table, at the intersection of each state and symbol, is written the rest of the instruction—the new state, new symbol, and direction of movement.
- For example, the following table represents a Turing machine that adds one to a binary number:

|   | 0 | 1 | B |
|---|---|---|---|
| q0| q1, 0, R | q0, 1, R | q2, B, L |
| q1| q1, 0, R | q1, 1, R | q3, 1, L |
| q2| q4, 1, L | q2, 0, L |   |
| q3| q4, 0, L | q3, 1, L |   |
| q4|   |   |   |

- The initial state is q0, and the final state is q4. The blank symbol is B. The input is assumed to be a binary number with the least significant bit on the left, followed by a blank symbol. For example, the input 101B represents the number 5. The output is the same binary number with one added to it, followed by a blank symbol. For example, the output 110B represents the number 6.
- A Turing machine can also be represented by a string of symbols, using a standard encoding scheme. For example, one possible encoding scheme is to use the symbols 0, 1, and # to encode the five-tuple of a Turing machine, as follows:
  - The set of states Q is encoded by assigning a unique binary number to each state, starting from 0. For example, if Q = {q0, q1, q2, q3, q4}, then q0 is encoded as 0, q1 as 1, q2 as 10, q3 as 11, and q4 as 100.
  - The set of input symbols Σ is encoded by assigning a unique binary number to each symbol, starting from 0. For example, if Σ = {0, 1}, then 0 is encoded as 0, and 1 as 1.
  - The set of tape symbols Γ is encoded by assigning a unique binary number to each symbol, starting from 0. For example, if Γ = {0, 1, B}, then 0 is encoded as 0, 1 as 1, and B as 10.
  - The transition function δ is encoded by listing all the defined transitions in the form (current state, current symbol, new state, new symbol, direction), separated by #. Each component of the transition is encoded by its corresponding binary number. For example, the transition (q0, 0, q1, 0, R) is encoded as 0#0#1#0#0, where R is encoded as 0, and L as 1.
  - The initial state q0 is encoded by its corresponding binary number.
  - The final state is encoded by a special symbol, such as *.
- The encoding of