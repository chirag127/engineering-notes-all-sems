### Simulation of DFA and NFA

Unit 1 - Basic Concepts and Automata Theory in the subject of Theory of Automata and Formal Languages

1. **DFA (Deterministic Finite Automaton)** is a finite state machine that accepts or rejects a given string of symbols, by running through a state sequence uniquely determined by the string.
2. **NFA (Nondeterministic Finite Automaton)** is a finite state machine where, for some cases, when a single input is given to the current state, the machine goes to multiple states.
3. The simulation of a DFA involves processing an input string symbol by symbol, transitioning from one state to another according to the transition function, and accepting or rejecting the string based on whether the final state is an accepting state or not.
4. The simulation of an NFA is similar to that of a DFA, but at each step, the machine may transition to multiple states. This can be handled by keeping track of all possible current states and processing the input symbol for each of them.
5. The simulation of an NFA can also be done by converting it to an equivalent DFA and then simulating the DFA. This is known as the **subset construction** method.
6. Both DFA and NFA are used to recognize regular languages, and for any given NFA, there exists an equivalent DFA that recognizes the same language.