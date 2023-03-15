### Two stack Pushdown Automata

- A pushdown automaton (PDA) is a finite state machine that has an additional component called a stack, which can store and retrieve symbols according to the last-in first-out (LIFO) principle.
- A PDA can use the top of the stack to decide which transition to take, and it can manipulate the stack as part of performing a transition.
- A two stack pushdown automaton (2-PDA) is a PDA that has two stacks instead of one .
- A 2-PDA can use the top symbols of both stacks to decide which transition to take, and it can manipulate both stacks as part of performing a transition .
- A 2-PDA can simulate a Turing machine by using one stack to store the tape symbols to the left of the head, and the other stack to store the tape symbols to the right of the head  .
- A 2-PDA can accept languages that are not accepted by any PDA with one stack, such as the language {a^n b^n c^n | n >= 0} .
- A 2-PDA can be deterministic or non-deterministic, but both variants have the same computation power as a Turing machine .