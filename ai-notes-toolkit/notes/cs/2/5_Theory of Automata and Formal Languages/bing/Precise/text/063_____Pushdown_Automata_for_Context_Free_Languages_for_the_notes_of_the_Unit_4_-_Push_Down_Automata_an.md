### Pushdown Automata for Context Free Languages

A pushdown automaton (PDA) is a type of automaton that is used to recognize context-free languages. It is similar to a finite automaton, but it has an additional component called a stack, which allows it to perform more complex operations.

Here are some key points to remember about pushdown automata:

1. A PDA is defined by a 7-tuple (Q, Σ, Γ, δ, q0, Z, F), where Q is a finite set of states, Σ is the input alphabet, Γ is the stack alphabet, δ is the transition function, q0 is the initial state, Z is the initial stack symbol, and F is the set of final states.

2. The transition function δ takes as input a state, an input symbol, and a stack symbol, and returns a set of state-stack symbol pairs. This allows the PDA to perform different actions depending on the current state, input symbol, and stack symbol.

3. The PDA reads the input string from left to right, one symbol at a time. At each step, it can perform one of the following actions: push a symbol onto the stack, pop a symbol from the stack, or do nothing (i.e., leave the stack unchanged).

4. The PDA accepts an input string if, after reading the entire string, it is in a final state and the stack is empty.

5. PDAs can be either deterministic or nondeterministic. In a deterministic PDA, the transition function returns at most one state-stack symbol pair for each input. In a nondeterministic PDA, the transition function can return multiple state-stack symbol pairs for each input.

6. Every context-free language can be recognized by a nondeterministic PDA. However, not every context-free language can be recognized by a deterministic PDA.

7. The class of languages recognized by deterministic PDAs is a proper subset of the class of languages recognized by nondeterministic PDAs.

8. The class of languages recognized by PDAs is exactly the class of context-free languages.
