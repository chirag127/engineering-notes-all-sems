# Transition Graph

A transition graph is a visual representation of a finite automaton. It is a directed graph where the nodes represent the states of the automaton and the edges represent the transitions between the states. The edges are labeled with the input symbols that trigger the transition.

Here are some key points to remember about transition graphs:

- The start state is indicated by an arrow pointing to it from nowhere.
- The accepting states are indicated by a double circle.
- The transitions are represented by directed edges between the states, labeled with the input symbol that triggers the transition.
- If there are multiple transitions from one state to another on different input symbols, there will be multiple edges between the two states, each labeled with the corresponding input symbol.
- If there is no transition defined for a particular state and input symbol, it is assumed that the input is rejected.

A transition graph provides a visual way to understand the behavior of a finite automaton and can be useful in designing and analyzing regular expressions and languages. It is an important concept in the study of Theory of Automata and Formal Languages.