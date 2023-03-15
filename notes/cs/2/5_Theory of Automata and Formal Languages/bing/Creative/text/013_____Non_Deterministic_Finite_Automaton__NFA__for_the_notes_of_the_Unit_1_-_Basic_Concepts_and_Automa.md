### Non Deterministic Finite Automaton (NFA)

- A non deterministic finite automaton (NFA) is a type of finite automaton that can have more than one possible transition from a given state for a given input symbol.
- An NFA can be formally defined as a 5-tuple (Q, Σ, δ, q0, F), where :
  - Q is a finite set of states
  - Σ is a finite set of input symbols (alphabet)
  - δ is a transition function that maps Q × Σε to 2^Q, where Σε = Σ ∪ {ε} and ε is the empty string
  - q0 is the initial state (q0 ∈ Q)
  - F is a set of final or accepting states (F ⊆ Q)
- An NFA accepts an input string if there exists at least one sequence of transitions from the initial state to a final state that consumes the entire input string.
- An NFA can be represented by a transition diagram, where the states are represented by circles, the transitions are represented by labeled arrows, and the initial and final states are marked by an incoming arrow and a double circle, respectively.
- An example of an NFA that accepts the language L = {xa | x ∈ {a,b}*} is shown below:

![NFA example](https://www.gatevidyalay.com/wp-content/uploads/2018/07/Non-Deterministic-Finite-Automata-Example-1.png)

- An NFA can be converted to an equivalent deterministic finite automaton (DFA) using the subset construction or the powerset construction.
- An NFA can be more expressive and concise than a DFA, but a DFA can be more efficient and easier to implement than an NFA.