### Two stack Pushdown Automata

- A pushdown automaton (PDA) is a finite state machine augmented with a stack. A stack is a data structure that allows only two operations: push and pop. Push adds a symbol to the top of the stack, and pop removes the top symbol from the stack. A PDA can use the top of the stack to decide which transition to take, and it can manipulate the stack as part of performing a transition .
- A two stack pushdown automaton (2-PDA) is a PDA that has two stacks instead of one. A 2-PDA can use both stacks to store and retrieve symbols, and it can switch between the stacks as needed. A 2-PDA can simulate a Turing machine, which is a more powerful model of computation that can accept languages that are not accepted by any PDA with one stack .
- A 2-PDA can be formally defined as a 7-tuple $(Q, \\Sigma, \\Gamma, \\delta, q_0, Z_0, F)$, where:

  - $Q$ is a finite set of states
  - $\\Sigma$ is a finite input alphabet
  - $\\Gamma$ is a finite stack alphabet
  - $\\delta$ is a transition function that maps $Q \\times (\\Sigma \\cup \\{\\epsilon\\}) \\times \\Gamma \\times \\Gamma \\times \\{1, 2\\}$ to $2^{Q \\times \\Gamma^* \\times \\Gamma^* \\times \\{1, 2\\}}$
  - $q_0$ is the initial state
  - $Z_0$ is the initial stack symbol
  - $F$ is a set of final states

- The transition function $\\delta$ specifies how the 2-PDA changes its state, stacks, and stack selection based on the current state, input symbol, top symbols of both stacks, and the current stack selection. The stack selection is either 1 or 2, indicating which stack is active. The transition function can return a set of possible transitions, each consisting of a new state, a string of symbols to push onto the first stack, a string of symbols to push onto the second stack, and a new stack selection. The 2-PDA can choose any transition from the set nondeterministically.
- The 2-PDA starts in the initial state $q_0$, with both stacks containing only the initial stack symbol $Z_0$, and with the first stack selected. It reads the input symbols one by one, and performs transitions according to the transition function. It can also perform epsilon transitions, which do not consume any input symbol. The 2-PDA accepts the input if it reaches a final state and both stacks are empty. Alternatively, the 2-PDA can accept by empty stack, which means that it accepts the input if both stacks are empty, regardless of the current state .
- An example of a 2-PDA that accepts the language $\\{a^n b^n c^n \\mid n \\geq 0\\}$ is given below. This language is not context-free, and cannot be accepted by any PDA with one stack.

  - $Q = \\{q_0, q_1, q_2, q_3, q_4, q_5\\}$
  - $\\Sigma = \\{a, b, c\\}$
  - $\\Gamma = \\{Z_0, A, B, C\\}$
  - $\\delta$ is defined as follows:

    - $\\delta(q_0, a, Z_0, Z_0, 1) = \\{(q_1, AZ_0, Z_0, 1)\\}$
    - $\\delta(q_1, a, A, Z_0, 1) = \\{(q_1, AA, Z_0, 1)\\}$
    - $\\delta(q_1, b, A, Z_0, 1) = \\{(q_2, \\epsilon, BZ_0, 2)\\}$
    - $\\delta(q_2, b, A, B, 2) = \\{(q_2, \\epsilon, BB, 2)\\}$
    - $\\delta(q_2, c, A, B,