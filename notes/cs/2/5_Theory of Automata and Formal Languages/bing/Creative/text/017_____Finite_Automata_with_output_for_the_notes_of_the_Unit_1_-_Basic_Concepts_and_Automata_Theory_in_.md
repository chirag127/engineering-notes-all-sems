### Finite Automata with Output

- A finite automata with output is a mathematical model of computation that can be in one of a finite number of states and can produce output symbols depending on the current state and the input symbol .
- A finite automata with output is also known as a finite state machine (FSM) or a transducer .
- There are two types of finite automata with output: Moore machines and Mealy machines  .
- A Moore machine is a finite automata with output where the output depends only on the current state  .
- A Mealy machine is a finite automata with output where the output depends on both the current state and the input symbol  .
- A finite automata with output can be represented by a five-tuple (Q, Σ, Δ, δ, λ), where  :
  - Q is a finite set of states
  - Σ is a finite input alphabet
  - Δ is a finite output alphabet
  - δ is a transition function that maps Q × Σ to Q
  - λ is an output function that maps Q × Σ (for Mealy machines) or Q (for Moore machines) to Δ
- A finite automata with output can be visualized by a state diagram, where each state is represented by a circle, each transition is represented by an arrow labeled with an input symbol, and each output is represented by a symbol next to the state (for Moore machines) or next to the transition (for Mealy machines)  .
- A finite automata with output can be used to model various systems that have discrete inputs, outputs, and states, such as digital circuits, communication protocols, parsers, etc.  .