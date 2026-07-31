# Moore Machine

- A Moore machine is a type of finite state machine (FSM) that has an output value associated with each state    .
- The output value of a Moore machine depends only on the current state, not on the input symbols    .
- A Moore machine can be formally defined as a 6-tuple (Q, Σ, Γ, δ, ω, q0), where    :
  - Q is a finite set of states.
  - Σ is a finite set of input symbols.
  - Γ is a finite set of output symbols.
  - δ : Q × Σ → Q is the transition function that maps a state and an input symbol to a next state.
  - ω : Q → Γ is the output function that maps a state to an output symbol.
  - q0 ∈ Q is the initial state.
- A Moore machine can be represented by a state diagram, where each state is labeled with its output symbol and each transition is labeled with an input symbol    .
- A Moore machine can be used to model systems that produce outputs based on their current states, such as traffic lights, vending machines, counters, etc    .
- A Moore machine is different from a Mealy machine, which is another type of FSM that has an output value associated with each transition . The output value of a Mealy machine depends on both the current state and the input symbol .
- A Moore machine typically has more states than a Mealy machine for a given problem, but a Mealy machine may have more transitions and output symbols.

## Example

- Suppose we have the following Moore machine:

![Moore machine example](https://learningmonkey.in/wp-content/uploads/2020/04/Moore-Machine-Example-1.png)

- The Moore machine has 6 states: q0, q1, q2, q3, q4, and q5.
- The Moore machine has 2 input symbols: 0 and 1.
- The Moore machine has 2 output symbols: A and B.
- The Moore machine has the following transition function:

| Current state | Input symbol | Next state |
|---------------|--------------|------------|
| q0            | 0            | q1         |
| q0            | 1            | q2         |
| q1            | 0            | q3         |
| q1            | 1            | q4         |
| q2            | 0            | q5         |
| q2            | 1            | q0         |
| q3            | 0            | q1         |
| q3            | 1            | q2         |
| q4            | 0            | q5         |
| q4            | 1            | q0         |
| q5            | 0            | q3         |
| q5            | 1            | q4         |

- The Moore machine has the following output function:

| State | Output symbol |
|-------|---------------|
| q0    | A             |
| q1    | A             |
| q2    | A             |
| q3    | B             |
| q4    | B             |
| q5    | B             |

- The Moore machine has q0 as the initial state.
- The Moore machine produces an output symbol for each state it enters, regardless of the input symbol that causes the transition.
- For example, if the Moore machine receives the input string 0101, it will go through the following sequence of states and outputs:

| Input symbol | Current state | Output symbol | Next state |
|--------------|---------------|---------------|------------|
| -            | q0            | A             | -          |
| 0            | q0            | A             | q1         |
| 1            | q1            | A             | q4         |
| 0            | q4            | B             |