### Moore Machine

- A Moore machine is a type of finite state machine (FSM) that produces outputs based on its current state only.
- A Moore machine can be formally defined as a sextuple M = (Q, q0, ∑, O, δ, λ) where:
  - Q is a finite set of states
  - q0 is the initial state
  - ∑ is the input alphabet
  - O is the output alphabet
  - δ is the transition function that maps Q×∑ → Q
  - λ is the output function that maps Q → O
- A Moore machine can be represented by a state diagram, where each state is labeled with its output value and the transitions are labeled with the input symbols.
- A Moore machine can be converted to a Mealy machine by attaching the output values of each state to the outgoing transitions.
- A Moore machine can be used to model sequential circuits, such as counters, shift registers, and encoders.

#### Example of a Moore machine

- Consider a Moore machine that accepts strings over the alphabet {0, 1} and produces an output 1 if the input string ends with 01, and 0 otherwise.
- The Moore machine can be defined as M = (Q, q0, ∑, O, δ, λ) where:
  - Q = {q0, q1, q2}
  - q0 is the initial state
  - ∑ = {0, 1}
  - O = {0, 1}
  - δ is defined by the following table:

| Current state | Input symbol | Next state |
| ------------- | ------------ | ---------- |
| q0            | 0            | q0         |
| q0            | 1            | q1         |
| q1            | 0            | q2         |
| q1            | 1            | q1         |
| q2            | 0            | q0         |
| q2            | 1            | q1         |

  - λ is defined by the following table:

| State | Output |
| ----- | ------ |
| q0    | 0      |
| q1    | 0      |
| q2    | 1      |

- The state diagram of the Moore machine is shown below:

![Moore machine example](https://learningmonkey.in/wp-content/uploads/2020/04/Moore-Machine-Example.png)

- The output of the Moore machine for some input strings are:

| Input string | Output string |
| ------------ | ------------- |
| 010          | 001           |
| 101          | 000           |
| 011          | 001           |
| 001          | 010           |
| 110          | 000           |
| 0101         | 0010          |