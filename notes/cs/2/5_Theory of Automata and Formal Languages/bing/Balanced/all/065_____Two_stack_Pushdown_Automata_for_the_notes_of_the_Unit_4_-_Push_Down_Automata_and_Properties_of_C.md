# Two Stack Pushdown Automata

- A pushdown automaton (PDA) is a finite state machine augmented with a stack. A stack is a data structure that allows only two operations: push and pop. Push adds a symbol to the top of the stack, and pop removes the symbol from the top of the stack. A PDA can use the top of the stack to decide which transition to take, and it can manipulate the stack as part of performing a transition.
- A two stack pushdown automaton (2-PDA) is a PDA that has two stacks instead of one. In each transition, it must specify which stack to push or pop, or whether to leave both stacks unchanged. A 2-PDA can simulate a queue by using one stack as the front and the other as the rear of the queue.
- A 2-PDA has the same computation power as a Turing machine, which is a more powerful model of computation than a PDA. A Turing machine can accept languages that are not accepted by any PDA with one stack, such as the language {a^n b^n c^n | n >= 0}. A 2-PDA can accept this language by using one stack to count the number of a's and the other stack to count the number of b's, and then compare them with the number of c's .
- A 2-PDA can be formally defined as a 7-tuple (Q, Σ, Γ, δ, q0, Z0, F), where:

  - Q is a finite set of states
  - Σ is a finite input alphabet
  - Γ is a finite stack alphabet
  - δ is a transition function that maps Q × (Σ ∪ {ε}) × Γ × Γ to a subset of Q × {push, pop, ε} × {push, pop, ε}
  - q0 is the initial state
  - Z0 is the initial stack symbol for both stacks
  - F is a set of final states

- A configuration of a 2-PDA is a triple (q, w, αβ), where q is the current state, w is the remaining input, and αβ is the content of the two stacks, with α being the top of the first stack and β being the top of the second stack. The initial configuration is (q0, w, Z0Z0), where w is the input string. The final configuration is (q, ε, εε), where q is a final state and both stacks are empty.
- A 2-PDA can make a transition from one configuration to another according to the transition function δ. For example, if δ(q, a, X, Y) = {(p, push, pop)}, then the 2-PDA can move from (q, aw, Xα, Yβ) to (p, w, aXα, β) by reading an input symbol a, pushing it to the first stack, and popping the second stack. If δ(q, ε, X, Y) = {(p, ε, ε)}, then the 2-PDA can move from (q, w, Xα, Yβ) to (p, w, Xα, Yβ) by making an ε-transition without changing the stacks.