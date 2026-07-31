### Moore Machine

- A Moore machine is a type of finite state machine (FSM) that has an output function that depends only on the current state.
- A Moore machine can be formally defined as a 6-tuple (Q, Σ, Δ, δ, λ, q0) where:
  - Q is a finite set of states
  - Σ is a finite input alphabet
  - Δ is a finite output alphabet
  - δ: Q × Σ → Q is the state transition function
  - λ: Q → Δ is the output function
  - q0 ∈ Q is the initial state
- A Moore machine can be represented by a state diagram, where each state is labeled with its output value and each transition is labeled with its input symbol.
- A Moore machine can also be represented by a state table, where each row corresponds to a state, each column corresponds to an input symbol, and each cell contains the next state and the output value.
- A Moore machine is said to be complete if δ is defined for every state and input symbol, and incomplete otherwise.
- A Moore machine can be converted to an equivalent Mealy machine by attaching the output value of each state to the outgoing transitions from that state.