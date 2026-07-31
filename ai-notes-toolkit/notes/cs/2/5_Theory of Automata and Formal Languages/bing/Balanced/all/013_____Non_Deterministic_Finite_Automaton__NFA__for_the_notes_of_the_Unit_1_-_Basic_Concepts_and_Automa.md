# Non Deterministic Finite Automaton (NFA)

- A Non Deterministic Finite Automaton (NFA) is a type of finite automaton that can have more than one possible transition from a given state for a given input symbol.
- An NFA can be defined as a 5-tuple (Q, Σ, δ, q0, F), where :
  - Q is a finite set of states
  - Σ is a finite set of input symbols
  - δ is a transition function that maps Q × Σε to 2^Q, where Σε = Σ ∪ {ε} and ε is the empty string
  - q0 is the initial state
  - F is a subset of Q that contains the final or accepting states
- An NFA accepts an input string if there exists at least one sequence of transitions from the initial state to a final state that consumes the entire input string.
- An NFA can be represented by a transition diagram, where each state is a node, each transition is an edge labeled by the input symbol, and the initial and final states are marked by arrows and double circles, respectively.
- An example of an NFA that accepts the language L = {xa | x ∈ {a,b}*} is shown below:

![NFA example](https://homepage.cs.uri.edu/faculty/hamel/courses/2014/spring2014/csc445/lecture-notes/ln445-05_files/image002.gif)

- An NFA can be converted to an equivalent Deterministic Finite Automaton (DFA) using the subset construction method, which constructs a DFA that simulates all possible moves of the NFA for each input symbol .
- An NFA can be more expressive and concise than a DFA, but a DFA can be more efficient and easier to implement than an NFA.