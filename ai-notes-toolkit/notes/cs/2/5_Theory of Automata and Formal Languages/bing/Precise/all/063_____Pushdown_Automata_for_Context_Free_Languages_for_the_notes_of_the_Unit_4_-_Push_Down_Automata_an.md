# Pushdown Automata for Context Free Languages

Pushdown Automata (PDA) is a type of automaton that is used to recognize context-free languages. It is an extension of the finite automaton with an additional stack data structure. The stack provides additional memory to the automaton, allowing it to recognize languages that are not regular.

Here are some key points to remember about Pushdown Automata:

1. A PDA is defined by a 7-tuple (Q, Σ, Γ, δ, q0, Z, F) where:
    - Q is a finite set of states
    - Σ is the input alphabet
    - Γ is the stack alphabet
    - δ is the transition function
    - q0 is the initial state
    - Z is the initial stack symbol
    - F is the set of final states
2. The transition function δ takes a state, an input symbol, and a stack symbol as arguments and returns a set of state-stack symbol pairs.
3. A PDA can be either deterministic or non-deterministic.
4. A PDA accepts an input string by final state or by empty stack.
5. The language recognized by a PDA is called a context-free language.
6. Every context-free language can be recognized by a PDA.
7. The class of context-free languages is closed under union, concatenation, and Kleene star operations.
