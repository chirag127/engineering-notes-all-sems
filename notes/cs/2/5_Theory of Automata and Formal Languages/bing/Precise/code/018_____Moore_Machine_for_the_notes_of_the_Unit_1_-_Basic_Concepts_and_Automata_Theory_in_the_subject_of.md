### Moore Machine

A Moore machine is a type of finite state machine (FSM) that is used in the study of automata theory and formal languages. It is named after Edward F. Moore, who introduced the concept in 1956.

Here are some key points to remember about Moore machines:

1. A Moore machine is a 6-tuple (Q, Σ, δ, λ, q0, F) where:
    - Q is a finite set of states.
    - Σ is a finite input alphabet.
    - δ: Q × Σ → Q is the transition function.
    - λ: Q → Σ is the output function.
    - q0 ∈ Q is the initial state.
    - F ⊆ Q is the set of final states.

2. In a Moore machine, the output is determined solely by the current state of the machine, and not by the input.

3. Moore machines are used to model systems where the output is dependent on the current state, rather than the input.

4. Moore machines can be used to recognize regular languages.

5. Moore machines can be converted to equivalent Mealy machines, and vice versa.

6. The state diagram of a Moore machine is similar to that of a DFA, with the addition of output labels on the states.
