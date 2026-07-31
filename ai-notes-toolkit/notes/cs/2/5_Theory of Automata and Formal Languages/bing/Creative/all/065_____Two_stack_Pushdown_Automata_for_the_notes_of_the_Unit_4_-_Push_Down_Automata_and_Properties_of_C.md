# Two stack Pushdown Automata

- A pushdown automaton (PDA) is a finite state machine that has an additional component called a stack, which can store and retrieve symbols according to the last-in first-out (LIFO) principle.
- A PDA can use the top of the stack to decide which transition to take, and it can manipulate the stack as part of performing a transition.
- A PDA with one stack can accept languages that are context-free, but not all recursively enumerable languages.
- A PDA with two stacks has the same computation power as a Turing machine, which can accept all recursively enumerable languages  .
- A two stack PDA is similar to a one stack PDA, but it has two stacks instead of one. In each transition, we must specify which stack to push or pop, or whether to leave both stacks unchanged.
- A two stack PDA can simulate a Turing machine by using one stack as the left part of the tape, and the other stack as the right part of the tape. The head of the Turing machine can be represented by the top symbols of the two stacks.
- A two stack PDA can also accept languages that are not context-free, such as $a^n b^n c^n$, by using one stack to match the $a$s and $b$s, and the other stack to match the $b$s and $c$s.