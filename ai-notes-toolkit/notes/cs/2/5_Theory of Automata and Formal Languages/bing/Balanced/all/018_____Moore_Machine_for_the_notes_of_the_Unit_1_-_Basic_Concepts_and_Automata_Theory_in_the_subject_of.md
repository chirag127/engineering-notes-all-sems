# Moore Machine

- A Moore machine is a type of finite state machine (FSM) that has an output value associated with each state    .
- The output value of a Moore machine depends only on the current state, not on the input symbols    .
- A Moore machine can be formally defined as a 6-tuple (Q, Σ, Γ, δ, ω, q0) where    :
  - Q is a finite set of states
  - Σ is a finite input alphabet
  - Γ is a finite output alphabet
  - δ is a transition function that maps Q × Σ to Q
  - ω is an output function that maps Q to Γ
  - q0 is the initial state
- A Moore machine can be represented by a state diagram, where each state is labeled with its output value and each transition is labeled with an input symbol    .
- A Moore machine can be used to model systems that produce outputs based on their current states, such as traffic lights, vending machines, counters, etc    .
- An example of a Moore machine is shown below:

![Moore machine example](https://learningmonkey.in/wp-content/uploads/2020/04/Moore-Machine-Example-1.png)

- This Moore machine has four states: A, B, C, and D, with output values 0, 1, 0, and 1 respectively.
- The input alphabet is {0, 1} and the output alphabet is {0, 1}.
- The initial state is A.
- The transition function is defined as follows:
  - δ(A, 0) = B
  - δ(A, 1) = C
  - δ(B, 0) = B
  - δ(B, 1) = D
  - δ(C, 0) = B
  - δ(C, 1) = C
  - δ(D, 0) = B
  - δ(D, 1) = D
- The output function is defined as follows:
  - ω(A) = 0
  - ω(B) = 1
  - ω(C) = 0
  - ω(D) = 1
- The behavior of this Moore machine can be described as follows:
  - If the input is 0, the machine moves to state B and outputs 1.
  - If the input is 1, the machine moves to state C and outputs 0.
  - If the machine is in state B or D, it stays in the same state and outputs 1 for any input.
  - If the machine is in state C, it stays in the same state and outputs 0 for any input.