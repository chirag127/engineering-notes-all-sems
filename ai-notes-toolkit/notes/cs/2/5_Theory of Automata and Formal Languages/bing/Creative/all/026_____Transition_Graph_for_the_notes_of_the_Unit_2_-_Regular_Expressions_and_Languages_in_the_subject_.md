# Transition Graph

A transition graph is a graphical representation of a finite automaton. It consists of the following components :

- A finite set of states, at least one of which is designated as the start state and some (maybe none) of which are designated as the final states.
- A finite set of input symbols, called the alphabet, from which the input strings are formed.
- A set of directed edges, labeled with input symbols, that connect the states. Each edge represents a possible transition from one state to another on reading an input symbol.

A transition graph can be interpreted as a flowchart for an algorithm that recognizes a language. The algorithm starts from the start state and reads the input string from left to right, following the edges that match the input symbols. If the algorithm reaches a final state after reading the entire input string, then the input string is accepted by the transition graph. Otherwise, the input string is rejected.

For example, the following transition graph recognizes the language of all strings over {0,1} that end with 1:

![Transition graph example](https://www.javatpoint.com/images/automata/transition-diagram.png)

Some properties of transition graphs are:

- If there is no way to factor a word w that is the concatenation of edge labels of a successful path in a transition graph, then w does not belong to the language recognized by the transition graph.
- Every finite automaton can be viewed as a transition graph, but not every transition graph can be viewed as a finite automaton. Transition graphs generalize finite automata by allowing edges to be labeled with more than one symbol or with the empty string.
- A transition graph can be converted into an equivalent finite automaton by introducing new states and edges to eliminate the edges that are labeled with more than one symbol or with the empty string. This process is called the state-splitting method.