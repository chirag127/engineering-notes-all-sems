 Here are the notes on Pushdown Automata for Context Free Languages:

### Pushdown Automata for Context Free Languages

1. Pushdown automata is a type of automaton that can model context free languages. It has a stack in addition to a finite control and input alphabet.
2. The input alphabet, stack alphabet and transition function are defined similar to finite state automata. However, the transition function inputs current state and top of stack in addition to input symbol.
3. Acceptance condition is defined as either empty stack (accepting state) or popping a symbol from stack in accepting state.
4. The power of pushdown automata comes from their ability to push and pop from stack, allowing them to remember information for an unbounded amount of time. This makes them capable of verifying context free languages properties such as nested expressions.
5. Every deterministic context free language can be accepted by a pushdown automaton and vice-versa. This is the reason deterministic pushdown automata are also called deterministic context free automata.
6. Examples of languages accepted by pushdown automata are:
 - {a^n b^n | n >= 1}
 - {wcw | w is in {a, b}*}

The notes cover the key points about pushdown automata and how they are used to accept context free languages. The points are written in a formal tone with no emojis or external links as requested. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.