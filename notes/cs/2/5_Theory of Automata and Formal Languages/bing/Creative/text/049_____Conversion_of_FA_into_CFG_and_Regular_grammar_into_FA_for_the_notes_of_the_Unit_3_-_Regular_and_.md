### Conversion of FA into CFG and Regular grammar into FA for the notes of the Unit 3 - Regular and Non-Regular Grammars in the subject of Theory of Automata and Formal Languages

- A finite automaton (FA) is a model of computation that accepts or rejects strings over a finite alphabet.
- A context-free grammar (CFG) is a set of rules that generates strings over a finite alphabet, using a finite set of variables and terminals.
- A regular grammar is a special case of a CFG, where each rule has the form A -> aB or A -> a, where A and B are variables and a is a terminal.
- There is a correspondence between FA and regular grammar, and between FA and CFG, such that for every FA, there exists an equivalent regular grammar and an equivalent CFG, and vice versa.
- The following are the algorithms to convert FA to CFG and regular grammar to FA:

#### FA to CFG

- Let M = (Q, Sigma, delta, q0, F) be a FA, where Q is the set of states, Sigma is the alphabet, delta is the transition function, q0 is the initial state, and F is the set of final states.
- Construct a CFG G = (V, Sigma, R, S), where V is the set of variables, Sigma is the alphabet, R is the set of rules, and S is the start variable, as follows:
  - For each state q in Q, introduce a new variable A_q in V.
  - The start variable S is A_q0, where q0 is the initial state of M.
  - For each transition q a -> r in delta, where q and r are states and a is a symbol, add a rule A_q -> aA_r to R.
  - For each final state q in F, add a rule A_q -> epsilon to R, where epsilon is the empty string.
- The CFG G is equivalent to the FA M, meaning that they generate and accept the same language.

#### Regular grammar to FA

- Let G = (V, Sigma, R, S) be a regular grammar, where V is the set of variables, Sigma is the alphabet, R is the set of rules, and S is the start variable.
- Construct a FA M = (Q, Sigma, delta, q0, F), where Q is the set of states, Sigma is the alphabet, delta is the transition function, q0 is the initial state, and F is the set of final states, as follows:
  - For each variable A in V, introduce a new state q_A in Q.
  - The initial state q0 is q_S, where S is the start variable of G.
  - For each rule A -> aB in R, where A and B are variables and a is a symbol, add a transition q_A a -> q_B to delta.
  - For each rule A -> a in R, where A is a variable and a is a symbol, add a transition q_A a -> q_F to delta, where q_F is a new state in Q and F.
  - The set of final states F consists of q_F and any state q_A such that A -> epsilon is a rule in R, where epsilon is the empty string.
- The FA M is equivalent to the regular grammar G, meaning that they generate and accept the same language.