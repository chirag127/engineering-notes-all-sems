### Two stack Pushdown Automata

- A pushdown automaton (PDA) is a finite state machine that has an additional component called a stack, which can store and retrieve symbols according to the last-in first-out (LIFO) principle.
- A PDA can use the top of the stack to decide which transition to take, and it can manipulate the stack as part of performing a transition.
- A PDA with one stack can accept languages that are context-free, but not all recursively enumerable languages.
- A PDA with two stacks has the same computation power as a Turing machine, which can accept all recursively enumerable languages  .
- A two stack PDA is similar to a one stack PDA, but it has two stacks instead of one. In each transition, we must specify which stack to push or pop, or whether to leave both stacks unchanged.
- A two stack PDA can simulate a Turing machine by using one stack to store the symbols on the left of the tape head, and the other stack to store the symbols on the right of the tape head. The tape head can be represented by the top symbols of both stacks.
- A two stack PDA can also accept languages that are not context-free, such as {a^n b^n c^n | n >= 0}. A possible algorithm is to push a symbol into one of the stacks for each a in the input, and wait for the b to come up. Then, push a symbol into the other stack for each b in the input, and wait for the c to come up. Then, pop both stacks together for each c in the input. If in the process all symbols match, and in the end both stacks are empty, accept .