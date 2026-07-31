### Moves for the notes of the Unit 4 - Push Down Automata and Properties of Context Free Languages in the subject of Theory of Automata and Formal Languages

1. **Push Down Automata (PDA)** is a type of automaton that is used to recognize context-free languages.
2. A PDA is defined by a 7-tuple (Q, Σ, Γ, δ, q0, Z, F) where:
    - Q is a finite set of states
    - Σ is the input alphabet
    - Γ is the stack alphabet
    - δ is the transition function
    - q0 is the initial state
    - Z is the initial stack symbol
    - F is the set of final states
3. A PDA can make moves based on the current state, the current input symbol, and the current stack symbol.
4. There are three types of moves that a PDA can make:
    - **Push move**: The PDA reads an input symbol, changes state, and pushes a symbol onto the stack.
    - **Pop move**: The PDA reads an input symbol, changes state, and pops a symbol from the stack.
    - **No move**: The PDA does not read an input symbol, but changes state and either pushes or pops a symbol from the stack.
5. The language accepted by a PDA can be defined in two ways:
    - **Acceptance by final state**: A PDA accepts an input string if, after reading the entire string, it is in a final state.
    - **Acceptance by empty stack**: A PDA accepts an input string if, after reading the entire string, its stack is empty.
6. Context-free languages have several properties that can be used to prove that a language is context-free or not.
7. Some of these properties include closure under union, concatenation, and Kleene star, as well as the pumping lemma for context-free languages.
8. These properties can be used to design algorithms for manipulating context-free languages, such as converting a context-free grammar to Chomsky normal form or Greibach normal form.
