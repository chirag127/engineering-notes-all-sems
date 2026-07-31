## Design, and verify the 4-bit synchronous counter for the notes of the Discrete Structure & Logic Lab in the subject of Discrete Structure & Logic

A 4-bit synchronous counter is a digital circuit that can count from 0 to 15 in binary using four flip-flops that are synchronized by a common clock signal. The flip-flops can be of any type, such as JK, D, or T, but they must have the same characteristic equation and propagation delay. The output of each flip-flop is connected to the input of the next one in a chain, and the input of the first flip-flop is controlled by a logic circuit that determines the counting sequence. The logic circuit can be designed using a state diagram, a state table, or a Karnaugh map.

The following steps can be followed to design and verify a 4-bit synchronous counter using JK flip-flops:

1. Draw the state diagram of the counter, showing the transitions from one state to another for each clock pulse. The states are labeled with the binary values of the outputs, and the transitions are labeled with the inputs that cause them. For example, the state diagram of a 4-bit synchronous up counter is shown below:

![State diagram of 4-bit synchronous up counter](https://physicsteacher.in/wp-content/uploads/2021/12/4-bit-synchronous-counter-state-diagram.png)

2. Draw the state table of the counter, showing the present state, the next state, and the inputs for each state transition. The present state and the next state are represented by the binary values of the outputs, and the inputs are represented by the values of J and K for each flip-flop. For example, the state table of a 4-bit synchronous up counter is shown below:

| Present State | Next State | Inputs |
| Q3 Q2 Q1 Q0 | Q3 Q2 Q1 Q0 | J3 K3 J2 K2 J1 K1 J0 K0 |
| 0 0 0 0 | 0 0 0 1 | 0 0 0 0 0 0 1 1 |
| 0 0 0 1 | 0 0 1 0 | 0 0 0 0 1 1 0 0 |
| 0 0 1 0 | 0 0 1 1 | 0 0 0 0 0 0 1 1 |
| 0 0 1 1 | 0 1 0 0 | 0 0 1 1 0 0 0 0 |
| 0 1 0 0 | 0 1 0 1 | 0 0 0 0 0 0 1 1 |
| 0 1 0 1 | 0 1 1 0 | 0 0 0 0 1 1 0 0 |
| 0 1 1 0 | 0 1 1 1 | 0 0 0 0 0 0 1 1 |
| 0 1 1 1 | 1 0 0 0 | 1 1 0 0 0 0 0 0 |
| 1 0 0 0 | 1 0 0 1 | 0 0 0 0 0 0 1 1 |
| 1 0 0 1 | 1 0 1 0 | 0 0 0 0 1 1 0 0 |
| 1 0 1 0 | 1 0 1 1 | 0 0 0 0 0 0 1 1 |
| 1 0 1 1 | 1 1 0 0 | 0 0 1 1 0 0 0 0 |
| 1 1 0 0 | 1 1 0 1 | 0 0 0 0 0 0 1 1 |
| 1 1 0 1 | 1 1 1 0 | 0 0 0 0 1 1 0 0 |
| 1 1 1 0 | 1 1 1 1 | 0 0 0 0 0