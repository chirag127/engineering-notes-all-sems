### Definition for the notes of the Unit 4 - Push Down Automata and Properties of Context Free Languages in the subject of Theory of Automata and Formal Languages.

Push Down Automata (PDA) is a type of automaton that recognizes context-free languages. It is an extension of the Finite State Machine (FSM) with an additional stack memory.

#### Formal Definition
A Push Down Automaton is defined as a 7-tuple (Q, Σ, Γ, δ, q0, Z, F), where,
- Q is a finite set of states.
- Σ is a finite input alphabet.
- Γ is a finite stack alphabet.
- δ is the transition function that maps Q x (Σ ∪ {ε}) x Γ -> P(Q x Γ*), where P(Q x Γ*) denotes the power set of Q x Γ*.
- q0 is the initial state.
- Z is the initial stack symbol.
- F is a set of final states.

#### Working of PDA
A PDA works by reading input symbols one by one and pushes them onto the stack. It can read the top symbol of the stack without modifying it. Based on the current state, input symbol, and top of the stack, the transition function determines the next state and the operation to be performed on the stack.

#### Acceptance of a String by PDA
A string is accepted by a PDA if it reaches a final state after processing the entire input string. The stack should be empty at the end of the computation.

#### Properties of Context-Free Languages
- Closure Properties: Context-free languages are closed under union, concatenation, and Kleene star operations.
- Pumping Lemma: The Pumping Lemma is a tool used to prove that a language is not context-free.
- Normal Forms: Every context-free language can be represented in the Chomsky Normal Form or the Greibach Normal Form.

#### Conclusion
Push Down Automata is an important concept in the study of automata and formal languages. It provides a mechanism to recognize context-free languages. The properties of context-free languages play a crucial role in the analysis of algorithms and programming languages. Understanding these concepts is essential for any student of computer science or related fields.