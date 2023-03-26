 Here is the content in Markdown format without any emojis or external links and in a formal tone:

## Finite-State Automata

### Note for Unit 1 - Introduction to Natural Language Processing

1. Finite-state automata (FSA) is a mathematical model of computation. It is an abstract machine that can be in only one of a finite number of states at any time.

2. The automaton reads input symbols one at a time and transitions from one state to another according to a transition function.

3. The transition function takes the current state and input symbol as arguments and returns the next state.

4. An FSA is defined by:

- A finite set of states
- A finite set of input symbols (alphabet)
- Transition function
- One or two states are designated as the start state and accept (final) state(s) respectively.

5. Two types of FSA:

- Deterministic finite automaton (DFA): For a given current state and input symbol, there can be only one next state.
- Non-deterministic finite automaton (NFA): For a given current state and input symbol, there can be more than one possible next states.

6. FSA can recognize regular languages. The language recognized by an FSA is the set of all input strings that cause the automaton to end in an accept state.

7. FSA has applications in lexical analysis, pattern matching, and other areas.

8. Limitations: FSA cannot recognize context-sensitive languages. They also suffer from the state explosion problem as the number of states grows exponentially with the size of the input.

 