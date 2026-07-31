# Finite Automata with Output

- A finite automata with output is a mathematical model of computation that can be in one of a finite number of states and can produce output symbols based on the input symbols and the current state .
- A finite automata with output is also known as a finite state machine (FSM) or a transducer .
- There are two types of finite automata with output: Moore machines and Mealy machines.
- A Moore machine is a finite automata with output where the output depends only on the current state. The output is associated with each state and is produced whenever the machine enters that state.
- A Mealy machine is a finite automata with output where the output depends on both the current state and the input symbol. The output is associated with each transition and is produced whenever the machine takes that transition.
- A finite automata with output can be represented by a 6-tuple (Q, Σ, Γ, δ, λ, q0) where :
  - Q is a finite set of states
  - Σ is a finite input alphabet
  - Γ is a finite output alphabet
  - δ is a transition function that maps Q × Σ to Q
  - λ is an output function that maps Q to Γ (for Moore machines) or Q × Σ to Γ (for Mealy machines)
  - q0 is the initial state in Q
- A finite automata with output can be used to model various systems that have discrete inputs, outputs, and states, such as digital circuits, communication protocols, parsers, etc.  .
- A finite automata with output can be converted from one type to another by adding or removing states and transitions.
- A finite automata with output can be simulated by a program that keeps track of the current state, reads the input symbols, updates the state according to the transition function, and produces the output symbols according to the output function.