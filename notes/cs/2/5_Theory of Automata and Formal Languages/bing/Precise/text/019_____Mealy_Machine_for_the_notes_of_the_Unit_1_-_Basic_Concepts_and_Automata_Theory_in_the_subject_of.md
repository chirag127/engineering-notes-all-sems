### Mealy Machine
A Mealy Machine is a type of finite state machine (FSM) where the output is determined by the current state and the input. It is named after George H. Mealy, who introduced the concept in 1955.

Here are some key points to remember about Mealy Machines:
- A Mealy Machine is a 6-tuple (Q, Σ, O, δ, λ, q0) where:
  - Q is a finite set of states
  - Σ is a finite input alphabet
  - O is a finite output alphabet
  - δ: Q × Σ → Q is the transition function
  - λ: Q × Σ → O is the output function
  - q0 ∈ Q is the initial state
- The output of a Mealy Machine depends on both the current state and the input.
- Mealy Machines are used in digital logic design, control systems, and communication systems.
- Mealy Machines can be represented using state transition diagrams or state transition tables.
- Mealy Machines can be converted to Moore Machines and vice versa.
