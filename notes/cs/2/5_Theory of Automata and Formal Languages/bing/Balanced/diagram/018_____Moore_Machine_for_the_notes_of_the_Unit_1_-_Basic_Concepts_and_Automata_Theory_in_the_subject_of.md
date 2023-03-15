### Moore Machine

A Moore machine is a type of finite state machine (FSM) that has an output value associated with each state. The output value depends only on the current state of the machine, and not on the input symbols. A Moore machine can be formally defined as a 6-tuple (Q, Σ, q0, Δ, δ, λ), where:

- Q is a finite set of states.
- Σ is a finite set of input symbols.
- q0 ∈ Q is the initial state.
- Δ is a finite set of output symbols.
- δ : Q × Σ → Q is the state transition function, which maps a state and an input symbol to a next state.
- λ : Q → Δ is the output function, which maps a state to an output symbol.

A Moore machine can be represented by a state diagram, where each state is labeled with its output value, and each transition is labeled with an input symbol. For example, the following state diagram shows a Moore machine that accepts strings over the alphabet {0, 1} that end with 01.

![Moore machine example](https://www.educative.io/api/edpresso/shot/5073373437659136/image/5073373437659136)

Some properties of Moore machines are:

- They are deterministic, meaning that for each state and input symbol, there is exactly one next state and output symbol.
- They are output-stable, meaning that the output value does not change unless the state changes.
- They are synchronous, meaning that the state and output change at the same time, in response to the input symbol.
- They may have more states than a Mealy machine for the same problem, because they need to encode the output value in the state.