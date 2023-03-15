# Equivalence of DFA and NFA

- A DFA (deterministic finite automaton) is a finite state machine that accepts or rejects a given string of symbols, where each move from a state to another is uniquely determined by the current state and the input symbol.
- An NFA (nondeterministic finite automaton) is a finite state machine that accepts or rejects a given string of symbols, where each move from a state to another is not uniquely determined by the current state and the input symbol. An NFA can have zero, one or more than one move from a given state on a given input symbol, and can also have null moves (moves without input symbol).
- A DFA and an NFA are equivalent if they recognize the same language, that is, if they accept the same set of strings.
- The equivalence of DFA and NFA can be proved by showing that for any DFA, there is an equivalent NFA, and vice versa.
- To construct an equivalent NFA from a given DFA, we can simply copy the states, transitions, initial state and final states of the DFA to the NFA. The resulting NFA will have the same behavior as the DFA, since there is no nondeterminism or null moves involved.
- To construct an equivalent DFA from a given NFA, we can use the subset construction algorithm, which is as follows:

  - Let the NFA be M1 = (Q1, E, q1,0, delta1, A1), where Q1 is the set of states, E is the input alphabet, q1,0 is the initial state, delta1 is the transition function, and A1 is the set of final states.
  - Let the DFA be M2 = (Q2, E, q2,0, delta2, A2), where Q2 is the set of states, E is the input alphabet, q2,0 is the initial state, delta2 is the transition function, and A2 is the set of final states.
  - The states of the DFA are subsets of the states of the NFA, that is, Q2 = 2^Q1, where 2^Q1 is the power set of Q1.
  - The initial state of the DFA is the epsilon-closure of the initial state of the NFA, that is, q2,0 = epsilon-closure(q1,0), where epsilon-closure(q) is the set of states that can be reached from q by following zero or more null moves.
  - The final states of the DFA are those subsets of the states of the NFA that contain at least one final state of the NFA, that is, A2 = {S | S is a subset of Q1 and S intersects A1 is not empty}.
  - The transition function of the DFA is defined as follows: for any state S in Q2 and any symbol a in E, delta2(S, a) = epsilon-closure(union of delta1(q, a) for all q in S), where delta1(q, a) is the set of states that can be reached from q by following one move on a in the NFA, and union is the set union operation.
  - The subset construction algorithm ensures that the DFA simulates the behavior of the NFA on any input string, by keeping track of all the possible states that the NFA can be in after reading each symbol of the input. Therefore, the DFA and the NFA accept the same language.