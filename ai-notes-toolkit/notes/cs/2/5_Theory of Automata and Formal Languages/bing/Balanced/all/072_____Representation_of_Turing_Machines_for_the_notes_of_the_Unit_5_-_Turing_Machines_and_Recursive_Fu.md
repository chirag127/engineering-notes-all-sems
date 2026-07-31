# Representation of Turing Machines

- A Turing machine is a theoretical model of computation that can perform any algorithmic task by manipulating symbols on an infinite tape according to a finite set of rules.
- A Turing machine consists of four components: a tape, a tape head, a state register, and a transition function.
- The tape is divided into cells, each of which can hold one symbol from a finite alphabet. The tape is infinite in both directions, and the tape head can move left or right along the tape.
- The state register stores the current state of the machine, which is one of a finite number of possible states. The initial state is usually denoted by q0, and the final state by qf.
- The transition function is a set of instructions that specify how the machine should change its state, symbol, and tape head movement based on the current state and symbol. The transition function can be represented by a table, a diagram, or a formula.
- A table representation of a Turing machine has the tape alphabet displayed on the x-axis, and the set of machine states across the y-axis. Inside the table, at the intersection of each state and symbol, is written the rest of the instruction—the new state, new symbol, and direction of movement. For example, the table below represents a Turing machine that adds one to a binary number.

| | 0 | 1 | B |
|---|---|---|---|
| q0 | q0, 0, R | q0, 1, R | q1, B, L |
| q1 | q2, 1, L | q1, 0, L | qf, B, R |
| q2 | q2, 0, L | q2, 1, L | q0, B, R |

- A diagram representation of a Turing machine has state cells connected by arrows. Each state cell represents a state of the machine, and each arrow represents a transition rule. The arrow is labeled with the input symbol, the output symbol, and the direction of movement. For example, the diagram below represents the same Turing machine as the table above.

![Turing machine diagram](https://human.libretexts.org/@api/deki/files/1330/TM_diagram.png)

- A formula representation of a Turing machine uses a mathematical notation to describe the transition function. For example, the formula below represents the same Turing machine as the table and the diagram above.

δ(q0, 0) = (q0, 0, R)  
δ(q0, 1) = (q0, 1, R)  
δ(q0, B) = (q1, B, L)  
δ(q1, 0) = (q2, 1, L)  
δ(q1, 1) = (q1, 0, L)  
δ(q1, B) = (qf, B, R)  
δ(q2, 0) = (q2, 0, L)  
δ(q2, 1) = (q2, 1, L)  
δ(q2, B) = (q0, B, R)

- A Turing machine can be in one of three modes: accepting, rejecting, or looping. An accepting mode means that the machine has reached the final state and has successfully completed its task. A rejecting mode means that the machine has reached a state that is not the final state and has no applicable transition rule. A looping mode means that the machine is stuck in an infinite cycle of states and symbols and never reaches the final state.