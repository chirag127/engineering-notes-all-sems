### Transition Graph for the notes of the Unit 2 - Regular Expressions and Languages in the subject of Theory of Automata and Formal Languages

- A transition graph is a graphical representation of a finite automaton that recognizes a language.
- A transition graph consists of three things:
  - A finite set of states, at least one of which is designated the start state and some of which are designated as final states.
  - An alphabet Σ of possible input symbols from which the input strings are formed.
  - A set of transitions, which are directed edges labeled with input symbols, connecting the states.
- A transition graph can be interpreted as a flowchart for an algorithm recognizing a language.
- A transition graph can also be generalized to allow transitions labeled with regular expressions over Σ, instead of single input symbols.
- A generalized transition graph is defined by a 5-tuple:
  - A finite set of states, Q.
  - A finite set of input symbols, Σ.
  - A non-empty set set of start states, S ⊆ Q.
  - A set of final or accepting states F ⊆ Q.
  - A finite set, Δ of transitions, (directed edge labels) (u,s,v), where u,v ∈ Q and s is a regular expression over Σ.
- A transition graph can be converted into a transition table, which is a tabular representation of the transitions between the states for each input symbol.
- A transition table has one row for each state and one column for each input symbol, and the entry in each cell is the set of states that can be reached from the current state by reading the input symbol.
- A transition graph can be used to determine whether a given input string belongs to the language recognized by the finite automaton, by following the transitions from the start state according to the input symbols, and checking if the final state is an accepting state.
- A transition graph can also be used to generate strings that belong to the language recognized by the finite automaton, by choosing transitions from the start state to an accepting state, and concatenating the labels of the transitions.
- A transition graph can be represented by a diagram, where the states are drawn as circles, the start state is marked with an arrow, the final states are marked with double circles, and the transitions are drawn as labeled arrows between the states.
- For example, the following diagram shows a transition graph for the language L = {w | w contains an even number of 0s and an odd number of 1s} over the alphabet Σ = {0,1}:

![transition graph example](https://i.imgur.com/1f7Yy0c.png)

: https://www.sanfoundry.com/automata-theory-transition-graph-table/
: https://sites.cs.ucsb.edu/~cappello/136/lectures/6/slides.pdf