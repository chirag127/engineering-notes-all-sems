### Transition Graph for the notes of the Unit 2 - Regular Expressions and Languages in the subject of Theory of Automata and Formal Languages

- A transition graph is a special kind of flowchart for language analysis that represents a finite automaton  .
- A transition graph consists of three things:
  - A finite set of states, at least one of which is designated the start state and some of which are designated as final states.
  - An alphabet Σ of possible input symbols from which the input strings are formed.
  - A transition function that maps each state and input symbol to a next state or a set of next states.
- A transition graph can be drawn as a directed graph where   :
  - The nodes represent the states of the automaton.
  - The edges represent the transitions between the states, labeled with the input symbols that trigger them.
  - The start state is indicated by an arrow pointing to it from nowhere.
  - The final states are indicated by double circles or by an arrow pointing out of them to nowhere.
- A transition graph can be interpreted as a flowchart for an algorithm recognizing a language. The algorithm starts from the start state and reads the input string one symbol at a time, following the transitions that match the input symbols. If the algorithm reaches a final state after reading the entire input string, the input string is accepted by the automaton. Otherwise, the input string is rejected by the automaton.
- A transition graph can also be represented using a transition table, which is a tabular form of the transition function. The table has one row for each state and one column for each input symbol. The entry in each cell indicates the next state or the set of next states for the corresponding state and input symbol. The start state and the final states are marked separately in the table.
- An example of a transition graph and a transition table for a finite automaton that accepts the language of all strings over {0, 1} that end with 01 is shown below :

![Transition graph](https://www.javatpoint.com/automata-theory/images/transition-diagram.jpg)

| State | 0 | 1 |
| ----- | - | - |
| ->q0  | q0| q1|
| q1    | q2| q1|
| *q2   | q0| q1|

- In the transition graph, the start state is q0 and the final state is q2. The transition function is defined as follows:
  - δ(q0, 0) = q0
  - δ(q0, 1) = q1
  - δ(q1, 0) = q2
  - δ(q1, 1) = q1
  - δ(q2, 0) = q0
  - δ(q2, 1) = q1
- In the transition table, the start state is marked with an arrow (->) and the final state is marked with an asterisk (*). The transition function is represented by the entries in the table. For example, the entry in the cell (q0, 1) is q1, which means δ(q0, 1) = q1.