### Conversion of FA into CFG and Regular grammar into FA for the notes of the Unit 3 - Regular and Non-Regular Grammars in the subject of Theory of Automata and Formal Languages

#### FA to CFG conversion

- A finite automaton (FA) is a model of computation that accepts or rejects strings over a finite alphabet.
- A context-free grammar (CFG) is a set of rules that generates strings over a finite alphabet, using a set of variables and terminals.
- A FA can be converted into a CFG by following these steps :
  - For each state q of the FA, introduce a new variable Q.
  - The variable corresponding to the starting state will be the starting variable of the new CFG.
  - For each transition of the FA q a -> q', add a rule Q -> aQ' to the CFG.
  - For each final state q of the FA, add a rule Q -> epsilon to the CFG, where epsilon is the empty string.

- Example: Consider the following FA that accepts strings over {a, b} that end with ab.

![FA](https://i.imgur.com/8YJ1w7f.png)

- The corresponding CFG is:

  - S -> aS | bA | epsilon
  - A -> aB | bA
  - B -> bS | epsilon

#### Regular grammar to FA conversion

- A regular grammar is a special type of CFG that has rules of the form A -> aB or A -> a, where A and B are variables and a is a terminal.
- A regular grammar can be converted into a FA by following these steps :
  - For each variable A of the grammar, create a state qA in the FA.
  - The state corresponding to the starting variable will be the starting state of the FA.
  - For each rule A -> aB in the grammar, add a transition qA a -> qB to the FA.
  - For each rule A -> a in the grammar, add a transition qA a -> qF to the FA, where qF is a new final state.
  - If the grammar has a rule S -> epsilon, where S is the starting variable, then make the starting state also a final state.

- Example: Consider the following regular grammar that generates strings over {a, b} that end with ab.

  - S -> aS | bA | epsilon
  - A -> aB | bA
  - B -> bS

- The corresponding FA is:

![FA](https://i.imgur.com/8YJ1w7f.png)