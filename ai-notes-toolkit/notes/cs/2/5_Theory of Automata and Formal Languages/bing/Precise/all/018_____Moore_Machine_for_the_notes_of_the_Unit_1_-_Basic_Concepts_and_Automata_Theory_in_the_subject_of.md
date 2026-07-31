### Moore Machine

A Moore machine is a type of finite state machine (FSM) that is used in the study of automata theory and formal languages. It is named after Edward F. Moore, who introduced the concept in 1956.

Here are some key points to remember about Moore machines:

1. A Moore machine is a 6-tuple (Q, Σ, δ, λ, q0, F) where:
    - Q is a finite set of states
    - Σ is a finite input alphabet
    - δ: Q × Σ → Q is the transition function
    - λ: Q → Σ is the output function
    - q0 ∈ Q is the initial state
    - F ⊆ Q is the set of final states
2. In a Moore machine, the output is determined solely by the current state of the machine, and not by the input.
3. The output function λ maps each state to an output symbol.
4. The transition function δ takes the current state and input symbol and returns the next state.
5. Moore machines are used to model systems where the output is dependent only on the current state, and not on the history of inputs.
6. Moore machines can be used to recognize regular languages.
