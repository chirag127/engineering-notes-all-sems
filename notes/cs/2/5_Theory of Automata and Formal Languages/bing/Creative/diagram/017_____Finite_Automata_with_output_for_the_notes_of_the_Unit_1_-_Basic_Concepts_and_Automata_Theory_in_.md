### Finite Automata with Output

- A finite automata with output is a mathematical model of computation that can be in one of a finite number of states and can produce output symbols depending on the current state and the input symbol .
- A finite automata with output is also known as a finite state machine (FSM) or a transducer .
- There are two types of finite automata with output: Moore machines and Mealy machines  .
- A Moore machine is a finite automata with output where the output depends only on the current state  .
- A Mealy machine is a finite automata with output where the output depends on both the current state and the input symbol  .
- A finite automata with output can be represented by a 6-tuple (Q, Σ, Δ, δ, λ, q0) where :
  - Q is a finite set of states
  - Σ is a finite input alphabet
  - Δ is a finite output alphabet
  - δ is a transition function that maps Q × Σ to Q
  - λ is an output function that maps Q × Σ to Δ for Mealy machines or Q to Δ for Moore machines
  - q0 is the initial state in Q
- A finite automata with output can be used to model various systems that have discrete inputs, outputs, and states, such as digital circuits, communication protocols, parsers, etc.  .
- A finite automata with output can be visualized by a state diagram, where each state is represented by a circle, each transition by an arrow, and each output by a label on the arrow (for Mealy machines) or on the circle (for Moore machines)  .
- For example, the following state diagram shows a Mealy machine that takes a binary number as input and produces its 1's complement as output:

![Mealy machine example](https://media.geeksforgeeks.org/wp-content/uploads/20210119171748/Mealy-Machine-1.png)

- The following state diagram shows a Moore machine that takes a binary number as input and produces its 1's complement as output:

![Moore machine example](https://media.geeksforgeeks.org/wp-content/uploads/20210119171748/Moore-Machine-1.png)