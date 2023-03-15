Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is some content on Non Deterministic Finite Automaton (NFA) for the notes of the Unit 1 - Basic Concepts and Automata Theory in the subject of Theory of Automata and Formal Languages.

### Non Deterministic Finite Automaton (NFA)

- A Non Deterministic Finite Automaton (NFA) is a mathematical model of computation that can accept or reject a string of symbols over a finite alphabet.
- An NFA consists of five components: a finite set of states Q, a finite set of input symbols Σ, a transition function δ that maps a state and an input symbol to a subset of states, an initial state q0, and a set of final or accepting states F.
- An NFA can have more than one possible transition for a given state and input symbol, or no transition at all. This means that the next state of the NFA is not uniquely determined by the current state and input symbol.
- An NFA accepts a string if there exists at least one sequence of transitions from the initial state to a final state that consumes the entire string. Such a sequence is called an accepting path or run of the NFA.
- An NFA can be represented by a transition diagram, which is a directed graph where the nodes are the states and the edges are labeled by the input symbols. The initial state is marked by an arrow and the final states are marked by double circles.
- An NFA can also be represented by a transition table, which is a matrix where the rows are the states, the columns are the input symbols, and the entries are the subsets of states that can be reached by the corresponding transition.
- The language recognized by an NFA is the set of all strings that are accepted by the NFA. The language is denoted by L(NFA) or L(M) where M is the name of the NFA.
- An NFA can be converted to an equivalent Deterministic Finite Automaton (DFA) using the subset construction or the powerset construction. The DFA has a state for each subset of states of the NFA, and a transition for each input symbol that follows the transitions of the NFA.
- An NFA can be used to model the behavior of non-deterministic systems, such as concurrent processes, backtracking algorithms, or regular expressions.

#### Example of NFA

- Consider the following NFA M that recognizes the language L(M) = {w | w ends with 01} over the alphabet Σ = {0, 1}.

![NFA example](https://www.gatevidyalay.com/wp-content/uploads/2018/07/Non-Deterministic-Finite-Automata-Example-1.png)

- The NFA has four states: q0, q1, q2, and q3. The initial state is q0 and the final state is q3. The transition function is given by the following table:

| State | 0 | 1 |
| ----- | - | - |
| q0    | {q0, q1} | {q0} |
| q1    | {q2} | ∅ |
| q2    | ∅ | {q3} |
| q3    | ∅ | ∅ |

- The NFA accepts the string 00101 because there is an accepting path q0 -> q0 -> q1 -> q2 -> q3 that consumes the entire string. The NFA also accepts the string 0101 because there is another accepting path q0 -> q1 -> q2 -> q3 that consumes the entire string.
- The NFA rejects the string 00100 because there is no accepting path that consumes the entire string. The NFA also rejects the string 011 because there is no transition from q1 to q3 on input 1.