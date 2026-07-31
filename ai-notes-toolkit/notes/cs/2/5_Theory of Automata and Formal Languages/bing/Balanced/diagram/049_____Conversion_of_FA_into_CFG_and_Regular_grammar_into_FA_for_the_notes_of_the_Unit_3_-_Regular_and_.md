### Conversion of FA into CFG and Regular grammar into FA

#### FA to CFG conversion

A finite automaton (FA) is a model of computation that accepts or rejects strings over a given alphabet. A context-free grammar (CFG) is a set of rules that generates strings over a given alphabet. A CFG can be used to describe the syntax of a programming language or a natural language.

The following algorithm can be used to convert a FA into a CFG:

- For each state q of the FA, introduce a new variable Q.
- The variable corresponding to the starting state will be the starting variable of the new CFG.
- For each transition of the FA q a -> q', we add a rule Q -> aQ' to the CFG.
- For each final state q of the FA, we add a rule Q -> epsilon to the CFG, where epsilon is the empty string.

For example, consider the following FA that accepts strings over {a,b} that end with b:

![FA](https://i.imgur.com/0y8JfZL.png)

The corresponding CFG is:

- S -> aS | bA
- A -> aS | bA | epsilon

#### Regular grammar to FA conversion

A regular grammar is a special type of CFG that has the following restrictions:

- The left-hand side of each rule is a single variable.
- The right-hand side of each rule is either a single terminal, a single terminal followed by a single variable, or epsilon.

A regular grammar can be used to describe the same class of languages as a FA. The following algorithm can be used to convert a regular grammar into a FA:

- For each variable A of the grammar, create a state q_A of the FA.
- The state corresponding to the starting variable of the grammar will be the starting state of the FA.
- For each rule A -> aB of the grammar, create a transition q_A a -> q_B of the FA.
- For each rule A -> a of the grammar, create a transition q_A a -> q_F of the FA, where q_F is a new final state.
- For each rule A -> epsilon of the grammar, mark the state q_A as a final state.

For example, consider the following regular grammar that generates strings over {a,b} that end with b:

- S -> aS | bA
- A -> aS | bA | epsilon

The corresponding FA is:

![FA](https://i.imgur.com/7Z1n0aE.png)