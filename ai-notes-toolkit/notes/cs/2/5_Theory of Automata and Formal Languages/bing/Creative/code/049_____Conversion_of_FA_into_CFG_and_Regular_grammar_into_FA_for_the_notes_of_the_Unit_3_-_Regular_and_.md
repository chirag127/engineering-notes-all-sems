### Conversion of FA into CFG and Regular grammar into FA for the notes of the Unit 3 - Regular and Non-Regular Grammars in the subject of Theory of Automata and Formal Languages

A finite automaton (FA) is a model of computation that accepts or rejects strings of symbols. A context-free grammar (CFG) is a set of rules that generates strings of symbols. A regular grammar is a special type of CFG that has restrictions on the form of the rules. There are algorithms to convert FA into CFG and regular grammar into FA.

#### FA to CFG conversion

The general idea of the algorithm is as follows :

- To each state q of the FA, introduce a new variable Q.
- The variable corresponding to the starting state will be the starting variable of the new CFG.
- For each transition of the FA q a -> q', we add a rule Q -> aQ'.
- For each final state q of the FA, we add a rule Q -> epsilon.

For example, consider the following FA that accepts strings of a's and b's that end with ab:

![FA](https://i.imgur.com/0wZ0x1M.png)

The corresponding CFG is:

- S -> aS | bS | aA
- A -> b

#### Regular grammar to FA conversion

The general idea of the algorithm is as follows :

- To each variable A of the regular grammar, introduce a new state q_A of the FA.
- The state corresponding to the starting variable will be the starting state of the new FA.
- For each rule A -> aB of the regular grammar, we add a transition q_A a -> q_B of the FA.
- For each rule A -> a of the regular grammar, we add a transition q_A a -> q_F of the FA, where q_F is a new final state.
- For each rule A -> epsilon of the regular grammar, we make q_A a final state of the FA.

For example, consider the following regular grammar that generates strings of a's and b's that end with ab:

- S -> aS | bS | aA
- A -> b

The corresponding FA is:

![FA](https://i.imgur.com/6x8Q6f9.png)