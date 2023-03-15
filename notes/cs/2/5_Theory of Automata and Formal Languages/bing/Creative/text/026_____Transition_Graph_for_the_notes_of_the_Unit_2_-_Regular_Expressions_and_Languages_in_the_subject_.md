### Transition Graph for the notes of the Unit 2 - Regular Expressions and Languages in the subject of Theory of Automata and Formal Languages

- A transition graph is a special kind of flowchart for language analysis that represents a finite automaton  .
- A transition graph consists of three things:
  - A finite set of states, at least one of which is designated the start state and some of which are designated as final states.
  - An alphabet Σ of possible input symbols from which the input strings are formed.
  - A transition function that maps each state and input symbol to a next state or a set of next states.
- A transition graph can be drawn as a directed graph, where each node represents a state and each edge represents a transition  .
- The start state is indicated by an arrow pointing to it, and the final states are indicated by double circles  .
- The transition function is shown by labeling each edge with the input symbol that triggers the transition  .
- For example, the following transition graph represents a finite automaton that accepts the language of all strings over {0, 1} that end with 01  :

![transition graph example](https://www.javatpoint.com/images/automata/transition-diagram.png)

- A transition table is another way of representing a finite automaton using a tabular format .
- A transition table has one row for each state and one column for each input symbol .
- The entry in each cell indicates the next state or the set of next states for the corresponding state and input symbol .
- The start state is marked with an arrow and the final states are marked with circles .
- For example, the following transition table represents the same finite automaton as the transition graph above :

| State | 0 | 1 |
| --- | --- | --- |
| ->q0 | q0 | q1 |
| q1 | q2 | q1 |
| *q2 | q0 | q1 |

- A transition sequence is a sequence of states that the finite automaton goes through when processing an input string.
- A transition sequence can be written as a string of states separated by commas.
- For example, the transition sequence for the input string 00101 on the finite automaton above is q0, q0, q0, q1, q2.
- A transition sequence is said to be valid if it starts with the start state and ends with a final state.
- A transition sequence is said to be accepting if it corresponds to an input string that belongs to the language accepted by the finite automaton.
- For example, the transition sequence q0, q0, q0, q1, q2 is valid and accepting for the input string 00101, but the transition sequence q0, q0, q1, q2, q0 is invalid and not accepting for the input string 00100.