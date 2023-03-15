### Mealy Machine

A Mealy Machine is a type of finite state machine (FSM) used in digital logic and computer science. It is named after George H. Mealy, who introduced the concept in 1955.

- A Mealy Machine is a 6-tuple (Q, Σ, O, δ, λ, q0) where:
  - Q is a finite set of states.
  - Σ is a finite input alphabet.
  - O is a finite output alphabet.
  - δ: Q × Σ → Q is the transition function.
  - λ: Q × Σ → O is the output function.
  - q0 ∈ Q is the initial state.

- In a Mealy Machine, the output is determined by the current state and the current input.
- The output is associated with the transition, rather than the state.
- Mealy Machines are used in the design of sequential logic circuits, such as counters, shift registers, and sequence detectors.
- Mealy Machines can be converted to equivalent Moore Machines, and vice versa.
