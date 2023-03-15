# Non Deterministic Finite Automaton (NFA)

- A Non Deterministic Finite Automaton (NFA) is a type of finite automaton that can have more than one possible transition from a given state for a given input symbol.
- An NFA can be formally defined as a 5-tuple (Q, Σ, δ, q0, F), where :
  - Q is a finite set of states
  - Σ is a finite set of input symbols (alphabet)
  - δ is a transition function that maps Q × Σε to 2^Q, where Σε = Σ ∪ {ε} and ε is the empty string
  - q0 is the initial state
  - F is a set of final or accepting states
- An NFA accepts an input string if there exists at least one sequence of transitions from the initial state to a final state that consumes the entire input string.
- An NFA can have ε-transitions, which are transitions that do not consume any input symbol and can be taken spontaneously.
- An NFA can also have multiple initial or final states, unlike a DFA.
- An NFA can be converted to an equivalent DFA using the subset construction algorithm.
- Every DFA is also an NFA, but not every NFA is a DFA.
- An NFA is more expressive and easier to construct than a DFA for a given regular language, but less efficient to simulate.

## Example of NFA

- Consider the following NFA that accepts the language L = {xa | x ∈ {a,b}*}, which is the set of strings that end with 'a':

![NFA example](https://homepage.cs.uri.edu/faculty/hamel/courses/2014/spring2014/csc445/lecture-notes/ln445-05_files/image002.gif)

- The NFA has four states: q0, q1, q2, and q3, where q0 is the initial state and q3 is the only final state.
- The NFA has five transitions: (q0, ε, q1), (q0, ε, q2), (q1, a, q1), (q1, b, q1), and (q2, a, q3).
- The NFA can accept the input string 'baa' by following the sequence of transitions: q0, ε, q2, a, q3.
- The NFA can also accept the input string 'aba' by following the sequence of transitions: q0, ε, q1, a, q1, b, q1, a, q3.
- The NFA cannot accept the input string 'abb' because there is no sequence of transitions that leads to a final state.